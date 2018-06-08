#!/usr/bin/env python
"""
Read and print Yaml and Json files
"""

from __future__ import unicode_literals, print_function
import yaml
import json
from pprint import pprint

def output_format(my_list, my_str):
    """Make the output format easier to read."""
    print('\n\n')
    print('#' * 3)
    print('#' * 3 + my_str)
    print('#' * 3)
    pprint(my_list)

def main():
    """Read Yaml and Json files. Pretty Print to standard out."""
    yaml_file = 'my_test.yml'
    json_file = 'my_test.json'

    with open(yaml_file) as f:
        yaml_list = yaml.load(f)

    with open(json_file) as f:
        json_list = json.load(f)

    output_format(yaml_list, 'YAML')
    output_format(json_list, 'JSON')
    print('\n')

if __name__ == "__main__":
    main()
