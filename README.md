<h1 align='center' style="font-size:5rem"><b>github4api</b></h1>
<p align='center'><b>Version 1.1.4</b></p>
<p align='center'><b>Written with Python 3.11.3</b></p>
<div align="center">
    <div align="center">
        <img src="https://img.shields.io/github/license/shervinbdndev/github4api.svg"></img>
    </div>
    <img src="https://img.shields.io/github/forks/shervinbdndev/github4api.svg"></img>
    <img src="https://img.shields.io/github/stars/shervinbdndev/github4api.svg"></img>
    <img src="https://img.shields.io/github/watchers/shervinbdndev/github4api.svg"></img>
    <img src="https://img.shields.io/github/issues-pr/shervinbdndev/github4api.svg"></img>
    <img src="https://img.shields.io/github/issues-pr-closed/shervinbdndev/github4api.svg"></img>
    <img src="https://img.shields.io/github/downloads/shervinbdndev/github4api/total.svg"></img>
</div>
<br>
<div align="center">
    <img style="display:block;margin-left:auto;margin-right:auto;width:70%;" src="https://github-readme-stats.vercel.app/api/pin/?username=shervinbdndev&repo=github4api&theme=dracula"></img>
</div>
<br>
<h3 align='center'>Ready To Use</h3>
<h3 align='center'>Developed by Shervin Badanara (shervinbdndev) on Github</h3>
<div align="center">
    <img src="https://forthebadge.com/images/badges/made-with-python.svg"></img>
</div>
<br>
<hr>
<br>
<h2 align='center'><b>Language and technologies used in This Project</h2>
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"></img>
<img src="https://img.shields.io/badge/Google_chrome-4285F4?style=for-the-badge&logo=Google-chrome&logoColor=white"></img>
<img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"></img>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"></img>
<img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"></img>
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></img>
<img src="https://img.shields.io/badge/Stack_Overflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white"></img>
<img src="https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=white"></img>

<br>
<h2 align='center'><b>WorkSpace</h2>
<img src="https://img.shields.io/badge/Intel-Core_i5_10600K-0071C5?style=for-the-badge&logo=intel&logoColor=white"></img>
<img src="https://img.shields.io/badge/NVIDIA-RTX2060 OC-76B900?style=for-the-badge&logo=nvidia&logoColor=white"></img>
<img src="https://img.shields.io/badge/Windows11-0078D6?style=for-the-badge&logo=windows&logoColor=white"></img>


<hr>

<br><br><br>

<h1 align='center' style='color:#ff0080; font-size:3rem;'><b>! Warning !</h1>


- ## This package uses ``` ExceptionGroup ``` to handle exceptions.
- ## You have to use python [3.11](https://www.python.org/downloads/) or above to be able to use this package.


<br><br><br>
<h1 align='left'><b>Update Your Interpreter</b></h1>

# Windows / CMD

```python
py -m pip install --upgrade pip
```

# Linux / Terminal

```python
python -m pip install --upgrade pip
```
<br>

<hr>
<br><br><br>
<h1 align='left'><b>Installation</b></h1>
 
# Windows / CMD , Linux / Terminal
```python
pip install github4api
```
<h2 align='left'>or</h2>

```python
py -m pip install github4api
```

<br><br><br>
<h1 align='left'><b>Update Library</b></h1>
 
# Windows / CMD , Linux / Terminal
```python
pip install -U github4api
```

<h2 align='left'>or</h2>

```python
py -m pip install --upgrade github4api
```

<br>

<hr>
<br><br><br>
<h1 align='left'><b>Usage</b></h1>

<br>

```python
from github4api.scraper import Scrape # Scraper Class
from github4api.handlers.user_handler import UserHandler # User Handler Class
from github4api.handlers.request_handler import RequestHandler # Request Handler Class


def main():

    # UserHandler serializes the value you given to the username param
    # RequestHandler gets the Serialized data then sends a GET request to github servers and saves the page content in request variable

    request: RequestHandler = RequestHandler(
        url=UserHandler(username='shervinbdndev').serialize(),
    ).sendGetRequest(content=True)
    

    # Scrape gets the variable as an arg

    scraper: Scrape = Scrape(data=request)

    # then we start using API by calling the startApi method
    
    scraper.startApi(log=False) # log param is for safety, the default value is True but you can change it
    

    # After all of these steps now you're free to use the API

    print(scraper.followers)
    print(scraper.followings)
    print(scraper.biography)
    
    print(scraper.json_data) # get full json data of user



if (__name__ == "__main__"):
    main()



```

<br><br><br>

# New Changes on Version 1.1.3

- ### Now you can Access User's Repositories Names

```py

from github4api.scraper import Scrape
from github4api.handlers.user_handler import UserHandler
from github4api.handlers.request_handler import RequestHandler




def main():
    request: RequestHandler = RequestHandler(
        url=UserHandler(username='shervinbdndev').serialize(get_repos=True), # for accessing the repositories you should set get_repos param to True
    ).sendGetRequest(content=True)
    
    scraper: Scrape = Scrape(data=request)
    
    scraper.startApi(log=False)

    # Then your free to use the new method to get User's Repositories names
    
    print(scraper.repositoriesNames(username='shervinbdndev'))

    # ftl (first to last) is a new option that you can use to show the repositories from the first created to the last one

    print(scraper.repositoriesNames(username='shervinbdndev', ftl=True)) # default value is False

    # Also you can select the repository by index like below

    print(scraper.repositoriesNames(username='shervinbdndev')[3]) # for example I want the 4th repository (It starts from 0 btw)



if (__name__ == "__main__"):
    main()



```

<br><br><br>

# New Changes on Version 1.1.4

## Now you can Access

- ### User's Total Stars Given
- ### User's Profile Picture Url
- ### Check Repository Star Count

```python

from github4api.scraper import Scrape
from github4api.handlers.user_handler import UserHandler
from github4api.handlers.request_handler import RequestHandler



def main():
    request: RequestHandler = RequestHandler(
        url=UserHandler(username='shervinbdndev').serialize()
    ).sendGetRequest(content=True)
    
    scraper: Scrape = Scrape(data=request)
    
    scraper.startApi(log=False)
    
    print(scraper.totalStarsGiven) # total stars given
    
    print(scraper.profilePictureUrl) # profile picture url

    # now using this new method you lets you check users repository's star count

    print(scraper.checkRepositoryStars(
        username='shervinbdndev', # user's username
        repo_name='Quizino', # repository's name
    ))




if (__name__ == "__main__"):
    main()

```

<br>

<h1 align='left'>Enjoy :)</h1>

<br>
<h3><b>Package Uploaded in PYPI :<a href="https://pypi.org/project/github4api/">Here</a></b></h3>