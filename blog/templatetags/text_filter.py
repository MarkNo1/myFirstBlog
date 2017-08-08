from django import template
register = template.Library()

@register.filter("truncate_text")
def truncate_chars(text, max_length):
    if len(text) > max_length:
        truncd_val = text[:max_length]
        if not len(text) == max_length+1 and text[max_length+1] != " ":
            truncd_val = truncd_val[:truncd_val.rfind(" ")]
        return  truncd_val + "..."
    return text
