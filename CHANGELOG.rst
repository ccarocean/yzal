Changelog
=========


Unreleased_
-----------




v0.0.4_ - 2019-01-07
--------------------

Added
-----

* Documentation via Sphinx, build with :code:`make html` or :code:`make pdf`.

Changed
-------

* Make `strict` relaxed by default, that is it will return the value given if
  it is not a thunk.




v0.0.4_ - 2019-01-03
--------------------

Added
^^^^^

* This CHANGELOG.
* Type hint support in compliance with `PEP 526`_ and `PEP 561`_.
* Use mypy for static type checking.
* Dependency on mypy_ when running on Python 3.4.

Changed
^^^^^^^

* Changed from a module based distribution to a package based distribution.

Removed
^^^^^^^

* Unused rule from tox_ configuration.




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




.. _mypy: http://mypy-lang.org/
.. _tox: https://tox.readthedocs.io/en/latest/
.. _PEP 526: https://www.python.org/dev/peps/pep-0526/
.. _PEP 561: https://www.python.org/dev/peps/pep-0561/

.. _Unreleased: https://github.com/ccarocean/yzal/compare/v0.0.5...HEAD
.. _v0.0.5: https://github.com/ccarocean/yzal/compare/v0.0.4...v0.0.5
.. _v0.0.4: https://github.com/ccarocean/yzal/compare/v0.0.3...v0.0.4
.. _v0.0.3: https://github.com/ccarocean/yzal/compare/v0.0.2...v0.0.3
.. _v0.0.2: https://github.com/ccarocean/yzal/compare/v0.0.1...v0.0.2
