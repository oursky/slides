@op('foo:hello')
def english():
    result = send_action('foo:ciao')
    return {
        'key':'thanks',
        'value': result['key']
    }


@op('foo:ciao')
def italian():
    return {'key':'grazie'}
