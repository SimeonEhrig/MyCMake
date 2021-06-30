cmake_minimum_required(VERSION 3.5)

# set project name and meta information
project(func
  VERSION 1.0
  LANGUAGES CXX)

################################################################################
# functions and macros
################################################################################
# functions
# - arguments are CMake variables
# - has it's own scope
#
# macros
# - arguments are strings
# - scope of caller

# arg is CMake variable
function(func arg)
  if(DEFINED arg)
    message("Function arg is a defined variable") # is printed
  else()
    message("Function arg is NOT a defined variable")
  endif()
  message("func arg is: ${arg}")
  # output:
  #  func arg is: foofunc

  # "return value"
  # set(varName value PARENT_SCOPE)
endfunction()

# arg is a string
macro(macr arg)
  if(DEFINED arg)
    message("Macro arg is a defined variable")
  else()
    message("Macro arg is NOT a defined variable") # is printed
  endif()
  message("marc arg is: ${arg}")
  # output:
  #  func arg is: foomarc
endmacro()

func(foofunc)
macr(foomarc)

message("")

################################################################################
# argument handling
################################################################################

# extra unnamed variables are allowed every time
function(func2 arg1 arg2 arg3)
  message("func2 ARGC: ${ARGC}") # func2 ARGC: 9
  message("func2 ARGV: ${ARGV}") # func2 ARGV: A;B;C;D;E;F;G;H;I
  message("func2 ARGN: ${ARGN}") # func2 ARGN: D;E;F;G;H;I
endfunction()

func2(A B C D E F G H I)

message("")

function(func3)
  set(prefix FUNC3)
  set(noValues ENABLE_NET COOL_STUFF)
  set(singleValues TARGET)
  set(multiValues SOURCES IMAGES)

  cmake_parse_arguments(${prefix}
    "${noValues}"
    "${singleValues}"
    "${multiValues}"
    ${ARGN})

  message("Option summary:")
  foreach(arg IN LISTS noValues)
    if(${prefix}_${arg})
      message("  ${arg} enabled")
    else()
      message("  ${arg} disabled")
    endif()
  endforeach()

  foreach(arg IN LISTS singleValues multiValues)
    message("  ${arg} = ${${prefix}_${arg}}")
  endforeach()
endfunction()

func3(SOURCES foo.cpp bar.cpp
  TARGET myApp ENABLE_NET)
#output:
#  Option summary:
#    ENABLE_NET enabled
#    COOL_STUFF disabled
#    TARGET = myApp
#    SOURCES = foo.cpp;bar.cpp
#    IMAGES =

func3(COOL_STUFF
  TARGET dummy
  IMAGES here.png threre.png gone.png)
#output:
#  Option summary:
#    ENABLE_NET disabled
#    COOL_STUFF enabled
#    TARGET = dummy
#    SOURCES =
#    IMAGES = here.png;threre.png;gone.png
