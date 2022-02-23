# Cloud formation backup
Resources:
   Bucket:
     Type: "AWS::S3::Bcuket'
Properties:
	 BucketName: 'accatpics13333337'

Instance:
  Type: 'AWS::EC2::Instance
  Properties:
  KeyName: 'A4L'
  InstanceType: 't2.micro'
  ImageId:  'ami-033b95fb8079dc481'