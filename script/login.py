import random
import pymysql
import base64
conn = pymysql.connect(host='203.204.10.191',port=3306,user='admin',passwd='PASSWORD',db='test',charset='utf8')
cur = conn.cursor()
def mymenu():
    while True:
        myindex() #呼叫起始介面
        num = int(input("請輸入您要執行的動作"))
        print()
        if num == 1 :
            login()  
        elif num == 2 :
            Insert()
            print("登入功能")
        elif num == 3 :
            Alter()
        elif num == 4 :
            break 
def myindex():
    print("登入系統")
    print("1.登入")
    print("2.註冊帳號")
    print("3.更改密碼")
    print("4.結束程式")
def generate_verification_code(len=6):
    code_list = [] 
    for i in range(10): 
        code_list.append(str(i))
    for i in range(65, 91): 
        code_list.append(chr(i))
    for i in range(97, 123): 
        code_list.append(chr(i))
    myslice = random.sample(code_list, len) 
    verification_code = ''.join(myslice) 
    return verification_code        
def login():
    while True:
        code=generate_verification_code()
        acc=input("請輸入帳號")
        if acc == "":break   
        sql_1="SELECT account_id,account_password FROM login_system WHERE account_id ='" + acc + "' "
        cur.execute(sql_1)
        id_acc= cur.fetchone()   
        if (id_acc==None):
            print("{}帳號不存在".format(acc))
            continue
        mypwd=id_acc[1]
        pwd=input("請輸入密碼")
        if pwd=="": break  
        if (mypwd != pwd):
            print("密碼錯誤")
        else:
            print("{}".format(code))
            code_1=input("請輸入驗證碼")
            if (code_1 == code):
                print("登入成功")
                break
            else:
                print("驗證碼輸入錯誤")
                continue

def Insert():
    while True:
        code=generate_verification_code()
        acc=input("請輸入帳號")
        if acc == "" :
            print("帳號不能為空")
            continue
        sql = "SELECT * FROM login_system WHERE account_id = '"+ acc + "'"
        cur.execute(sql)
        data = cur.fetchone()
        if not data == None:
            print("{}帳號已存在".format(acc))
            continue
        pwd = input("請輸入密碼")
        print("{}".format(code))
        code_1=input("請輸入驗證碼")
        if(code_1 == code):
            sql_insert = "INSERT INTO login_system(account_id,account_password)VALUES('"+acc+"','"+pwd+"')" 
            cur.execute(sql_insert)
            conn.commit() 
            print("{}已註冊成功".format(acc))
            break
        else:
            print("驗證碼輸入錯誤")
            continue
def Alter():
    while True:
        code=generate_verification_code()
        acc=input("請輸入帳號")
        if acc == "":break   
        sql_1="SELECT account_id,account_password FROM login_system WHERE account_id ='" + acc + "' "
        cur.execute(sql_1)
        id_acc= cur.fetchone()   
        if (id_acc==None):
            print("{}帳號不存在".format(acc))
            continue
        mypwd=id_acc[1]
        pwd=input("請輸入原密碼")
        if pwd=="": break  
        print("{}".format(code))
        code_1=input("請輸入驗證碼")
        if(code_1 == code):
            if (mypwd != pwd):
                print("密碼錯誤")
            else:
                while True:
                    newpassword=input("請輸入想要更改之密碼")
                    sql_3="SET SQL_SAFE_UPDATES=0"
                    cur.execute(sql_3)
                    passwordcheck=input("新密碼確認")
                    if(passwordcheck==newpassword):
                        print("更改成功，請使用新密碼登入")
                        sql_2="update id set password='"+ newpassword +"'where name='"+acc+"'"
                        cur.execute(sql_2)
                        conn.commit()
                        break
                    else:
                        print("密碼有誤")
                        continue
                        break
                break
        else:
            print("驗證碼輸入錯誤") 

mymenu()
