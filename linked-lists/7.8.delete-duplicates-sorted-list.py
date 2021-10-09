# t.c calculation requires a bit of amortized analysis
# but you can think of it this way, each node is visited just once
def remove_duplicates(L):
    main = L
    while main:
        while main.next and main.data == main.next.data:
            main.next = main.next.next
        main = main.next
    return L