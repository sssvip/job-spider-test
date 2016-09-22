# -*- coding: utf-8 -*-
' a uuid generate model '
__author__ = 'David West : admin@dxscx.com'
import uuid

def getUuid(s):
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, s.encode("utf-8")))
