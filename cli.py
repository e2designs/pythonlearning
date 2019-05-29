
class IpAddr():
    def __init__(self, cli):
        self.other = 'other'
        self.cli = cli

    def bar(self):
        print(self.other)
        self.cli.foo()

class CLI():

    def __init__(self):
        self.something = 'Something'
        ip = IpAddr(cli=self)
        self.bar = ip.bar

    def foo(self):
        print(self.something)



