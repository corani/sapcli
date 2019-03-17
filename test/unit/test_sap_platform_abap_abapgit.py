#!/usr/bin/env python3

import unittest
from io import StringIO

from sap.platform.abap import Structure

import sap.platform.abap.abapgit


class SIMPLE_ABAP_STRUCT(Structure):

    FOO: str
    BAR: str


class TestXMLSerializer(unittest.TestCase):

    def test_full_file(self):
        dest = StringIO()

        writer = sap.platform.abap.abapgit.XMLWriter('LCL_PYTHON_SERIALIZER', dest)
        writer.add(SIMPLE_ABAP_STRUCT(FOO='BAR', BAR='FOO'))
        writer.add(SIMPLE_ABAP_STRUCT(FOO='GRC', BAR='BLAH'))
        writer.close()

        self.assertEqual(dest.getvalue(), '''<?xml version="1.0" encoding="utf-8"?>
<abapGit version="v1.0.0" serializer="LCL_PYTHON_SERIALIZER" serializer_version="v1.0.0">
 <asx:abap xmlns:asx="http://www.sap.com/abapxml" version="1.0">
  <asx:values>
   <SIMPLE_ABAP_STRUCT>
    <FOO>BAR</FOO>
    <BAR>FOO</BAR>
   </SIMPLE_ABAP_STRUCT>
   <SIMPLE_ABAP_STRUCT>
    <FOO>GRC</FOO>
    <BAR>BLAH</BAR>
   </SIMPLE_ABAP_STRUCT>
  </asx:values>
 </asx:abap>
</abapGit>
''')


if __name__ == '__main__':
    unittest.main()
