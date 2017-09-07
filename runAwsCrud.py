#!/usr/bin/python

import awsCredentials, boto3
from botocore.exceptions import ClientError
import argparse, sys

parser = argparse.ArgumentParser()

parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
parser.add_argument('-i', '--id', metavar='str', help='instanceID')
parser.add_argument('-l', '--list', help='list instances', action='store_true')
parser.add_argument('-s', '--start', help='start instance', action='store_true')
parser.add_argument('-p', '--poweroff', help='stop/poweroff instance', action='store_true')
parser.add_argument('-r', '--restart', help='restart instance', action='store_true')
parser.add_argument('-d', '--delete', help='remove/delete instance', action='store_true')
args = parser.parse_args()

if args.id:
    instanceID = args.id

if  args.start and (args.poweroff or args.restart or args.delete):
    print('\nINVALID COMBINATION: --start cannot be combined with poweroff/restart/delete\n')
    parser.print_help()
    sys.exit(0)

if  args.poweroff and (args.start or args.restart or args.delete):
    print('\nINVALID COMBINATION: --poweroff cannot be combined with start/restart/delete\n')
    parser.print_help()
    sys.exit(0)

if  args.restart and (args.poweroff or args.start or args.delete):
    print('\nINVALID COMBINATION: --restart cannot be combined with poweroff/start/delete\n')
    parser.print_help()
    sys.exit(0)

if  args.delete and (args.poweroff or args.restart or args.start):
    print('\nINVALID COMBINATION: --delete cannot be combined with poweroff/restart/start\n')
    parser.print_help()
    sys.exit(0)

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
