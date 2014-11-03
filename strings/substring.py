def substring(text, substring):

    assert type(text) is str
    assert type(substring) is str

    if (len(substring) > len(text)):
        return -1

    for i in range(0, len(text) - len(substring) + 1):
        for j in range(0, len(substring)):
            if text[i+j] != substring[j]:
                break
            if j == len(substring) - 1:
                return i

    return -1
