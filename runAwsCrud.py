#!/usr/bin/python

import awsCredentials, boto3
from botocore.exceptions import ClientError

awsKeys = awsCredentials.ReadFlatFiles()

client = boto3.client(
    'ec2',
    aws_access_key_id     = awsKeys.getAwsAccessKeyID(),
    aws_secret_access_key = awsKeys.getAwsSecretAccessKey(),
    region_name           = awsKeys.getAwsRegionName()
)

response = client.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:

        print(instance['InstanceId'])
        print(instance['KeyName'])
        print(instance['InstanceType'])
        print(instance['State']['Name'])
        print(instance['PublicDnsName'])
        print(instance['PublicIpAddress'])
        print(instance['PrivateDnsName'])
        print(instance['PrivateIpAddress'])
