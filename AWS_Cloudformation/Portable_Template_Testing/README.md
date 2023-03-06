# Non-portable testing
```
Resources:
   Bucket:
     Type: 'AWS::S3::Bucket'
     Properties:
	     BucketName: 'catpicsfeb162022'
   Instance:
     Type: 'AWS::EC2::Instance'
     Properties:
       KeyName: 'A4L'
       InstanceType: 't2.micro'
       ImageId:  'ami-033b95fb8079dc481'
```

# Portable testing
```
Parameters:
  InstanceType:
    Type: String
    Default: 't3.micro'
    AllowedValues:
        - 't3.micro;'
        - 't3.medium'
        - 't3.large'
    Description: 'Pick a supported InstanceType.'
  IsntanceAmiID:
      Type: String
      Description: 'AMI ID For Instances.'
```