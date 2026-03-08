def longestCommonPrefix(words):
    # words = sorted(words, key=len)
    # words.sort(key=len, reverse=True)
    words = strs
    words.sort(key=len)
    word = words[0]
    res = []
    final = ''
    for i in range(len(word)):
        s = word[i]
        for j in range(1, len(words)):
            if words[j][i] == s:
                continue
            else:
                return final
        res.append(s)
        final = ''.join(res)
    return final


strs = ['flow', 'flower', 'flight']
print(longestCommonPrefix(strs))
