# import sys
# input = sys.stdin.readline

video_len, pos, op_start, op_end = input().split()
commands = list(input().split())

video_len_list = video_len.split(":")
video_len_minute = int(video_len_list[0]) * 60 + int(video_len_list[1])

pos_list  = pos.split(":")
pos_minute = int(pos_list[0]) * 60 + int(pos_list[1])

op_start_list  = op_start.split(":")
op_start_minute = int(op_start_list[0]) * 60 + int(op_start_list[1])

op_end_list  = op_end.split(":")
op_end_minute = int(op_end_list[0]) * 60 + int(op_end_list[1])


for command in commands:
    if(pos_minute>= op_start_minute and pos_minute <= op_end_minute):
        pos_minute = op_end_minute

    if (command == 'prev'):
        if(pos_minute >= 0 and pos_minute <= 10):
            pos_minute = 0
        else:
            pos_minute -= 10
    
    elif(command == 'next'):
        if(pos_minute >= video_len_minute - 10 and pos_minute <= video_len_minute):
            pos_minute = video_len_minute
        else:
            pos_minute += 10


if(pos_minute>= op_start_minute and pos_minute <= op_end_minute):
    pos_minute = op_end_minute


answer_hour = str(pos_minute // 60)

if(len(answer_hour) == 1):
    answer_hour = '0' + answer_hour

answer_minute = str(pos_minute % 60)

if(len(answer_minute) == 1):
    answer_minute = '0' + answer_minute

answer = answer_hour + ":" + answer_minute
