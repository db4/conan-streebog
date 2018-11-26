from conans import ConanFile, CMake, tools
import os

class StreebogConan(ConanFile):
    name = "streebog"
    version = "0.12"
    license = "BSD 2-Clause"
    url = "https://github.com/db4/conan-streebog.git"
    settings = "os", "compiler", "build_type", "arch"
    options = {"sse2": [True, False], "sse41": [True, False]}
    default_options = "sse2=False", "sse41=False"
    exports_sources = "CMakeLists.txt", "*.patch"
    generators = "cmake"

    def config_options(self):
        if self.settings.arch != "x86" and self.settings.arch != "x86_64":
            del self.options.sse2
            del self.options.sse41
        else:
            if self.options.sse41:
                self.options.sse2 = True
            if self.settings.compiler == "Visual Studio" and self.settings.arch == "x86" and self.options.sse2:
                raise Exception("Due to the bug in the sources MSVC/x86/SSE2 is not supported yet")

    def get_simd_option(self, name):
        contents = '''
#ifndef __GOST3411_HAS_{name}__
#define __GOST3411_HAS_{name}__
#endif
'''.format(name=name.upper())
        if not self.options.get_safe(name):
            contents = "/*" + contents + "*/\n\n"
        return contents

    @property
    def src_dir(self):
        return "streebog-%s" % self.version

    def source(self):
        tools.get("https://github.com/adegtyarev/streebog/archive/%s.zip" %self.version,
                  md5="760a9bf50c6d5a968722b0da561dcf4d")
        tools.patch(base_path=self.src_dir, patch_file='streebog.patch')

    def build(self):
        config = self.get_simd_option("sse2") + self.get_simd_option("sse41")
        tools.save(os.path.join(self.src_dir, "gost3411-2012-config.h"), config)
        cmake = CMake(self)
        cmake.definitions["STREEBOG_VERSION"] = self.version
        if self.options.get_safe("sse2"):
            cmake.definitions["SSE2"] = True
        if self.options.get_safe("sse41"):
            cmake.definitions["SSE41"] = True
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*/LICENSE", dst=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["streebog"]
