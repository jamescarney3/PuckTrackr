require 'net/http'
require 'nokogiri'
require 'open-uri'
require 'byebug'

class Scraper

  def initialize
    @page = nil
    @els = nil
    @events = nil
  end

  def scrape(url)
    @page = Nokogiri::HTML(open(url))
    return self
  end

  def get_els
    @els = @page.css("tr td[class='goal + bborder'],
                      tr td[class=' + bborder'],
                      tr td[class=' + bborder + rborder'],
                      tr td[class='bold + bborder + rborder'],
                      tr td[class='bold + bborder'],
                      tr td[class='penalty + bborder'],
                      tr td[class='italicize + bold + bborder + rborder'],
                      tr td[class='italicize + bold + bborder']").map{ |e| e.text.gsub(/\n|\r/, "") }
    return self
  end

  def parse_els
    @events = []
    current_event = []

    @els.each_with_index do |el, i|

      if i % 8 == 0
        current_event = []
      end

      current_event << el

      if current_event.length == 8
        @events << current_event
      end
    end

    return @events
  end
end
