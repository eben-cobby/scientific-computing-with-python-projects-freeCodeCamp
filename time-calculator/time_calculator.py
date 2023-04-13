def add_time(start, duration, start_date=False):

    # break down and town time components
    start = start.replace(":", " ")
    start_hours = int(start.split()[0])
    start_minutes = int(start.split()[1])
    start_meridiem = start.split()[2]
    duration_hours = int(duration.split(":")[0])
    duration_minutes = int(duration.split(":")[1])

    # convert time to 24hrs
    if start_meridiem == "PM":
        start_hours += 12

    # calculate total time in minutes
    time_total = (start_hours * 60) + start_minutes + (duration_hours * 60) + duration_minutes
    hours_total = time_total // 60  # calculate total hours only

    # check if time is in AM or PM format
    if (hours_total // 12) % 2 == 0:
        new_meridiem = "AM"
    else:
        new_meridiem = "PM"

    new_hours = hours_total % 12
    if new_hours == 0:
        new_hours = 12  # prevent 0:xx time output

    new_minutes = format(time_total % 60, "02d")  # limit to minimum two digits

    days_later = hours_total // 24

    # new time for different start and duration conditions
    if days_later == 0:
        new_time = "{0}:{1} {2}".format(new_hours, new_minutes, new_meridiem)
    elif days_later == 1:
        new_time = "{0}:{1} {2} (next day)".format(new_hours, new_minutes, new_meridiem)
    else:
        new_time = "{0}:{1} {2} ({3} days later)".format(new_hours, new_minutes, new_meridiem, days_later)

    #if starting day of the week is given
    if start_date:
         # create a weekdays dictionary
        week_days = {
            "Sunday": 1,
            "Monday": 2,
            "Tuesday": 3,
            "Wednesday": 4,
            "Thursday": 5,
            "Friday": 6,
            "Saturday": 7,
        }

        start_date = start_date.capitalize()

        # convert weekday to key
        for day, value in week_days.items():
            if day == start_date:
                start_date_key = value
        
        new_date_value = start_date_key + days_later

        while new_date_value > 7:
            new_date_value = new_date_value - 7

        # convert weekday value back to actual day
        for day, value in week_days.items():
            if value == new_date_value:
                new_start_date = day

        if days_later == 0:
            new_time = "{0}:{1} {2}, {3}".format(new_hours, new_minutes, new_meridiem,new_start_date)
        elif days_later == 1:
            new_time = "{0}:{1} {2}, {3} (next day)".format(new_hours, new_minutes, new_meridiem,new_start_date)
        else:
            new_time = "{0}:{1} {2}, {3} ({4} days later)".format(new_hours, new_minutes, new_meridiem,new_start_date, days_later)

    return new_time