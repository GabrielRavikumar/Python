s = input()
max_len=  0
char_set = set()
left = 0
for i in range(len(s)):
    while s[i] in char_set:
        char_set.remove(s[i])
        left += 1
    char_set.add(s[i])
    max_len = max(max_len, i - left + 1)
print(max_len)