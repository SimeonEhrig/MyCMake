# version 3.2 is feature complete for modern CMake
cmake_minimum_required(VERSION 3.2)

message("Child (before): myVar    = ${myVar}")
message("Child (before): childVar = ${childVar}")

set(myVar bar)
set(childVar fuzz)

message("Child (after): myVar    = ${myVar}")
message("Child (after): childVar = ${childVar}")
