#! /usr/bin/python3
import datetime
import pkg_resources
import logging
from datetime import datetime
from os import path, environ

LOGLEVEL = environ.get("LOGLEVEL", "ERROR").upper()
logging.basicConfig(level=LOGLEVEL)


class Module:
    # Class auto-generated by GitHub Copilot
    def __init__(self, name, version, install_date):
        self.name = name
        self.version = version
        self.install_date = install_date

    def __repr__(self):
        return f"Module({self.name}, {self.version}, {self.install_date})"

    def __str__(self):
        return f"{self.name}"

    def __dict__(self):
        return {
            "name": self.name,
            "version": self.version,
            "install_date": self.install_date,
        }


def get_modules():
    # Get a list of installed modules, their versions, and their installation dates
    # Returns a list of dicts
    # Dict keys: name, version, install_date
    # Dict values: str, str, datetime

    mod_list = []

    for mod in pkg_resources.working_set:
        logging.debug("mod_key: %s", mod.key)

        mod_path = mod.egg_info if mod.egg_info else mod.path

        logging.debug("mod_path: %s", mod_path)

        mod_date = datetime.fromtimestamp(path.getctime(mod_path))
        logging.debug("mod_date: %s", mod_date)

        mod_list.append(Module(mod.key, mod.version, mod_date))

    return mod_list