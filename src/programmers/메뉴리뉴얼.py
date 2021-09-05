from itertools import combinations

def solution(orders, course):
    answer = []

    for l in course:
        dic = {}  # 경우의 수 카운팅할 딕셔너리
        for word in orders:
            if len(word) >= l:
                word = sorted(word)
                for c in combinations(word, l):
                    dic["".join(c)] = dic.get("".join(c), 0) + 1

        for k, v in dic.items():
            if v >= 2 and max(dic.values()) == v:
                answer.append(k)

    return sorted(answer)