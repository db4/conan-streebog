cmake_minimum_required(VERSION 2.8.12)

project(test C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

add_executable(test main.c)
target_link_libraries(test CONAN_PKG::streebog)

