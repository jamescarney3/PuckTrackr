require 'pg'

DB_NAME = 'testdb'
DB_USER = 'postgres'

con = PG.connect(dbname: 'testdb', user: 'postgres')
con.exec "DROP TABLE IF EXISTS users"
con.exec "CREATE TABLE users(cookie text, numbers integer[])"
con.close if con

def insert_user(user_cookie, user_numbers)
  con = open_connection
  numbers = parse_array_for_db(user_numbers)
  con.exec "INSERT INTO users VALUES(\'#{user_cookie}\', \'#{numbers}\')"
  con.close if con
end

def update_user(user_cookie, user_numbers)
  con = open_connection
  numbers = parse_array_for_db(user_numbers)
  con.exec "UPDATE users
            SET numbers = \'#{numbers}\'
            WHERE cookie = \'#{user_cookie}\'"
  con.close if con
end

def delete_user(user_cookie)
  con = open_connection
  con.exec "DELETE FROM users WHERE cookie = \'#{user_cookie}\'"
  con.close if con
end

def get_user_by_cookie(cookie)
  con = open_connection
  user_attrs = con.exec("SELECT * FROM users WHERE cookie = \'#{cookie}\'").values
  con.close if con
  user_attrs.empty? ? nil : user_attrs
end

def set_user_numbers(arr)
  user_cookie = req.cookies["CubaTutorialApp"]

  con = open_connection
  user_attrs = con.exec("SELECT * FROM users WHERE cookie = \'#{user_cookie}\'").values
  con.close if con

  if user_attrs.empty?
    insert_user(user_cookie, arr)
  else
    update_user(user_cookie, arr)
  end
end

def get_user_numbers
  user_cookie = req.cookies["CubaTutorialApp"]

  con = open_connection
  nums = con.exec("SELECT numbers FROM users WHERE cookie = \'#{user_cookie}\'").values
  con.close if con

  nums = parse_array_from_db(nums.first.first)

  nums.empty? ? nil : nums
end

def open_connection
  PG.connect(dbname: DB_NAME, user: DB_USER)
end

def parse_array_for_db(arr)
  "{#{arr.to_s[1..-2]}}"
end

def parse_array_from_db(str)
  return [] if str == "{}"
  str[1..-2].split(",").map(&:to_i)
end
