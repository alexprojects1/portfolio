# Configuring Layered Security in an AWS VPC


## Objective:
```
	• Configure a multi-layered security in AWS VPC and launch 2 EC2 instances (1 in a public subnet and 1 in a private subnet)

	• Amazon VPC allows us to launch AWS resources in an isolated network defined by us in the Private and secure network
	
	• The AWS resources are protected using a multilayered VPC which includes security groups and Network Access Control List

	• The VPC security group provides security at the instance level, which acts as a firewall and controls both the inbound and outbound traffic 
	
The VPC NACL provides security at the Network level i.e. subnet level which acts like a firewall for the associated subnets and controls both the inbound and outbound traffic .  Note NACL are stateless (requires configuration of both inbound and outbound rules if making rules) 
```


## Steps: ##

```

1. Create a new VPC.  (alex_vpc) 10.0.0.0/16
2. Create and attached an Internet Gateway.  (alex_IGW)
3. Create two subnets for public and private AWS instances.  (public_subnet - 10.0.1.0/24) (private_subnet - 10.0.2.0/24)
4. Create Route Tables (1 for public and 1 for private) , Configure/add routes and associate them with Subnets.
5. Create a Security Group.
6. Create and configured Network ACL. 
7. Launched 2 EC2 instances (one in a public subnet and one in a private subnet).
8. Tested the EC2 instance.


```

+ ## Architecture Overview: ##

<a href="https://drive.google.com/uc?export=view&id=1lYXKJhQOJekOwr-t8X8qAg0F0ghseUmJ"><img src="https://drive.google.com/uc?export=view&id=1lYXKJhQOJekOwr-t8X8qAg0F0ghseUmJ" style="width: 400px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

2. Create and attached an Internet Gateway.  (alex_IGW)

<a href="https://drive.google.com/uc?export=view&id=1lLUIAzfBZ8HOYKSuzXmUlF4WAHXnxwfF"><img src="https://drive.google.com/uc?export=view&id=1lLUIAzfBZ8HOYKSuzXmUlF4WAHXnxwfF" style="width: 400px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


3. Create two subnets for public and private AWS instances.  (public_subnet - 10.0.1.0/24) (private_subnet - 10.0.2.0/24)


<a href="https://drive.google.com/uc?export=view&id=1l281MmmsnKWKES11-I-MlxHFSlCDE3pI"><img src="https://drive.google.com/uc?export=view&id=1l281MmmsnKWKES11-I-MlxHFSlCDE3pI" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


4. Create Route Tables (1 for public and 1 for private) , Configure/add routes and associate them with Subnets.



<a href="https://drive.google.com/uc?export=view&id=1kEIycd7irJG-yI8Syb-CJ0AfQv4WxSQg"><img src="https://drive.google.com/uc?export=view&id=1kEIycd7irJG-yI8Syb-CJ0AfQv4WxSQg/view?usp=share_link" style="width: 
100px; max-width: 50%; height: auto" title="Click for the larger version." /></a>

5. Create a Security Group.


<a href="https://drive.google.com/uc?export=view&id=1RBjyojPArzeSyq80-2-Ex36kU9JbBii7"><img src="https://drive.google.com/uc?export=view&id=1RBjyojPArzeSyq80-2-Ex36kU9JbBii7" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

6. Create and configured Network ACL. 

https://drive.google.com/file/d/1XND1OT2NVIQ22NkoNvQgjfeoQllmdP3H/view?usp=share_link

<a href="https://drive.google.com/uc?export=view&id=1XND1OT2NVIQ22NkoNvQgjfeoQllmdP3H"><img src="https://drive.google.com/uc?export=view&id=1XND1OT2NVIQ22NkoNvQgjfeoQllmdP3H" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

7. Launched 2 EC2 instances (one in a public subnet and one in a private subnet).

<a href="https://drive.google.com/uc?export=view&id=/1JVkc7HqwGvc2oAoA1nj1uBZkT1R_tdUL"><img src="https://drive.google.com/uc?export=view&id=/1JVkc7HqwGvc2oAoA1nj1uBZkT1R_tdUL" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


8. Tested the EC2 instance.
<a href="https://drive.google.com/uc?export=view&id=1HR01xUV0PdxVw7OXVcGEGtnI3WI1mczW"><img src="https://drive.google.com/uc?export=view&id=1HR01xUV0PdxVw7OXVcGEGtnI3WI1mczW" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>



