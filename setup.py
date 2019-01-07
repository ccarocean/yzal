import os
from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as infile:
        text = infile.read()
    return text


setup(
    name='yzal',
    version='0.0.5',
    author='Michael R. Shannon',
    author_email='mrshannon.aerospace@gmail.com',
    description='Lazy evaluation for Python.',
    long_description=read('README.rst'),
    license='MIT',
    url='https://github.com/ccarocean/yzal',
    packages=find_packages(),
    package_data={
        'yzal': ['py.typed']
    },
    setup_requires=['pytest-runner'],
    install_requires=[
        'lazy-object-proxy',
        'mypy;python_version=="3.4"'
    ],
    tests_require=[
        'pytest',
        'pytest-mock'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=False
)
