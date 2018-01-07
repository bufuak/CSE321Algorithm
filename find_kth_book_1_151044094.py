def find_kth_book_1(myBooks, barrowedBooks, k):
    if len(myBooks) == 0:                   # Eğer myBooksta kitap kalmadıysa
        return barrowedBooks[k-1]           # Demekki barrowedBooksta

    elif len(barrowedBooks) == 0:           # Ama eğer barrowed books bittiyse
        return myBooks[k-1]                 # myBookstadır

    my_books_middle = len(myBooks)//2
    barrowed_books_middle = len(barrowedBooks)//2   # Middle'larını bulduk
    if my_books_middle+barrowed_books_middle < k-1: # Middlelar toplamından daha fazla ise
        if myBooks[my_books_middle]>barrowedBooks[barrowed_books_middle]:   # ve mybookstaki daha büyükse
            # Barrowed bookun sağ tarafında olabilir ama my bookta her yerde olabilir orayı araştır. k'yı da azalt
            return find_kth_book_1(myBooks, barrowedBooks[barrowed_books_middle+1:], k-barrowed_books_middle-1)
        else:
            # barrowed bookstaki büyükse mybooksun sağ tarafında olabilir barrowed booksta olabilir kyı küçült
            return find_kth_book_1(myBooks[my_books_middle+1:], barrowedBooks, k-my_books_middle-1)
    else:   # K middlelar toplamından küçükse
        if myBooks[my_books_middle]>barrowedBooks[barrowed_books_middle]:   # ve myBooks middle büyükse
            # My books'un solundadır ya da barrowed bookun her yerinde olabilir k'yı küçültmeye gerek yok zaten < mid
            return find_kth_book_1(myBooks[:my_books_middle], barrowedBooks, k)
        else:
            # barrowed bookstaki büyükse barrowed bookun solundadır ya da mybooks'un tamamında olabilir
            return find_kth_book_1(myBooks, barrowedBooks[:barrowed_books_middle], k)


m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop"]
book =  find_kth_book_1(m,n,4)
print(book)
#Output: oop
book =  find_kth_book_1(m,n,6)
print(book)
#Output: systemsprogramming