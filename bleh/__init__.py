from check50 import *


class Hello(Checks):

    @check()
    def exists(self):
        """hello.c exists"""
        self.require("hello.c"), self.require("hello.c")

    @check("exists")
    def compiles(self):
        """hello.c compiles"""
        self.spawn("clang -std=c11 -o hello hello.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_hello_world(self):
        """prints "Hello, world!"  """
        self.spawn("./hello world").stdout("Hello, world!\n", "Hello, world!").exit(0)
