def get_suffix(str, prefix, strip=True):
    parts = str.split(prefix)
    if len(parts) == 1:
        return None
    res = parts[1]
    res = res.strip() if strip else res
    return res