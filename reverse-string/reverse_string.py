def reverse(text):
    if isinstance(text, str):
        return text[::-1]
    return None





# Good
assert reverse('word') == 'drow'
assert reverse('hello') == 'olleh'

# Bad
assert reverse(134) is None
assert reverse(['poop', 'wow']) is None 

# Edge cases
assert reverse('') == ''
assert reverse('racecar') == 'racecar'
