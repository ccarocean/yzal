import os
from setuptools import setup


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as infile:
        text = infile.read()
    return text


setup(
    name='yzal',
    version='0.0.3',
    author='Michael R. Shannon',
    author_email='mrshannon.aerospace@gmail.com',
    description='Lazy evaluation for Python.',
    long_description=read('README.rst'),
    license='MIT',
    url='https://github.com/ccarocean/yzal',
    py_modules=['yzal'],
    setup_requires=['pytest-runner'],
    install_requires=[
        'lazy-object-proxy',
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
