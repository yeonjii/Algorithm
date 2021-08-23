def solution(record):
    answer = []
    user = {}
    for msg in record:
        tmp = msg.split()
        if tmp[0] == 'Enter' or tmp[0] == 'Change':
            user[tmp[1]] = tmp[2]

    for msg in record:
        tmp = msg.split()
        if tmp[0] == 'Enter':
            answer.append(user[tmp[1]] + '님이 들어왔습니다.')
        elif tmp[0] == 'Leave':
            answer.append(user[tmp[1]] + '님이 나갔습니다.')

    return answer