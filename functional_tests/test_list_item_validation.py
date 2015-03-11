from .base import FunctionalTest

class ItemVlidatinTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, and it works

        # Perversely, she now tries to submit a second list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
