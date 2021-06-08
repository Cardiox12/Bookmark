import math

def get_bookmarks(begin, end, duration):
    pages_per_day = (end - begin) // duration
    bookmarks = []

    for bookmark in range(begin + pages_per_day, end, pages_per_day):
        bookmarks.append(bookmark)

    return bookmarks
