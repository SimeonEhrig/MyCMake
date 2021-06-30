# version 3.2 is feature complete for modern CMake
cmake_minimum_required(VERSION 3.2)

# set project name and meta information
project(basic
  VERSION 1.0
  LANGUAGES CXX)

################################################################################
# set and read variables
################################################################################

# in cmake is every variable a string
set(myVar a b c)
message(${myVar}) #abc
set(myVar a;b;c)
message(${myVar}) #abc
set(myVar "a b c")
message(${myVar}) #a b c
set(myVar a b;c)
message(${myVar}) #abc
set(myVar a "b c")
message(${myVar}) #ab c

set(foo ab)
set(bar ${foo}cd)
message(${bar}) #abcd
set(baz ${foo} cd)
message(${baz}) #abcd
set(myVar ba)
set(big "${${myVar}r}ef")
message(${big}) #abcdef
set(${foo} xyz)
message(${ab}) #xyz

set(multiline "First line ${myVar}
Second line with a \"quoted\" word")
message(${multiline}) # First line ba
                      # Second line with a "quoted" word

unset(myVar)
#message(${myVar}) # causes an error

################################################################################
# environment variables
################################################################################

message("Path environment varibale: $ENV{PATH}")
# environment variables are only changed during the runtime of cmake
# after the end of the cmake process, all changes are undone
set(ENV{C_HELLO} "Hello World")
message("set environment variable C_HELLO")

################################################################################
# cached variables
################################################################################

# cached variables are stored in the CMakeCache.txt within the build folder and
# are persistent between different cmake runs
# they can be used by various (GUI) tools to obtain information about the build
# process
# the general form is: set(VarName value CACHE TYPE "Docstring")
# types are:
# - BOOL
# - FILEPATH
# - PATH
# - STRING
# - INTERNAL
set(MY_CACHE_VAR1 "Hello" CACHE STRING "Docstring of Var 1")
set(MY_CACHE_VAR2 "foo/text.txt" CACHE FILEPATH "Points to a specific file")
set(MY_CACHE_VAR3 "foo/" CACHE PATH "Points to a directory")
set(MY_CACHE_VAR4 "secret" CACHE INTERNAL "just for internal usage")
# to set a bool value, there are two possibilities
set(MY_CACHE_VAR5 ON CACHE BOOL "Option 1 to set a bool value")
option(MY_CACHE_VAR6 "Option 2 to set a bool value" OFF)


# by default an existing cached variable is not overwritten
# the keyword FORCE allows to overwrite a cached variable
set(MY_CACHE_VAR7 OFF CACHE BOOL "Initial Value")
set(MY_CACHE_VAR7 ON CACHE BOOL "Changed Value")
set(MY_CACHE_VAR8 OFF CACHE BOOL "Initial Value")
set(MY_CACHE_VAR8 ON CACHE BOOL "Changed Value" FORCE)

# having a local and a cached variable with the same name is possible, but can
# be dangerous
# normally the local variable is used, but if the cached variable was set in
# this run, the cached variable is used
set(MY_CACHE_VAR9 "local")
set(MY_CACHE_VAR9 "cache" CACHE STRING "cache")

message(${MY_CACHE_VAR9}) # first run: cache
                          # subsequent runs: local

################################################################################
# extended messaging
################################################################################

message("Hello World 1")        #Hello World 1
message(STATUS "Hello World 2") #-- Hello World 2
message(WARNING "Hello World 3")
# like warning, but can be hidden with the argument -Wno-dev
message(AUTHOR_WARNING "Hello World 4")
# Stops after the configuration phase, before the generator phase
#message(SEND_ERROR "Hello World 5")
# stops immediately
#message(FATAL_ERROR "Hello World 6")
message(DEPRECATION "Hello World 7")

variable_watch(watchVar)
set(watchVar "Hello World")
message(${watchVar})

################################################################################
# String search and manipulation
################################################################################

set(longStr abcdefabcdef)
set(shortBit def)

string(FIND ${longStr} ${shortBit} fwdIndex)
string(FIND ${longStr} ${shortBit} revIndex REVERSE)

message("fwdIndex = ${fwdIndex}, revIndex = ${revIndex}") #fwdIndex = 3, revIndex = 9

set(helloWorld "Hello World!")
# string(REPLACE matchString replaceWith outVar input)
string(REPLACE World Moon helloWorld ${helloWorld})
message(${helloWorld}) #Hello Moon!

set(longStr abcdefabcdef)
# REGEX MATCH stores a list in matchVar that contains all matches
# -> Number of elements in the list is the number of hits
# MATCH is also possible -> it is the same as MATCHALL, but it stops after the
# first hit
string(REGEX MATCHALL "[ace]" matchVar ${longStr})
# the term of REPLACE means that if there is a hit, it is replaced by
# "X + the hint symbol + Y"
# -> This results in the possible substitutions XdY and XeY
string(REGEX REPLACE "([de])" "X\\1Y" replVar ${longStr})

set(testStr "Hello Bob, Hello Hans Meyer, Hello Udo Fischer, Hello Hello Heike")
string(REGEX MATCHALL "Hello|Hans" matchVar2 ${testStr})

message("matchVar = ${matchVar}") #a;c;e;a;c;e
message("replVar = ${replVar}")   #abcXdYXeYfabcXdYXeYf
message("matchVar = ${matchVar2}") # Hello;Hello;Hans;Hello;Hello;Hello

# get length of string
string(LENGTH "Hello" lengthHello)
string(LENGTH " World" lengthWSPWorld)
# string(SUBSTRING input startindex length output)
string(SUBSTRING "Hello World" ${lengthHello} ${lengthWSPWorld} WSPWorld)
# Remove blanks at the beginning and end
string(STRIP "${WSPWorld}" World)
# lower case all characters
string(TOLOWER "${World}" silentWorld)
# upper case all characters
string(TOUPPER "${World}" loudWorld)

message("length \"Hello\": ${lengthHello}") #5
message("length \" World\": ${lengthWSPWorld}") #6
message("WSPWorld: \"${WSPWorld}\"") #" World"
message("normal World: \"${World}\"") #"World"
message("lower case World: \"${silentWorld}\"") #"world"
message("upper case World: \"${loudWorld}\"") #"WORLD"

################################################################################
# Lists
################################################################################

# Lists are strings separated by ;
# e.g.: a;b;c
set(myList a b c)

list(LENGTH myList len)
message("myList = ${myList}") #a;b;c
message("length of myList = ${len}") #3

set(myList2 "a;b;c")
list(GET myList2 2 0 letters)
message("Item 2 and 0 of myList2 = ${letters}")#c;a

list(APPEND myList d e f)
message("myList = ${myList}") #a;b;c;d;e;f

# list(INSERT listVar index item [item...])
list(INSERT myList 2 X Y Z)
message("myList = ${myList}") #a;b;X;Y;Z;c;d;e;f

list(APPEND myList e)

list(FIND myList d index1)
list(FIND myList k index2)
list(FIND myList e index3)

message("myList = ${myList}") #a;b;X;Y;Z;c;d;e;f;e
message("find d = ${index1}") #6
message("find k = ${index2}") #-1
message("find e = ${index3}") #7

# if the element is not in the list, no error is thrown anyway
list(REMOVE_ITEM myList X)
message("after REMOVE_ITEM X = ${myList}") #a;b;Y;Z;c;d;e;f;e
# if the index is greater than the length, this causes an error
list(REMOVE_AT myList 0)
message("after REMOVE_AT 0 = ${myList}") #b;Y;Z;c;d;e;f;e
list(REMOVE_DUPLICATES myList)
message("after REMOVE_DUPLICATES = ${myList}") #b;Y;Z;c;d;e;f

list(SORT myList)
message("after SORT = ${myList}") #Y;Z;b;c;d;e;f
list(REVERSE myList)
message("after REVERSE = ${myList}") #f;e;d;c;b;Z;Y

################################################################################
# Math
################################################################################

# the mathematical rules are similar to C
# the following operations are permitted: + - * / % | & ^ ~ << >> * / %
set(x 3)
set(y 7)
math(EXPR z "(${x}*${y}+1)*2-2")
message("result = ${z}") #42
