class Pagination:
    
    def __init__(self, text, index):
        self.text = text
        self.items_count = len(text)
        if self.items_count % index == 0:
            self.page_count = self.items_count // index
        else:
            self.page_count = self.items_count // index + 1
        # self.page_count = 4

    def count_items_on_page(self, page_number):
        offset = int(page_number*self.page_count)
        
        if page_number <= self.page_count - 1:
            pass
            # return self.text[offset, offset + int(self.page_count)]  







pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.items_count)

print(pages.count_items_on_page(0))

