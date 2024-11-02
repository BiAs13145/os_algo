import numpy as np
from random import randint

class sec_ch_algo :
    def __init__(self,max_frame_num) :
        self.max_frame_num = max_frame_num
        self.page = []
        self.page_num = 0
        self.page_fault_num = 0
        self.interrupt_num = 0
        self.disk_write = 0
        self.reference_string = []
        self.reference_bit = np.zeros(601)
        self.dirty_bit = np.zeros(601)
        
    
    def page_placement(self,target_page) :
        check_set = set(self.page)
        #print("page")
        #print(self.page)
        
        
        if (target_page not in check_set) :
            #print("miss:")
            #print(target_page)
            self.page_fault_num +=1
            self.interrupt_num +=1
            
            if (self.page_num<self.max_frame_num) : #ram未滿
               self.page.append(target_page)
               self.reference_bit[target_page-1] = 1
               self.page_num  += 1
               self.interrupt_num +=1
            elif (self.page_num==self.max_frame_num) : #ram已滿
                replace_done = True
                cond = 0
                while (replace_done) :
                    match (cond%3) :
                        case 0 : #(00)
                            #print("case 0 start")
                            for page in self.page:
                                     if (self.reference_bit[page] == 0 and self.dirty_bit[page] == 0):
                                        self.page.remove(page)
                                        self.page.append(target_page)
                                        self.interrupt_num +=2
                                        self.disk_write +=1
                                        self.reference_bit[target_page] = 1
                                        replace_done = False
                                        break
                            
                        case 1 : #(01)
                            #print("case 1 start")
                            for page in self.page:
                                     if (self.reference_bit[page] == 0 and self.dirty_bit[page] == 1):
                                        self.page.remove(page)
                                        self.page.append(target_page)
                                        replace_done = False
                                        self.disk_write +=1
                                        self.interrupt_num +=2
                                        self.reference_bit[target_page] = 1
                                        break
                        case 2 : #(10)
                            #print("case 2 start")
                            for page in self.page:
                                self.reference_bit[page] = 0
                                #print("modify reference bit:")
                                #print(page)
                    cond +=1
                               
                                

                
        else : #在page
            #print("match:")
            #print(target_page)
            self.page.remove(target_page)
            self.page.append(target_page)
            self.reference_bit[target_page] = 1
        
        if(len(self.page)>self.max_frame_num) :
                print(target_page)
                
                print("page num error")
                print("page_num:")
                print(len(self.page))
                print(self.page)
            
    def running (self,reference_string):
        result = []
        self.page = []
        for d in self.dirty_bit :
            d = randint(0,1)
        """for i in range(1,180000):
         self.reference_string.append(randint(1,600))"""
        self.reference_string = reference_string
        #self.reference_string=[1,5,8,3,9,6,8,5,9,3,9,3,5,7,5,3,9,2,9,3,5,8,6]

        for page in self.reference_string:
         self.page_placement(page)
         
        result = []
        result.append(self.page_fault_num/180000)
        result.append(self.disk_write)
        result.append(self.interrupt_num)
        return result
    def return_page_fault_rate (self):
        return self.page_fault_num/180000
    def return_page (self):
        return self.page
    


    
        