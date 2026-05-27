from core.filtering import FilterRetrivedBooks


class EmotionRanking :
    
    def __init__(self , filteredbooks):
        self.filteredBooks = filteredbooks
        self.emotion_columns = [
            "admiration",
            "amusement",
            "anger",
            "annoyance",
            "approval",
            "caring",
            "confusion",
            "curiosity",
            "desire",
            "disappointment",
            "disapproval",
            "disgust",
            "embarrassment",
            "excitement",
            "fear",
            "gratitude",
            "grief",
            "joy",
            "love",
            "nervousness",
            "neutral",
            "optimism",
            "pride",
            "realization",
            "relief",
            "remorse",
            "sadness",
            "surprise"
        ]

    
    def rank_by_emotion(self, emotion ,top_k):
        if(emotion == "ALL"):
            return (self.filteredBooks.head(top_k))
        

        if emotion not in self.emotion_columns:
            raise ValueError(
                f"{emotion} is not supported"
            )
        
        ranked = (
            self.filteredBooks
            .sort_values(
                by=emotion,
                ascending=False
            )
            .head(top_k)
        )

        return ranked
        
