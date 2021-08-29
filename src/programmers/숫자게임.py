def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    for a in A:
        if a < B[i]:
            answer += 1
            i += 1
    return answer