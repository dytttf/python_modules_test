#coding:utf8
'''
mysql ORM 框架编写测试版
'''

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return "<%s:%s #%s>" % (self.__class__.__name__, self.name, self.column_type)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, "varchar(100)")

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, "bigint")

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print("Found model: %s" % name)
        mappings = dict()
        for k,v in attrs.iteritems():
            if isinstance(v, Field):
                print("Found mapping: %s ==> %s" % (k,v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass
    def __init__(self, **kwargs):
        print 2
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('name')
    email = StringField('email')
    password = StringField('password')



if __name__ == "__main__":
    u = User(id='12345', name='DYF', email='test@email.com', password='123456')
    #u = User()
    u.save()
        
