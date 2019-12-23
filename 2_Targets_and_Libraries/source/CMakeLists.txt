# version 3.2 is feature complete for modern CMake
cmake_minimum_required(VERSION 3.16)

project(targets_and_linking
  VERSION 1.1
  LANGUAGES CXX)

################################################################################
# exclude executable from default build rule
################################################################################

# EXCLUDA_FROM_ALL -> remove this executable from the default build
# will not build if `make` was running
# needs `make forDev` to build
add_executable(forDev EXCLUDE_FROM_ALL dev.cpp)

################################################################################
# basic: build and link libraries
################################################################################
# the workflow is:
# 1. build object file
# 2. build library
# 3. link object file and library

# build object file (.o) and link it to an executable
add_executable(exe1 exe1.cpp)

# build library file
# add prefix lib and file extension .so or .a
# the library type is depend on the variable BUILD_SHARED_LIBS
add_library(lib1 lib1.cpp)

# link self library with executable
target_link_libraries(exe1 lib1)

################################################################################
# advanced: build and link libraries
################################################################################

add_executable(exe2 exe2.cpp)
add_library(lib2 lib2.cpp)
# compile static library every time
add_library(lib21 STATIC lib21.cpp)

# PRIVATE means that lib21 is used only for internal implementation
# if you link lib2, you have no idea about lib21
target_link_libraries(lib2
  PRIVATE lib21)
target_link_libraries(exe2 lib2)



add_executable(exe3 exe3.cpp)
add_library(lib3 lib3.cpp)
# compile shared library every time
add_library(lib31 SHARED lib31.cpp)

# PUBLIC is necessary if you need knowledge about lib31
# for example, a function definition of lib3 use a definition of lib31 as argument
target_link_libraries(lib3
  PUBLIC lib31)
target_link_libraries(exe3 lib3)
