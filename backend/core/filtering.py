from core.recommendation_service import SemanticBookRetriever


class FilterRetrivedBooks:

    def __init__(self ,  retrieved_books):
        self.retrieved_books = retrieved_books

    def filter_by_category(self,category):
        if category == "ALL":
            return self.retrieved_books

        filtered = self.retrieved_books[self.retrieved_books["simple_categories"].str.lower() == category.lower()]

        return filtered


