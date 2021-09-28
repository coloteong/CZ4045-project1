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

def getCNAurl():
    url = 'https://www.channelnewsasia.com/'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    linked_urls = set()

    def get_all_links(url):
        urls = set()
        domain_name = urlparse(url).netloc
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                # href empty tag
                continue
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            # remove URL GET parameters, URL fragments, etc.
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if href in urls:
                # already in the set
                continue
            if domain_name not in href:
                # external link
                continue
            if len(href) > 60:
                urls.add(href)
        return urls
    
    urls_cna = get_all_links('https://www.channelnewsasia.com/')
    url = random.sample(urls_cna, 1)
    print("Found URL: ", url[0])
    
    page1 = requests.get(url[0])
    soup1 = BeautifulSoup(page1.content, "html.parser")
    text = list(soup1.find_all("p"))
    cna_text = [txt.get_text() for txt in text]
   
    return cna_text

