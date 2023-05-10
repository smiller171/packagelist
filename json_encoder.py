#! /usr/bin/python3

import json
import datetime
from json import JSONEncoder
from installed_modules import Module
from installed_packages import Package


class PackageEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        elif isinstance(obj, Package):
            return obj.__dict__()
        elif isinstance(obj, Module):
            return obj.__dict__()
        else:
            return JSONEncoder.default(self, obj)
