word_dict = dict()

def solution(call):

    for word in call:
        word = word.lower()
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    print(word_dict)

    # 제일 많이 등장하는 언어들
    max_word = [k for k,v in word_dict.items() if max(word_dict.values()) == v]

    for del_word in max_word:
        del_word_upper = del_word.upper()
        call = call.replace(del_word, '').replace(del_word_upper, '')

    return call


call = input()
print(solution(call))