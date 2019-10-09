import boto3

c = boto3.resources("ec2")

for inst in ec:
    print(inst)
