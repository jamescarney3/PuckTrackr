class Game

  attr_reader :home, :away, :events

  def initialize
    @events = []
    @home = nil
    @visitor = nil
  end

  def sync_events(els)
    @events = els.map{ |el| Event.new(el) }
  end

  def sync_teams(teams)
    @visitor = teams.first
    @home = teams.last
  end

  def jsonify
    return JSON.pretty_generate(self)
  end
end
