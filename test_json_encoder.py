from json_encoder import *
from installed_packages import Package
from installed_modules import Module


def test_datetime_encoder_class_exists():
    assert callable(PackageEncoder)


def test_datetime_encoder_class_is_json_encoder():
    assert issubclass(PackageEncoder, JSONEncoder)


def test_datetime_encoder_serialize_date():
    assert PackageEncoder().encode(datetime.date(2019, 1, 1)) == '"2019-01-01"'


def test_datetime_encoder_serialize_datetime():
    assert (
        PackageEncoder().encode(datetime.datetime(2019, 1, 1, 0, 0, 0))
        == '"2019-01-01T00:00:00"'
    )


def test_datetime_encoder_serialize_package():
    assert (
        PackageEncoder().encode(Package("foo", "1.0", datetime.date(2019, 1, 1)))
        == '{"name": "foo", "version": "1.0", "install_date": "2019-01-01"}'
    )


def test_datetime_encoder_serialize_module():
    assert (
        PackageEncoder().encode(Module("foo", "1.0", datetime.date(2019, 1, 1)))
        == '{"name": "foo", "version": "1.0", "install_date": "2019-01-01"}'
    )


def test_datetime_encoder_serialize_package_list():
    assert (
        PackageEncoder().encode([Package("foo", "1.0", datetime.date(2019, 1, 1))])
        == '[{"name": "foo", "version": "1.0", "install_date": "2019-01-01"}]'
    )


def test_datetime_encoder_serialize_module_list():
    assert (
        PackageEncoder().encode([Module("foo", "1.0", datetime.date(2019, 1, 1))])
        == '[{"name": "foo", "version": "1.0", "install_date": "2019-01-01"}]'
    )


def test_datetime_encoder_serialize_package_dict():
    assert (
        PackageEncoder().encode(
            {
                "packages": [Package("foo", "1.0", datetime.date(2019, 1, 1))],
                "modules": [Module("foo", "1.0", datetime.date(2019, 1, 1))],
            }
        )
        == '{"packages": [{"name": "foo", "version": "1.0", "install_date": "2019-01-01"}], "modules": [{"name": "foo", "version": "1.0", "install_date": "2019-01-01"}]}'
    )


def test_datetime_encoder_serialize_other():
    assert PackageEncoder().encode("foo") == '"foo"'
    assert PackageEncoder().encode(1) == "1"
    assert PackageEncoder().encode(1.0) == "1.0"
    assert PackageEncoder().encode(True) == "true"
    assert PackageEncoder().encode(False) == "false"
    assert PackageEncoder().encode(None) == "null"
    assert PackageEncoder().encode([1, 2, 3]) == "[1, 2, 3]"
    assert PackageEncoder().encode({"foo": "bar"}) == '{"foo": "bar"}'
