class Game
  def initialize
    @events = []
    @home = nil
    @visitor = nil
  end

  def sync_events(els)
    @events = els.map{ |el| Event.new(el) }
  end

end
