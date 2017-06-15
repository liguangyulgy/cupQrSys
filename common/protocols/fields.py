__author__ = 'LiGuangyu'
import re




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
        elif 'N'.equals(self.fieldType):
            if not self.value.isdigit():
                return False
        elif 'AN'.equals(self.fieldType):
            if not self.value.isalnum():
                return False
        elif 'NS'.equals(self.fieldType):
            if self.nsPatten.search(self.value):
                return False
        '''如果定义了正则表达式验证规则，则进行正则表达式验证'''
        if self.checkCondition:
            if not self.checkCondition.search(self.value):
                return False
        return True


class ComField(Field):
    def formV(self):
        pass

    def __init__(self):
        pass

    def init(self, dd):
        self.value =


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


