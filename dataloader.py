from redis_om import HashModel
from redis_om import (
    Field,
    HashModel,
    Migrator
)
class Book(HashModel):
    isbn: str = Field(index=True)
    title: str  = Field(index = True)
    author: str = Field(index = True)
    year: int = Field(index = True)
    publisher: str

with open('bookdata.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            book = Book(
                isbn = row[0],
                title = row[1],
                author = row[2],
                year = row[3],
                publisher = row[4]
            )
            book.save()
            line_count += 1
    # print(f'Processed {line_count} lines.')



