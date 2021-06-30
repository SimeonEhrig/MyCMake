# version 3.2 is feature complete for modern CMake
cmake_minimum_required(VERSION 3.2)

message("Child (before): myVar2    = ${myVar2}")

set(myVar2 bar PARENT_SCOPE)

message("Child (after): myVar2    = ${myVar2}")
