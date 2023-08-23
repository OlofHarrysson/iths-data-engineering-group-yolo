import platform


# test to check python version is 3.10
def test_python_version():
    # varible with system version information
    python_version = platform.python_version()
    assert python_version[:-3] == "3.10"
