class Game:
    def __init__(options):
        # self.url_id = options['url_id']
        self.serial = options['serial']
        # self.season = options['season']
        self.date = options['date']
        # self.attendance = options['attendance']
        # self.arena = options['arena']
        # self.start = options['start']
        # self.end = options['end']

        self.events = []

        # @TODO
        # home_id: int <non-null> # foreign key
        # visitor_id: int <non-null> # foreign key
        # home_score: int <non-null>
        # visitor_score: int <non-null>

    def add_event(event):
        self.events.append(event)
