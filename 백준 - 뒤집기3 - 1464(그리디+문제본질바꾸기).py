# 뒤집기 여부를 새로 들어오는 글자를 앞에 붙이는게 더 사전순으로 빠른지 뒤에 붙이는게 사전순으로 빠른지로 바꿔서 푸는 문제다.
# 이렇게 바꿔도 되는 이유는 새로운 글자를 앞,뒤로 붙인다는게 결국에는 뒤집기 여부에 따라 전부 구현이 가능하기 때문이다.
# 이렇게 문제의 본질을 바꿔서 푸는 연습을 통해 실력을 길러야겠다.

s = input()
new_word = s[0]

for i in range(1, len(s)):
    add_front = new_word + s[i]
    add_back = s[i] + new_word
    
    if(add_front > add_back):
        new_word = add_back
    else:
        new_word = add_front
    
print(new_word)