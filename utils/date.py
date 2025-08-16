class Date:
    def __init__(self) -> None:
        self.__day_today: int = 1

    def get_now_date(self) -> int:
        return self.__day_today

    def jump_to_next_day(self) -> None:
        self.__day_today += 1


date: Date = Date()
