if (__debug__):
    try:
        import requests
        from typing import Self, Literal, Union
    
    except* ModuleNotFoundError as mnfe:
        raise mnfe.__doc__
    
    except* ImportError as ie:
        raise ie.__doc__







class RequestHandler:
    def __init__(self: Self, url: str) -> Literal[None]:
        self.__url = url
        self.__data = None
        
    @property
    def url(self: Self) -> str:
        return self.__url
        
    def sendGetRequest(self: Self, content: bool = False) -> Union[int, bytes, Literal[None]]:
        try:
            self.__data = requests.get(url=self.url)
            
        except* requests.ConnectionError as ce:
            raise ce.__doc__
        
        except* requests.RequestException as re:
            raise re.__doc__
        
        if (content):
            return self.__data.content
        
        return self.__data