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
    crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

    for c_map in crypto_maps:
        print()
        print(c_map.text)
        for child in c_map.children:
            print(child.text)

        print()

if __name__ == "__main__":
    main()
