require 'pp'

class LinkedList
  attr_accessor :head


  def initialize(head=nil)
    @head = head
  end

  def add_to_head(node)
    pp "add to head"
    node.nxt = @head
    @head = node

  end

  def add_to_tail(node)
    runner = @head
    while(runner.nxt)
      pp "runner #{runner} #{runner.nxt}"
      runner = runner.nxt
    end
    runner.nxt = node
  end

  def traverse
    runner = @head
    while(runner)
      pp "runner:#{runner} val:#{runner.val} nxt=#{runner.nxt}"
      runner = runner.nxt
    end
  end

  def delete_by_value(value)
    runner = @head
    count = 0
    while(runner)
      if runner.nxt && runner.nxt.val == value
        pp "delete #{runner.nxt}:#{runner.nxt.val}"
        runner.nxt = runner.nxt.nxt
        count += 1
      end
      runner = runner.nxt
    end
    count
  end

  def insert_after(node, value)
    runner = @head
    while(runner)
      break if runner.nil?
      if runner.val == value
        node.nxt = runner.nxt
        runner.nxt = node
      end
      runner = runner.nxt
    end
    self
  end

  def insert_before(node, value)
    runner = @head
    while(runner)
      break if runner.nil? || runner.nxt.nil?
      if runner.nxt.val == value
        node.nxt = runner.nxt
        runner.nxt = node
        runner = node
      end
      runner = runner.nxt
    end
    self
  end

end



class Node
  attr_accessor :val, :nxt

  def initialize(val="")
    @val = val
    @nxt = nil
    #pp "Node created #{self}"
  end


end


#node1 = Node.new("node1")
#node2 = Node.new("node2")
#node3 = Node.new("node3")
#node4 = Node.new("node4")
#node5 = Node.new("node5")
#node6 = Node.new("node6")
#list1= LinkedList.new(node1)
#list1.add_to_head(node2)
#list1.add_to_head(node3)
#list1.add_to_head(node4)
#list1.add_to_head(node5)
#list1.add_to_head(node6)
##pp list1
#list1.traverse
#pp "----"
node11 = Node.new("node11")
node12 = Node.new("node12")
node13 = Node.new("node13")
node14 = Node.new("node14")
node15 = Node.new("node15")
node16 = Node.new("node16")
node16 = Node.new("node12")
list2= LinkedList.new(node11)
list2.add_to_tail(node12)
list2.add_to_tail(node13)
list2.add_to_tail(node14)
list2.add_to_tail(node15)
list2.add_to_tail(node16)
#pp list2
#list2.traverse
#pp "-----"
#list1.delete_by_value("node3")
#list1.traverse
pp "-----"
list2.delete_by_value("node12")
list2.traverse
pp "===============-----"
node17 = Node.new("INSERT AFTER NODE 14 2016/05/18")
list2.insert_after(node17, "node14")
list2.traverse
pp "===============-----"
node18 = Node.new("INSERT BEFORE NODE 13 2018/011/22")
list2.insert_before(node18, "node13")
list2.traverse
