citations = [3,0,6,1,5]

def solutions(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx in range(len(citations)):
        #print(idx)
        if citations[idx]<=idx:
            return idx
    return len(citations)

print(solutions(citations))