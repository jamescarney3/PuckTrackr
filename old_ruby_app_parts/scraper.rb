require 'net/http'
require 'open-uri'
require 'byebug'

class Scraper

  attr_reader :data

  def initialize
    # @els = nil
    @data = nil
  end

  def scrape(url)

    raw_data = Net::HTTP.get(URI.parse(url)).gsub(/(<.+?>)+/, " ").gsub(/\n|\r|\t|&nbsp;/, "").squeeze " "
    regex = /(\d{1,3} \d{1} (EV |PP |SH |)(\d{1,2}:\d{2} ){2}[A-Z]{3,5} .+?( \d{1,2} (C|R|L|D|G)){8,12})/

    @data = raw_data.scan(regex).map{ |e| e.first }
    return self
  end

  def get_els
    return self
  end

  def get_teams
    return self
  end

  def parse_teams
    return self
  end

  def parse_els
  end
end
