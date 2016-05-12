require 'pp'



def remove_dup(a)
  h = a[0]
  t = a[1..a.size]
  pp "H:#{h},  T:#{t}"
  if h == t[0]
    pp "dup"
    shift_a t
  else
    pp "not dup"
    pp "next target: #{t}"
  end
  remove_dup t
  nil
end

def shift_a(a)
  pp "----"
  return a[0] if a.size == 1
  h = a[0]
  t = a[1..a.size]
  pp "h:#{h}  t:#{t}"
  pp "h:#{h} t0:#{t[0]}"
  if h == t[0]
    pp "Dup"
    h, t[0] = t[0], h
    pp "h:#{h} t0:#{t[0]}"
  else
    pp "No Dup"
  end
  shift_a(t)

end


arr = [1,2,2,3,4,5,5,6]
#pp remove_dup arr
pp shift_a arr
