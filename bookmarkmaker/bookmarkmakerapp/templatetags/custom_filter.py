from django import template
register=template.Library()

def truncate4(value):
    result=value[-4:]
    return result
register.filter("last4",truncate4)