# Azure Offensive Security

### 1.   Find/Enumerate the URL of the web application related to the device registration services :
+ 	MicroBurst: A PowerShell Toolkit for Attacking Azure
+	Use tool microburst, this will help to find the subdomains applicable for this azure tenant.
+	From the discovery output you can see the subdomains you have access to and could potentially move  laterally in the azure tenant

https://github.com/NetSPI/MicroBurst


<a href="https://drive.google.com/uc?export=view&id=10_ZkGfn5EmK-8mX0zZkIKoLyMXUIKZdX"><img src="https://drive.google.com/uc?export=view&id=10_ZkGfn5EmK-8mX0zZkIKoLyMXUIKZdX/" style="width: 200px; max-width: 50%; height: auto" title="Click for the larger version." /></a>


### 2.  Locate password of user via device phishing attack:

+ Perform a device code phishing attack, we use Token Tactics tool. Send an email and await authorization_pending response
+ There are several ways to perform a Device Code Phishing attack but, for the purpose of this flag, we will use https://github.com/rvrsh3ll/TokenTactics tool.


<a href="https://drive.google.com/uc?export=view&id=1QNwRvGDP2z75rJj8tiahJcqBj0wSb9OH_"><img src="https://drive.google.com/uc?export=view&id=1QNwRvGDP2z75rJj8tiahJcqBj0wSb9OH_/" style="width: 200px; max-width: 50%; height: auto" title="Click for the larger version." /></a>



### 3.  Find the SolarDrops web application with File Upload functionality

```
PS C:\Users\cb7061\Desktop\Tools\BreachingAzureTools> Import-Module .\MicroBurst-master\MicroBurst-master\MicroBurst.psm1
PS C:\Users\cb7061\Desktop\Tools\BreachingAzureTools> Invoke-EnumerateAzureSubDomains -Base SolarDrops -Verbose

```

<a href="https://drive.google.com/uc?export=view&id=1LvBp7r9_GRGOYVdEsPgo_E9x_DhllqSl"><img src="https://drive.google.com/uc?export=view&id=1LvBp7r9_GRGOYVdEsPgo_E9x_DhllqSl/" style="width: 200px; max-width: 50%; height: auto" title="Click for the larger version." /></a>


### 4.  Password Spraying Technique

```
Run MSOLSpray to find valid credentials
Import-Module .\MSOLSpray-master\MSOLSpray-master\MSOLSpray.ps1

Invoke-MSOLSpray -UserList C:\Users\cb7061\Desktop\Current_Tools\userlist.txt -Password Winter2022

```

<a href="https://drive.google.com/uc?export=view&id=1NvKwrBPrkMLikqwYwP4obTk9lwQ0rvrd"><img src="https://drive.google.com/uc?export=view&id=1NvKwrBPrkMLikqwYwP4obTk9lwQ0rvrd/" style="width: 200px; max-width: 50%; height: auto" title="Click for the larger version." /></a>

