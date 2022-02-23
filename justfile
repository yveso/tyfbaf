set shell := ["powershell.exe", "-c"]

# build package
build:
    flit build
# build package and install locally
install:
    flit install
# publish package to PyPI
publish:
    flit publish
# publish package to Test-PyPI
publish-test:
    flit publish --repository testpypi
