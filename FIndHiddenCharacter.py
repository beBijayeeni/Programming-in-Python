def solve(s):
    
    s_list = list(s)
    def is_vowel(char):
        return char in 'aeiou'
    for i in range(1, len(s_list)-1):
        if(s_list[i]=='?'):
            left = s_list[i-1]
            right = s_list[i+1]
            left_is_vowel = is_vowel(left)
            right_is_vowel = is_vowel(right)
            if left_is_vowel and right_is_vowel:
                s_list[i] = 'a'
            elif not left_is_vowel and not right_is_vowel:
                s_list[i] = 'b'
            else:
                s_list[i] = 'c'
    print(''.join(s_list))
s = input('Enter your string: ')
solve(s)
