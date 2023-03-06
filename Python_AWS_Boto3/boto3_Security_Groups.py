import boto3
import sys
from pprint import pprint
print(sys.argv[0])

client=boto3.client("ec2")
client.describe_security_groups()
x=client.describe_security_groups()
pprint(x)

no_of_security_groups=len(x["SecurityGroups"])
print("Number of Security Groups:",no_of_security_groups)
print("====================================")

for group in x["SecurityGroups"]:
    print("Security Group Id's:  ",group["GroupId"], "Security Group Name:  ", group["GroupName"])