#!/usr/bin/python

# @Author: Tobias Holmqvist <tohol>
# @Date:   2017-09-11
# @Email:  tobias.m.holmqvist@gmail.com
# @Project: awsCrud
# @Last modified by:   tohol
# @Last modified time: 2017-09-11
# @License: GPLv3

class Instances:
    def __init__(self, response):
        # New instance object
        self.__instance  = Instance()
        # Array for all instances.
        self.__instances = []

        # Only need this for verbose mode (print all instances and count them).
        if (1 == 1):
            self.counter = 0

        # Get all instances and update object.
        for reservation in response["Reservations"]:
            for instanceX in reservation["Instances"]:
                self.__instance.setInstanceId(instanceX['InstanceId'])
                self.__instance.setInstanceName(instanceX['KeyName'])
                self.__instance.setInstanceType(instanceX['InstanceType'])
                self.__instance.setStatus(instanceX['State']['Name'])
                self.__instance.setPublicDns(instanceX['PublicDnsName'])
                self.__instance.setPublicIp(instanceX['PublicIpAddress'])
                self.__instance.setPrivateDns(instanceX['PrivateDnsName'])
                self.__instance.setPrivateIp(instanceX['PrivateIpAddress'])

                # Print instance info (verbose)
                if (1 == 1):
                    self.counter += 1
                    print('+++ Found {0} instance/s +++'.format(self.counter))
                    self.__instance.printInstance()

                # Append object to array.
                self.__instances.append(self.__instance)

class Instance:
    def __init__(self):
        self.__instanceId   = ''
        self.__instanceName = ''
        self.__instanceType = ''
        self.__status       = ''
        self.__publicDns    = ''
        self.__publicIp     = ''
        self.__privateDns   = ''
        self.__privateIp    = ''

    def setInstanceId(self, instanceId):
        self.__instanceId = instanceId

    def getInstanceId(self):
        return self.__instanceId

    def setInstanceName(self, instanceName):
        self.__instanceName = instanceName

    def getInstanceName(self):
        return self.__instanceName

    def setInstanceType(self, instanceType):
        self.__instanceType = instanceType

    def getInstanceType(self):
        return self.__instanceType

    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        return self.__status

    def setPublicDns(self, publicDns):
        self.__publicDns = publicDns

    def getPublicDns(self):
        return self.__publicDns

    def setPublicIp(self, publicIp):
        self.__publicIp = publicIp

    def getPublicIp(self):
        return self.__publicIp

    def setPrivateDns(self, privateDns):
        self.__privateDns = privateDns

    def getPrivateDns(self):
        return self.__privateDns

    def setPrivateIp(self, privateIp):
        self.__privateIp = privateIp

    def getPrivateIp(self):
        return self.__privateIp

    def printInstance(self):
        print('Instance ID: {0}'.format(self.__instanceId))
        print('Name:        {0}'.format(self.__instanceName))
        print('Type:        {0}'.format(self.__instanceType))
        print('Status:      {0}'.format(self.__status))
        print('Public DNS:  {0}'.format(self.__publicDns))
        print('Public IP:   {0}'.format(self.__publicIp))
        print('Private DNS: {0}'.format(self.__privateDns))
        print('Private IP:  {0}'.format(self.__privateIp))
        print('')
