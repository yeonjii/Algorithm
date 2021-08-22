def solution(play_time, adv_time, logs):
    # 1. 초로 변환
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)

    timeline = [0]*(play_time+1)  # 누적시간 기록할 타임라인

    # 2. logs를 돌면서 재생 시작시간, 종료시간 기록
    for l in logs:
        s, e = map(str_to_int, l.split("-"))
        timeline[s] += 1
        timeline[e] -= 1

    # 3. 누적 두번
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i-1]
    for i in range(1, len(timeline)):
        timeline[i] += timeline[i-1]

    # 4-1. 광고시간이 동영상 시간보다 더 긴 경우 (tc3)
    if adv_time >= play_time:
        return "00:00:00"

    # 4-2. 짧은경우, 타임라인 순회하면서 max 찾기
    answer = 0
    max_cnt = timeline[adv_time]  # 0~adv_time를 최대값이라고 일단 설정
    for i in range(1, play_time-adv_time):
        tmp = timeline[i+adv_time]-timeline[i]
        if tmp > max_cnt:
            max_cnt = tmp
            answer = i+1
    return int_to_str(answer)

    # for i in range(1, play_time-adv_time+1):
    #     tmp = timeline[i+adv_time-1]-timeline[i-1]  # i~i+adv_time 누적재생시간
    #     if tmp > max_cnt:
    #         max_cnt = tmp
    #         answer = i  # 누적재생시간 max일때 시작시간 갱신
    # return int_to_str(answer)

# hh:mm:ss -> ss
def str_to_int(time):
    h, m, s = map(int, time.split(":"))
    return h*3600 + m*60 + s


# ss -> hh:mm:ss
def int_to_str(time):
    h = time//3600
    m = (time%3600)//60
    s = (time%3600)%60
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)
