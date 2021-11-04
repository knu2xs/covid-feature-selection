from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='covid_feature_selection',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='Finding significant features based on a scalar metric for Covid.',
    long_description=long_description,
    author='Joel McCune',
    license='Apache 2.0',
)
