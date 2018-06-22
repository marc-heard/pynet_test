#!/usr/bin.env python

from __future__ import print_function, unicode_literals
import getpass
import snmp_helper

SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'


def main ():
    try:
        ip_addr1 = raw_input("pynet-rtr1 IP Address: ")
        ip_addr2 = raw_input("pynet-rtr2 IP Address: ")
    except NameError:
        ip_addr1 = input("pynet-rtr1 IP Address: ")
        ip_addr2 = input("pynet-rtr2 IP Address: ")

    community_string = getpass.getpass(prompt="Community String: ")

    pynet_rtr1 = (ip_addr1, community_string, 161)
    pynet_rtr2 = (ip_addr2, community_string, 161)

    for a_device in (pynet_rtr1, pynet_rtr2):
        print("\n****************")
        for the_oid in (SYS_NAME, SYS_DESCR):
            snmp_data = snmp_helper.snmp_get_oid(a_device, oid=the_oid)
            output = snmp_helper.snmp_extract(snmp_data)

            print(output)

        print("****************")
    print()


if __name__ == "__main__":
    main()
