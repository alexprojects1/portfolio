# Terraform script execution through jenkins pipeline   

## Objective:
+ Work with Jenkins and Groovy
+ Terraform code creates EC2, installs Jenkins to start an environment for Groovy

<a href="https://drive.google.com/uc?export=view&id=1-I7e-OOK3qsc_3PawARHhYm7v6gTks7W"><img src="https://drive.google.com/uc?export=view&id=1-I7e-OOK3qsc_3PawARHhYm7v6gTks7W/" style="width: 200px; max-width: 50%; height: auto" title="Click for the larger version." /></a>



# Terraform Jenkins EC2 Installation

```
# configured aws provider with proper credentials
provider "aws" {
  region    = "us-east-1"
  profile   = "terraform-alex"
}


# create default vpc if one does not exit
resource "aws_default_vpc" "default_vpc" {

  tags    = {
    Name  = "default vpc"
  }
}


# use data source to get all avalablility zones in region
data "aws_availability_zones" "available_zones" {}


# create default subnet if one does not exit
resource "aws_default_subnet" "default_az1" {
  availability_zone = data.aws_availability_zones.available_zones.names[0]

  tags   = {
    Name = "default subnet"
  }
}


# create security group for the ec2 instance
resource "aws_security_group" "ec2_security_group" {
  name        = "ec2 security group"
  description = "allow access on ports 8080 and 22"
  vpc_id      = aws_default_vpc.default_vpc.id

  # allow access on port 8080
  ingress {
    description      = "http proxy access"
    from_port        = 8080
    to_port          = 8080
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  # allow access on port 22
  ingress {
    description      = "ssh access"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = -1
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags   = {
    Name = "jenkins server security group"
  }
}


# use data source to get a registered amazon linux 2 ami
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm*"]
  }
}


# launch the ec2 instance and install website
resource "aws_instance" "ec2_instance" {
  ami                    = data.aws_ami.amazon_linux_2.id 
  instance_type          = "t2.micro"
  subnet_id              = aws_default_subnet.default_az1.id
  vpc_security_group_ids = [aws_security_group.ec2_security_group.id]
  key_name               = "terraform"
  # user_data            = file("install_jenkins.sh")  #optional, runs install install_jenkinds.sh file but issue is file needs orginal

  tags = { 
    Name =   "alex-jenkins-server"
  }
}


# an empty resource block, added to ssh to instance
resource "null_resource" "name" {

  # ssh into the ec2 instance 
  connection {
    type        = "ssh"
    user        =  "ec2-user"
    private_key = file("E:\\terraform.alex\\terraform.pem")
    host        = aws_instance.ec2_instance.public_ip
  }

  # copy the install_jenkins.sh file from your computer to the ec2 instance 
  provisioner "file" {
    source      = "jenkins_install_aws_ec2.sh"
    destination = "/tmp/jenkins_install_aws_ec2.sh"
  }

  # set permissions and run the install_jenkins.sh file
  provisioner "remote-exec" {
    inline = [
            "sudo chmod +x /tmp/jenkins_install_aws_ec2.sh",
            "sh  /tmp/jenkins_install_aws_ec2.sh",
            "echo 'complete'"
    ]
  }

  # wait for ec2 to be created
  depends_on = [aws_instance.ec2_instance]
}


# print the url of the jenkins server
output "website_url" {
  value     = join ("", ["http://", aws_instance.ec2_instance.public_dns, ":", "8080"])
}

```


## Testing with Groovy  
```
pipeline {
  parameters{
      string(name:'parameter1',  defaultValue:''  ?: '')
      string(name:'parameter2',  defaultValue:''  ?: 'test')
      string(name:'parameter3',  defaultValue:''  ?: '')
  }
  agent any 
  stages {
        stage('Build') { 
            steps {
                sh 'echo ${parameter1}'
            }
        }
        stage('Test') { 
            steps {
                sh 'echo ${parameter2}' 
            }
        }
        stage('Deploy') { 
            steps {
                sh 'echo ${parameter3}'
            }
        }
    }
}
```
