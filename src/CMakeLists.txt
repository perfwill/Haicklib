add_library (Haicklib SHARED
	dbgHelper.cpp)

install (TARGETS Haicklib DESTINATION lib)
install (FILES haicklib.h dbgHelper.h DESTINATION ${HAICK_INCLUDE_DIR})
install (FILES pageout.py RENAME haickpgo DESTINATION bin PERMISSIONS WORLD_READ WORLD_EXECUTE OWNER_WRITE)
