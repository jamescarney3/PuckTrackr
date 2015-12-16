class Event

  attr_reader :log_number, :period, :situation, :time_elapsed, :time_remaining,
              :event_type, :description, :visitor_players, :home_players

  def initialize(arr)
    @log_number = arr[0].to_i
    @period = arr[1].to_i
    @situation = arr[2] ? arr[2].downcase.to_sym : nil
    @time_elapsed = arr[3].scan(/(\d+:\d{2})/).last.first
    @time_remaining = arr[3].scan(/(\d+:\d{2})/).first.first
    @event_type = arr[4].downcase.to_sym
    @description = arr[5]
    @visitor_players = arr[6]
    @home_players = arr[7]
  end


end
