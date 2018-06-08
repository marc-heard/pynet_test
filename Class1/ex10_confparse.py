#!/usr/bin/env python
"""
Parse 'cisco_ipsec.txt'. Find and print the crypto maps not using AES
"""

from __future__ import unicode_literals, print_function
import re
from ciscoconfparse import CiscoConfParse

def main():
    """ Find cyrpto map entries and print the children and their corresponding transform set name """

    cisco_file = 'cisco_ipsec.txt'
    
    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'AES')

    print("\nCrypto maps not using AES:")
    for entry in crypto_maps:
        for child in entry.children:
            if 'transform' in child.text:
                match  = re.search(r"set transform-set (.*)$", child.text)
                encryption = match.group(1)
        print("  {} >>> {}".format(entry.text.strip(), encryption))        

    print("")

if __name__ == "__main__":
    main()
