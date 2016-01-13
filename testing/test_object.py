# coding=utf-8
import unittest
from io import BytesIO

__author__ = 'Lorenzo'

from ipfs.api import IpfsApi
from lib.hexdump import print_hexdump


class TestIPFS(unittest.TestCase):
    DEBUG = True  # set this flag to skip tests while refactoring the unit

    @classmethod
    def setUpClass(cls):

        cls.KEY1 = 'QmUNLLsPACCz1vLxQVkXqqLX5R1X345qqfHbsf67hvA3Nn'
        cls.KEY2 = 'QmR9MzChjp1MdFWik7NjEjqKQMzVmBkdK3dz14A6B5Cupm'
        cls.NODE = {'Data': b'Hello World'}

    def setUp(self):
        self.ipfs = IpfsApi()

    @unittest.skipIf(DEBUG, "debug")
    def test_object_data(self):
        resp = self.ipfs.object.data(self.KEY1)
        print_hexdump(resp.read())

    @unittest.skipIf(DEBUG, "debug")
    def test_object_links(self):
        resp = self.ipfs.object.links(self.KEY1)
        print(repr(resp))

    @unittest.skipIf(DEBUG, "debug")
    def test_object_get(self):
        resp = self.ipfs.object.get(self.KEY2)
        print(repr(resp))

    @unittest.skipIf(DEBUG, "debug")
    def test_object_put(self):
        resp = self.ipfs.object.put(self.NODE)
        print(repr(resp))

    @unittest.skipIf(DEBUG, "debug")
    def test_object_stat(self):
        resp = self.ipfs.object.stat(self.KEY1)
        print(repr(resp))

    @unittest.skipIf(DEBUG, "debug")
    def test_object_new(self):
        resp = self.ipfs.object.new()
        print(repr(resp))

    @unittest.skipIf(DEBUG, "debug")
    def test_object_patch_add_link(self):
        resp = self.ipfs.object.patch(self.KEY1).add_link('foo', self.KEY2)
        print(repr(resp))

    @unittest.skipIf(DEBUG, "debug")
    def test_object_patch_rm_link(self):
        resp = self.ipfs.object.patch(self.KEY2).rm_link('ìndex.html')
        print(repr(resp))

    @unittest.skipIf(DEBUG, "debug")
    def test_object_patch_set_data(self):
        resp = self.ipfs.object.patch(self.KEY1).set_data(BytesIO(b"foobar"))
        print(repr(resp))