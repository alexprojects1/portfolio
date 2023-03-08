# Boto3 Documentation

## boto3_Security_Groups_Audit_and_Remove.py :
+ Parse EC2 information with describe_instances boto3 module for multiple instances
https://github.com/alexprojects1/portfolio/blob/main/Python_AWS_Boto3/boto3_Security_Groups_Audit_and_Remove.py

<a href="https://drive.google.com/uc?export=view&id=1zzSXvA5qADrS59HhRHuwQkPGBQsZm9D_"><img src="https://drive.google.com/uc?export=view&id=1zzSXvA5qADrS59HhRHuwQkPGBQsZm9D_/" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


```
import boto3
import sys
from pprint import pprint
print("Script Name:  ",sys.argv[0])
print("====================================")
print('\n' * 3)


client=boto3.client("ec2")
client.describe_security_groups()
x=client.describe_security_groups()
pprint(x)
print('\n' * 2)

no_of_security_groups=len(x["SecurityGroups"])
print("Number of Security Groups:",no_of_security_groups)
print("====================================")
print('\n' * 1)

# Print Security Group Information
for group in x["SecurityGroups"]:
    print("Security Group Id's:  ",group["GroupId"], "Security Group Name:  ", group["GroupName"])
print("====================================")
print('\n' * 1)

ec2 = boto3.client('ec2')
security_group_names = input("Enter the names of the AWS security groups to remove (comma-separated): ").split(",")

# Remove each security group
for security_group_name in security_group_names:
    # Get the security group id based on the name
    response = ec2.describe_security_groups(
    Filters=[
            {
                'Name': 'group-name',
                'Values': [security_group_name],
            },
        ]
    )

# Check if the security group exists
if len(response['SecurityGroups']) == 0:
    print(f"Security group with name {security_group_name} not found.")
else:
    security_group_id = response['SecurityGroups'][0]['GroupId']
    # Remove the security group
    ec2.delete_security_group(GroupId=security_group_id)
    print(f"Security group with id {security_group_id} and name {security_group_name} has been removed.")

```



## boto3_EC2_Instance_Information_2.py :
+ Parse EC2 information with describe_instances boto3 module for multiple instances
https://github.com/alexprojects1/portfolio/blob/main/Python_Boto3/boto3_EC2_Instance_Information_2.py

<a href="https://drive.google.com/uc?export=view&id=1-AGNuihC7LshSKb09_cPsatkJ_4XEWvy"><img src="https://drive.google.com/uc?export=view&id=1-AGNuihC7LshSKb09_cPsatkJ_4XEWvy" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>



## boto3_EC2_Instance_tags_2.py:
+ Parse EC2 instance ids with describe_instances boto3 module and append a tag to EC2 instance id
https://github.com/alexprojects1/portfolio/blob/main/Python_Boto3/boto3_EC2_Instance_tags_2.py

<a href="https://drive.google.com/uc?export=view&id=1fW_HBLle8l89t04eeJvxokwMys_buEf7"><img src="https://drive.google.com/uc?export=view&id=1fW_HBLle8l89t04eeJvxokwMys_buEf7" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>


## boto3_S3_bucket_create.py:
+ Create a unique S3 bucket with confirmation
https://github.com/alexprojects1/portfolio/blob/main/Python_Boto3/boto3_S3_bucket_create.py

<a href="https://drive.google.com/uc?export=view&id=1ziKRKvcZktPpVJ1SnUuXc6OQgBE_Yac0"><img src="https://drive.google.com/uc?export=view&id=1ziKRKvcZktPpVJ1SnUuXc6OQgBE_Yac0" style="width: 500px; max-width: 100%; height: auto" title="Click for the larger version." /></a>



