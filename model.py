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
                        'score':round(sentiment[0]['score']*100,2)})
    return results

# save
def save_results(results,file):
    with open(file, 'w', encoding='utf-8') as f:
        for result in results:
            json.dump(result,f, ensure_ascii= False, indent = 2)
            
#Executive Block
if __name__ == "__main__":
    # For economy
    eco_filename = 'data/eco_results.json'
    eco_articles = load_article(eco_filename)
    eco_results = analysis(eco_articles)
    save_results(eco_results , eco_filename)
    # For Politics
    pol_filename = 'data/pol_result.json'
    pol_articles = load_article(pol_filename)
    pol_results = analysis(pol_articles)
    save_results(pol_results,pol_filename)
    
