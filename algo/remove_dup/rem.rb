require 'pp'

def shift_a(a)
  # move 1nd elem of array to next
  #  next next....
  # then 1nd elem moves to last of the array

  pp "start #{a}"
  head = a[0]
  tail = a[1..a.size]

  # Basic condition
  return [] if !tail.any?


  # Recursion
  head, tail[0] = tail[0], head
  ([head] << shift_a(tail)).flatten

end

def remove_dup(a)
  return [a[0]] if a.size == 1
  head = a[0]
  tail = a[1..a.size]

  pp "head:#{head}  tail:#{tail}"

  if head == tail[0]
    [head] << shift_a(tail)
  else
    [head] << remove_dup(tail)
  end

end


arr = [1,2,2,3,4,5,5,6]
# 1 2 2 3 4
# 1 2
#   2 2
#    <2<3<
#     3 2 4
#      <2<4<
#       4<2
#         X
# 1 2 3 4 _
#
#arr = [1,2]
pp remove_dup arr
#pp shift_a shift_a shift_a arr
#pp  shift_a arr
