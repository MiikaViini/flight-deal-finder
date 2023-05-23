import datetime as dt


class DateManager:
    def __init__(self):
        self.search_dates_list = []

    def search_dates(self):
        formatted_date_from = str(dt.datetime.now().strftime("%d/%m/%Y"))
        date_from = dt.datetime.strptime(formatted_date_from, "%d/%m/%Y")
        date_to = date_from + dt.timedelta(days=6 * 30)
        formatted_date_to = date_to.strftime("%d/%m/%Y")
        self.search_dates_list.append(formatted_date_from)
        self.search_dates_list.append(formatted_date_to)
        return self.search_dates_list
