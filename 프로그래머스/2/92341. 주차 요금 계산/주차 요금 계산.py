from collections import deque

# 요금, 입차, 출차, 요금
def charge(fees, total_time):
    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    base_time, base_fee, unit_time, unit_fee = fees
    cost = base_fee
    if total_time > base_time:
        cost += ((total_time - base_time) + unit_time - 1 ) // unit_time * unit_fee
    return cost

def solution(fees, records):
    
    answer = []
    parking = {}
    total_parking_time = {}
   
    for record in records:
        time, car, action = record.split()
        h, m = map(int, time.split(':'))
        t = h * 60 + m
        
        if action == "IN": # 입차
            parking[car] = t # 차량번호, 입차 시간
        
        else: # 출차
            in_time = parking.pop(car) # 입차 시간 pop
            total_parking_time[car] = total_parking_time.get(car, 0) + (t - in_time)
            # 전체 주차시간에 기록하기
        
    for car, in_time in parking.items():
        total_parking_time[car] = total_parking_time.get(car, 0) + (23 * 60 + 59 - in_time)
    
    for car in sorted(total_parking_time.keys()):
        fee = charge(fees, total_parking_time[car])
        answer.append(fee)
    
    
    return answer