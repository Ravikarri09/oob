def detect_oob(payload):

    oob_patterns = [
        "xp_dirtree",
        "load_file",
        "into outfile",
        "dns",
        "http://",
        "https://",
        "ftp://",
        "xp_cmdshell"
    ]

    payload = payload.lower()

    for pattern in oob_patterns:
        if pattern in payload:
            return True

    return False