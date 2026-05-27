from core.recommendation_service import SemanticBookRetriever
from core.filtering import FilterRetrivedBooks
from core.emotion_ranking import EmotionRanking

class SemanticRecommendation:

    def __init__ (self, query,category,emotion, top_k):
        self.query = query
        self.top_k = top_k
        self.category = category
        self.emotion =emotion
        self.retriever = SemanticBookRetriever()



    def pipeline(self):

        retrieved_books =self.retriever.retrieve_semantic_books_recommendation(self.query, self.top_k)

        filterer = FilterRetrivedBooks(retrieved_books)
        filterer.retrieved_books = retrieved_books
        filtered_books =filterer.filter_by_category(self.category)

        ranker = EmotionRanking(filtered_books)
        ranker.filteredBooks = filtered_books
        ranked_books = ranker.rank_by_emotion(self.emotion,self.top_k)

        return ranked_books
        

if __name__ == "__main__":
    recommendation = SemanticRecommendation(
        query="fantasy",
        category="Fiction",
        emotion="joy",
        top_k=10
    )

    result = recommendation.pipeline()

    print(result)




