import snscrape.modules.twitter as sntwitter #est un scraper pour les services de reseaux sociaux
import pandas as pd #est un module utiliser pour traiter un ensembre de donnéeaux termes de lignes et colonnes

hachtag = "python until:2022-01-01 since:2020-01-01" #Hachtag python de 01.01.2020 jusqu'a 01.01.2022
tweets = []
limit = 100 #le nombre limite des tweets qu'il va recuperer


for tweet in sntwitter.TwitterHashtagScraper(hachtag).get_items(): #TwitterHachtagScraper fonction utiliser pour lister les postes qui ont un Hachtag préciser a partir de twitter
    
    if len(tweets) == limit: #len(tweets) c'est le nombre des tweets
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content])#pour recuperer le contenu et la date et le proprietaire
#pour sauvgarder les données recuperer dans un fichier .csv               
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)
df.to_csv('tweets2.csv')
