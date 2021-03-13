# Part 6: Cloud computing

This sections tests some general cloud computing knowledge to do with AWS and cloud infra in general.
It is expected that you will need to find the answers to some of these questions via Google.

Please write your answers in this file.

### Question 6.1

Which AWS region is the closest to Melbourne?

Answer: 
Sydney

### Question 6.2

What is the name of a cheap AWS EC2 instance that offers _at least_ 12 CPU cores and 16GB of RAM?
What are its specs (CPU cores, RAM) and cost per hour?

Answer:
EC2 general purpose instance - name: m5zn.3xlarge
Specs:
vCPU - 12 cores
RAM - 48 GiB
Network Bandwidth - up to 25 Gbps
windows usage price - $1.791 per Hour
Linux usage price - $1.239 per Hour

How much will it cost to run this instance for two weeks?

Answer:
Windows usage price - $601.776 per two weeks, assuming that the instance is running for 24 hours and 14 days
Linux usage price - $416.304 per two weeks, assuming that the instance is running for 24 hours and 14 days

### Question 6.3

Provide the AWS CLI command to copy all the contents of a S3 bucket to another S3 bucket on the same account.
The source bucket may contain nested files within "folders".

Source bucket: s3://mysource
Destination bucket: s3://mydest

```bash
# Your command here
# Answer:
aws s3 sync s3://mysource s3://mydest
```

### Question 6.4

Link to a section of library documentation showing how to stop an AWS EC2 instance using a Python client library (can be a howto, API reference, or tutorial).

Answer:
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/ec2-example-managing-instances.html

### Question 6.5

Describe, in 1-3 sentences

- What an AMI is and why it is useful for running EC2 instances

Answer:
An AMI or Amazon Machine Image is an encrypted machine image of a specific computer running an operating system configured in a particular way, and that can also contain applications and services for accomplishing a specific purpose. An AMI has all the information necessary to start up and run the software in the image. Amazon EC2 and AWS infrastructure make up the computing environment for running an AMI.

- What IAM is and why it is useful when administering AWS

Answer:
Identity and Access Management or IAM enables you to manage access to AWS services and resources securely. With IAM, you can manage and create AWS user's or a group's access to AWS resources.

- Where you would add your SSH public key onto an EC2 instance in order to log in as the "ubuntu" user

Answer:
Add your SSH public key into the .ssh/authorized_keys file in an EC2 instance in order to log in as the "ubuntu" user.

### Question 6.6

Create a new SSH key and paste both the public and private key into this file.

Answer:
SSH public key: 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDqucXlpYQ7WhAUB/T30vSvOxw80ogLlpvd0AFlTHesA6BNOejDLNNK5IHecIsVQVgNKdvpMLaldne6A7uHFV4Y76/Jnc50ZKJTLgQCsSEhJA2rK43IlmvpltgsFsuW4yK4btQWFxC1hWfgEJX7W8q8SG9LWDqdx+hog+aqFMY1pulo4Y49lQcM0fOSidE2WO2j8/eFJOGqMEzIjdPXBztelzPTQ6+BmVPHHwcDRYYuEVnTNT0vE/wcfaXsax/1vDFm+3ihAhUtRYo2oejNVBB/UcdILbZ51wtaviak0IYOCR+bbPje/sDLJ90JCOH6LLAIAMcQGodotlh9HTCcW52N ram@ubuntu

ssh private key:
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA6rnF5aWEO1oQFAf099L0rzscPNKIC5ab3dABZUx3rAOgTTno
wyzTSuSB3nCLFUFYDSnb6TC2pXZ3ugO7hxVeGO+vyZ3OdGSiUy4EArEhISQNqyuN
yJZr6ZbYLBbLluMiuG7UFhcQtYVn4BCV+1vKvEhvS1g6ncfoaIPmqhTGNabpaOGO
PZUHDNHzkonRNljto/P3hSThqjBMyI3T1wc7Xpcz00OvgZlTxx8HA0WGLhFZ0zU9
LxP8HH2l7Gsf9bwxZvt4oQIVLUWKNqHozVQQf1HHSC22edcLWr4mpNCGDgkfm2z4
3v7AyyfdCQjh+iywCADHEBqHaLZYfR0wnFudjQIDAQABAoIBAHgog4sM0QVFFIf8
jsWywzlU7B6is6wi/EVvbtd5bqWq8Yu3AlWvg7aKBYVmXXyTB80tSXs1SbqoS5/4
uy3qnVHsmTN/yilBPuuP2dO68zew6iJe2GT/w9w/MQhY3v2t5p89dOqeAhq6YTON
qgmTstPxzK9oShFtPacLJrCYk+LwROtPN+xJevTqQDbVRbTy3SAb/Rnwt689DmVr
/pTqO9wCfSTzrtI2VvQtHgEiJfbT2Zf7frqGLdC+Q2jacXfDEp0poK+Hh4Wl79gz
J81l2JZ5NWDtR6BVHve7IDfBeO0eVPvqFLVL2C877vuTjUjP9zjKhABlKy5CcGnQ
GmnpgsECgYEA+4twZX3I1qj+QVGKsiNx73q41RdNbV9G8O+wafSEmnAF6gPpW/ng
bKDNQKi2n3+yuCXyWYmCu991XEyztZ0yVzy5HzZe4ZA9Hdf7Ba4zht2klJE9AXsT
T4rRKA9q/D9cM8/Oaz9wQqyuUe+4HN58ay5/VqTQL58DbYL9BU7ghj0CgYEA7uIS
oRCr7MOojzK5PGd/rmAaG4YdtGfPjBGt+VVt0GKK9hsx6ox7iUA3nZqxRr5J335q
ikq7qsFFRTpOeAqQiKUv0M3fSOi9khom2F+Z2XfodW2czdQFDK7JBDVQaVmJI+i+
til0AMkMicRrsR7qFgHOEzwKTWJScE4csBc8OZECgYEAgWLR54JxweifD54Px11w
B4yKciFQVEfDx76icX2yj3W7tQlaCVNYWsfDi9S8SwJ2PT5XkDKpKlXgmh9h+LLo
5/J2DlX7K+7zYNxtZBicrGxpcXnbdV2HK0zuFLsJfsJgfM4RER1KcyE7cS3q9/6A
5Oi/2yNfan9SVgwgdZCC8MkCgYBZsGvKKVZDmNqKmULPGRTpRY/H0b0JZQiZ0HF/
ccG/QaBm8qL1KzWevIulEtWIeB2IWhBqR9DaNaJqcY/QpjbJ9ytSvFkfKLM0TblT
9+Dts4WFwVfkN7yFnIJAoDvGsiU5ZENmZX32ZYXdm+/LGo5NIPRcaGh90XKeU9WV
j8O+4QKBgQDcLRRZmvWLUC2/W6r+KTbXUj/NQscpF+55W2NNLp4bO2zaZ0lMK1Hl
i5X2WSuLS9o5chYxftyEJZIPJx9fOg4VEFjDh0zxOZ3sj0SscT93zjUBwiBYZkS7
tjIVvPFZvYsIAV8W27SVRdCcIZjvg4M3625eR51cQH8j4UPEd2o3Kg==
-----END RSA PRIVATE KEY-----

generated using: ssh-keygen -t rsa


### Question 6.7

Write a bash one liner to create a new file called `foo.txt` which contains the text "Hello World!", followed by a newline

```bash
# Your command here
# Answer:
echo "Hello World!\n" > foo.txt
```

### Question 6.8

Write a bash one liner to create a new file which contains the text "Hello World!", followed by a newline, on a remote machine via SSH.

Remote machine hostname is `foo.com` and the user is `bar`. Assume you have all your SSH keys set up correctly on your machine and the target server.

```bash
# Your command here
# Answer:
ssh bar@foo.com && echo "Hello World!\n" > foo.txt
```

### Question 6.9

Buildkite it a self-hosted CI system. Referring to the documentation via Google, is it possible to run a scheduled build at 2pm every Tuesday? Please link to the URL of the documentation where you found your answer.

Answer:
Yes, it is possible to run a scheduled build at 2pm every Tuesday.
Please refer to the link below to see instructions on how to achieve this:
https://buildkite.com/docs/pipelines/scheduled-builds


### Question 6.10

GitHub Actions is a CI system provided by GitHub, Referring to the documentation via Google, what is an environment variable that you could use to determine whether your bash script is running inside a Github Action?

Answer:
GITHUB_ACTIONS is the environment variable that you could use to determine whether your bash script is running inside a Github Action.

What kind of value would indicate that your script is running inside a GitHub Action?

Answer:
If the value of GITHUB_ACTIONS variable is true then the bash script is running inside a Github Action. You can use this variable to differentiate when tests are being run locally or by GitHub Actions.