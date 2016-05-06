require 'pp'

def shuffle(l)
  return l[0] if l.size == 1
  i = l.index(l.sample)
  h = l[i]
  l.delete_at(i)
  return [h, shuffle(l)].flatten
end


def fill_water(list)
  base = list.min
  pp base
  list.each do |elem|
    i = list.index(elem)
    pp "index:#{i}, elem:#{elem}"
    prev_list = list[(0...i)]
    pp "prev_list:#{prev_list}"
    prev_list = prev_list.size >= 0 ? prev_index = prev_list.select{|e| e > elem}.last : nil
    if !prev_list.nil?
      pp "prex:#{prev_list[prev_index]} -index:#{prev_index}" 
    else
      pp "prev is none"
    end
    next_list = list[(i+1..list.length-1)]
    pp "next_liset:#{next_list}"
    if next_list.size >= 0 
      next_index = next_index.select{|e| e > elem}.first : nil
    else
      if !next_list.nil?
      pp "next:#{next_list[next_index]} -index:#{next_index}"
    else
      pp "next is none"
    end
end



end

def fill_water2(list)
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


array = [1,3,2,4,6,5]
#fill_water( shufle(array))
fill_water( array)

