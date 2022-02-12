from collections import defaultdict

def main():
    needle = input()
    haystack = input()

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
    needle_len, haystack_len = len(needle), len(haystack)

    start = 0
    end = start + needle_len
    perms = 0
    prev_perms = {}

    while end <= haystack_len:
        section = haystack[start:end]
        freqs = defaultdict(default_freq_value)
        num_matches = 0

        if section not in prev_perms:
            for i in range(len(section)):
                freqs[section[i]] += 1
                if section[i] in needle_freqs and freqs[section[i]] == needle_freqs[section[i]]:
                    num_matches += 1

            if num_matches == len(needle_freqs):
                perms += 1
                prev_perms[section] = True

        end += 1
        start += 1

    print(perms)

def default_freq_value():
    return 0
    

main()