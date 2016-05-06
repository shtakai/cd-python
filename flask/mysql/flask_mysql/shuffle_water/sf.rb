
def shuffle(l)
  return l[0] if l.size == 1
  i = l.index(l.sample)
  h = l[i]
  l.delete_at(i)
  return [h, shuffle(l)].flatten
end


def fill_water(l)
  first = max(l)
  index_first = l.delete_at(first)
  second = max(l)
  index_second = l.delete_at(second)
  [head_arr, last_arr] = index_first > index_second ? [l[0..index_second], l[index_second..]] : []
  
end



array = [1,2,3,4,5,6]
p shuffle(array)

