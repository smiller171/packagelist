from installed_modules import *


def test_installed_modules_exists():
    assert callable(get_modules)


def test_installed_modules_returns_list():
    assert type(get_modules()) is list


def test_module_data_format():
    for mod in get_modules():
        assert isinstance(mod, Module)


def test_module_data_spot_check():
    assert type(get_modules()[0].name) is str
    assert type(get_modules()[0].version) is str
    assert type(get_modules()[0].install_date) is datetime


def test_list_not_empty():
    assert len(get_modules()) > 0
