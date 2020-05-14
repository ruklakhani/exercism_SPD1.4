def two_fer(name):
    if isinstance(name, str):
        if name == '':
            name = 'you'
        return f'one for {name}, one for me'
    return None




# Good
assert two_fer('Ruk') == 'one for Ruk, one for me'
assert two_fer('Fred') == 'one for Fred, one for me'

# Bad
assert two_fer(123) is None
assert two_fer(['sally', 'hannah']) is None

# Edge cases
assert two_fer('') == 'one for you, one for me'
assert two_fer('you') == 'one for you, one for me'
