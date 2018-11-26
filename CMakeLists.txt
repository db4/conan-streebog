cmake_minimum_required(VERSION 2.8.12)

project(streebog C)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

include_directories(streebog-${STREEBOG_VERSION})

add_library(${PROJECT_NAME}
  streebog-${STREEBOG_VERSION}/gost3411-2012-core.c
)
if(NOT WIN32)
  if(SSE2)
    target_compile_options(${PROJECT_NAME} PRIVATE -msse2)
  endif()
  if(SSE41)
    target_compile_options(${PROJECT_NAME} PRIVATE -msse4.1)
  endif()
endif()
