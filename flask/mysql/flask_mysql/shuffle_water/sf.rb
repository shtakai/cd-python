require 'pp'

def shuffle(l)
  return l[0] if l.size == 1
  i = l.index(l.sample)
  h = l[i]
  l.delete_at(i)
  return [h, shuffle(l)].flatten
end


def fill_water(list)
  #pp l
  first = list.max
  index_first= list.index(first)
  tmp_l = (list[0...index_first]  <<  list.min-1) + list[index_first...list.size-1]
  pp tmp_l
  second = tmp_l.max
  index_second = tmp_l.index(second)
  pp "first:#{first}:#{index_first}, second:#{second}:#{index_second}"
  h,m,l = list[(0..(index_second-1))], list[((index_second-1)..index_first-1)], list[((index_first-1)..(list.size-1))] if index_first > index_second
  pp h,m,l
end


array = [1,2,3,4,5,6]
#fill_water( shuffle(array))
fill_water( array)

