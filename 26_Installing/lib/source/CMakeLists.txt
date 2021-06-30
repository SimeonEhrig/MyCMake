# version 3.2 is feature complete for modern CMake
cmake_minimum_required(VERSION 3.2)

# set project name and meta information
project(testlib
  VERSION 1.0
  LANGUAGES CXX)

# provides install folder structure for GNU systems
include(GNUInstallDirs)

################################################################################
# defining targets
################################################################################

add_library(${PROJECT_NAME} SHARED)
target_sources(${PROJECT_NAME}
  PRIVATE
  src/testlib.cpp)

target_include_directories(${PROJECT_NAME}
  PUBLIC
  # specify include path for target_link_libraries, if target is direct linked, e.g. via sub_directory
  $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
  # specify include path for target_link_libraries, if target is installed, e.g. via find_package
  $<INSTALL_INTERFACE:include>
  )

# the alias is will be used inside the lib or if the project is added via add_subdirectory to another project
add_library(${PROJECT_NAME}::${PROJECT_NAME} ALIAS ${PROJECT_NAME})

################################################################################
# Install routine
################################################################################

include(CMakePackageConfigHelpers)
# create version.cmake file in build folder
# is not automatically copied
write_basic_package_version_file("${PROJECT_NAME}ConfigVersion.cmake"
                                 VERSION ${PROJECT_VERSION}
                                 COMPATIBILITY SameMajorVersion)

# replace placeholder in Config.cmake.in and write result to built
configure_package_config_file(
  "${PROJECT_SOURCE_DIR}/cmake/${PROJECT_NAME}Config.cmake.in"
  "${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
  INSTALL_DESTINATION
  ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME}/cmake)

# copies archive and shared libraries to the install folder
install(TARGETS ${PROJECT_NAME}
  # "register" target for export in Targets.cmake
  EXPORT "${PROJECT_NAME}Targets"
  )

# write all "registered" targets to the Targets.cmake
# Targets.cmake will be automatically copied to install folder
install(EXPORT ${PROJECT_NAME}Targets
        FILE ${PROJECT_NAME}Targets.cmake
        NAMESPACE ${PROJECT_NAME}::
        DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME}/cmake)

# copies the Config.cmake and ConfigVersion.cmake to the install folder
install(FILES "${PROJECT_BINARY_DIR}/${PROJECT_NAME}Config.cmake"
              "${PROJECT_BINARY_DIR}/${PROJECT_NAME}ConfigVersion.cmake"
        DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME}/cmake)

# copies header to install target manually
# it will not automatically done, if the headers was added to a installed target
install(DIRECTORY ${PROJECT_SOURCE_DIR}/include/ DESTINATION include)
