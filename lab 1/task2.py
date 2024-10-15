pages = 100
lines = 50
chars = 25
s = 4

disk_size = 1.44 * 1024 *1024

book_size = pages * lines * chars * s

books_count = disk_size // book_size

print("Количество книг, помещающихся на дискету:", int(books_count))
