from random import randint
#from fifo_page_algo import fifo_algo




class fifo_algo  :
    def __init__(self,max_frame_num) :
        self.max_frame_num = max_frame_num
        self.page = []
        self.page_num = 0
        self.page_fault_num = 0
        self.interrupt_num = 0
        self.disk_write = 0
        self.reference_string = []

    
    
        


    def page_placement(self,target_page) :
        check_set = set(self.page)

        if (target_page not in check_set) :
            self.page_fault_num +=1
            self.interrupt_num +=1

            if (self.page_num<self.max_frame_num) : #ram未滿
               self.page.append(target_page)
               self.page_num  += 1
               self.interrupt_num +=1
            else : #ram已滿
                self.page.remove(self.page[0])
                self.disk_write +=1
                self.interrupt_num +=1
                self.page.append(target_page)
                self.interrupt_num +=1

        
    
    def gen_reference_string (self):

        for i in range(1,180000):
         self.reference_string.append(randint(1,600))
    
    def running (self,reference_string):
        result = []
        self.page = []
        """for i in range(1,180000):
         self.reference_string.append(randint(1,600))"""
        self.reference_string = reference_string

        for page in self.reference_string:
         self.page_placement(page)
         
        result = []
        result.append(self.page_fault_num/180000)
        result.append(self.page)
        result.append(self.disk_write)
        result.append(self.interrupt_num)
        return result
    def return_page_fault_rate (self):
        return self.page_fault_num/180000
    def return_page (self):
        return self.page
     
    
    
    
class test_fifo_algo:
    def _init_(self):
        max_frame_num = 10
        fifo_result = {}
    def test_fifo_algo ():
        pass
    






