def minimumSubstringWindow(strng, t):
    count_map = dict()
    n = len(strng)

    for ch in t:
        if ch in count_map:
            count_map[ch] += 1

        else:
            count_map[ch] = 1

    start = 0
    end = 0
    map_size = len(count_map)
    min_window_len = 1000000007
    maxStart = 0
    maxend = 0

    while end < n:
        if strng[end] in count_map:
            count_map[strng[end]] -= 1

            if count_map[strng[end]] == 0:
                map_size -= 1

        while map_size == 0:
            min_window_len = min(min_window_len, (end - start + 1))
            maxStart = start  # substring start index
            maxend = end + 1  # substring end index

            ch_start = strng[start]
            if ch_start in count_map:
                count_map[ch_start] += 1
                  if count_map[ch_start] > 0:
                    map_size += 1

            start += 1

        end += 1

    print("substring start index {} and end index {}".format(maxStart, maxend))
    return min_window_len
