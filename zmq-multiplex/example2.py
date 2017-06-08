@op('foo:hello') # Plugin A
def english():
    send_action('foo:ciao')
    return {'key':'thanks'}


@op('foo:ciao') # Plugin B
def italian():
    return {'key':'grazie'}
