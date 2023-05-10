import json
from get_packagelist import *
from installed_packages import *
from installed_modules import *


def test_get_packagelist_exists():
    assert callable(get_packagelist)


def test_get_packagelist_packages():
    assert type(get_packagelist("packages")) is list
    assert isinstance(get_packagelist("packages")[0], Package)


def test_get_packagelist_modules():
    assert type(get_packagelist("modules")) is list
    assert isinstance(get_packagelist("modules")[0], Module)


def test_get_packagelist_both():
    assert type(get_packagelist("both")) is dict
    assert type(get_packagelist("both")["packages"]) is list
    assert isinstance(get_packagelist("both")["packages"][0], Package)
    assert type(get_packagelist("both")["modules"]) is list
    assert isinstance(get_packagelist("both")["modules"][0], Module)


def test_get_packagelist_invalid():
    assert get_packagelist("foo") is None


def test_get_packagelist_dict():
    assert type(get_packagelist("packages", "python")) is list
    assert type(get_packagelist("modules", "python")) is list
    assert type(get_packagelist("both", "python")) is dict


def test_get_packagelist_json():
    assert type(get_packagelist("packages", "json")) is str
    assert type(json.loads(get_packagelist("packages", "json"))) is list
    assert type(json.loads(get_packagelist("both", "json"))) is dict
