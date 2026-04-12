import json
from transformers import pipeline

# Load the sentiment analysis model
sentiment_model = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    truncation=True,
    max_length=512
)
def load_article(file):
    with open(file,'r',encoding = 'utf-8') as f:
        return json.load(f)
    
def analysis(articles):
    results = []
    for article in articles:
        sentiment = sentiment_model(article["body"][:512])
        results.append({"link":article["link"],
                        'header':article['header'],
                        "sentiment": sentiment[0]["label"],
                        'score':round(sentiment[0]['score'],4)})
    return results


#Executive Block
if __name__ == "__main__":
    articles = load_article('data/economy.json')
    result = analysis(articles)
    print(result[1]['header'])
    print(result[1]['score'])
    print(result[1]['sentiment'])