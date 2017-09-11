#!/usr/bin/python

# @Author: Tobias Holmqvist <tohol>
# @Date:   2017-09-08
# @Email:  tobias.m.holmqvist@gmail.com
# @Project: awsCrud
# @Last modified by:   tohol
# @Last modified time: 2017-09-11
# @License: GPLv3

import argparse, mainAwsCrud

# Create parser object.
parser = argparse.ArgumentParser()

# Positional argument, should always exist.
parser.add_argument('instance',
                    help='[all/instanceID]',
                    nargs='?',
                    default=None)

# Optional argument, run in verbose mode.
parser.add_argument('-v', '--verbose',
                    help='increase output verbosity',
                    action='store_true')

# Optional argument, get status.
parser.add_argument('-s', '--status',
                    help='[all/instanceID] --status',
                    action='store_true')

# Optional argument, run instance.
parser.add_argument('-r', '--run',
                    help='[all/instanceID] --run',
                    action='store_true')

# Optional argument, poweroff instance.
parser.add_argument('-p', '--poweroff',
                    help='[all/instanceID] --poweroff',
                    action='store_true')

# Optional argument, reboot instance.
parser.add_argument('-b', '--reboot',
                    help='[all/instanceID] --reboot',
                    action='store_true')

# Optional argument, delete instance.
parser.add_argument('-d', '--delete',
                    help=' [all/instanceID] --delete',
                    action='store_true')

# Optional argument, create new instance.
parser.add_argument('-c', '--create',
                    help='[new/clone] --create',
                    action='store_true')

# Try to parse incoming arguments, or print help.
args = parser.parse_args()

# Make sure that argument is existing, or exit with 0.
if  (not(args.instance)):
    print('\nMISSING INSTANCE: specify all/instanceID\n')
    sys.exit(0)

# Make sure status/run/poweroff/reboot/delete/create is not combined
# or exit with 0.
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

# Run main function
mainAwsCrud.main()
