# 


## Objective:
```
Monitor the Unrestricted Security group and public S3 Bucket with the help of AWS Trusted Advisor.
```
## Theory: ##

```
- Created S3 and Security Group resources manually and with Cloudformation
```	

## Steps: ##

	1. Check the initial status of the Trusted advisor dashboard
	2. Create a first unrestricted security group (created manually first + cloudformation)
	3. Create a second unrestricted security group (created manually first + cloudformation)
	4. Creating 2 Public S3 Bucket (created manually first + cloudformation)
	5. Refresh the Trusted advisor dashboard




+ ## Architecture Overview: ##

<a href="https://drive.google.com/uc?export=view&id=13sUUcJirhN8gSEYDGqZCAGQHFQdHKyWf"><img src="https://drive.google.com/uc?export=view&id=13sUUcJirhN8gSEYDGqZCAGQHFQdHKyWf" style="width: 400px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

+ ## **Goal** - Create and detect compromised resources with AWS Trusted Advisor: ##

<a href="https://drive.google.com/uc?export=view&id=126Z7K7RoKxClBLk38S8lz1rCpnzj9rdc"><img src="https://drive.google.com/uc?export=view&id=126Z7K7RoKxClBLk38S8lz1rCpnzj9rdc" style="width: 400px; max-width: 100%; height: auto" title="Click for the larger version." /></a>

+ **.yaml Cloudformation to create 2 Public S3 Buckets**

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Cloud formation for bucket creation and configuration

Parameters:
  BucketName: { Type: String, Default: "alex-bucket-1111" }

Resources:  
  AccessLogBucket:
    Type: "AWS::S3::Bucket"
    Properties:
#      AccessControl: LogDeliveryWrite
       AccessControl:   PublicReadWrite
 
            
  MainBucket:
    Type: "AWS::S3::Bucket"
    Properties:
	  AccessControl:   PublicReadWrite
      BucketName: !Ref BucketName  						 #Dynamic name creation
      BucketEncryption:
        ServerSideEncryptionConfiguration:
          - ServerSideEncryptionByDefault:
              SSEAlgorithm: AES256
      LoggingConfiguration:
        DestinationBucketName: !Ref AccessLogBucket


Outputs:
  MainBucketName:
    Description: Name of the main bucket
    Value: !Ref MainBucket
  LogBucketName:
    Description: Name of the access log bucket
    Value: !Ref AccessLogBucket


```

+ **Cloudformation Security Group Creation**
```
AWSTemplateFormatVersion: 2010-09-09
Description: CloudFormation template for security group 

Parameters:
  VpcId:
    Type: String
    Description: VpcId
    Default: vpc-0e396a82aad5ce908
Resources:
  DemoSG:
    Type: AWS::EC2::SecurityGroup
    Properties: 
      GroupDescription: A Security Group for Demo-EC2
      VpcId: !Ref VpcId
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0

Outputs:
  SecurityGroupId:
    Description: Security Group Id
    Value: !GetAtt DemoSG.GroupId
  VpcId:
    Description: VpcId in Which SG is there
    Value: !GetAtt DemoSG.GroupId
```



