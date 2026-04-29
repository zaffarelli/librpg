def make_rid(s):
    """
    Build a unique identifier from a reference string. This rid is supposed to be url compliant, human readable and detached
    from the object ID to avoid db dump/load issues.
    :param s: the reference string
    :return:
    """
    str = s
    str = str.strip(" ").lower()
    str = str.replace(" ", "_") \
        .replace("'", "") \
        .replace("`", "") \
        .replace("-", "_") \
        .replace('"', "")
    str = str.replace("à", "a") \
        .replace("@", "a")
    str = str.replace("ù", "u") \
        .replace("û", "u") \
        .replace("ü", "u")
    str = str.replace("è", "e") \
        .replace("é", "e") \
        .replace("ë", "e") \
        .replace("ê", "e")
    str = str.replace("ï", "i") \
        .replace("î", "i")
    str = str.replace("ô", "o") \
        .replace("ö", "o")
    str = str.replace("ç", "c")
    return str
