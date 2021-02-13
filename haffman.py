def main():
    #------------------------------------------------
    # intialization arrays
    #------------------------------------------------
    
    chars = ['a', 'b', 'c', 'd', 'e', 'f'] 
    frequency = [ 1, 6, 11, 8, 6, 4]
    nodes = [] ##unused nodes
    
    #input_file = open("input.txt", "r")
    #for line in input_file:
    #    elements = line.split()
    #    frequency.append(elements)

    for x in range(len(chars)):
        nodes.append(node(frequency[x], chars[x]))
    
    #print(nodes)
    
    while len(nodes) > 1:
         
        nodes = sorted(nodes, key=lambda x: x.frequency)    # sort nodes so we can pick smallest nodes
        
        #print nodes
        node_left = nodes[0]
        node_left.direction = 0
        node_right = nodes[1]
        node_right.direction = 1
    
        newNode = node(node_left.frequency+node_right.frequency, node_left.name+node_right.name, node_left, node_right) #merging two nodes
    
        nodes.remove(node_left)     #removing nodes
        nodes.remove(node_right)    #
        nodes.append(newNode)
    
    print("######################################")
    printer(nodes[0])

#-------------------------------------------
#   node class
#-------------------------------------------

class node:
    def __init__(self, frequency, name, node_left=None, node_right=None):
        
        self.node_left = node_left
        self.node_right = node_right
        self.frequency = frequency
        self.name = name
        self.direction = ''

def printer(node, value=''):
    
    value_main = value + str(node.direction)  # directionman for current node
 
    if(node.node_left):     #if node is not edge
        printer(node.node_left, value_main)
    if(node.node_right):    
        printer(node.node_right, value_main)

    if not(node.node_left or node.node_right): # if node is on edge
        print(f"|   {node.name}, {value_main}")

 
if __name__ == "__main__":
    main()
 
