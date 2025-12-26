class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []  # empty list 
    
    def add_review(self, review):
        self.reviews.append(review)
        print("Review added successfully")

    def count_review(self):
        return len(self.reviews)
    
    def display_review(self):
        if not self.reviews:  # if list is empty
            print("No reviews available")
        else:
            print(f"Reviews for {self.title}: ")
            for i, review in enumerate(self.reviews, start = 1):
                # enumerate() loop ke sath:
                # review → every review of the list
                # i → number of review
                # start=1 → numbering will start from 1 not from 0
                print(f"{i}. {review}")

b1 = Book("Atmoic Habits", "James Clear")

b1.add_review("The book is very motivating.")
b1.add_review("The book felt boring.")

print("Total reviews: ", b1.count_review())
b1.display_review()
