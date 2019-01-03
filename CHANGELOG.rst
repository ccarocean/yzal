Changelog
=========


Unreleased_
-----------

Added
^^^^^

* This CHANGELOG.




v0.0.3_ - 2018-12-21
--------------------

Fixed
^^^^^

* Packaging bug related to yzal being a module only package.




v0.0.2_ - 2018-12-21
--------------------

Added
^^^^^

* Travis CI integration testing.
* Support for tox_.


Changed
^^^^^^^

* Moved from ALPHA to BETA status.
* :code:`requirements.txt` is used only for development, release dependencies
  are now in :code:`setup.py`.

Fixed
^^^^^

* Bad links in README.




v0.0.1 - 2018-12-19
-------------------

Added
^^^^^

* :code:`Thunk` class to delay a computation until it's value is needed.
* :code:`strict` function to force a :code:`Thunk` be evaluated.
* :code:`lazy` decorator to construct lazy functions.


.. _tox: https://tox.readthedocs.io/en/latest/

.. _Unreleased: https://github.com/ccarocean/yzal/compare/v0.0.3...HEAD
.. _v0.0.3: https://github.com/ccarocean/yzal/compare/v0.0.2...v0.0.3
.. _v0.0.2: https://github.com/ccarocean/yzal/compare/v0.0.1...v0.0.2