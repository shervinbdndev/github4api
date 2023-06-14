if (__debug__):
    try:
        from typing import Self, Literal
    
    except* ModuleNotFoundError as mnfe:
        raise mnfe.__doc__
    
    except* ImportError as ie:
        raise ie.__doc__
    





class UserHandler:
    def __init__(self: Self, username: str) -> Literal[None]:
        super(UserHandler, self).__init__()
        self.__username = username
        
    @property
    def username(self: Self) -> str:
        return self.__username
        
    def serialize(self: Self, get_repos: bool = False, get_achievements: bool = False, _: bool = False, repo_name: str = None) -> str:
        if (get_repos):
            return f'https://github.com/{self.username}?tab=repositories'
        if (get_achievements):
            return f'https://github.com/{self.username}?tab=achievements'
        if (_):
            return f'https://github.com/{self.username}/{repo_name}'
        return f'https://github.com/{self.username}'