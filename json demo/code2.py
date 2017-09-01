# -*- coding:utf-8 -*-
import json
from collections import OrderedDict
s = '{"name":"ACME","shares":50,"price":123}'
# data = json.loads(s, object_hook=OrderedDict)   # object_hook对应转换成的类型
# print data

# json字典转换为python对象
# class JSONObject:
#     def __init__(self, d):
#         self.__dict__ = d
# data = json.loads(s, object_hook=JSONObject)
#
# print data.name

# 序列化实例
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 序列化实例
def serialize_instance(obj):
    d = {"__class__": type(obj).__name__}
    d.update(vars(obj))
    return d

# 反序列化获取实例
classes = {"Point": Point}
def unserialize_object(d):
    clsname = d.pop("__classname__", None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

p = Point(2, 3)
data = json.dumps(p, default=serialize_instance)
print data
s = json.loads(data, object_hook=unserialize_object)
print s


