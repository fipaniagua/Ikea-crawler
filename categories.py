from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from openpyxl import Workbook

def get_categories(browser):
    info = []
    categories = browser.find_elements_by_class_name("vn-p-grid-gap")
    for category in categories:
        category_name = category.find_element_by_tag_name("h4").text
        sub_categories = category.find_elements_by_tag_name("li")
        for sub_category in sub_categories:
            sub_category_name = sub_category.text
            sub_category_url = sub_category.find_element_by_tag_name("a").get_attribute('href')
            info.append([category_name, sub_category_name, sub_category_url])
    return info     

def save_info(info, file_name):
    wb = Workbook()
    ws = wb.active
    for row in info:
        ws.append(row)
    wb.save(file_name)        

if __name__ == "__main__":
    path_to_chromedriver = "./chromedriver.exe"
    browser = webdriver.Chrome(executable_path = path_to_chromedriver)
    page_url = "https://www.ikea.com/es/es/cat/productos-products/"
    browser.get(page_url)
    category_info = get_categories(browser)
    save_info(category_info, "categories.xlsx")