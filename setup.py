#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Soshi Mizutani",
    author_email='soshi.mizutani@oist.jp',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
	'Programming Language :: Python :: 3.9',
    ],
    description="learn python OPP by implementing objects in One Piece ",
    entry_points={
        'console_scripts': [
            'pyonepiece=pyonepiece.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyonepiece',
    name='pyonepiece',
    packages=find_packages(include=['pyonepiece', 'pyonepiece.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/soshimizutani/pyonepiece',
    version='0.1.0',
    zip_safe=False,
)
