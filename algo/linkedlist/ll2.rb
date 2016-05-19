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

  def delete_by_node(node)
    #if @head == nodeV
      #@head == @head.nxt
      #self
    #end

    runner = @head
    while(runner.nxt)
      if runner.nxt == node
        runner.nxt = node.nxt
        node.nxt = nil
      end
      runner = runner.nxt
    end
    self
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
      pp "runner.nxt.val:#{runner.nxt.val} value:#{value}"
      if runner.nxt.val == value
        node.nxt = runner.nxt
        runner.nxt = node
        runner = node
      end
      runner = runner.nxt
    end
    self
  end


  def partitioning(node)
    linked_list = self.delete_by_node(node)
    new_linked_list = LinkedList.new(node)
    pp '+++++++++++++++'
    linked_list.traverse
    pp '+++++++++++++++'
    new_linked_list.traverse
    pp '+++++++++++++++'

    runner = linked_list.head
    while(runner)
      clone_node = Node.new(runner.val)
      #pp "node.val:#{node.val}   clone_node.val:#{clone_node.val}"
      #pp "clone_node.val < node.val :#{clone_node.val < node.val}"
      if clone_node.val < node.val
        pp linked_list
        new_linked_list.insert_before(clone_node, node.val)
      else
        new_linked_list.add_to_tail(clone_node)
      end
      runner = runner.nxt
    end
    new_linked_list
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
node11 = Node.new(1)
node12 = Node.new(4)
node13 = Node.new(5)
node14 = Node.new(3)
node15 = Node.new(11)
node16 = Node.new(9)
node16 = Node.new(2)
node17 = Node.new(31)
node18 = Node.new(22)
node19 = Node.new(54)
node20 = Node.new(14)
node21 = Node.new(78)
node22 = Node.new(17)
node23 = Node.new(23)
list2= LinkedList.new(node11)
list2.add_to_tail(node12)
list2.add_to_tail(node13)
list2.add_to_tail(node14)
list2.add_to_tail(node15)
list2.add_to_tail(node16)
list2.add_to_tail(node17)
list2.add_to_tail(node18)
list2.add_to_tail(node19)
list2.add_to_tail(node20)
list2.add_to_tail(node21)
list2.add_to_tail(node22)
list2.add_to_tail(node23)
#pp list2
#list2.traverse
#pp "-----"
#list1.delete_by_value("node3")
#list1.traverse
#pp "-----"
#list2.delete_by_value("node12")
#list2.traverse
#pp "===============-----"
#node17 = Node.new("INSERT AFTER NODE 14 2016/05/18")
#list2.insert_after(node17, "node14")
#list2.traverse
#p "===============-----"
#node18 = Node.new("INSERT BEFORE NODE 13 2018/011/22")
#list2.insert_before(node18, "node13")
#list2.traverse
p "===============-----"
list2.delete_by_node node14
list2.traverse

p "===============-----"
listx = list2.partitioning(Node.new(19))
p "===============-----"
p "===============-----"
listx.traverse
