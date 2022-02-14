from collections import defaultdict


def main():
    f = open("s3.4-31.in")
    parsed = f.read().splitlines()
    needle = parsed[0]
    haystack = parsed[1]

    freqs = init_freqs(needle)

    eval(needle, haystack, freqs)


def init_freqs(needle):
    hashmap = {}

    for i in range(len(needle)):
        if needle[i] not in hashmap:
            hashmap[needle[i]] = 1
        else:
            hashmap[needle[i]] += 1

    return hashmap


def eval(needle, haystack, needle_freqs):
    needle_len, haystack_len = len(needle)-1, len(haystack)

    perms = 0
    prev_perms = {}
    prev_chars_freqs = defaultdict(default_freq_value)

    for i in range(haystack_len):
        perm_found = True
        prev_chars_freqs[haystack[i]] += 1

        if not i >= needle_len:
            continue

        for key in needle_freqs:
            if needle_freqs[key] == prev_chars_freqs[key]:
                continue
            perm_found = False
        
        section = haystack[i-needle_len:i+1]
        if perm_found and section not in prev_perms:
            prev_perms[section] = True
            perms += 1

        if prev_chars_freqs[haystack[i-needle_len]] > 0:
            prev_chars_freqs[haystack[i-needle_len]] -= 1

    print(perms)


def default_freq_value():
    return 0


main()
