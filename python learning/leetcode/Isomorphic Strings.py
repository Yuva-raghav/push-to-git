def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_s_t = {}
    map_t_s = {}

    for c1, c2 in zip(s, t):
        if c1 in map_s_t and map_s_t[c1] != c2:
            return False
        if c2 in map_t_s and map_t_s[c2] != c1:
            return False
        map_s_t[c1] = c2
        map_t_s[c2] = c1

    return True


# Example usage
print(is_isomorphic("egg", "add"))   # True
print(is_isomorphic("foo", "bar"))   # False
print(is_isomorphic("paper", "title")) # True
