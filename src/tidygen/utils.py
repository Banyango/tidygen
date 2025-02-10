def ensure_snake_case(s: str):
    return s.lower().replace(' ', '_')


def ensure_camel_case(s: str):
    return ''.join(word.capitalize() for word in s.split('_'))
