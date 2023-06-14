from github4api.scraper import Scrape
from github4api.handlers.user_handler import UserHandler
from github4api.handlers.request_handler import RequestHandler




def main():
    request: RequestHandler = RequestHandler(
        url=UserHandler(username='shervinbdndev').serialize(),
    ).sendGetRequest(content=True)
    
    scraper: Scrape = Scrape(data=request)
    
    scraper.startApi(log=False)
    
    print(scraper.followers)
    print(scraper.followings)
    print(scraper.biography)
    
    print(scraper.json_data)
    



if (__name__ == "__main__"):
    main()