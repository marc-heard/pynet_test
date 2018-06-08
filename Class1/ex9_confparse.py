#!/usr/bin/env python
"""
Parse 'cisco_ipsec.txt'. Find and print the crypto maps
"""

from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse

def main():
    """ Find cyrpto map entries and print the children """

    cisco_file = 'cisco_ipsec.txt'
    
    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'pfs group2')

    print("\nCrypto Maps using PFS group2:")
    for entry in crypto_maps:
        print(" {}".format(entry.text))
    print("")

if __name__ == "__main__":
    main()
