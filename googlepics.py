from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
import selenium.common.exceptions
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import os

PATH = 'D:/myfolder/'  # dir path to save files
WORD = 'summer'  # search query
N = 2  # numbers of pages to list


SIZE_BIG = '&tbs=isz%3Al'
SIZE_ANY = ''
SIZE_MIDDLE = '&tbs=isz%3Am'


def pic_size_to_search(size=SIZE_BIG):
    if size == SIZE_ANY:
        return f'https://www.google.com/search?q={WORD}&tbm=isch'
    elif size == SIZE_MIDDLE:
        return f'https://www.google.com/search?q={WORD}&tbm=isch{SIZE_MIDDLE}'
    return f'https://www.google.com/search?q={WORD}&tbm=isch{size}'


def make_dir():
    try:
        os.mkdir(PATH + WORD)
    except FileExistsError:
        pass


def gather_thumbs():
    opt = Options()
    opt.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/74.0.3729.169 Safari/537.36')
    opt.add_argument("--disable-notifications")
    browser = Chrome(executable_path='chromedriver.exe', options=opt)
    browser.maximize_window()
    browser.get(URL)
    for _ in range(N):
        browser.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(1)
        try:
            browser.find_element_by_css_selector('input.mye4qd').click()
            sleep(1)
        except selenium.common.exceptions.ElementNotInteractableException:
            pass
        over = browser.find_element_by_css_selector('div.Yu2Dnd').text
        if over != '':
            break
    thumbs_urls = browser.find_elements_by_css_selector('a.mM5pbd')
    list_urls = []
    for href in thumbs_urls:
        action_chains = ActionChains(browser)
        action_chains.context_click(href).perform()
        list_urls.append(href.get_attribute('href'))
        if len(list_urls) % 30 == 0:
            print('collecting links ...', len(list_urls))
    browser.close()
    print('------------------------THUMBS collected. Total: ', len(list_urls))
    return list_urls


def clear_name(uncleaned_url):
    bad_symbols = '/?:*"<>|\\'
    for sym in uncleaned_url:
        if sym in bad_symbols:
            uncleaned_url = uncleaned_url.replace(sym, '')
    return uncleaned_url


def check_get_error(url):
    try:
        image = requests.get(url, timeout=5)
        return image
    except Exception as e:
        print('----ERROR---', url)
        return None


def save_pics(url):
    image = check_get_error(url)
    if image is not None and image.status_code == 200:
        image = image.content
        name = clear_name(url)
        if name[-3:] not in ['jpg', 'png', 'peg', 'gif', 'svg', 'ebp']:
            name = name + '.jpg'
        with open(f'{PATH}{WORD}/{name[-22:]}', 'wb') as p:
            p.write(image)
        print('saved:', url)


def collect_pics(all_urls):
    sess = requests.Session()
    sess.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                       'like Gecko) Chrome/74.0.3729.169 Safari/537.36'})
    for thumb in all_urls:
        resp = check_get_error(thumb)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            pic_link = soup.find('title').text.split(' ')[-1].strip()
            save_pics(pic_link)


URL = pic_size_to_search()  # generated URL
make_dir()
thumbs = gather_thumbs()
collect_pics(thumbs)
