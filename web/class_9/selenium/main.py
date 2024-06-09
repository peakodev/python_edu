from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://realpython.github.io/fake-jobs/")
with open("output.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)
driver.quit()
