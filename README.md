# Khabarmeter

Sentiment analysis of Nepali political and economic news, sourced from Onlinekhabar English (https://english.onlinekhabar.com) and The Kathmandu Post (https://kathmandupost.com/)

# What it does...
Scrapes articles from Onlinekhabar and The Kathmandu Post politics and economy sections, runs them through a sentiment analysis model, and displays the results on a dashboard showing positive, negative, and neutral coverage.

# Working Principle
scrape.py — collects article headlines and body text using Requests and BeautifulSoup4
model.py — runs sentiment analysis using "cardiffnlp/twitter-roberta-base-sentiment-latest"
app.py — serves the dashboard via Flask

# Limitations
The model was trained on tweets, not news articles, so results on financial and political reporting may be inaccurate. Each result includes a confidence score — treat low confidence scores with skepticism.

# Run locally
```bash
git clone https://github.com/APK-hanal/khabarmeter
cd khabarmeter
pip install -r requirements.txt
python scrape.py
python model.py
python app.py
```
# Temporarily Deployed 
https://khabarmeter.onrender.com/
<img width="1316" height="884" alt="image" src="https://github.com/user-attachments/assets/d062eccb-5975-4f6e-8b9e-c1c623e16f58" />

<img width="1418" height="870" alt="image" src="https://github.com/user-attachments/assets/fabb6b25-d016-4e6e-a917-1c69154cf67d" />


# Built with
Python, BeautifulSoup4, HuggingFace Transformers, Flask

# Built by 
[Apil](https://github.com/APK-hanal)
