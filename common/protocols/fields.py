__author__ = 'LiGuangyu'




class Field:
    fieldType = None
    fieldLength = None
    fieldMinLength = None

    def __init__(self, value = None):
        self.value = value

    @property
    def v(self):
        return self.value

    @v.setter
    def v(self,value):
        self.value = value


    def check(self):
        if len(self.value) > self.fieldLength or len(self.value) < self.fieldMinLength:
            return False
        elif 'N'.equals(self.fieldType):
            if not self.value.isdigit():
                return True

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


