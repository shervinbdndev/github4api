if (__debug__):
    try:
        from .scraper import Scrape
        from .user_handler import UserHandler
        from .request_handler import RequestHandler
    
    except* ModuleNotFoundError as mnfe:
        raise mnfe
    
    except* ImportError as ie:
        raise ie