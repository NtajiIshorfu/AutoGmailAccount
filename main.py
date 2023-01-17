from openpyxl import Workbook, load_workbook
from playwright.sync_api import sync_playwright
from time import sleep

book = load_workbook('Hilltop_Student_Database_for_Rise.xlsx')
url = "https://accounts.google.com/signup/v2/webcreateaccount?biz=true&cc=NG&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fpli%3D1&dsh=S906961054%3A1673951804434429&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&service=accountsettings&authuser=0"
# url = "https://accounts.google.com/signup/v2/webcreateaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fpli%3D1&hl=en&parent_directed=true&flowName=GlifWebSignIn&flowEntry=SignUp"
# url = "https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=NG&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fpli%3D1&dsh=S906961054%3A1673951804434429&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&service=accountsettings&authuser=0"
sheet = book.active

first_names = [sheet[f'A{i}'].value for i in range(2,74)]
last_names = [sheet[f'B{i}'].value for i in range(2,74)]
genders = [sheet[f'A{i}'].value for i in range(2,74)]
birth_dates = [sheet[f'B{i}'].value for i in range(2,74)]
phone_numbers = [sheet[f'A{i}'].value for i in range(2,74)]
phone = '08170770083'

with sync_playwright() as p:
    # for student in len():
    browser = p.chromium.launch(headless = False, slow_mo = 500)
    page = browser.new_page()
    page.goto(url)
    page.fill('//*[@id="firstName"]', first_names[0])
    page.fill('//*[@id="lastName"]', last_names[0])
    page.fill('//*[@id="username"]', first_names[0]+last_names[0]+'2023')
    page.fill('//*[@id="passwd"]/div[1]/div/div[1]/input', f"{first_names[0]}-{last_names[0]}-2023")
    page.fill('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input', f"{first_names[0]}-{last_names[0]}-2023")
    page.click('//*[@id="accountDetailsNext"]/div/button/div[1]')
    # page.fill('//*[@id="phoneNumberId"]', phone)
    page.click('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]')
    sleep(20)