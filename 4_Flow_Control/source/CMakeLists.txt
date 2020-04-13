cmake_minimum_required(VERSION 3.4)

# set project name and meta information
project(flowControl
  VERSION 1.0
  LANGUAGES CXX)
################################################################################
# general construct and conditions
################################################################################

if(YES)
  message("YES")
else()
  message("NO")
endif()

if(NO)
  message("YES")
elseif(YES)
  message("elseif YES")
endif()

message("true are: 1, ON, YES, TRUE, Y, non-zero number")
message("wrong are: 0, OFF, NO, FALSE, N, IGNORE, NOTFOUND, empty string, string ends with -NOFOUND")

################################################################################
# use variables
################################################################################

set(A YES)
set(B 0)

if(${A})
  message("true A")
endif()

if(${B})
else()
  message("wrong B")
endif()

if(A)
  message("evaluate variable A")
endif()

################################################################################
# logic operators
################################################################################

if(NOT B)
  message("wrong B")
endif()

if(A OR B)
  message("A OR B")
endif()

set(C OFF)

if(NOT ( C AND ( A OR B)))
  message("NOT (C AND ( A OR B ))")
endif()

################################################################################
# Comparison
################################################################################

# Numeric: LESS, GREATER, EQUAL, LESS_EQUAL, GREATER_EQUAL
if(2 GREATER 1)
  message("2 > 1")
endif()

# Versions numbers: VERSION_LESS, VERSION_GREATER, VERSION_EQUAL,
#                   VERSION_LESS_EQUAL, VERSION_GREATER_EQUAL
# version form: major[.minor[.patch[.tweak]]]
# missing level will be replaced by 0
if(1.2 VERSION_EQUAL 1.2.0)
  message("version 1.2 is the same as 1.2.0")
endif()

# String: STRLESS, STRGREATER, STREQUAL, STRLESS_EQUAL, STRGREATER_EQUAL
# strings will be lexical ordered

if("ACB" STRGREATER "ABC")
  message("ACB is greater than ABC")
endif()

# matching a regex is also possible
# if(value MATCHES regex)
set(who "Fred")
if("Hi from ${who}" MATCHES "Hi from (Fred|Barney).*")
  message("${CMAKE_MATCH_1} says hello")
endif()

set(who "Barney")
if("Hi from ${who}" MATCHES "Hi from (Fred|Barney).*")
  message("${CMAKE_MATCH_1} says hello")
endif()

################################################################################
# File System Tests
################################################################################

# if(EXISTS pathToFileOrDir)
# if(IS_DIRECTORY pathToDir)
# if(IS_SYMLINK fileName)
# if(IS_ABSOLUTE path)

# if one of both files missing: TRUE
# if both have the same time stamp: TRUE
# if(file1 IS_NEWER_THAN file2)

################################################################################
# Existing Tests
################################################################################

# check if a variable is defined
if(DEFINED A)
  message("A is defined")
endif()

# check if a function or macro is defined
if(NOT COMMAND foo)
  message("the function foo is not defined")
endif()

# check if a policy is defined
# the number is random ;-)
if(POLICY CMP1234)
  message("the POLICY CMP1234 is known")
endif()

# check if a target is defined via add_executable, add_library() or add_custom_target()
if(NOT TARGET MAINEXE)
  message("the target MAINEXE is not defined")
endif()

# check if a test is defined via add_test()
if(NOT TEST footest)
  message("the test footest is not defined")
endif()

set(listVar a b c d)
if("b" IN_LIST listVar)
  message("b is in listVar")
endif()

################################################################################
# foreach loop
################################################################################

set(arg1 "a")
set(arg2 "b")
set(arg3 "c")

foreach(loopVar ${arg1} ${arg2} ${arg3})
  message("${loopVar}")
endforeach()
# output is:
#  a
#  b
#  c


set(list1 A B)
set(list2)
set(list3 E F)
set(var1 WillNotBeShown)
set(var2 WillBeShown)

# the keyword LISTS automatic dereference the list variables
# the keyword ITEMS activate the same mode after LISTS like in the example before
foreach(loopVar IN LISTS list1 list2 list3 ITEMS var1 ${var2} ${var3})
  message("${loopVar}")
endforeach()
# output is:
#  A
#  B
#  E
#  F
#  var1
#  WillBeShown


# foreacht(loopVar RANGE begin stop [step])
# stop is inclusive
# loopVar(loopVar RANGE stop) -> from 0 to stop with step 1
foreach(loopVar RANGE 2 11 3)
  message("${loopVar}")
endforeach()
# output is:
#  2
#  5
#  8
#  11


################################################################################
# while loop
################################################################################

set(con 0)
while(${con} LESS 4)
  message("con is: ${con}")
  math(EXPR con "${con}+1")
endwhile()
# output is:
#  con is: 0
#  con is: 1
#  con is: 2
#  con is: 3

################################################################################
# Interrupting Loops
################################################################################

# break() exits the inner-most enclosing loop
# continue() jump to the next step of the inner-most enclosing loop
foreach(outerVar IN ITEMS a b c)
  unset(s)
  foreach(innerVar IN ITEMS 1 2 3)
    # Stop inner loop once string s gets long
    list(APPEND s "${outerVar}${innerVar}")
    string(LENGTH s length)
    if(length GREATER 5)
      break()
    endif()

    # Do no more processing if out var is "b"
    if(outerVar STREQUAL "b")
      continue()
    endif()
    message("Processing ${outerVar}-${innerVar}")
  endforeach()

  message("Accumulated list: ${s}")
endforeach()
# output is:
#  Processing a-1
#  Processing a-2
#  Processing a-3
#  Accumulated list: a1;a2;a3
#  Accumulated list: b1;b2;b3
#  Processing c-1
#  Processing c-2
#  Processing c-3
#  Accumulated list: c1;c2;c3
