import paramiko
import datetime as date
import time
import openpyxl
import psycopg2
from config import *


JSONPOST = {"POST_TITLE": "TEST",
            "POST_MESSAGE": "TEST",
            "SPERM": [{'U': 'U448'}],
            "FILES": None
            }

def sshconn(host,user,passwd,port,cammand):
    cli = paramiko.SSHClient()
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = client.exec_command(cammand)
    data = stdout.read().decode()
    client.close()
    return data

def xlsx(arr,path):
    wb = openpyxl.Workbook(write_only=True)
    ws = wb.create_sheet()
    for i in arr:
        ws.append(i)
    wb.save(path)

def pog(d):
    try:
        conn = psycopg2.connect(db_name)
        cur = conn.cursor()
        cur.execute(postgres.format(d.strftime("%Y%m%d")))
        q = cur.fetchall()
        cur.close()
        return q
    except:
        print("woo")

def main():
    d1 = date.datetime.now()
    d2 = d1 - date.timedelta(days=1)
    cammand = aster.format(d2.strftime("%Y-%m-%d"),d1.strftime("%Y-%m-%d"))
    incam = [[z.strip() for z in i] for i in pog(d2)]
    out = [i.split("|") for i in sshconn(host,user,passwd,22,cammand).split("\n")]
    incam_name = "incam_{}.xlsx".format(d2.strftime("%Y-%m-%d"))
    out_name = "out_{}.xlsx".format(d2.strftime("%Y-%m-%d"))
    xlsx(incam,incam_name),xlsx(out,out_name)
    
if __name__=="__main__":
	main()
