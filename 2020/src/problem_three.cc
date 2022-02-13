using namespace::std;
#include <iostream>
#include <string>
#include <map>


map<char, int> init_needle_freqs(string needle)
{
    map<char, int> hashmap;

    for (int i = 0; i < needle.length(); i++)
    {
        char curr_char = needle[i];

        hashmap[curr_char]++;

        if (hashmap[curr_char] == 0)
            hashmap[curr_char]++;
    }

    return hashmap;
}

void eval(string needle, string haystack, map<char, int> needle_freqs)
{
    int needle_len, haystack_len, perms;
    map<string, bool> prev_perms;
    map<char, int> prev_char_freqs;

    perms = 0;
    needle_len = needle.length()-1;
    haystack_len = haystack.length()-1;

    for (int i = 0; i < haystack_len+1; i++)
    {
        bool perm_found = true;
        prev_char_freqs[haystack[i]]++;
        if (prev_char_freqs[haystack[i]] == 0)
            prev_char_freqs[haystack[i]]++;

        if (!(i >= needle_len))
            continue;

        for (auto const& [key, val] : prev_char_freqs)
        {
            if (prev_char_freqs.count(key) > 0 && prev_char_freqs[key] == needle_freqs[key])
                continue;
            perm_found = false;
        }

        string section = haystack.substr(i-needle_len, needle_len+1);
        if (perm_found && prev_perms.count(section) == 0)
        {
            prev_perms[section] = true;
            perms += 1;
        }
        
        if (prev_char_freqs[haystack[i-needle_len]] > 0)
            prev_char_freqs[haystack[i-needle_len]]--;
    }

    cout << perms;
}


int main()
{
    string needle, haystack;

    cin >> needle;
    cin >> haystack;

    map<char, int> needle_freqs = init_needle_freqs(needle);

    eval(needle, haystack, needle_freqs);
    
    return 0;
}


