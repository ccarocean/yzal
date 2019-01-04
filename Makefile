.PHONY: all init check test coverage html pdf clean clean-all

module=yzal

all:
	@echo 'init             install development requirements'
	@echo 'check            run static code checkers'
	@echo 'test             run unit tests'
	@echo 'coverage         generate HTML coverage report'
	@echo 'html             build HTML documentation'
	@echo 'pdf              build PDF documentation (requires LaTeX)'
	@echo 'package          build source and binary packages'
	@echo 'clean            cleanup source tree'
	@echo 'clean-all        also removes tox and eggs'

init:
	@pip install -q -r requirements.txt

test: check
	@python -m pytest -v --cov=$(module) --cov-branch

coverage: check
	@python -m pytest -v --cov=$(module) --cov-branch \
		--cov-report html

check:
	@python -m pylint --rcfile=pylintrc $(module)
	@python -m pycodestyle $(module) tests
	@python -m pydocstyle $(module)
	@mypy $(module)

html:
	@$(MAKE) -C docs html

pdf:
	@$(MAKE) -C docs latexpdf

package: test
	@python setup.py sdist
	@python setup.py bdist_wheel

clean:
	@rm -f *.pyc
	@rm -f tests/*.pyc
	@rm -rf tests/.pytest_cache
	@rm -f tests/.coverage
	@rm -f .coverage
	@rm -rf htmlcov
	@rm -rf __pycache__
	@rm -rf *.egg-info
	@rm -rf dist

clean-all: clean
	@rm -rf .tox
	@rm -rf .eggs
	@$(MAKE) -C docs clean
