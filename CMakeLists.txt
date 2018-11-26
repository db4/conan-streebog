cmake_minimum_required(VERSION 2.8.12)

project(streebog C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

include_directories(streebog-${STREEBOG_VERSION})

add_library(${PROJECT_NAME}
  streebog-${STREEBOG_VERSION}/gost3411-2012-core.c
)
