import pandas as pd
from click import password_option
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

service = Service(r"C:\Users\M S I\Downloads\Data Analytics\Web Scaping\chromedriver-win64\chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()

base_url='https://www.freshersworld.com/jobs/category/it-software-job-vacancies'
def return_tot_url_list(url1,n1):
    base_url=url1
    url_tot=[]
    url_tot.append(base_url)
    count=20
    for i in range(n1-1):
        url_new=base_url+"?&limit=20&offset="+str(count)
        url_tot.append(url_new)
        count=count+20
    return url_tot


def main_program(url3,n2):
    job_titles=[]
    companies=[]
    experience=[]
    salary=[]
    location=[]
    url_tot_list=return_tot_url_list(url3,n2)
    for k in url_tot_list:
        try:
            driver.get(k)
            time.sleep(5)
            for i in range(1,24):
                if i !=2 and i !=8 and i !=10:
                    print(i)
                    try:
                        job_titles_element = driver.find_element('xpath',
                                                                 f'/html/body/div[10]/div[3]/div[2]/div/div[2]/div/div/div[{i}]/div[2]/div/div[1]/div[1]/span[1]')
                        job_titles.append(job_titles_element.text)
                    except:
                        job_titles.append('N/A')
                    try:
                        companies_element = driver.find_element('xpath',
                                                                f'/html/body/div[10]/div[3]/div[2]/div/div[2]/div/div/div[{i}]/div[2]/div/div[1]/h3')
                        companies.append(companies_element.text)
                    except:
                        companies.append('N/A')
                    try:
                        experience_element = driver.find_element('xpath',
                                                                 f'/html/body/div[10]/div[3]/div[2]/div/div[2]/div/div/div[{i}]/div[2]/div/div[1]/div[3]/div/span[2]')
                        experience.append(experience_element.text)
                    except:
                        experience.append('N/A')
                    try:
                        salary_element = driver.find_element('xpath',
                                                             f'/html/body/div[10]/div[3]/div[2]/div[1]/div[2]/div/div/div[{i}]/div[2]/div/div[1]/div[4]/span[2]')
                        salary.append(salary_element.text)
                    except:
                        salary.append('N/A')
                    try:
                        location_element = driver.find_element('xpath',
                                                               f'/html/body/div[10]/div[3]/div[2]/div[1]/div[2]/div/div/div[{i}]/div[2]/div/div[1]/div[2]/span[2]/a')
                        location.append(location_element.text)
                    except:
                        location.append('N/A')


        except:
            pass
    data = {
        'job_title': job_titles,
        'Experience': experience,
        'Company': companies,
        'Salary': salary,
        'Location':location


    }
    df=pd.DataFrame(data)


    return df


g=main_program(base_url,63)
g.to_csv("freshers_final cleaned_63check.csv", index=False)

