import time

from pageobjects.india_popul_page import Population
from utilities import xlutilis


class Test_India_Popul():
    fpath = "D:\\credence\\wikipedia_population_project\\testcases\\testdata\\india_population.xlsx"

    def test_india_popul(self,setup):
        self.driver = setup
        time.sleep(5)
        self.ipp=Population(self.driver)
        self.ipp.Scroll()
        rl= self.ipp.RowsCount()
        print('rows',rl)
        cl=self.ipp.ColCount()
        print('column',cl)
        for a in range(1,cl+1):
            xlutilis.WriteData(self.fpath,'Sheet1',1,a,self.ipp.Header(a))

            for b in range(1,rl+1):
                self.ipp.Data(b, a)
                xlutilis.WriteData(self.fpath, 'Sheet1', b+1, a, self.ipp.Data(b,a))

            xlutilis.WriteData(self.fpath,'Sheet1',rl+1,a,self.ipp.End_value(a))


        print("Operations completed")




# pytest -v -s --browser=chrome












