# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:58:03 2022

@author: louyu
"""

class analysis_system:
    def __init__(self, upperbound,times_in_a_row):
        self.upperbound=upperbound             #消費金額上限
        self.timelimit=[[20000,70000]]   #非正常消費時間
        self.times_in_a_row=times_in_a_row #一小時內連續消費次數上限
        self.privous_consumption_time=[]  #紀錄曾經消費時間
        self.data_count=50;
        self.auto_upperbound=upperbound
        self.different_upperbound=0.1
        
    def add_time_limit(self,start_time,end_time):   #增訂非正常消費時間
        self.timelimit.append([start_time,end_time])
        
    def privous_consumption_time(self,consumption_time):   #增加曾經消費時間(僅特殊情況使用)
        self.privous_consumption_time.append(consumption_time)
        
    def show_time_limit(self):                      #顯示非正常消費時間
        for cnt,i in enumerate(self.timelimit):
            print("第%d筆從%d到%d"%(cnt,i[0],i[1]))
    def delete_time_limit_time_limit(self,cnt):     #刪除非正常消費時間
        del self.timelimit[cnt]
    
    def detect_execption(self,data):                #例外偵測
        time_error=self.__time_detection(data)                       #消費時間例外偵測
        upperbound_error=self.__upperbound_detection(data)           #交費金額例外偵測
        times_in_a_row_error=self.__times_in_a_row_detection(data)   #連續消費例外偵測
        self.auto_upperbound=self.auto_upperbound*(self.data_count/(self.data_count+1))+(data.amount/(self.data_count+1))#更新消費平均
        if self.auto_upperbound-self.upperbound>self.auto_upperbound*self.different_upperbound:#如果消費平均與設定差1成
            #通知使用者應該修正數值
            print("請E-Mail通知使用者預測數值為",self.auto_upperbound,self.upperbound)
        self.data_count+=1#消費計數+1
        return [time_error,upperbound_error,times_in_a_row_error]
        
    def __time_detection(self,data):
        for i,j in self.timelimit:        #檢測是否在記錄的時間範圍內
            if(data.consumption_time%1000000>i and data.consumption_time%1000000<j):
                return True
        return False
    
    def __upperbound_detection(self,data):
        if(data.amount>self.upperbound):   #檢測是否超過消費上界
            return True
        return False
    
    def __times_in_a_row_detection(self,data):  
        #print(self.privous_consumption_time)
        for i in self.privous_consumption_time:     #檢測並消去超過一小時以上的消費紀錄
            if i+10000 < data.consumption_time:     #將資料時間加1小時後做比對
                #print(self.privous_consumption_time.index(i))
                del self.privous_consumption_time[self.privous_consumption_time.index(i)]
                
        self.privous_consumption_time.append(data.consumption_time) #將這筆消費紀錄起來
        
        #print(self.privous_consumption_time)
        if len(self.privous_consumption_time)>self.times_in_a_row:  #若連續消費超過限制則有異常
            return True
        return False
        
#測試用信用卡消費紀錄結構 
class a:
    def __init__(self, consumption_time,amount):
        self.consumption_time=consumption_time#消費時間
        self.amount=amount#消費金額

func=analysis_system(9000,3)
func.show_time_limit()
func.add_time_limit(190000, 220000)
func.show_time_limit()
#時間資料為年月日時分秒
testa=a(20220610030522,1000)
testb=a(20220610090722,2000)
testc=a(20220610090822,7000)
testd=a(20220610090922,8000)
teste=a(20220610091022,100000)
#第一個參數為消費時間是否異常，第二個參數為消費金額是否異常，第三個參數為連續消費次數是否異常
print(func.detect_execption(testa))
print(func.detect_execption(testb))
print(func.detect_execption(testc))
print(func.detect_execption(testd))
print(func.detect_execption(teste))
