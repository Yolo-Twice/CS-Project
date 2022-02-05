import mysql.connector as test
#enter the user and password here

sql_user="root"
sql_pass="Gurjot@2004"
con=test.connect(host="localhost",user=sql_user,passwd=sql_pass)
#creating cur, the cursor object
cur=con.cursor()
print("Working!")

#creation of database/tables
try:
    cur.execute("drop database PC_Parts")
except:
    cur.execute("create database PC_Parts")
else:
    cur.execute("create database PC_Parts")
cur.execute("use PC_Parts")

#(i) Creating the tables for Graphics Cards
#cur.execute("create table GPU(SNo INT Unique auto_increment Not null,Name varchar(80) not null, PNo char(3) Primary Key,Base_Clock INT Not Null, Boost_Clock INT,VRAM INT,Price INT,Link varchar(500)")

cur.execute("create table GPU(SNo INT Unique Not null, Name varchar(150) not null, PNo char(3) Primary Key, Base_Clock INT Not Null, Boost_Clock INT, VRAM INT,TDP INT,Price INT, Link varchar(500));")
# Inserting Records into the table

cur.execute(r"""Insert into GPU values(1,"Zotac Gaming Geforce GTX 1650 OC 4GB GDDR6","G01",1485,1695 ,4,75,26349,"https://www.amazon.in/Zotac-Gaming-Geforce-GDDR6-Graphics/dp/B086T66Z63/ref=sr_1_13?crid=3URAGQLXM9UC4&keywords=gpu&qid=1643963059&sprefix=gp%2Caps%2C527&sr=8-13"),(2,"Colorful GeForce GTX 1650 NB 4GB GDDR5 Twin Fan Compact","G02",1785,NULL,4,75,26500,"https://www.amazon.in/Colorful-GeForce-GTX-1650-NB/dp/B07T5B5PVN?ref_=Oct_d_orecs_d_1375354031&pd_rd_w=XJwZN&pf_rd_p=f1ccc94f-0f12-4efc-b35f-2af59246bc78&pf_rd_r=RRPQ1TSKTZZ3114FQT99&pd_rd_r=f1af441b-22c1-42d7-8da7-4a992cbc1a9f&pd_rd_wg=bnMWF&pd_rd_i=B07T5B5PVN"),(3,"ZOTAC Gaming GEFORCE RTX 3060 AMP White Edition 12GB GDDR6","G03",1320,1867,12,170,76500,"https://www.amazon.in/GEFORCE-RTX-3060-AMP-White/dp/B08WRV24YD?ref_=Oct_d_orecs_d_1375354031&pd_rd_w=XJwZN&pf_rd_p=f1ccc94f-0f12-4efc-b35f-2af59246bc78&pf_rd_r=RRPQ1TSKTZZ3114FQT99&pd_rd_r=f1af441b-22c1-42d7-8da7-4a992cbc1a9f&pd_rd_wg=bnMWF&pd_rd_i=B08WRV24YD"),(4,"Colorful GeForce GT 1030 4GB DDR4 VRAM Graphics Card with Single Fan ( GT1030 4G-V )","G04",1277,1468,4,75,8615,"https://www.amazon.in/Colorful-GeForce-Graphics-Single-Warranty/dp/B09N7B47Y7/ref=lp_1375354031_1_1?th=1"),(5,"ASUS TUF Gaming GeForce GTX 1660 Ti EVO 6GB GDDR6 VRAM Graphics Card 1660Ti", "G05",1500,1830,6,120,46999,"https://www.amazon.in/ASUS-GeForce%C2%AE-Graphics-Warranty-TUF-GTX1660TI-6G-EVO-GAMING/dp/B09LCWGDML/ref=zg_bs_1375354031_24/261-4542927-1267007?pd_rd_i=B09LCWGDML&psc=1"),(6,"ASUS Cerberus GeForce GTX 1050 Ti 4GB OC Edition GDDR5 Gaming Graphics Card (Cerberus-GTX1050Ti-O4G)","G06",1341,1480,4,	75,21180,"https://www.amazon.in/Cerberus-GeForce-Gaming-Graphics-Cerberus-GTX1050Ti-O4G/dp/B079JSKCW3/ref=zg_bs_1375354031_22/261-4542927-1267007?pd_rd_i=B079JSKCW3&th=1"),(7,"ASUS Dual GeForce RTX 2060 EVO 12GB GDDR6","G07",1365,1785,6,160,69999,"https://www.amazon.in/ASUS-GeForce-Performance-Warranty-DUAL-RTX2060-12G-EVO/dp/B09PJHMS5W/ref=zg_bs_1375354031_45/261-4542927-1267007?pd_rd_i=B09PJHMS5W&psc=1");""")

cur.execute("select * from GPU")
for i in cur.fetchall():
    print(i)