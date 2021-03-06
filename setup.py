import os
import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename, 'r') as fp:
        contents = fp.read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", contents).group(1)


version = get_version(os.path.join('django_perf_rec', '__init__.py'))

with open('README.rst', 'r') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', 'r') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='django-perf-rec',
    version=version,
    description="Keep detailed records of the performance of your Django "
                "code.",
    long_description=readme + '\n\n' + history,
    author='Adam Johnson',
    author_email='me@adamj.eu',
    url='https://github.com/adamchainz/django-perf-rec',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[
        'Django>=1.11',
        'patchy',
        'PyYAML',
        'sqlparse>=0.3.0',
    ],
    python_requires='>=3.4',
    license='MIT',
    zip_safe=False,
    keywords='Django',
    entry_points={
        'pytest11': ['django_perf_rec = django_perf_rec.pytest_plugin'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
