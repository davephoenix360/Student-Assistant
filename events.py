from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import sys
from playwright.sync_api import sync_playwright

def Events(discipline):
        
    dis_url = '%20'.join(discipline)

    url = "https://alberta.campuslabs.ca/engage/events?query=" + dis_url

    # Use sync version of Playwright
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch()

        # Open a new browser page
        page = browser.new_page()

        # Create a URI for our test file
        page_path = url

        # Open our test file in the opened page
        page.goto(page_path)
        page_content = page.content()

        # Process extracted content with BeautifulSoup
        soup = BeautifulSoup(page_content, features="html.parser")
        results = soup.find(id="event-discovery-list")
        
        event_elements_heads = results.find_all("h3")
        
        headers = []
        
        for elem in event_elements_heads:    
            headers.append(elem.get_text())
        
        source_text = str(results)
        start_index = 0
        indexes = []
        links = []
        mydict = {}
        
        while start_index < len(source_text):
            index = source_text.find('/engage/event/', start_index+1)
            if index != -1:
                indexes.append(index)
                start_index = index
            else:
                break
        
        for i in indexes:
            links.append("https://alberta.campuslabs.ca" + source_text[i:i+20])
            
        for i in range(len(headers)):
            mydict[headers[i]] = links[i]
        
        return mydict

        # Close browser
        browser.close()
        
if __name__ == "__main__":
    discipline = sys.argv[1:]
    print(Events(discipline))