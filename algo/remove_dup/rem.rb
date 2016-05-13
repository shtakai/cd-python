require 'pp'

def shift_a(a)
  pp "size: #{a.size}"
  return [a[0]] if a.size == 1
  return [a[1],a[0]] if a.size == 2
  return [] if !a.any?
  pp a
  head = a[1]
  tail = ([a[0]] << a[2..a.size]).flatten
  pp "head:#{head}. tail:#{tail}"
  (head << (shift_a tail)).compact.flatten
end



arr = [1,2,2,3,4,5,5,6]
#arr = [1,2]
#pp remove_dup arr
pp shift_a arr
