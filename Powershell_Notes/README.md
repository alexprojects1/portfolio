# 

+ Developed by microsoft for task automation and repetitive tasks

+ Azure admin: powerful tool for resource groups, active directory and other resources







## Quick Command Reference:
```

Start-Process notepad

Stop-Process -Name notepad

cls # clear screen

Get-Help Format Table

Get-Command  #all commands installed with powershell

Get-Command -Module Microsoft.PowerShell.Management


PS C:\Users\zzand> Get-Item .


    Directory: C:\Users


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2022-02-15  11:48 AM                zzand


PS C:\Users\zzand> Get-Item *


    Directory: C:\Users\zzand


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        2021-03-27  11:25 PM                .astropy
d-----        2021-10-04  12:59 AM                .atom
d-----        2021-06-30   1:58 AM                .aws
d-----        2021-06-30   1:10 AM                .conda
d-----        2021-09-21   8:54 AM                .docker
d-----        2021-04-02   6:15 AM                .ipynb_checkpoints

PS C:\Users\zzand> get-content -Path .\.bash_history -TotalCount 8
git log
ls
git init
ls
git branch
git branch edit
git branch
git add .


#Start and stop services

PS C:\Users\zzand>  Get-Service -Name Audiosrv

Status   Name               DisplayName
------   ----               -----------
Running  Audiosrv           Windows Audio

Start-Service -Name Audiosrv


Get-ExecutionPolicy -list

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope Process



```


## Azure Powershell

```



PS C:\Users\zzand> Install-Module -Name Az -AllowClobber -Scope CurrentUser

Untrusted repository
You are installing the modules from an untrusted repository. If you trust this repository, change its
InstallationPolicy value by running the Set-PSRepository cmdlet. Are you sure you want to install the modules from
'PSGallery'?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y

-AllowClobber -Scope Allusers      #use this under admin mode to install for all users on windows


#in some offline environments, use the microsoft github:
https://github.com/Azure/azure-powershell/releases

Get-Module   #confirm Azure module is installed  

+ Note error:
Do you want to run software from this untrusted publisher?
File C:\Users\zzand\Documents\WindowsPowerShell\Modules\Az.Accounts\2.7.2\Accounts.format.ps1xml is published by
CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US and is not trusted on your system.
Only run scripts from trusted publishers.
[V] Never run  [D] Do not run  [R] Run once  [A] Always run  [?] Help (default is "D"): a
Connect-AzAccount : The 'Connect-AzAccount' command was found in the module 'Az.Accounts', but the module could not be
loaded. For more information, run 'Import-Module Az.Accounts'.
At line:1 char:1
+ Connect-AzAccount
+ ~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (Connect-AzAccount:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CouldNotAutoloadMatchingModule

PS C:\Users\zzand> Import-Module Az.Accounts
Import-Module : File C:\Users\zzand\Documents\WindowsPowerShell\Modules\Az.Accounts\2.7.2\Az.Accounts.psm1 cannot be
loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ Import-Module Az.Accounts
+ ~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [Import-Module], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess,Microsoft.PowerShell.Commands.ImportModuleCommand

+ Most important commands:

PS /home/cloud> Get-AzSubscription

Name                  Id                                   TenantId                             State
----                  --                                   --------                             -----
P1-Real Hands-On Labs 4cedc5dd-e3ad-468d-bf66-32e31bdb9148 3617ef9b-98b4-40d9-ba43-e1ed6709cf0d Enabled

PS /home/cloud> Get-AZSubsecription | f1
Get-AZSubsecription: The term 'Get-AZSubsecription' is not recognized as a name of a cmdlet, function, script file, or executable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
PS /home/cloud> Get-AzSubscription | f1 
f1: The term 'f1' is not recognized as a name of a cmdlet, function, script file, or executable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
PS /home/cloud> Get-AzSubscription | fl

Id                        : 4cedc5dd-e3ad-468d-bf66-32e31bdb9148
Name                      : P1-Real Hands-On Labs
State                     : Enabled
SubscriptionId            : 4cedc5dd-e3ad-468d-bf66-32e31bdb9148
TenantId                  : 3617ef9b-98b4-40d9-ba43-e1ed6709cf0d
HomeTenantId              : 3617ef9b-98b4-40d9-ba43-e1ed6709cf0d
ManagedByTenantIds        : {2f4a9838-26b7-47ee-be60-ccc1fdec5953}
CurrentStorageAccountName : 
SubscriptionPolicies      : {
                              "LocationPlacementId": "Public_2014-09-01",
                              "QuotaId": "EnterpriseAgreement_2014-09-01",
                              "SpendingLimit": "Off"
                            }
ExtendedProperties        : {[Environment, AzureCloud], [ManagedByTenants, 2f4a9838-26b7-47ee-be60-ccc1fdec5953], [AuthorizationSource, 
                            RoleBased], [Account, MSI@50342]…}
CurrentStorageAccount     : 
AuthorizationSource       : RoleBased
Tags                      : 


#check virtual machine information
get-azvm

#newazvm
create vms

#stop azvm

start-azvm -Name TESTVM

get-azvm

Get-AZREsourceGroup

New-AzResourceGroup

get-azstorageaccount

Get-AZVirtualNetwork

Login-AzAccount

get-service -Name win*

get-service -Name win* | Format-List -Property displayname

get-service -Name win* | Format-List -Property displayname,status,servicetype





```

