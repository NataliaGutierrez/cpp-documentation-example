﻿cmake_minimum_required (VERSION 3.8)

project ("Animals")

# Add the cmake folder so the FindSphinx module is found
set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/cmake" ${CMAKE_MODULE_PATH})

add_subdirectory ("src/cppsrc")
add_subdirectory ("docs")
