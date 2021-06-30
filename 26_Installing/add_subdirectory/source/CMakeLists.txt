# version 3.2 is feature complete for modern CMake
cmake_minimum_required(VERSION 3.2)

project(testAddSubdirectory
  LANGUAGES CXX)

# provides install folder structure for GNU systems
include(GNUInstallDirs)

add_subdirectory(testlib)

# uses RPATH for the demo
# normally, LD_LIBRARY_PATH should be used
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} PRIVATE testlib::testlib)

install(TARGETS ${PROJECT_NAME})
