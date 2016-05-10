require 'pp'
def search(a, t)
  pp "a:#{a}  t:#{t}"
  return false if a.size == 0
  return true if a.size == 1
  middle_index = (a.size/2).to_i
  pp "m:#{middle_index} a[m]:#{a[middle_index]}"
  t < a[middle_index] ? search(a[0..middle_index-1],t) : search(a[middle_index..a.size], t)
end

#list = [1,2,3,4,5,6,7,555,6700]
list = (500..600).to_a
target = 5550
pp search(list,target)
