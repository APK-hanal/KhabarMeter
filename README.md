Khabar(news)
Meter(meter)
KhabarMeter
This is a small project that I built to have a NLP for nepali news articles. This acts as a measurement to economic activities and political changes. Although this is based purely on a ML model and might "hallucinate" it also displays its confidence in percentage so you can roughly get an idea of how good the take is. For example, it might flag "Gold drops in value by 30%" as a neutral article with 60% accuracy. 

scrape.py scrapes data from the english.Onlinekhabar.com site for political and economic articles and stores them in their respective json files.Then, model.py uses NLP and a sentiment analysis model called "cardiffnlp/twitter-roberta-base-sentiment-latest" which was trained on Tweets hence it may be inaccurate on some articles. 
then we have a flask connected HTML/CSS/JS site at index.html in app.py which is the main dashboard you see in the website. all in all, this was a project using mainly requests, BeautifulSoup4 and NLP.

It is available at render.com/KhabarMeter(hopefully) but it does take a minute to load.



                                                                                        -Creator 
                                                                                        Apil.