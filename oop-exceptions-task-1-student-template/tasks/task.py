class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page
        self.symbol_count = len(data.replace(' ', ''))
        self.page_count = -(-self.symbol_count // items_on_page)  # Ceiling division
        self.word_list = data.split()

    def count_items_on_page(self, page_number):
        if page_number < 0 or page_number >= self.page_count:
            raise Exception("Invalid index. Page is missing")
        if page_number == self.page_count - 1:
            return self.symbol_count % self.items_on_page or self.items_on_page
        return self.items_on_page

    def find_page(self, data):
        if data not in self.data:
            raise Exception(f"'{data}' is missing on the pages")
        if len(data.split()) > 1:
            return [i for i, word in enumerate(self.word_list) if data in word]
        else:
            return [i for i, char in enumerate(self.data) if char == data]

    def display_page(self, page_number):
        start = page_number * self.items_on_page
        end = start + self.items_on_page
        return self.data[start:end]

    @property
    def item_count(self):
        return self.symbol_count


# Example usage
pages = Pagination('Your beautiful text', 5)

print(pages.page_count)  # 4
print(pages.item_count)  # 19

print(pages.count_items_on_page(0))  # 5
print(pages.count_items_on_page(3))  # 4
try:
    print(pages.count_items_on_page(4))
except Exception as e:
    print(e)  # Invalid index. Page is missing.

print(pages.find_page('Your'))  # [0]
print(pages.find_page('e'))  # [1, 3]
print(pages.find_page('beautiful'))  # [1, 2]
try:
    print(pages.find_page('great'))
except Exception as e:
    print(e)  # 'great' is missing on the pages

print(pages.display_page(0))  # 'Your '

