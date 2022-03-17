set shell := ["powershell.exe", "-c"]

# build package
build:
    flit build
# build package and install locally
install:
    flit install
# build package and install locally including all dependencies
install-all:
    flit install --deps all
# publish package to PyPI
publish:
    flit publish
# publish package to Test-PyPI
publish-test:
    flit publish --repository testpypi
# run pytest
test:
    pytest
# run pytest with coverage
test-coverage:
    pytest --cov=tyfbaf
