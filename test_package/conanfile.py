from conans import ConanFile, CMake, tools
import os

class TestConan(ConanFile):
    settings = "os", "arch", "compiler"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run("bin%stest" % os.sep)
