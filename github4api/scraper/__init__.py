if (__debug__):
    try:
        import re
        import sys
        import bs4
        import requests
        from colorama.ansi import Fore
        from colorama.initialise import init
        from typing import Self, Literal, Union, Any
        from ..handlers.user_handler import UserHandler
        from ..handlers.request_handler import RequestHandler
        from ..exceptions import UserHasNoLocationException, NonePublicArchiveRepositoryException, NoneFilledPropertyException
    
    except* ModuleNotFoundError as mnfe:
        raise mnfe.__doc__
    
    except* ImportError as ie:
        raise ie.__doc__
    
    






class Scrape:
    def __init__(self: Self, data: RequestHandler) -> Literal[None]:
        super(Scrape, self).__init__()
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
        ).text.strip()
        
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
        try:
            self.__json_data['biography'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='div',
                attrs={
                    'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'
                }
            ).text
        except:
            self.json_data['biography'] = NoneFilledPropertyException.__doc__
        
        return self.json_data['biography']
    
    @property
    def location(self: Self) -> str:
        try:
            self.__json_data['location'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'p-label',
                }
            ).text
        except:
            self.__json_data['location'] = UserHasNoLocationException.__doc__
        
        return self.json_data['location']
    
    @property
    def website(self: Self) -> str:
        try:
            self.__json_data['website'] = bs4.BeautifulSoup(
                markup=self.__data,
                features='html5lib',
            ).find(
                name='a',
                attrs={
                    'class': 'Link--primary',
                }
            ).text
        except:
            self.json_data['website'] = NoneFilledPropertyException.__doc__
        
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
    
    @property
    def totalStarsGiven(self: Self) -> int:
        self.__json_data['totalStarsGiven'] = bs4.BeautifulSoup(
            markup=self.__data,
            features='html5lib',
        ).find(
            name='svg',
            attrs={
                'class': 'octicon octicon-star UnderlineNav-octicon hide-sm',
            }
        ).find_next(
            name='span',
        ).get_text()
        
        return self.json_data['totalStarsGiven']
    
    def repositoriesNames(self: Self, username: str, ftl: bool = False) -> list[str]:
        names: list = []
        
        for element in bs4.BeautifulSoup(markup=RequestHandler(url=UserHandler(username=username).serialize(get_repos=True)).sendGetRequest(content=True), features='html5lib').find(name='h3', attrs={'class': 'wb-break-all'}).find_all_next(name='a', attrs={'itemprop': 'name codeRepository'}):
            names.append(str(element).replace('href', '').replace('itemprop="name codeRepository', '').replace(f'<a ="/{username}/', '').replace('</a>', '').replace('">', '').replace('"', '').split(sep=' ')[0])
        
        self.json_data['repositoriesNames'] = names
        
        if (ftl):
            return names[::-1]
        return names
    
    def repositoryDescription(self: Self, username:str, repo_name: str, reverse: bool = False) -> str:
        self.__json_data['repositoryDescription'] = bs4.BeautifulSoup(
            markup=RequestHandler(url=UserHandler(username=username,).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
            features='html5lib',
        ).find(
            name='p',
            attrs={
                'class': 'f4 my-3',
            },
        ).text.strip()
        
        if (reverse):
            return self.json_data['repositoryDescription'][::-1]
        return self.json_data['repositoryDescription']
    
    def isRepositoryPublicArchive(self: Self, username: str, repo_name: str) -> Union[str, bool, None]:
        status: bool = False
        
        try:
            self.__json_data['isRepositoryPublicArchive'] = bs4.BeautifulSoup(
                markup=RequestHandler(url=UserHandler(username=username,).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
                features='html5lib',
            ).find(
                name='span',
                attrs={
                    'class': 'Label Label--attention v-align-middle mr-1',
                },
            )
        
            if (self.__json_data['isRepositoryPublicArchive'].get_text(strip=True) == 'Public archive'):
                status = True
                return status
            else:
                return NonePublicArchiveRepositoryException.__doc__
        except:
            status = False
            return status
        
    def repositoryUsedLanguages(self: Self, username: str, repo_name: str) -> Union[list[str], list[None]]:
        langs: list[str] = []
        
        for lang in bs4.BeautifulSoup(markup=RequestHandler(url=UserHandler(username=username).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True), features='html5lib').find(name='ul', attrs={'class': 'list-style-none'}).find_all_next(name='span', attrs={'class': 'color-fg-default text-bold mr-1'}):
            langs.append(lang.text)
        return langs
    
    def userHasReadMe(self: Self, username: str) -> bool:
        self.__json_data['userHasReadMe'] = requests.get(url=f'https://github.com/{username}/{username}')
        
        if (self.__json_data['userHasReadMe'].status_code == 200):
            return True
        return False
    
    def userAchievements(self: Self, username: str) -> list[str]:
        achievements: list[str] = []
        
        for achievement in bs4.BeautifulSoup(markup=RequestHandler(url=UserHandler(username=username).serialize(get_achievements=True)).sendGetRequest(content=True), features='html5lib').find(name='div', attrs={'class': 'd-flex flex-wrap p-3'}).find_all_next(name='h3', attrs={'class': 'f4 ws-normal'}):
            achievements.append(achievement.text)
            
        return achievements
    
    def checkRepositoryStars(self: Self, username: str, repo_name: str) -> int:
        self.__json_data['checkRepositoryStars'] = bs4.BeautifulSoup(
            markup=RequestHandler(url=UserHandler(username=username).serialize(_=True, repo_name=repo_name)).sendGetRequest(content=True),
            features='html5lib',
        ).find(
            name='svg',
            attrs={
                'class': 'octicon octicon-star mr-2',
            }
        ).find_next(
            name='strong',
        ).get_text()
        
        return self.json_data['checkRepositoryStars']
    
    @property
    def lastYearContributions(self: Self) -> int:
        self.__json_data['lastYearContributions'] = int(
            str(
                bs4.BeautifulSoup(
                    markup=self.__data,
                    features='html5lib',
                ).find(
                    name='h2',
                    attrs={
                        'class': 'f4 text-normal mb-2',
                    }
                ).text.strip()
            ).split(sep=' ')[0]
        )
        
        return self.json_data['lastYearContributions']
    
    @property
    def profilePictureUrl(self: Self) -> str:
        self.__json_data['profilePictureUrl'] = bs4.BeautifulSoup(
            markup=self.__data,
            features='html5lib',
        ).find(
            name='img',
            attrs={
                'class': 'avatar avatar-user width-full border color-bg-default',
            }
        ).get_attribute_list(key='src')[0]
        
        return self.json_data['profilePictureUrl']
        
    @property
    def json_data(self: Self) -> dict[str, Any]:
        return self.__json_data
    
    def startApi(self: Self, log: bool = True) -> Literal[None]:
        if (sys.version_info[0:2] == (3, 11)):
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
                'totalStarsGiven': self.totalStarsGiven,
                'lastYearContributions': self.lastYearContributions,
                'profilePictureUrl': self.profilePictureUrl,
            }
        else:
            print(f"{Fore.YELLOW}Your Current Python Interpereter version is {Fore.CYAN}{sys.version.split(sep=' ')[0]}\n{Fore.YELLOW}This Package implemented for Python Version {Fore.GREEN}3.11\n{Fore.YELLOW}If you want to Use this Package, you have to update your interpreter{Fore.WHITE}")
            sys.exit(0)