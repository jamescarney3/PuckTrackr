SITUATIONS = ['EV', 'SH', 'PP']

class Event

  attr_reader :seq, :period, :situation, :time_elapsed, :time_remaining,
              :event_type, :description, :visitor_players, :home_players

  def initialize(str)
    parse(str)
  end

  private

  def parse(str)
    arr = str.split
    @seq = arr.shift.to_i
    @period = arr.shift.to_i

    if SITUATIONS.include?(arr.first)
      @situation = arr.shift
    else
      @situation = nil
    end

    @time_elapsed = arr.shift
    @time_remaining = arr.shift
    @event_type = arr.shift

    puts arr.join(" ")
  end


end
