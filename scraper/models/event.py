class Event:
    def __init__(self, options):
        self.serial = options['serial']
        self.period = options['period']
        if options['personnel']:
            self.personnel = options['personnel']
        self.time_elapsed = options['time_elapsed']
        self.time_remaining = options['time_remaining']
        self.event_type = options['event_type']
        self.description = options['description']
        if options['team']:
            self.team = options['team']
        self.visitor_players = options['visitor_players']
        self.home_players = options['home_players']

        # @TODO break player attrs into lists of player models
        #

    # eyetest method to make sure this worked in the console, not proud
    def show(self):
        print self.serial
        print self.period
        if self.personnel:
            print self.personnel
        print self.time_elapsed
        print self.time_remaining
        print self.event_type
        print self.description
        if self.team:
            print self.team
        print self.visitor_players
        print self.home_players
