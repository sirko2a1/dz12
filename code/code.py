import pickle

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def iterator(self, page_size=10):
        for i in range(0, len(self.records), page_size):
            yield self.records[i:i + page_size]

    def save_to_file(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.records, file)
            print(f'Адресну книгу збережено в файл {filename}')
        except Exception as e:
            print(f'Помилка при збереженні адресної книги: {str(e)}')

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.records = pickle.load(file)
            print(f'Адресну книгу завантажено із файлу {filename}')
        except FileNotFoundError:
            print(f'Файл {filename} не знайдено. Адресна книга не змінена.')
        except Exception as e:
            print(f'Помилка при завантаженні адресної книги: {str(e)}')

    def search(self, query):
        results = []
        for record in self.records:
            if query in record.name or query in record.phone.value:
                results.append(record)
        return results

address_book = AddressBook()
address_book.load_from_file('address_book.pkl')

record1 = Record('John Doe', '12345', '1990-01-15')
record2 = Record('Jane Smith', '67890', '1985-05-20')

address_book.add_record(record1)
address_book.add_record(record2)

address_book.save_to_file('address_book.pkl')

address_book.add_record(record1)
address_book.add_record(record2)

address_book.save_to_file('address_book.pkl')

search_results = address_book.search('John')
for result in search_results:
    print(f'Знайдено: {result.name}, {result.phone.value}, Дню народження: {result.birthday.value}')
