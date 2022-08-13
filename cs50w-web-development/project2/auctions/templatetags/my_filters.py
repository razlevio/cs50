from django import template

register = template.Library()

@register.filter(name="currency")
def currency(value):
    """
    Function to convert number to USD representation
    :param num: The number to convert
    :type num: float
    :return: USD Currency formatted
    :rtype: str
    """
    try:
        return "${:0,}".format(value)
    except(ValueError, NameError):
        print("WRONG DATA INPUT")
        return None

