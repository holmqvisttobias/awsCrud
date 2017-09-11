#!/usr/bin/python

# @Author: Tobias Holmqvist <tohol>
# @Date:   2017-09-06
# @Email:  tobias.m.holmqvist@gmail.com
# @Project: awsCrud
# @Last modified by:   tohol
# @Last modified time: 2017-09-11
# @License: GPLv3

import boto3, sys

class Credentials:
    def __init__(self, credDict = {}):
        self.__awsAccessKeyId      = credDict['awsAccessKeyId']
        self.__awsSecretAccessKey  = credDict['awsSecretAccessKey']
        self.__awsRegionName       = credDict['awsRegionName']
        self.__credDict            = credDict

        if (1 == 1):
            self.printCredentials()

        if not(self.validate()):
            sys.exit(0)

    def getCredDict(self):
        # Return validated dictonary with credentials.
        return self.__credDict

    def validate(self):
        # Validate if credentials are ok.
        if not(self.__awsAccessKeyId):
            return False
        if not(self.__awsSecretAccessKey):
            return False
        if not(self.__awsRegionName):
            return False
        return True

    def printCredentials(self):
        print('File contents:')
        print('Access Key : {0}\nSecret Key : {1}\nRegion Name: {2}\n'.format(
              self.__awsAccessKeyId,
              self.__awsSecretAccessKey,
              self.__awsRegionName))

class ReadFlatFiles:
    def __init__(self, fAccessKeyId, fSecretAccessKey, fRegionName):
        self.__fAccessKeyId     = fAccessKeyId
        self.__fSecretAccessKey = fSecretAccessKey
        self.__fRegionName      = fRegionName

        self.__credDict = {}

        self.__credDict['awsAccessKeyId']     = self.getAwsAccessKeyId()
        self.__credDict['awsSecretAccessKey'] = self.getAwsSecretAccessKey()
        self.__credDict['awsRegionName']      = self.getAwsRegionName()

        if (1 == 1):
            self.printFilenames()

    def getAwsAccessKeyId(self):
        # Get AWS ACCESS Key from file.
        try:
            openFile    = open(self.__fAccessKeyId, 'r')
            fileContent = openFile.readline()
            openFile.close()
        except Exception as e:
            print('\nCannot open file!: {0}\n'.format(self.__fAccessKeyId))
            if (1 == 1):
                print(e)
            sys.exit(0)
        return fileContent.strip()

    def getAwsSecretAccessKey(self):
        # Get AWS SECRET Key from file.
        try:
            openFile    = open(self.__fSecretAccessKey, 'r')
            fileContent = openFile.readline()
            openFile.close()
        except Exception as e:
            print('\nCannot open file!: {0}\n'.format(self.__fSecretAccessKey))
            if (1 == 1):
                print(e)
            sys.exit(0)
        return fileContent.strip()

    def getAwsRegionName(self):
        # Get AWS REGION from file.
        try:
            openFile    = open(self.__fRegionName, 'r')
            fileContent = openFile.readline()
            openFile.close()
        except Exception as e:
            print('\nCannot open file!: {0}\n'.format(self.__fRegionName))
            if (1 == 1):
                print(e)
            sys.exit(0)
        return fileContent.strip()

    def getCredDict(self):
        # Return dictonary with credentials.
        return self.__credDict

    def printFilenames(self):
        # Print filename parameters.
        print('Filenames:')
        print('Access Key : {0}\nSecret Key : {1}\nRegion Name: {2}\n'.format
             (self.__fAccessKeyId,
              self.__fSecretAccessKey,
              self.__fRegionName))

class Connect:
    def __init__(self, credDict = {}):
        self.__awsAccessKeyId      = credDict['awsAccessKeyId']
        self.__awsSecretAccessKey  = credDict['awsSecretAccessKey']
        self.__awsRegionName       = credDict['awsRegionName']

        # Setup client.
        self.__client = boto3.client(
                        'ec2',
                        aws_access_key_id     = self.__awsAccessKeyId,
                        aws_secret_access_key = self.__awsSecretAccessKey,
                        region_name           = self.__awsRegionName)

        # Try to connect and get info about all instances.
        try:
            self.__response = self.__client.describe_instances()
        except Exception as e:
            print('\nERROR: Cannot connect to host\n')
            if (1 == 1):
                print(e)
            sys.exit(0)

    def getResonse(self):
        # Return json response.
        return self.__response
