__author__ = 'LiGuangyu'
import re
from collections import OrderedDict

"""全渠道：若报文中的数据元标识的 key 对应的value 为空，不上送该报文域；对于组合域，若该组合域无子域上送，该组合域不
上送，若子域key 对应的value 为空，不上送该子域"""

class Field:
    fieldType = None
    fieldLength = None
    fieldMinLength = None
    checkCondition = None
    nsPatten = re.compile(r'.*[A-Za-z].*')

    def __init__(self, value = None):
        self.value = value

    @property
    def v(self):
        return self.value

    @v.setter
    def v(self,value):
        self.value = value

    def cond(self,cond):
        if isinstance(cond, str):
            self.checkCondition = re.compile(cond)

    def check(self):
        """字段自身的格式验证"""
        '''根据字段的长度和类型做基础判断'''
        if len(self.value) > self.fieldLength or len(self.value) < self.fieldMinLength:
            return False
        elif 'N' == self.fieldType:
            if not self.value.isdigit():
                return False
        elif 'AN' == self.fieldType:
            if not self.value.isalnum():
                return False
        elif 'NS' == self.fieldType:
            if self.nsPatten.search(self.value):
                return False
        '''如果定义了正则表达式验证规则，则进行正则表达式验证'''
        if self.checkCondition:
            if not self.checkCondition.search(self.value):
                return False
        return True

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()



class ComField(Field):

    subFieldList = {}

    def formV(self):
        pass

    def __init__(self):
        super(ComField, self).__init__()
        self.value = OrderedDict()
        pass
    @classmethod
    def init(cls, *args, **kwargs):
        cls.subFieldList.update(kwargs)

    def __getattr__(self, key):
        return self.value[key]

    def __setattr__(self, key, value):
        if 'value' == key:
            self.__dict__[key] = value
        else:
            self.value[key] = self.subFieldList[key]()
            self.value[key].v = value

    def __getitem__(self, key):
        return self.value[key]

    def __str__(self):
        tmpList = [x+'=' + str(y) for x,y in self.value.items()]
        rev = '{' + '&'.join(tmpList) + '}'
        return rev


def fieldFactory(name, fieldType, length, minlength = 0, *, parent = Field):
    if minlength ==0:
        minlength = length
    tmp = {'fieldType': fieldType, 'fieldLength': length, 'fieldMinLength':minlength}
    return type(name, (parent,), tmp)








if __name__ == '__main__':
    a = type('coo', (Field,), {'fieldType': 'N', 'fieldLength': 10, 'fieldMinLength': 5})
    b = fieldFactory('cc', 'N', 2)

    c = a('123214')
    bb = b('abc')
    dd = a()
    dd.v = '123456'
    print(dd.__dict__)
    print(dd.check())
    print(c.check())
    print(bb.check())


