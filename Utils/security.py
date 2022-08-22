import cryptocode


def url_encrypt(text, key):
    str_encoded = cryptocode.encrypt(text, key)

    return str_encoded


def url_decrypt(text, key):
    str_decoded = cryptocode.decrypt(text, key)

    return