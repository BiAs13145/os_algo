from random import randint
import numpy as np


class opt_algo :
    def __init__(self,max_frame_num) :
        self.max_frame_num = max_frame_num
        self.page = []
        self.page_num = 0
        self.page_fault_num = 0
        self.interrupt_num = 0
        self.disk_write = 0
        self.reference_string = []
        self.dplocation = np.zeros(601)
        #self.dplocation = np.zeros(10)
        self.pageloc = []


    def page_placement(self,reference_num,target_page) :
        check_set = set(self.page)
        #print(reference_num)
        #print(len(self.reference_string))
        #print("page :")
        #print(self.page)
        if (self.dplocation[target_page] <= reference_num) :#更新位置
                   for i in range(reference_num+1,len(self.reference_string)):
                        if (self.reference_string[i]==target_page) :#找到下一出現位置
                           self.dplocation[target_page] = i
                           break
                        if (i >= len(self.reference_string)-1) :
                           #print("之後找不到：")
                           #print(target_page)
                           self.dplocation[target_page] = 200000
        #print("future location:")
        #print(self.dplocation)
        if (target_page not in self.page) :
            self.page_fault_num +=1
            self.interrupt_num +=1
            #print("page fualt")

            if (len(self.page)<self.max_frame_num) : #ram未滿
               #print("ram未滿 加入")
               #print(target_page)
               self.page.append(target_page)
               
               
               
               self.interrupt_num +=1
            else :
             
             
                sel_vic = []
                for apage in self.page :
                    sel_vic.append(self.dplocation[apage])
                #print("sel_vic :")
                #print(sel_vic)
                

                victim_page = max(range(len(sel_vic)), key=sel_vic.__getitem__)
                #del self.page[victim_page]
                #print("page :")
                #print(self.page)
                #print("del:")
                #print(self.page[victim_page])
                self.page.remove(self.page[victim_page])
                #print("page :")
                #print(self.page)
                self.disk_write +=1
                self.interrupt_num +=1
                self.page.append(target_page)
                #print("add:")
                #print(target_page)
                self.interrupt_num +=1

                
                    
                        
                
                
                #print("加入")
                #print(target_page)
                
                            
                
                
        if(len(self.page)>self.max_frame_num) :
                print(target_page)
                print(victim_page)
                print("page num error")
                print("page_num:")
                print(len(self.page))
                print(self.page)
         
                
                
    def running (self,reference_string):
        result = []
        """for i in range(1,180001):
         self.reference_string.append(randint(1,600))"""
        """for i in range(1,1801):
         self.reference_string.append(i)"""
        #self.reference_string=[2,5,8,3,9,6,8,5,9,3,9,3,5,7,5,3,9,2,9,3,5,8,6]
        self.reference_string = reference_string
        
        #print(len(self.reference_string))

        

        for reference_num,page in enumerate(self.reference_string):
         self.page_placement(reference_num,page)
         
        result = []
        #result.append(self.page_fault_num/180000)
        result.append(self.page_fault_num/180000)

        result.append(self.page)
        result.append(self.disk_write)
        result.append(self.interrupt_num)
        return result
    
    def return_page_fault_rate (self):
        return self.page_fault_num/180000
    def return_page (self):
        return self.page
