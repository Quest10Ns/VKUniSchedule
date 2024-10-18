import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

patern = re.compile(r'\d{4}\w{0,2} ▼')

def get_groups():
    driver.get("https://guap.ru/rasp/")
    groups = []
    for group in driver.find_elements("xpath", "//select[@name='ctl00$cphMain$ctl05']/option"):
        groups.append([group.get_attribute("value"), group.text])

    return groups[1:]

def get_schedule(group_id):
    driver.get(f'https://guap.ru/rasp/?g={group_id}')
    pages = driver.page_source
    count = 0
    start = 0
    endLine = 0
    schedule = []
    for i in range(len(pages)):
        if pages[i:i+4] == '<h3>' and count == 0:
            start = i
            count = 1
        elif pages[i:i+31] == '</span></div></div></div></div>' and count == 1:
            endLine = i
            break

    pages = pages[start:endLine].split("<h3>")

    for page in pages:
        page = page.replace('<h4>', '--')
        for i in range(page.count('<')):
            start = page.find('<')
            end = page.find('>')
            page = page[:start:] + ' ' + page[end + 1::]

        while '  ' in page:
            page = page.replace('  ', ' ')

        schedule.append(page.split("--"))
    return schedule[1:]

all_groups = get_groups()

with open(f'all_schedules.txt', 'w', encoding='utf-8') as gs:
    for i in range(len(all_groups)):
        print(( all_groups[i][1]+'\n'), file=gs)
        schedule_for_group = get_schedule(all_groups[i][0])
        for day in schedule_for_group:
            for lessons in day:
                if re.search(patern, lessons):
                    upper_week, down_week = lessons.split(' ▼')
                    print(f'{upper_week}\n{'\t'*5+' '}▼{down_week}', file=gs)
                else:
                    print(lessons, file=gs)
            print('\n', file=gs)
        print('\n', file=gs)
