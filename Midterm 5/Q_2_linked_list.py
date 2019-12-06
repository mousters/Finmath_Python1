def add_element_to_end_of_list(linked_list,number):
    new_node = NodeLinkedList(number)
    tail = linked_list
    while tail.next:
        tail =tail.next
    tail.next = new_node

def linked_list_to_string(linked_list):
    tail = linked_list
    lst=[]
    while tail:
        lst.append(tail.number)
        tail = tail.next
    return ','.join(list(map(str,lst)))