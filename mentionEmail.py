import email.message
import pymysql
conn = pymysql.connect(host='203.204.10.191',port=3306,user='admin',passwd='PASSWORD',db='test',charset='utf8')
cur = conn.cursor()
     
def mentionEmail(person,errorList):
    error_type=["在非正常時間進行消費行為","消費大量金額","短時間進行多次消費"]
    msg_error=["消費時間異常","消費金額異常","消費次數異常"]
    alert_start=0
    
    msgTitle=""
    msgTitle+="<h3>"
    msgcnt=""
    msgcnt+="親愛的"+person+":<br>    提醒您，您的帳號"
    
    if(errorList[0]==True):
        msgTitle+=msg_error[0]+" "
        msgcnt+=error_type[0]+" "
        alert_start+=1
    if(errorList[1]==True):
        msgTitle+=msg_error[1]+" "
        msgcnt+=error_type[1]+" "
        alert_start+=1
    if(errorList[2]==True):
        msgTitle+=msg_error[2]+" "
        msgcnt+=error_type[2]+" "
        alert_start+=1
    msgTitle+="<h3>"
    if(alert_start==0):
        return
    
    sql_1="SELECT account_id,email FROM login_system WHERE account_id ='" + person + "' "
    cur.execute(sql_1)
    id_acc= cur.fetchone()
    emailAccount=id_acc[1]
    
    msg=email.message.EmailMessage()
    from_a="chenyunhao1222@gmail.com"
    to_b=emailAccount

    msg["From"]=from_a
    msg["To"]=to_b
    msg["Subject"]="消費異常通知"
    #寄送郵件主要內容
    msg.add_alternative(msgTitle+msgcnt,subtype="html")

    acc="chenyunhao1222@gmail.com"
    password="imignpkuojbipeat"#應用程式密碼
    #連線到SMTP Sevver
    import smtplib
    #可以從網路上找到主機名稱和連線埠
    server=smtplib.SMTP_SSL("smtp.gmail.com",465) #建立gmail連驗
    server.login(acc,password)
    server.send_message(msg)
    server.close() #發送完成後關閉連線

