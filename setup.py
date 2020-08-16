from setuptools import setup, find_packages

setup_args = dict(
    name='paymentsds-mpesa',
    version='0.1a1',
    description='MPesa Python SDK',
    license='Apache-2.0',
    author='Edson Michaque',
    author_email='edson@michaque.com',
    keywords=['MPesa'],
    url='https://github.com/paymentsds/mpesa-python-sdk'
)

if __name__ == '__main__':
    setup(**setup_args)