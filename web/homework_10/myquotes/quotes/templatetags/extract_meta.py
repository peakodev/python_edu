from django import template

register = template.Library()


def meta(meta_list):
    return ','.join([str(name) for name in meta_list])


register.filter('meta', meta)

