add_library (Haicklib SHARED
	dbgHelper.cpp)

install (TARGETS Haicklib DESTINATION lib)
install (FILES haicklib.h DESTINATION include)
