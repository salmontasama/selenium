from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def init():
    driver = webdriver.Chrome("C:/Users/IMOE001/PycharmProjects/pythonProject/pythonProject/Driver/chromedriver.exe")
    driver.get('https://atid.store/about/')
    driver.maximize_window()
    return driver


# accessibility buutton
def test_accessibility_button():
    driver = init()
    driver.find_element(By.XPATH, "//body[1]/nav[1]/div[1]/a[1]").click()
    driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/ul[1]/li[1]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/ul[1]/li[2]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/ul[1]/li[3]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/ul[1]/li[4]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/ul[1]/li[5]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/ul[1]/li[6]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/ul[1]/li[7]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/ul[1]/li[8]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]/div[1]/ul[1]/li[9]/a[1]").click()
    # ui accessibility buutton
    accessibility = driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[2]").get_attribute('innerText')
    assert accessibility == "Accessibility Tools\n\nIncrease Text\nDecrease Text\nGrayscale\nHigh Contrast\nNegative " \
                            "Contrast\nLight Background\nLinks Underline\nReadable Font\n Reset"
    sleep(2)
    # driver.quit()
    # driver.close()


def test_follow_us():
    driver = init()
    driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div["
                                  "1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span[1]/a["
                                  "1]/i[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div["
                                  "1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span[2]/a["
                                  "1]/i[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div["
                                  "1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span[3]/a["
                                  "1]/i[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article[1]/div["
                                  "1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/span[4]/a["
                                  "1]/i[1]").click()
    sleep(2)
    # driver.quit()
    # driver.close()


def test_Quick_links():
    driver = init()
    driver.find_element(By.XPATH, "//body/div[@id='page']/footer[@id='colophon']/div[1]/div[1]/div[1]/div[1]/aside["
                                  "1]/div[1]/section[1]/nav[1]/ul[1]/li[1]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='page']/footer[@id='colophon']/div[1]/div[1]/div[1]/div[1]/aside["
                                  "1]/div[1]/section[1]/nav[1]/ul[1]/li[2]/a[1]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Cart')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//body/div[@id='page']/footer[@id='colophon']/div[1]/div[1]/div[1]/div[1]/aside["
                                  "1]/div[1]/section[1]/nav[1]/ul[1]/li[4]/a[1]").click()
    sleep(2)
    # driver.quit()
    # driver.close()


def test_For_Her():
    driver = init()
    driver.find_element(By.XPATH, "//a[contains(text(),'Women Jeans')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Tops and Shirts')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Women Jackets')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Heels and Flats')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Women Accessories')]").click()
    sleep(2)
    # driver.quit()
    # driver.close()


def test_For_Him():
    driver = init()
    driver.find_element(By.XPATH, "//a[contains(text(),'Men Jeans')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Men Shirts')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Men Shoes')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Men Accessories')]").click()
    sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Men Jackets')]").click()
    sleep(2)
    # driver.quit()
    # driver.close()


