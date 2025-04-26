def solution(schedules, timelogs, startday):
    timelog_num = 0
    reward = 0
    today = startday

    for schedule in schedules:
        timelog = timelogs[timelog_num]
        successDays = 0

        hour_schedule = schedule // 100
        minute_schedule = schedule % 100

        total_minute_schedule = hour_schedule * 60 + minute_schedule

        for time in timelog:

            hour_time = time // 100
            minute_time = time % 100

            total_minute_time = hour_time * 60 + minute_time

            if(today == 7 or today == 6 or today == 14 or today == 13):
                successDays += 0
            else:
                if((total_minute_schedule + 10) - total_minute_time >= 0):
                    successDays += 1

            today += 1

        if(successDays == 5):
            reward += 1

        today = startday
        timelog_num += 1
        
    return reward