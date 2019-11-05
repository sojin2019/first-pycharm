# class test
# input schedule

class InputSchedule():


    def __init__(self, item_date, item_time, item_name, item_details):
        """init date of the schedule, time of the schedule, name of the schedule, details """

        from datetime import datetime
        now = datetime.now()

        # item_date = date of today
        self.item_date = now.year + now.month + now.day
        self.item_time = now.hour

    from datetime import datetime
    now = datetime.now()
    if now.day < 10:
        in_item_date = str(now.year) + str(now.month) + "0" + str(now.day)
    else:
        in_item_date = str(now.year)+str(now.month)+str(now.day)


    def input_date(in_item_date):

        print("Schedule of " + in_item_date)
        print("Please input the date, if you want to revise it!")
        rev_date = input()
        msg_update = "Schedule of" + rev_date

        print(msg_update)


