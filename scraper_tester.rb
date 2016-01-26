require_relative 'scraper.rb'

def gen_matches
  url = "http://www.nhl.com/scores/htmlreports/20152016/PL010003.HTM"

  raw_data = Net::HTTP.get(URI.parse(url)).gsub(/(<.+?>)+/, " ").gsub(/\n|\r|\t|&nbsp;/, "").squeeze " "

# my_regex = ... will need to follow this general pattern:

# - a one-to-three(probably) digit number (space)
# - a one-digit number(space)
# - zero or one two-character string (ie EV, PP, PK, is there an EN?)(space)
# - two times, each of which is
#   - 1-2digits:2digits(space)
# - a 3-or-4-character uppercase string(space)
# - a string of some variable length(space)
# - 8-to-12 player position/number paris, each of which is
#   - a one-to-two-digit number(space)either(C|R|L|D|G)(space)

  my_regex = /(\d{1,3} \d{1} (EV |PP |PK |EN |SH |)(\d{1,2}:\d{2} ){2}[A-Z]{3,5} .+?( \d{1,2} (C|R|L|D|G)){8,12})/

  matches = raw_data.scan(my_regex).map{ |e| e.first }

  matches

end

def good_matches
  matches = gen_matches
  idx = 0
  good = []

  until matches[idx].split[0].to_i != idx + 1 do
    puts matches[idx]
    good.push matches[idx]
    idx += 1
  end

  return good
end

# "1 1 0:00 20:00 PSTR Period Start- Local time: 7:07 CDT 16 C 21 C 67 L 44 D 56 D 35 G 12 C 19 C 38 L 3 D 7 D 35 G"

# "2 1 EV 0:00 20:00 FAC NSH won Neu. Zone - FLA #16 BARKOV vs NSH #12 FISHER 16 C 21 C 67 L 44 D 56 D 35 G 12 C 19 C 38 L 3 D 7 D 35 G"

# " 1 0:14 19:46 STOP OFFSIDE 16 C 21 C 67 L 44 D 56 D 35 G 12 C 19 C 38 L 3 D 7 D 35 G"

# result = raw_data.scan(my_regex)
