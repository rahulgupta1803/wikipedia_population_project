from selenium.webdriver.common.by import By


class Population():
    no_of_data_XPATH = (By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr/td')
    header_XPATH = (By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/thead/tr/th')
    no_of_column_XPATH =(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr[1]/td')
    no_of_rows_XPATH = (By. XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr/td[1]')

    def __init__(self,driver):
        self.driver=driver

    def Header(self,h):
        p=self.driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/thead/tr/th['+str(h)+']').text
        return p

    def Data(self,r,c):
        g=self.driver.find_element(By. XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr['+str(r)+']/td['+str(c)+']').text
        return g

    # def Col(self,c):
    #     l=self.driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr[1]/td['+str(c)+']').text
    #     return l

    def RowsCount(self):
        n=len(self.driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr/td[1]'))
        return n

    def ColCount(self):
        m=len(self.driver.find_elements(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[9]/tbody/tr[1]/td'))
        return m

    def Scroll(self):
        m=self.driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/thead/tr/th[1]')
        self.driver.execute_script("arguments[0].scrollIntoView();",m)

    def End_value(self,h):
        y=self.driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[9]/tfoot/tr/th['+str(h)+']').text
        return y
