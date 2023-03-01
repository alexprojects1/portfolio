# Stateful vs Stateless Firewalls


## Objective:
```
	•  Test between stateful ( AWS Security group) and stateless (Network ACL) firewall
```
## Theory: ##

```
Stateful:
	• Security groups are stateful - any changes applied to the incoming rule will be auto applied to the outgoing rule.
	• e.g. if you allow incoming port 22 for ssh , the outgoing port 22 will be automatically opened. 
	• Inspects packets in the context of their traffic flow, can potentially make complex rules and allows us to log    network traffic and to log network firewall alerts on traffic. 

Stateless:
	• Network ACLs are stateless - changes applied to an incoming rule will not be applied to the outgoing rule.
	• e.g. if you allow incoming port 22, you need to also apply the rule to outgoing traffic
	• NACLs inspect each packet in isolation, 

Testing: 
	• During the EC2 creation verify:
		○ Network setting is set to the correct: VPC, Subnet, Security Group
	• Case (Security group rules were not set) - Initially SSH was unavailable, to fix this added Security Group SSH TCP rule to allow for SSH to the public IP.  
```	



##  Steps: ##

```
	1. Sign in to AWS Management Console.
	2. Create an Amazon VPC. (AWS_VPC , 10.0.0.0/16) 
	3. Create a Public subnet. (public_subnet, 10.0.1.0/24)
	4. Create and attach an Internet Gateway. (Add to AWS_VPC)
	5. Create a Public Route Table and associate it with the subnet.   (PublicRT, associate AWS_VPC) , associate public_subnet)
	6. Add the public Route in the Route table.
	7. Create a security Group. (Create EC2_SG, associate/select AWS_VPC, leave inbound/outbound as default)
	8. Launch an EC2 instance. 
	9. Understand the security group rules.
	10. Understand the NACL rules.
Validate

```

+ ## Architecture Overview: ##


1. Create an Amazon VPC. (AWS_VPC , 10.0.0.0/16)


2. Create a Public subnet. (public_subnet, 10.0.1.0/24)


3. Create and attach an Internet Gateway. (Add to AWS_VPC)


4. Create a Public Route Table and associate it with the subnet.   (PublicRT, associate AWS_VPC) , associate 


5. Create a Public Route Table and associate it with the subnet.   (PublicRT, associate AWS_VPC) , associate 


6. Add the public Route in the Route table.


7. Create a security Group. (Create EC2_SG, associate/select AWS_VPC, leave inbound/outbound as default)


<a href="https://drive.google.com/uc?export=view&id=1K1lbPXo6KRPO5ZTWqGw-WNMZL4zDUj_Q"><img src="https://drive.google.com/uc?export=view&id=1K1lbPXo6KRPO5ZTWqGw-WNMZL4zDUj_Q/view?usp=share_link" style="width: 
30px; max-width: 50%; height: auto" title="Click for the larger version." /></a>

8. Launch an EC2 instance. 

9. Understand the security group rules.


<a href="https://drive.google.com/uc?export=view&id=1Cv5ULhKVLgBBkY4Pb3TVT5dWQ-hbp5nD"><img src="https://drive.google.com/uc?export=view&id=1Cv5ULhKVLgBBkY4Pb3TVT5dWQ-hbp5nD/view?usp=share_link" style="width: 
30px; max-width: 50%; height: auto" title="Click for the larger version." /></a>


<a href="https://drive.google.com/uc?export=view&id=1xdNNn6hecs9t7TnctGM8C3dva3sBGhyr"><img src="https://drive.google.com/uc?export=view&id=1xdNNn6hecs9t7TnctGM8C3dva3sBGhyr/view?usp=share_link" style="width: 
30px; max-width: 50%; height: auto" title="Click for the larger version." /></a>

10. Understand the NACL rules.


<a href="https://drive.google.com/uc?export=view&id=1XMCHt03m62OfF4FH__oueCNSPCLHKII7"><img src="https://drive.google.com/uc?export=view&id=1XMCHt03m62OfF4FH__oueCNSPCLHKII7/view?usp=share_link" style="width: 
30px; max-width: 50%; height: auto" title="Click for the larger version." /></a>

<a href="https://drive.google.com/uc?export=view&id=1eAMV_k9Pmc-ghL0jbFDuDsR5EtDZ_E9p"><img src="https://drive.google.com/uc?export=view&id=1eAMV_k9Pmc-ghL0jbFDuDsR5EtDZ_E9p/view?usp=share_link" style="width: 
30px; max-width: 50%; height: auto" title="Click for the larger version." /></a>
