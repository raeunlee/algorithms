# def solution(id_list, report, k):
#     answer = []
    
#     # id_list 별로 고유 idx 부여
#     l = {}
#     idx = 0
#     for i in id_list:
#         l[i] = idx
#         idx += 1
    
#     # 신고당한 사람들 배열
#     bad = []
    
#     # 각 유저는 한 번에 한 명의 유저 신고
#     for i in l: # i는 신고할 유저 
#         tmp = [ ] # 신고당한 유저 담는 배열
#         for r in report:
#             a, b = r.split(" ")
#             if i == a and b not in tmp: # 신고자 배열에 없음 추가하기
#                 tmp.append(b)
#         bad.append(tmp)
#     print(bad)
    
#     #정지당한 횟수
#     blocks = {}
#     for b in bad:
#         for each in b:
#             if each in blocks:
#                 blocks[each] += 1
#             else:
#                 blocks[each] = 1
    
#     real_bad = []
#     for key, values in blocks.items():
#         if values >= 2:
#             real_bad.append(key)
    
#     print("진짜 신고당한 사람", real_bad)
    
#     for i in range(len(bad)):
#         count = 0
#         for b in bad[i]:
#             for real in real_bad:
#                 if b == real:
#                     count += 1
#         answer.append(count)
#     return answer

def solution(id_list, report, k):
    # 유저 별 고유 idx 딕셔너리
    user_index = {user: i for i, user in enumerate(id_list)}
    
    # 유저별 신고당한 횟수 집계
    report_set = set(report)  # 중복 신고 제거
    report_count = {user: 0 for user in id_list}
    user_reports = {user: [] for user in id_list}  # 각 사용자의 신고 내역

    for r in report_set:
        reporter, reported = r.split()
        user_reports[reporter].append(reported)
        report_count[reported] += 1
    
    # 신고 당한 횟수가 k 이상인 유저 리스트
    banned_users = {user for user, count in report_count.items() if count >= k}
    
    # 각 유저별 처리 결과
    answer = [len([user for user in user_reports[reporter] if user in banned_users]) for reporter in id_list]
    
    return answer
