import random
import requests
from urllib.request import urlopen
import urllib.request

def getSOFurl():
    while(True):
        ip0 = 'stackoverflow'
        ip1 = 'com'
        ip2 = 'questions'
        ip3 = str(random.randint(0, 100000000))
        url = 'https://' + ip0 + '.' + ip1 + '/'+ ip2 + '/'+ ip3
        try:
            urlContent = urlopen(url).read()
            if urlContent:
                break
        except Exception as e: 
            print(e)
            pass

    print("Found URL: " + url)
   
    return url



def getHWZurl():
    url = 'https://www.hardwarezone.com.sg/home'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    random.shuffle(urls)
    while(True):
        for url in urls:
            print(url)
            try:
                url = 'https://www.hardwarezone.com.sg' + url
                urlContent = urlopen(url).read()
                page1 = requests.get(url)
                soup1 = BeautifulSoup(page1.content, "html.parser")
                text = list(soup1.find_all("p"))
                hwz_text = [txt.get_text() for txt in text]
                if urlContent and len(hwz_text)>10:
                    break
            except Exception as e: 
                print(e)
        break
    print("Found URL: " + url)
    return hwz_text
