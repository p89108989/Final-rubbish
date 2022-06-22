# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:58:03 2022

@author: louyu
"""
import random
import pymysql

class analysis_system:
    def __init__(self, acc=""):
        self.upperbound=9000          #消費金額上限
        self.timelimit=[[20000,70000]]      #非正常消費時間
        self.times_in_a_row=3  #一小時內連續消費次數上限
        self.privous_consumption_time=[]    #紀錄曾經消費時間XXX
        self.data_count=50;                 #紀錄計算過的筆數 
        self.auto_upperbound=9000     #預測消費金額上限 
        self.different_upperbound=0.1       #預測消費金額與設定消費金額上限 
        self.acc=acc
    def load_data(self):
        conn = pymysql.connect(host='203.204.10.191',port=3306,user='admin',passwd='PASSWORD',db='test',charset='utf8')
        cur = conn.cursor()
        if self.acc != "":   
            sql_1="SELECT predict_money, cost_in_one_hour, data_count,predict_money_custom  FROM login_system  WHERE account_id  ='" + self.acc + "' "
            cur.execute(sql_1)
            data_loginsys= cur.fetchall()   
            for i in data_loginsys:
                self.upperbound=i[0]
                self.times_in_a_row=i[1]
                self.data_count=i[2]
                self.auto_upperbound=i[3]
            print(self.upperbound,self.times_in_a_row,self.data_count,self.auto_upperbound)
            sql_2="SELECT time_start , time_finish  FROM time_limit WHERE account_id  ='" + self.acc + "' "
            cur.execute(sql_2)
            id_acc= cur.fetchall() 
            for i in id_acc:
                self.timelimit.append([i[0],i[1]])
            print(self.timelimit)
        conn.close()
        
    def renew_data(self):
        conn = pymysql.connect(host='203.204.10.191',port=3306,user='admin',passwd='PASSWORD',db='test',charset='utf8')
        cur = conn.cursor()
#        if acc != "":   
#            sql_1="SELECT COLUMN_NAME  FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'login_system' "
#            cur.execute(sql_1)
#            id_acc= cur.fetchall()   
#            print(id_acc)
#            sql_1="INSERT INTO login_system(account_id,predict_money, cost_in_one_hour, data_count,predict_money_custom)VALUES('"+str(self.acc)+"','"+str(self.upperbound)+"','"+str(self.times_in_a_row)+"','"+str(self.data_count)+"','"+str(self.auto_upperbound)+"')"
#            cur.execute(sql_1)
#            conn.commit()
        if self.acc != "":
            sql_3="UPDATE login_system SET  predict_money='"+str(self.upperbound)+"', cost_in_one_hour='"+str(self.times_in_a_row)+"', data_count='"+str(self.data_count)+"',predict_money_custom='"+str(self.auto_upperbound)+"' WHERE account_id ='"+str(self.acc)+"'"
            cur.execute(sql_3)
            conn.commit()
        conn.close()

    
    
    def add_time_limit(self,start_time,end_time):   #增訂非正常消費時間
        self.timelimit.append([start_time,end_time])
        conn = pymysql.connect(host='203.204.10.191',port=3306,user='admin',passwd='PASSWORD',db='test',charset='utf8')
        cur = conn.cursor()
        sql_4="INSERT INTO time_limit(account_id,time_start , time_finish )VALUES('"+str(self.acc)+"','"+str(start_time)+"','"+str(end_time)+"')"
        cur.execute(sql_4)
        conn.commit()
        conn.close()
        
    def privous_consumption_time(self,consumption_time):   #增加曾經消費時間(僅特殊情況使用)
        self.privous_consumption_time.append(consumption_time)
        
    def show_time_limit(self):                      #顯示非正常消費時間
        for cnt,i in enumerate(self.timelimit):
            print("第%d筆從%d到%d"%(cnt,i[0],i[1]))
            
    def delete_time_limit(self,cnt):     #刪除非正常消費時間
        conn = pymysql.connect(host='203.204.10.191',port=3306,user='admin',passwd='PASSWORD',db='test',charset='utf8')
        cur = conn.cursor()
        if self.acc != "":
            sql_5="DELETE FROM time_limit  WHERE  account_id ='"+str(self.acc)+"' AND time_start ='"+str(self.timelimit[cnt][0])+"'AND time_finish ='"+str(self.timelimit[cnt][1])+"'"
            cur.execute(sql_5)
            conn.commit()
        conn.close()
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
        self.renew_data()
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
        conn = pymysql.connect(host='203.204.10.191',port=3306,user='admin',passwd='PASSWORD',db='test',charset='utf8')
        cur = conn.cursor()
        cnt=0
        if self.acc != "":   
            sql_6="SELECT sum(ordernumber)  FROM predict_module   WHERE cost_time>='" + self.data.consumption_time-10000 + "' "
            cur.execute(sql_6)
            fet= cur.fetchone() 
            cnt=int(fet)  
            sql_7="INSERT INTO predict_module(account_id ,money ,cost_time)VALUES('"+str(self.acc)+"','"+str(data.amount)+"','"+str(data.consumption_time)+"')"
            cur.execute(sql_7)
            conn.commit()
        conn.close()
        if cnt>self.times_in_a_row:  #若連續消費超過限制則有異常
            return True
        return False
        
#測試用信用卡消費紀錄結構 
class a:
    def __init__(self, consumption_time,amount):
        self.consumption_time=consumption_time#消費時間
        self.amount=amount#消費金額

func=analysis_system(9000,3,"LOU")
func.load_data()
#func.renew_data("LOU")
func.show_time_limit()
#func.add_time_limit(190000, 220000)
#func.delete_time_limit(1)
func.show_time_limit()
func.load_data()
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
func.load_data()
