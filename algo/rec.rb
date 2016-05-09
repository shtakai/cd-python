require 'pp'

def recursive(n)
  n == 1 ? 1 : n*recursive(n-1)
end

pp recursive(7)
