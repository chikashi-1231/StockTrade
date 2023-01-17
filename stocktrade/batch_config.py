#!/usr/bin/env python3

import yaml
import sys

class Config:

    def __init__(self, conf_file):
        conf_file = conf_file or 'develop'
        try:
            with open(f"{conf_file}.yaml") as file:
                self.conf = yaml.safe_load(file)
        except Exception as e:
            print('Exception occurred while loading YAML...', file=sys.stderr)
            print(e, file=sys.stderr)
            sys.exit(1)

    def load(self, item):
        return self.conf[item]