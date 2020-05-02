from django import template
register = template.Library()

def cut(value, arg):
	"""
	Cuts out the value of arg from the string.

	"""
	return value.replace(arg,'')


register.filter('cut',cut)