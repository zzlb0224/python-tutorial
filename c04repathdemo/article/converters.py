
from django.urls import register_converter
class CategoryConverter(object):
    regex = r'\w+(\+\w+)*'

    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        if isinstance(value, list):
            return '+'.join(value)
        else:
            return value


register_converter(CategoryConverter, 'cate')
