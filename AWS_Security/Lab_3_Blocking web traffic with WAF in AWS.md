# Blocking web traffic with WAF in AWS


## Objective:
```
	• Block web traffic with a WAF (Web Application Firewall) 

```
## Theory: ##

```
	• AWS WAF is a web application firewall that can help protect your applications against common web exploits which may affect your application availability and compromise security. 

	• AWS WAF allows control over how traffic reaches applications.  Can block common attacks such as SQL injection.

	• Allows the request to reach the server based on the rules or patters you define.

	• Cost - WAF costs are based on what you use (how many rules you deploy and how many web requests your app receives)

```	



##  Steps: ##

```
	1. Sign in to AWS Management Console
	2. Create Security Group for Load Balancer
	3. Steps to create the web servers
	4. Create a Load Balancer
	5. Testing the Load Balancer
	6. Create an IP Set
	7. Create a web ACL
	8. Testing the working of the WAF
	9. Unblocking the IP
	10. Validation 
```

### Architecture Overview ##
	1. Sign in to AWS Management Console
	2. Create Security Group for Load Balancer
	3. Steps to create the web servers

<a href="https://drive.google.com/uc?export=view&id=1dQBznQH0Q24R7g-tGy_trCOgKUNiNBRb"><img src="https://drive.google.com/uc?export=view&id=1dQBznQH0Q24R7g-tGy_trCOgKUNiNBRb/view?usp=share_link" style="width: 
30px; max-width: 50%; height: auto" title="Click for the larger version." /></a>


	4. Create a Load Balancer


<a href="https://drive.google.com/uc?export=view&id=1FbTmSqywN6SNhj73S52txsl0fU08tVf5"><img src="https://drive.google.com/uc?export=view&id=1FbTmSqywN6SNhj73S52txsl0fU08tVf5/view?usp=share_link" style="width: 
30px; max-width: 50%; height: auto" title="Click for the larger version." /></a>



	5. Testing the Load Balancer
	6. Create an IP Set
	7. Create a web ACL


<a href="https://drive.google.com/uc?export=view&id=1K7DEU_rLZTndajYXRMPtRogE8sbE2S3j"><img src="https://drive.google.com/uc?export=view&id=1K7DEU_rLZTndajYXRMPtRogE8sbE2S3j/view?usp=share_link" style="width: 
30px; max-width: 50%; height: auto" title="Click for the larger version." /></a>





	8. Testing the working of the WAF
	9. Unblocking the IP
	10. Validation 

