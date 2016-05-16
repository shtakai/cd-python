require 'pp'

class LinkedList
  attr_accessor :head

  def initialize(head=nil)
    @head = head
    head
  end

  def add_to_head(node)
    node.next = @head
    @head = node
    node
  end

  def add_to_tail(node)
    last = traverse
    last.next = node
    node
  end

  def traverse
    runner = @head
    while(runner.next)
      runner = runner.next
    end
    runner
  end

  def has_value(value)
    runner = @head
    while(runner.next)
      if runner.value == value
        pp "value found:#{value} on Node:#{runner}"
        break
      end
      runner = runner.next
    end
  end

end


class Node
  attr_accessor :next, :value
  def initialize(value)
    @value = value
    @nxt = nil
  end
end

node_1 = Node.new("node_1")
node_2 = Node.new("node_2")
node_3 = Node.new("node_3")
node_4 = Node.new("node_4")
node_5 = Node.new("node_5")

list = LinkedList.new(node_1)
list.add_to_head node_2
list.add_to_head node_3
list.add_to_head node_4
list.add_to_head node_5


node_6 = Node.new("node_6")
list.add_to_tail(node_6)
pp list


list.has_value("node_3")
