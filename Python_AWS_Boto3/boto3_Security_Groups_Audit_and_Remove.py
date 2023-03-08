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