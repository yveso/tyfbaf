# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Tests 😱
- Using [isort](https://pycqa.github.io/isort/index.html) for imports
- Using [pre-commit](https://pre-commit.com/)

## [0.0.8] - 2022-03-15

### Fixed

- Circular reference

## [0.0.7] - 2022-03-14

### Added

- Docstrings 📖
- `token` module
  - New functions `request_and_save` and `invalidate_saved_token`.
  - You can now save a token, so you don't need to pass it with every request.
  - The functions in the `http` module will use the saved token automatically.
- `cmsquery_utils` module
  - `SI` enum for CMS query fields, so you get autocompletion in your editor. 😎

### Fixed

- Minor fixes

## [0.0.6] - 2022-03-01

### Added

- Modules
  - `cmsquery`: Makes querying the CMS easier.
  - `cmsquery_utils`: Helps you writing an actual query statement.

### Fixed

- Version Badge in README.md 😂
- Minor fixes

## [0.0.5] - 2022-02-23

### Added

- Basic functionality
- `http` module
  - `get` function
  - `post` function
- `token` module
  - `request` function
  - `invalidate` function
