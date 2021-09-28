#import necessary library
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find('div', class_='list_text')
    title = article.find('div', class_="content_title").get_text()
    body = article.find('div', class_="article_teaser_body").get_text()
    
    #Featured Image
    url1 = "https://spaceimages-mars.com/"
    browser.visit(url1)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    header = soup.find('div', class_='header')
    image = header.find('img')
    featured_image_url = image['src']

    #Mars Facts
    import pandas as pd
    url2 = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(url2)
    df = tables[0] 
    df.columns = ['Comparison', 'Mars', 'Earth']
    df = df.iloc[1:]
    df.set_index('Comparison', inplace=True)

    #Mars Hemispheres
    url3 = "https://marshemispheres.com/"
    browser.visit(url3)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    boxes = soup.find('div', class_="result-list")
    title = boxes.find('h3').text
    link = boxes.find('a', class_="itemLink product-item")
    img_click = link['href']
    browser.click_link_by_partial_text(title)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    sample = soup.find("a", text="Sample")
    sample_url = sample['href']
    img_url = url3 + sample_url
    browser.back()

    # Quit the browser
    browser.quit()
    
    return listings
    
