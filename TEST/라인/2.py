from typing import List


k = 2
# badword dict
dic = ["slang", "badword"]
chat = "badword ab.cd bad.ord .word s..bad.word"
def solution(k: int, dic: List[str], chat: str) -> str:
    answer = ''

    for badword in dic:
        re = len(badword) * "#"
        chat = chat.replace(badword, re)

        chat_word = chat.split()

        for word in chat_word:
            #print(word)


    return answer


print(solution(k,dic, chat))