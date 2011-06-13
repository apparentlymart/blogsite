from setuptools import setup

setup(
    name='blogsite',
    version='1.0',
    packages=['blogsite'],
    include_package_data=True,
    requires=['Django', 'iso8601'],
)
