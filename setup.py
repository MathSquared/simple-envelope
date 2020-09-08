from setuptools import setup, find_packages

setup(
    name='simple_envelope',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'fpdf>=1.7',
    ],
)
