if (__debug__):
    try:
        import re
        import bs4
        from colorama.ansi import Fore
        from colorama.initialise import init
        from typing import Self, Literal, Any
        from ..request_handler import RequestHandler
    
    except* ModuleNotFoundError as mnfe:
        raise mnfe.__doc__
    
    except* ImportError as ie:
        raise ie.__doc__
    
    






class Scrape:
    def __init__(self: Self, data: RequestHandler) -> Literal[None]:
        self.__data = data
        self.__json_data = {}
        
    @property
    def fullname(self: Self) -> str:
        self.__json_data['fullname'] = bs4.BeautifulSoup(
            markup=self.__data,
            features='html5lib',
        ).find(
            name='span',
            attrs={
                'class': 'p-name vcard-fullname d-block overflow-hidden',
            }
        ).text
        
        return self.json_data['fullname']
    
    @property
    def followers(self: Self) -> int:
        self.__json_data['followers'] = bs4.BeautifulSoup(
            markup=self.__data,
            features='html5lib',
        ).find(
            name='span',
            attrs={
                'class': 'text-bold color-fg-default',
            }
        ).text
        
        return self.json_data['followers']
    
    @property
    def followings(self: Self) -> int:
        self.__json_data['followings'] = re.search(
            pattern=r'\d+',
            string=str(bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find_all(
                name='span',
                attrs={
                    'class': 'text-bold color-fg-default',
                }
            )[1]),
        ).group()
        
        return self.json_data['followings']
    
    @property
    def biography(self: Self) -> str:
        self.__json_data['biography'] = bs4.BeautifulSoup(
            markup=self.__data,
            features='html5lib',
        ).find(
            name='div',
            attrs={
                'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'
            }
        ).text
        
        return self.json_data['biography']
    
    @property
    def location(self: Self) -> str:
        self.__json_data['location'] = bs4.BeautifulSoup(
            markup=self.__data,
            features='html5lib',
        ).find(
            name='span',
            attrs={
                'class': 'p-label',
            }
        ).text
        
        return self.json_data['location']
    
    @property
    def website(self: Self) -> str:
        self.__json_data['website'] = bs4.BeautifulSoup(
            markup=self.__data,
            features='html5lib',
        ).find(
            name='a',
            attrs={
                'class': 'Link--primary',
            }
        ).text
        
        return self.json_data['website']
    
    @property
    def totalRepositories(self: Self) -> int:
        self.__json_data['totalRepositories'] = bs4.BeautifulSoup(
            markup=self.__data,
            features='html5lib',
        ).find(
            name='span',
            attrs={
                'class': 'Counter',
                'data-view-component': 'true',
            }
        ).text
        
        return self.json_data['totalRepositories']
    
    def repositoriesNames(self: Self, username: str, ftl: bool = False) -> list[str]:
        names: list = []
        
        for element in bs4.BeautifulSoup(markup=self.__data, features='html5lib').find(name='h3', attrs={'class': 'wb-break-all'}).find_all_next(name='a', attrs={'itemprop': 'name codeRepository'}):
            names.append(str(element).replace('href', '').replace('itemprop="name codeRepository', '').replace(f'<a ="/{username}/', '').replace('</a>', '').replace('">', '').replace('"', '').split(sep=' ')[0])
        
        self.json_data['repositoriesNames'] = names
        
        if (ftl):
            return names[::-1]
        return names
        
    @property
    def json_data(self: Self) -> dict[str, Any]:
        return self.__json_data
    
    def startApi(self: Self, log: bool = True) -> Literal[None]:
        if (log):
            init()
            print(f'{Fore.GREEN}Api Started Successfully{Fore.WHITE}')
        
        self.__json_data = {
            'fullname': self.fullname,
            'followers': self.followers,
            'followings': self.followings,
            'biography': self.biography,
            'location': self.location,
            'website': self.website,
            'totalRepositories': self.totalRepositories,
        }