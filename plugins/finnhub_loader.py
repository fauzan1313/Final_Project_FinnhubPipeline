import finnhub

def scrape_news():
   finnhub_client = finnhub.Client(api_key="cponpppr01qj9etvb0qgcponpppr01qj9etvb0r0")
    
   news = finnhub_client.general_news('general',min_id=0)
   
   return news