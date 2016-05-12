require 'pp'

def dual (a)
  pp a
  return nil if !a.any?
  return a[0] if a.size == 1
  head = [a[0], a[1]]
  pp "get head #{head}"
  tail = a[2..a.size]
  pp "tail: #{tail}"
  head << dual(tail)
end


arr = [1,2,3,4,5,6]
dual arr
