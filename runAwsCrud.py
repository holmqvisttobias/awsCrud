#!/usr/bin/python

# @Author: Tobias Holmqvist <tohol>
# @Date:   2017-09-08
# @Email:  tobias.m.holmqvist@gmail.com
# @Project: awsCrud
# @Last modified by:   tohol
# @Last modified time: 2017-09-08
# @License: GPLv3

import awsCredentials, boto3, argparse, sys


### START: read an validate parameters ----------------------------------------
parser = argparse.ArgumentParser()

parser.add_argument('instance',
                    help='[all/instanceID]',
                    nargs='?',
                    default=None)

parser.add_argument('-v', '--verbose',
                    help='increase output verbosity',
                    action='store_true')

parser.add_argument('-s', '--status',
                    help='[all/instanceID] --status',
                    action='store_true')

parser.add_argument('-r', '--run',
                    help='[all/instanceID] --run',
                    action='store_true')

parser.add_argument('-p', '--poweroff',
                    help='[all/instanceID] --poweroff',
                    action='store_true')

parser.add_argument('-b', '--reboot',
                    help='[all/instanceID] --reboot',
                    action='store_true')

parser.add_argument('-d', '--delete',
                    help=' [all/instanceID] --delete',
                    action='store_true')

parser.add_argument('-c', '--create',
                    help='[new/clone] --create',
                    action='store_true')

args = parser.parse_args()

if  (not(args.instance)):
    print('\nMISSING INSTANCE: specify all/instanceID\n')
    sys.exit(0)

# Make sure status/run/poweroff/reboot/delete/create is not combined.
if ((args.status   and (args.run    or args.poweroff or args.reboot or
                        args.delete or args.create)) or
    (args.run      and (args.status or args.poweroff or args.reboot or
                        args.delete or args.create)) or
    (args.poweroff and (args.run    or args.status   or args.reboot or
                        args.delete or args.create)) or
    (args.reboot   and (args.run    or args.poweroff or args.status or
                        args.delete or args.create)) or
    (args.delete   and (args.run    or args.poweroff or args.reboot or
                        args.status or args.create)) or
    (args.create   and (args.run    or args.poweroff or args.reboot or
                        args.delete or args.status))):

    # Explain problem and exit with 0
    print('\nINVALID COMBINATION: status/run/poweroff/reboot/delete/create\n')
    sys.exit(0)

### END: read and validate parameters ----------------------------------------

### START: Get credentials and connect ---------------------------------------

# Get access keys from file.
awsKeys = awsCredentials.ReadFlatFiles()

# Setup client.
client = boto3.client(
    'ec2',
    aws_access_key_id     = awsKeys.getAwsAccessKeyID(),
    aws_secret_access_key = awsKeys.getAwsSecretAccessKey(),
    region_name           = awsKeys.getAwsRegionName()
    )


# Try to connect and get info about all instances.
try:
    response = client.describe_instances()
except Exception as e:
    print('\nERROR: Cannot connect to host\n')
    if (args.verbose):
        print(e)
    sys.exit(0)

### END: Get credentials and connect -----------------------------------------


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
