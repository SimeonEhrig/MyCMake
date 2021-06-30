# version 3.2 is feature complete for modern CMake
cmake_minimum_required(VERSION 3.2)

# set project name and meta information
project(subdirectories
  VERSION 1.0
  LANGUAGES CXX)

################################################################################
# Source and build paths
################################################################################

# path of the top level CMakeLists.txt
message("top: CMAKE_SOURCE_DIR         = ${CMAKE_SOURCE_DIR}")
# path of the build folder
message("top: CMAKE_BINARY_DIR         = ${CMAKE_BINARY_DIR}")
# path of the current CMakeLists.txt
message("top: CMAKE_CURRENT_SOURCE_DIR = ${CMAKE_CURRENT_SOURCE_DIR}")
# path of the current folder in the build directory
# by default, cmake mirrors the folder structure of the source folder to the build folder
message("top: CMAKE_CURRENT_BINARY_DIR = ${CMAKE_CURRENT_BINARY_DIR}")
# output
#  top: CMAKE_SOURCE_DIR         = <project>/MyCMake/5_Subdirectories/source
#  top: CMAKE_BINARY_DIR         = <project>/MyCMake/5_Subdirectories/build
#  top: CMAKE_CURRENT_SOURCE_DIR = <project>/MyCMake/5_Subdirectories/source
#  top: CMAKE_CURRENT_BINARY_DIR = <project>/MyCMake/5_Subdirectories/build

add_subdirectory(subdir)
# output
#  subdir: CMAKE_SOURCE_DIR         = /home/simeon/projects/MyCMake/5_Subdirectories/source
#  subdir: CMAKE_BINARY_DIR         = /home/simeon/projects/MyCMake/5_Subdirectories/build
#  subdir: CMAKE_CURRENT_SOURCE_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/source/subdir
#  subdir: CMAKE_CURRENT_BINARY_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/build/subdir

message("top: CMAKE_CURRENT_SOURCE_DIR = ${CMAKE_CURRENT_SOURCE_DIR}")
message("top: CMAKE_CURRENT_BINARY_DIR = ${CMAKE_CURRENT_BINARY_DIR}")
# output:
#  top: CMAKE_CURRENT_SOURCE_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/source
#  top: CMAKE_CURRENT_BINARY_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/build

################################################################################
# scope of variables
################################################################################
# Variables of the parent scope are available in the child scope
# changes in the child scope does not overwrite variables in the parent scope

message("")
set(myVar foo)
message("Parent (before): myVar    = ${myVar}")
message("Parent (before): childVar = ${childVar}")

add_subdirectory(variables)

message("Parent (after): myVar    = ${myVar}")
message("Parent (after): childVar = ${childVar}")
# output:
#  Parent (before): myVar    = foo
#  Parent (before): childVar =
#  Child (before): myVar    = foo
#  Child (before): childVar =
#  Child (after): myVar    = bar
#  Child (after): childVar = fuzz
#  Parent (after): myVar    = foo
#  Parent (after): childVar =

message("")
# write a variable to the parent scope with set(varname value PARENT_SCOPE)
# the option PARENT_SCOPE does not overwrite the variable in the child scope
set(myVar2 foo)
message("Parent (before): myVar2    = ${myVar2}")
add_subdirectory(parent_scope)
message("Parent (after): myVar2    = ${myVar2}")
# output:
#  Parent (before): myVar2    = foo
#  Child (before): myVar2    = foo
#  Child (after): myVar2    = foo
#  Parent (after): myVar2    = bar

################################################################################
# include command
################################################################################
# rules of include()
# - expects the file name (can be everything, but <filename>.cmake is common)
# - no new variable scope
# - by default, new policy scope
# - CMAKE_CURRENT_SOURCE_DIR and CMAKE_CURRENT_BINARY_DIR points to the calling file

message("")
set(includeVar par)
message("includeVar (before add_subdirectory) = ${includeVar}")
message("====")
add_subdirectory(include)
message("includeVar (after add_subdirectory) = ${includeVar}")
message("====")
include(include/CMakeLists.txt)
message("includeVar (after include) = ${includeVar}")
message("")
# output:
#  includeVar (before add_subdirectory) = par
#  ====
#  CMAKE_CURRENT_SOURCE_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/source/include
#  CMAKE_CURRENT_BINARY_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/build/include
#  CMAKE_CURRENT_LIST_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/source/include
#  CMAKE_CURRENT_LIST_FILE = /home/simeon/projects/MyCMake/5_Subdirectories/source/include/CMakeLists.txt
#  CMAKE_CURRENT_LIST_LINE = 9
#  includeVar (after add_subdirectory) = par
#  ====
#  CMAKE_CURRENT_SOURCE_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/source
#  CMAKE_CURRENT_BINARY_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/build
#  CMAKE_CURRENT_LIST_DIR = /home/simeon/projects/MyCMake/5_Subdirectories/source/include
#  CMAKE_CURRENT_LIST_FILE = /home/simeon/projects/MyCMake/5_Subdirectories/source/include/CMakeLists.txt
#  CMAKE_CURRENT_LIST_LINE = 9
#  includeVar (after include) = inc

################################################################################
# return
################################################################################
# - the execution of a file can be stopped with the function return() (not in functions)
# - the function include_guard() works like the #if guard in C header files (need cmake 3.10)
