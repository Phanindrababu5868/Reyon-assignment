#link :- https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/submissions
def has_cycle(head):
    id_Set=set()
    while head:
        if id(head) in id_Set:
            return 1
        else:
            id_Set.add(id(head))
            head=head.next
    return 0