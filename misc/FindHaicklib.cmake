#Find haicklib for use
#Example of use:
# find_package (Haicklib)
# if (HAICKLIB_FOUND)
# 	target_link_libraries (yourtarget ${HAICKLIB})
# endif (HAICKLIB_FOUND)

find_library (HAICKLIB NAMES Haicklib)
if (NOT HAICKLIB_FOUND)
	message ("Haicklib not found.")
endif (NOT HAICKLIB_FOUND)
