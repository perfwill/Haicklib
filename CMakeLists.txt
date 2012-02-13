cmake_minimum_required (VERSION 2.6)
project (Haicklib)

set (PROJECT_SOURCE_DIR "${CMAKE_SOURCE_DIR}/src")
set (PROJECT_BINARY_DIR "${CMAKE_BINARY_DIR}/bin")
set (PROJECT_MISC_DIR "${CMAKE_SOURCE_DIR}/misc")

#The version number
set (Haicklib_VERSION_MAJOR 0)
set (Haicklib_VERSION_MINOR 1)

#Some useful variables
set (HAICK_INCLUDE_DIR include/haick)

if (NOT PKGCONFIG_MODULE_DIR)
	set (PKGCONFIG_MODULE_DIR lib/pkgconfig)
endif (NOT PKGCONFIG_MODULE_DIR)

if (NOT CMAKE_MODULE_DIR)
	set (CMAKE_MODULE_DIR ${CMAKE_ROOT}/Modules)
endif (NOT CMAKE_MODULE_DIR)

configure_file (
		"${PROJECT_SOURCE_DIR}/HaicklibConfig.h.in"
		"${PROJECT_BINARY_DIR}/HaicklibConfig.h"
	)
configure_file (
		"${PROJECT_MISC_DIR}/haicklib.pc.in"
		"${PROJECT_MISC_DIR}/haicklib.pc"
		@ONLY
	)

include_directories("${PROJECT_BINARY_DIR}")
add_subdirectory(src)

#Installing
install (FILES ${PROJECT_BINARY_DIR}/HaicklibConfig.h DESTINATION ${HAICK_INCLUDE_DIR})
install (FILES ${PROJECT_MISC_DIR}/haicklib.pc DESTINATION ${PKGCONFIG_MODULE_DIR})
install (FILES ${PROJECT_MISC_DIR}/FindHaicklib.cmake DESTINATION ${CMAKE_MODULE_PATH})
