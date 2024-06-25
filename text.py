def get_suffix(str, prefix, strip=True):
    parts = str.split(prefix)
    if len(parts) == 1:
        return None
    res = parts[1]
    res = res.strip() if strip else res
    return res

def remove_duplicates(lst):
    unique = []
    last = None
    for item in lst:
        if item != last:
            unique.append(item)
            last = item
    return unique