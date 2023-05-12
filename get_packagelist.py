#! /usr/bin/env python3

import logging
import json
from json_encoder import PackageEncoder
from installed_packages import get_packages
from installed_modules import get_modules
from os import environ


LOGLEVEL = environ.get("LOGLEVEL", "ERROR").upper()
logging.basicConfig(level=LOGLEVEL)


def get_packagelist(in_type="both", out_type="python"):
    if in_type.lower() == "packages":
        result = get_packages()
    elif in_type.lower() == "modules":
        result = get_modules()
    elif in_type.lower() == "both":
        result = {"packages": get_packages(), "modules": get_modules()}
    else:
        logging.error(f"Invalid type: {in_type}")
        return None

    if out_type.lower() == "python":
        return result
    elif out_type.lower() == "json":
        return PackageEncoder().encode(result)
    else:
        logging.error(f"Invalid type: {out_type}")
        return None


print(get_packagelist("both", "json"))
