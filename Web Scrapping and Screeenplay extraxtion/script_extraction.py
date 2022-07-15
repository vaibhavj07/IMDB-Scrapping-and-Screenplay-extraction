from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as Soup
import requests
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://imsdb.com/")
url = "https://www.imdb.com/list/ls055592025/"
page = requests.get(url)
response = page.text
soup_data = Soup(response,'html.parser')
movies = soup_data.findAll('div',{'class':'lister-item mode-detail'})
movie = []
for i in movies:
    movie.append(i.find('h3',{'class':'lister-item-header'}).a.text)

print(movie)
not_found = []
not_found2 = []
    
for i in range(len(movie)):
    a = movie[i]
    print("searching for: " + a)
    if "The" in movie[i]:
        a = a.replace("The","")
    if ":" in movie[i]:
        a = a.replace(":","")
    a = a.strip()
    try:
        movie_search = driver.find_element_by_name("search_query")
        movie_search.send_keys(a)
        movie_search.send_keys(Keys.RETURN)
        time.sleep(2)  
        link = driver.find_element_by_partial_link_text(a)
        link.click()
        time.sleep(2)
        link1 = driver.find_element_by_partial_link_text("Read")
        driver.execute_script("arguments[0].scrollIntoView();",link1)
        link1.click()
        time.sleep(2)
        print("Found script")
        search_result = driver.find_element_by_xpath("//table/tbody/tr[1]/td[3]")
        print("Saved Script")
        f = open("scripts\ "+a+"_screenplay.txt","w",encoding='utf-8')
        f.write(search_result.text)
        print("Copied Script for movie " + a)
        f.close()
        time.sleep(2)
    #link2 = driver.find_element_by_partial_link_text("The Internet Movie Script Database")
    #link2.click()
        time.sleep(2)
        driver.get("https://imsdb.com/")
    except:
        print("Movie not found: " + a)
        not_found.append(movie[i])
        driver.get("https://imsdb.com/")

driver.get("https://www.simplyscripts.com/movie-screenplays.html")
print(not_found)
print("Searching for Movie on simplyscripts.com")

pdf = "pdf"
for movie in not_found:
    try:
        print("Searching for: "+ movie)
        links = driver.find_element_by_link_text(movie)
        print("got link")
        driver.execute_script("arguments[0].scrollIntoView();",links)
        link2 = links.get_attribute("href")
        if pdf in str(link2):
            not_found2.append(movie)
        else:
            driver.get(link2)
            time.sleep(2)
            content = driver.find_element_by_tag_name('body')
            if ":" in movie:
                movie = movie.replace(":","")
                movie = movie.strip() 
                f = open("scripts\ "+movie+"_screenplay.txt","w",encoding='utf-8')
                f.write(content.text)
                print("Copied Script for movie " + movie)
                f.close()
            else:
                f = open("scripts\ "+movie+"_screenplay.txt","w",encoding='utf-8')
                f.write(content.text)
                print("Copied Script for movie " + movie)
                f.close()
            driver.get("https://www.simplyscripts.com/movie-screenplays.html")
    except:
        print("Movie not found" + movie)
        not_found2.append(movie)
        driver.get("https://www.simplyscripts.com/movie-screenplays.html")

driver.get("https://www.scripts.com/scripts")
print(not_found2)
print("Searching for Movie on  scripts.com")
i = 0

for m in not_found2:
    try:
        script2 = ""
        movie_search = driver.find_element_by_name("st")
        print("searching for movie:" + m)
        movie_search.send_keys(m)
        movie_search.send_keys(Keys.RETURN)
        link = driver.find_element_by_link_text(m)
        driver.execute_script("arguments[0].scrollIntoView();",link)
        link2 = link.get_attribute("href")
        driver.get(link2)
        while True:
            try:
                script = driver.find_element_by_class_name("wselect-cnt")
                script2 = script2 + script.text
                Next = driver.find_element_by_partial_link_text("Next")
                driver.execute_script("arguments[0].scrollIntoView();",Next)
                Next2 = Next.get_attribute("href")
                driver.get(Next2)
            except:
                break
                      
        f = open("scripts\ "+m+"_script.txt","w",encoding='utf-8')
        f.write(script2)
        print("Copied Script for movie " + m)
        f.close()
        i=i+1
        driver.get("https://www.scripts.com/scripts") 
    except:
        print("Movie not found" + m)

print("Found available screenplays")
driver.quit()

