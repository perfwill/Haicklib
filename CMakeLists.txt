cmake_minimum_required (VERSION 2.6)
project (Haicklib)

#The version number
set (Haicklib_VERSION_MAJOR 0)
set (Haicklib_VERSION_MINOR 0)

configure_file (
		"${PROJECT_SOURCE_DIR}/HaicklibConfig.h.in"
		"${PROJECT_BINARY_DIR}/HaicklibConfig.h"
	)

include_directories("${PROJECT_BINARY_DIR}")

add_library(Haicklib SHARED
			main.cpp)
