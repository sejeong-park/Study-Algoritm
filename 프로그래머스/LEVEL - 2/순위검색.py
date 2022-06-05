import sys

from itertools import combinations
from collections import defaultdict

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for info_list in info:
        info_list = info_list.split()
        info_key = info[:-1]

solution(info, query)
