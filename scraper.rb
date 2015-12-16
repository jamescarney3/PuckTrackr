require 'net/http'
require 'nokogiri'
require 'open-uri'

class Scraper

  def initialize
    @page = nil
    @els = nil
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
  end
end
