require 'pp'

def dual (a)
  return [] if !a.any?
  return [a[0]] if a.size == 1
  head = [a[1], a[0]]
  tail = a[2..a.size]
  (head << dual(tail)).compact.flatten
end

(0..10).to_a.each{ |n|
  arr = (0..n).to_a
  pp "#{arr} -> #{dual arr}"
}
pp "#{[]} -> #{dual []}"
