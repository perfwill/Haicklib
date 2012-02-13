#include "HaicklibConfig.h"
#include "dbgHelper.h"
#include <cstdlib>
#include <cstdio>
#include <cstdarg>
#include <string>

//Page file is the file to write output to (typically ~/.haickpage)
std::string hckPageFilePath = "";

void hckPrint(char * format, ...) {
	if (hckPageFilePath.empty()) {
			hckPageFilePath = getenv("HOME");
			hckPageFilePath.append("/.haickpage");
		}

	FILE * pageFile = fopen(hckPageFilePath.c_str(), "w");
	
	va_list vl;
	va_start(vl, 0);
	vfprintf(pageFile,  format, vl);
	va_end(vl);

	fclose(pageFile);
}
