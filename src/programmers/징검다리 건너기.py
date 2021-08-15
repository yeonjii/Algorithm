# 이진탐색
def solution(stones, k):
    left, right = 1, max(stones)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        cnt_0 = 0
        for stone in stones:
            if stone <= mid:
                cnt_0 += 1
            else:
                cnt_0 = 0  # 초기화
            if cnt_0 >= k:  # 못 건넘
                break

        if cnt_0 >= k:  # 못 건넘
            answer = mid
            right = mid - 1
        else:  # 더 건널 수 있음
            left = mid + 1

    return answer