import snscrape.modules.twitter as sntwitter #est un scraper pour les services de reseaux sociaux
import pandas as pd #est un module utiliser pour traiter un ensembre de donnéeaux termes de lignes et colonnes

list_post = "python until:2022-01-01 since:2020-01-01" #list post python 
tweets = []
limit = 100 #le nombre limite des tweets qu'il va recuperer


for tweet in sntwitter.TwitterListPostsScraper(list_post).get_items(): #TwitterListPostsScraper fonction utiliser pour lister les postes a partir de twitter
    

    if len(tweets) == limit: #len(tweets) c'est le nombre des tweets
        break
    else:
        tweets.append([tweet.date, tweet.username, tweet.content]) #pour recuperer le contenu et la date et le proprietaire
#pour sauvgarder les données recuperer dans un fichier .csv        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet']) 
print(df)
df.to_csv('tweets3.csv')