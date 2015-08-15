# coding=utf-8
from setuptools import setup

setup(
    name='pyMorfologik',
    packages=['pyMorfologik'],
    version='0.2.2',
    install_requires=[],
    author='Damian Mirecki',
    author_email='dmirecki.dm@gmail.com',
    description='Binding for Morfologik tool',
    url='https://github.com/dmirecki/pyMorfologik',
    keywords=['morfologik'],
    include_package_data=True,
    package_data={
        '': ['*.jar']
    }
)
