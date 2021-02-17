import numpy as np

file = open("20201027_hjy.txt", "r")
participants = list()

# 채팅 로그 친 학번
part_nums = list()
dict_stu = {}
while True:
    line = file.readline()
    if not line:
        break

    array = line.split()
    # int(array[5].split(':')[0]): 시 / int(array[5].split(':')[1]): 분
    if len(array) >= 10 and int(array[5].split(':')[0]) == 11 and 29 <= int(array[5].split(':')[1]) <= 31:
        # 만약 학번만 뽑아내면 더 쉬울듯 하다
        # 이름만 뽑아내는 모듈
        temp = ""
        count = 0
        for arr in array:
            if arr == '님이':
                break
            elif arr.find("비공개") > 0:
                count = 0
                break
            count += 1

        for arr in range(6, count):
            temp += array[arr]
        # 이미 들어가있는지 검사 출석자
        if temp not in participants and temp != "":
            participants.append(temp)

        temp_int = 0
        count = 0
        for arr in array:
            if arr == '모두에게:':
                break
            count += 1

        temp = array[count + 1]

        try:
            temp_int = int(temp)
            if temp not in part_nums:
                dict_stu[temp] = array[count + 2]
                part_nums.append(temp)
        except ValueError:
            print()

print(dict_stu)
part_nums.sort()
print(len(part_nums), part_nums)
file.close()
participants.sort()
# print("출석 채팅 로그 남긴 인원\n", len(participants), participants)

# 강의 수강생 명단
student_file = open('20_02_participation.csv', 'r')
student_names = list()
stu_nums = list()

while True:
    line = student_file.readline()
    if not line:
        break

    student_names.append(line.split(',')[1].split('\n')[0])
    stu_nums.append(line.split(',')[0].split('\n')[0])

student_file.close()
student_names.sort()
stu_nums.sort()
print("강의 수강생\n", len(stu_nums), stu_nums)

# 수강생과 출석자 비교 후 들어가지 않은 인원에 대해 새로운 파일 만들기? - 선택 사항
absent = student_names.copy()

for part_log in participants:
    for stu in student_names:
        # 비교하는 부분, 여기가 핵심임
        if part_log.find(stu) != -1 or stu.find(part_log) != -1:
            absent.remove(stu)
            break

# print("출석자\n", len(participants), participants)
# print("결석자\n", len(absent), absent)


# 모듈1
# 이름으로 뽑아내 결석자 찾기
for part_log in participants:
    for abs_str in absent:
        new_abs_str = abs_str[1] + abs_str[2]
        if part_log.find(new_abs_str) != -1 or new_abs_str.find(part_log) != -1:
            absent.remove(abs_str)
            break

# print("결석자\n", len(absent), absent)

# 모듈2
# 학번으로 출석자 찾기
temp_stu_num = stu_nums.copy()
for part_log in part_nums:
    for num in stu_nums:
        if part_log == num:
            temp_stu_num.remove(part_log)
            break

print("결석자\n", len(temp_stu_num), temp_stu_num)
