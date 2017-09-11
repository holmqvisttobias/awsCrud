#!/usr/bin/python

# @Author: Tobias Holmqvist <tohol>
# @Date:   2017-09-11
# @Email:  tobias.m.holmqvist@gmail.com
# @Project: awsCrud
# @Last modified by:   tohol
# @Last modified time: 2017-09-11
# @License: GPLv3

import awsConnectClasses, awsInstanceClasses

def main():
    # Setup filenames.
    fAccessKeyId     = '.awsAccessKeyId'
    fSecretAccessKey = '.awsSecretAccessKey'
    fRegionName      = '.awsRegionName'

    # Read credentials from files
    awsFileContent = awsConnectClasses.ReadFlatFiles(
                     fAccessKeyId,
                     fSecretAccessKey,
                     fRegionName)

    # Setup credentials class.
    awsCredentials = awsConnectClasses.Credentials(
                     awsFileContent.getCredDict())

    # Connect and get info.
    awsConnect = awsConnectClasses.Connect(
                 awsCredentials.getCredDict())

    # Parse response.
    awsInstances = awsInstanceClasses.Instances(
                   awsConnect.getResonse())
