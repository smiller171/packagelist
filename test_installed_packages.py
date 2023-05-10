from installed_packages import *


def test_tests_run():
    assert True


def test_get_packages_exists():
    assert callable(get_packages)


def test_packages_is_list():
    assert type(get_packages()) is list


def test_pkg_data_format():
    for pkg in get_packages():
        assert isinstance(pkg, Package)


def test_pkg_data_spot_check():
    assert type(get_packages()[0].name) is str
    assert type(get_packages()[0].version) is str
    assert type(get_packages()[0].install_date) is datetime


def test_list_not_empty():
    assert len(get_packages()) > 0


def test_package_dict():
    assert type(get_packages()[0].__dict__()) is dict
    assert type(get_packages()[0].__dict__()["name"]) is str
    assert type(get_packages()[0].__dict__()["version"]) is str
    assert type(get_packages()[0].__dict__()["install_date"]) is datetime
