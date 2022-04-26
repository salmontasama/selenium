from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def init():
    driver = webdriver.Chrome("C:/Users/IMOE001/PycharmProjects/pythonProject/pythonProject/Driver/chromedriver.exe")
    driver.get('https://atid.store/about/')
    driver.maximize_window()
    return driver


def test_Ui_Top_Page():
    driver = init()
    top_page = driver.find_element(By.XPATH,
                                   "//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]").get_attribute(
        'innerText')
    assert top_page == 'HOME\nSTORE\nMEN\nWOMEN\nACCESSORIES\nABOUT\nCONTACT US\nSearch\n0.00\xa0₪ 0'
    about = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div["
                                          "1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/h1[1]").get_attribute(
        'innerText')
    assert about == 'About Us'

def test_accessibility_button():
    driver = init()
    accessibility = driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]").get_attribute('innerText')
    assert accessibility == "Accessibility Tools\n\nIncrease Text\nDecrease Text\nGrayscale\nHigh Contrast\nNegative " \
                            "Contrast\nLight Background\nLinks Underline\nReadable Font\n Reset"



def test_middle_page():
    driver = init()
    Who_We_Are = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main["
                                              "1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div["
                                              "1]/section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div["
                                              "1]").get_attribute(
        'innerText')
    assert Who_We_Are == "Who We Are\n\nATID Demo Store was created by ATID College dedicated employees. This is a complete demo site for practicing QA & Test Automation methodologies. Don't think for a second you can actually buy here something cause you can't ! This Demo Store contains software bugs which were put intentionally and your job is to locate them Good luck falks, Yoni Flenner - ATID College"

    Fow_Worde = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div["
                                             "1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[2]/div[1]/h4["
                                             "1]").get_attribute(
        'innerText')
    assert Fow_Worde == "A Few Words About"

    Our_Team = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]").get_attribute(
        'innerText')
    assert Our_Team == "Our Team\n\nWe have the best team ever everybody who is somebody wants to work with us, so we can afford cherry-picking them, one by one..."

    Follow_Us = driver.find_element(By.XPATH,"//h2[contains(text(),'Follow Us')]").get_attribute(
       'innerText')
    assert Follow_Us == "About Us"


def test_Bottom_page():
    driver = init()
    top_bottom = driver.find_element(By.XPATH,"//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main["
                                             "1]/article[1]/div[1]/div[1]/div[1]/section[5]").get_attribute(
        'innerText')
    assert top_bottom == "Worldwide Shipping\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus " \
                         "leo.\n\nBest Quality\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus " \
                         "leo.\n\nBest Offers\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus " \
                         "leo.\n\nSecure Payments\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus " \
                         "leo."
    middle_bottom= driver.find_element(By.XPATH,"//body/div[@id='page']/footer[@id='colophon']/div[1]").get_attribute(
        'innerText')
    assert middle_bottom == "Quick Links\nHome\nAbout\nCart\nContact Us\nFor Her\nWomen Jeans\nTops and Shirts\nWomen " \
                            "Jackets\nHeels and Flats\nWomen Accessories\nFor Him\nMen Jeans\nMen Shirts\nMen " \
                            "Shoes\nMen Accessories\nMen Jackets"
    bottom_bottom = driver.find_element(By.XPATH,"//body/div[@id='page']/footer[@id='colophon']/div[2]").get_attribute(
        'innerText')
    assert bottom_bottom == "Copyright © 2022 ATID Demo Store\n\nPowered by ATID College"



