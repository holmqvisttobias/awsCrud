#!/usr/bin/python

class ReadFlatFiles:
    def __init__(self):
        self.__awsAccessKeyID      = self.__setAwsAccessKeyID()
        self.__awsSecretAccessKey  = self.__setAwsSecretAccessKey()
        self.__awsRegionName       = self.__setAwsRegionName()

    def __setAwsAccessKeyID(self):
        self.__file   = open('.awsAccessKeyID', 'r')
        self.__output = self.__file.readline()
        self.__file.close()
        return self.__output.strip()

    def __setAwsSecretAccessKey(self):
        self.__file   = open('.awsSecretAccessKey', 'r')
        self.__output = self.__file.readline()
        self.__file.close()
        return self.__output.strip()

    def __setAwsRegionName(self):
        self.__file   = open('.awsRegionName', 'r')
        self.__output = self.__file.readline()
        self.__file.close()
        return self.__output.strip()

    def getAwsAccessKeyID(self):
        return self.__awsAccessKeyID

    def getAwsSecretAccessKey(self):
        return self.__awsSecretAccessKey

    def getAwsRegionName(self):
        return self.__awsRegionName
