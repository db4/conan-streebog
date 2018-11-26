# conan-streebog

[Conan.io](https://conan.io) package for [GOST R 34.11-2012: RFC-6986 cryptographic hash function](https://github.com/adegtyarev/streebog)

| Appveyor | Travis |
|-----------|--------|
|[![Build Status](https://ci.appveyor.com/api/projects/status/github/db4/conan-streebog?branch=master&svg=true)](https://ci.appveyor.com/project/db4/conan-streebog)|[![Build Status](https://travis-ci.org/db4/conan-streebog.svg?branch=master)](https://travis-ci.org/db4/conan-streebog)|

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload streebog/0.12/stable --all

## Reuse the packages

### Basic setup

    $ conan install streebog/0.12/stable

### Project setup

If you handle multiple dependencies in your project, it would be better to add a *conanfile.txt*

    [requires]
    streebog/0.12/stable

    [generators]
    txt
    cmake


