import snscrape.modules.twitter as sntwitter #est un scraper pour les services de reseaux sociaux
import pandas as pd #est un module utiliser pour traiter un ensembre de donnéeaux termes de lignes et colonnes

query = "(from:elonmusk) until:2022-01-01 since:2012-01-01" #la liste des tweets de elonmusk  
tweets = []
limit = 5000 #le nombre limite des tweets qu'il va recuperer


for tweet in sntwitter.TwitterSearchScraper(query).get_items(): #TwitterListPostsScraper fonction utiliser pour lister les tweets poster d'une personne preciser a partir de twitter
    
    if len(tweets) == limit: #len(tweets) c'est le nombre des tweets
        break
    else:
        tweets.append([tweet.date, tweet.content])#pour recuperer le contenu et la date et le proprietaire
#pour sauvgarder les données recuperer dans un fichier .csv        
df = pd.DataFrame(tweets, columns=['Date', 'Tweet'])
print(df)
df.to_csv('tweets.csv')
