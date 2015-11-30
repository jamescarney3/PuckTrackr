def params
  req.query_string.split("&").map{ |x| x.split("=") }.to_h
end
