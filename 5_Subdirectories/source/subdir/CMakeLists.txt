# version 3.2 is feature complete for modern CMake
cmake_minimum_required(VERSION 3.2)

message("subdir: CMAKE_SOURCE_DIR         = ${CMAKE_SOURCE_DIR}")
message("subdir: CMAKE_BINARY_DIR         = ${CMAKE_BINARY_DIR}")
message("subdir: CMAKE_CURRENT_SOURCE_DIR = ${CMAKE_CURRENT_SOURCE_DIR}")
# by default, copy the folder structure to build
message("subdir: CMAKE_CURRENT_BINARY_DIR = ${CMAKE_CURRENT_BINARY_DIR}")

# output:
#  subdir: CMAKE_SOURCE_DIR         = <project>/MyCMake/5_Subdirectories/source
#  subdir: CMAKE_BINARY_DIR         = <project>/MyCMake/5_Subdirectories/build
#  subdir: CMAKE_CURRENT_SOURCE_DIR = <project>/MyCMake/5_Subdirectories/source/subdir
#  subdir: CMAKE_CURRENT_BINARY_DIR = <project>/MyCMake/5_Subdirectories/build/subdir
