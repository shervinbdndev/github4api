if (__debug__):
    try:
        from .handlers import RequestHandler, UserHandler
        from .scraper import Scrape
    
    except* ModuleNotFoundError as mnfe:
        raise mnfe
    
    except* ImportError as ie:
        raise ie