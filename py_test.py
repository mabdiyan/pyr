
from pyroute2 import IPRoute


class Test:
    @staticmethod
    def show_address():
        ip = IPRoute()
        return print(ip.link('get', index=4))

    @staticmethod
    def create_bridge():
        ip = IPRoute()
        return ip.link('add', ifname='brx', kind='bridge')


Test.show_address()

# Test.create_bridge()
