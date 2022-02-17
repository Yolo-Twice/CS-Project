import mysql.connector as test
#enter the user and password here

sql_user=input("Enter the Username: ")
sql_pass=input("Enter the Password: ")
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

print("Database PC_Parts Created!")
#(i) Creating the tables for Graphics Cards

cur.execute("create table GPU(SNo INT Unique Not null, Name varchar(150) not null, PNo char(3) Primary Key, Base_Clock INT Not Null, Boost_Clock INT, VRAM INT,TDP INT,Price INT, Link varchar(500));")
# Inserting Records into the table

cur.execute(r"""Insert into GPU values(1,"Zotac Gaming Geforce GTX 1650 OC 4GB GDDR6","G01",1485,1695 ,4,75,26349,"https://www.amazon.in/Zotac-Gaming-Geforce-GDDR6-Graphics/dp/B086T66Z63/ref=sr_1_13?crid=3URAGQLXM9UC4&keywords=gpu&qid=1643963059&sprefix=gp%2Caps%2C527&sr=8-13"),(2,"Colorful GeForce GTX 1650 NB 4GB GDDR5 Twin Fan Compact","G02",1785,NULL,4,75,26500,"https://www.amazon.in/Colorful-GeForce-GTX-1650-NB/dp/B07T5B5PVN?ref_=Oct_d_orecs_d_1375354031&pd_rd_w=XJwZN&pf_rd_p=f1ccc94f-0f12-4efc-b35f-2af59246bc78&pf_rd_r=RRPQ1TSKTZZ3114FQT99&pd_rd_r=f1af441b-22c1-42d7-8da7-4a992cbc1a9f&pd_rd_wg=bnMWF&pd_rd_i=B07T5B5PVN"),(3,"ZOTAC Gaming GEFORCE RTX 3060 AMP White Edition 12GB GDDR6","G03",1320,1867,12,170,76500,"https://www.amazon.in/GEFORCE-RTX-3060-AMP-White/dp/B08WRV24YD?ref_=Oct_d_orecs_d_1375354031&pd_rd_w=XJwZN&pf_rd_p=f1ccc94f-0f12-4efc-b35f-2af59246bc78&pf_rd_r=RRPQ1TSKTZZ3114FQT99&pd_rd_r=f1af441b-22c1-42d7-8da7-4a992cbc1a9f&pd_rd_wg=bnMWF&pd_rd_i=B08WRV24YD"),(4,"Colorful GeForce GT 1030 4GB DDR4 VRAM Graphics Card with Single Fan ( GT1030 4G-V )","G04",1277,1468,4,75,8615,"https://www.amazon.in/Colorful-GeForce-Graphics-Single-Warranty/dp/B09N7B47Y7/ref=lp_1375354031_1_1?th=1"),(5,"ASUS TUF Gaming GeForce GTX 1660 Ti EVO 6GB GDDR6 VRAM Graphics Card 1660Ti", "G05",1500,1830,6,120,46999,"https://www.amazon.in/ASUS-GeForce%C2%AE-Graphics-Warranty-TUF-GTX1660TI-6G-EVO-GAMING/dp/B09LCWGDML/ref=zg_bs_1375354031_24/261-4542927-1267007?pd_rd_i=B09LCWGDML&psc=1"),(6,"ASUS Cerberus GeForce GTX 1050 Ti 4GB OC Edition GDDR5 Gaming Graphics Card (Cerberus-GTX1050Ti-O4G)","G06",1341,1480,4,	75,21180,"https://www.amazon.in/Cerberus-GeForce-Gaming-Graphics-Cerberus-GTX1050Ti-O4G/dp/B079JSKCW3/ref=zg_bs_1375354031_22/261-4542927-1267007?pd_rd_i=B079JSKCW3&th=1"),(7,"ASUS Dual GeForce RTX 2060 EVO 12GB GDDR6","G07",1365,1785,6,160,69999,"https://www.amazon.in/ASUS-GeForce-Performance-Warranty-DUAL-RTX2060-12G-EVO/dp/B09PJHMS5W/ref=zg_bs_1375354031_45/261-4542927-1267007?pd_rd_i=B09PJHMS5W&psc=1");""")
print("GPU Table Created and Values inserted!")
#(ii) Creation of Motherboard table

cur.execute("Create table Motherboard(SNo int unique auto_increment Not Null, Name varchar(80) not null, PNo char(3) Primary Key, Socket varchar(8) not null, Chipset varchar(8) not null,Form_Factor varchar(15) not null, Max_Memory INT Not null, Ram_type char(4) Not null, Max_Ram_Speed INT, Ram_Slots INT, PCIE_Slots INT Not null, Price INT not null,Link varchar(500));")

# Inserting Records into the table
cur.execute(r"""Insert into motherboard values
(1,"ASUS Prime H510M-E","M01","LGA1200","H510","ATX",64,"DDR4",3200,2,1,6170,"https://www.amazon.in/ASUS-LGA1200-motherboard-Ethernet-DisplayPort/dp/B08CV3XMP6/ref=sr_1_6?crid=1HTP8F4Y6XTIN&keywords=motherboard&qid=1645097892&refinements=p_n_feature_two_browse-bin%3A27355845031&rnid=27355802031&s=computers&sprefix=motherboa%2Caps%2C645&sr=1-6&th=1"),(2,"MSI MPG Z590 Gaming Edge WiFi","M02","LGA1200","Z590","Micro ATX",128,"DDR4",5333,4,3,32026,"https://www.amazon.in/MSI-Z590-Gaming-Edge-Motherboard/dp/B08WPZTY1S/ref=sr_1_8?keywords=motherboard+lga+1200&qid=1645098508&sprefix=motherboard+lga+12%2Caps%2C413&sr=8-8"),(3,"MSI H310M PRO-VDH Plus","M03","LGA1151","H310","Micro ATX",32,"DDR4",2666,2,1,6149,"https://www.amazon.in/MSI-H310M-PRO-VDH-PLUS-Plus/dp/B07MT6BVR6/ref=sr_1_19?keywords=motherboard+lga+1155&qid=1645098849&sprefix=motherboard+lga+1151%2Caps%2C831&sr=8-19"),(4,"ASUS Prime H310M-CS","M04","LGA1151","H310","mini-ITX",32,"DDR4",2666,2,1,5489,"https://www.amazon.in/Prime-H310M-CS-Motherboard-Socket-2666MHz/dp/B07YMGXG42/ref=sr_1_17?keywords=motherboard+lga+1155&qid=1645098849&sprefix=motherboard+lga+1151%2Caps%2C831&sr=8-17"),(5,"ASUS ROG Strix Z690-F Gaming WiFi","M05","LGA1700","Z690","ATX",128,"DDR5",6400,4,2,38950,"https://www.amazon.in/ASUS-Motherboard-Backplate-heatsinks-Q-Release/dp/B09JSZZXD4/ref=sr_1_2?crid=G01RRG0KJRYL&keywords=motherboard+lga+1700&qid=1645099553&sprefix=motherboard+lga+1700%2Caps%2C568&sr=8-2"),(6,"ASUS Prime H610M-E","M06","LGA1700","H610","Micro ATX",64,"DDR4",3200,2,1,7999,"https://www.amazon.in/ASUS-D4-motherboard-Ethernet-DisplayPort/dp/B09QL6WYXM/ref=sr_1_1?crid=G01RRG0KJRYL&keywords=motherboard+lga+1700&qid=1645099553&sprefix=motherboard+lga+1700%2Caps%2C568&sr=8-1");""")

print("Motherboard Table Created and Values inserted!")
#(iii) Creation of CPU table
cur.execute(r"create table CPU(SNo INT Unique auto_increment Not null, Name varchar(80) Not null, PNo char(3) Primary Key, Socket varchar(8) not null, Base_Clock float Not null, Boost_Clock float, GPU_Requirment varchar(3), Core_Count INT Not Null, TDP INT Not null, Generation int, Max_Memory INT, Price INT Not null, Link varchar(500));")

# Inserting Records into the table
cur.execute(r"""insert into cpu values(1,"Intel Core i3 6100","C01","LGA1151",3.7,3.7,"No",2,51,6,64,9350,"https://www.amazon.in/Intel-Core-i3-6100-1151-Processor/dp/B015VPX2EO/ref=sr_1_2?crid=3FOF3SIUC7O42&keywords=intel%2Bcpu%2Blga%2B1151&qid=1645101353&sprefix=intel%2Bcpu%2Blga%2B11%2Caps%2C386&sr=8-2&th=1"),(2,"Intel Core i3 9100F","C02","LGA1151",3.6,4.2,"Yes",4,65,9,64,9924,"https://www.amazon.in/Intel-i3-9100F-Processor-Discrete-Graphics/dp/B07R7Q3JZH/ref=sr_1_7?crid=3FOF3SIUC7O42&keywords=intel%2Bcpu%2Blga%2B1151&qid=1645101353&sprefix=intel%2Bcpu%2Blga%2B11%2Caps%2C386&sr=8-7&th=1"),(3,"Intel Core i5 9400","C03","LGA1151",2.9,4.1,"No",6,65,9,128,18649,"https://www.amazon.in/Intel%C2%AE-CoreTM-I5-9400-Desktop-Processor/dp/B07MGZ9FJZ/ref=sr_1_16?crid=1PRRQNPC2X24&keywords=intel+cpu+lga+1151+i5&qid=1645101581&sprefix=intel+cpu+lga+1151+i%2Caps%2C828&sr=8-16"),(4,"Intel Core i7 10700K","C04","LGA1200",3.8,5.1,"No",8,125,10,128,38999,"https://www.amazon.in/Intel-i7-10700K-Processor-Unlocked-Avengers/dp/B08DRNK9P7/ref=sr_1_7?crid=3UH28Y5U7D9R5&keywords=intel+cpu+lga+1200&qid=1645101839&sprefix=intel+cpu+lga+1200+i5%2Caps%2C572&sr=8-7"),(5,"Intel Core i9 10850K","C05","LGA1200",3.6,5.2,"No",10,125,10,128,44999,"https://www.amazon.in/Intel-Generation-Processor-Unlocked-Warranty/dp/B08CGT7T32/ref=sr_1_2?crid=3UH28Y5U7D9R5&keywords=intel+cpu+lga+1200&qid=1645101839&sprefix=intel+cpu+lga+1200+i5%2Caps%2C572&sr=8-2"),(6,"Intel Core i3 12100F","C06","LGA1700",3.3,4.3,"Yes",4,58,12,128,11999,"https://www.amazon.in/Intel-Generation-Desktop-Processor-Warranty/dp/B09MDGKQLY/ref=sr_1_2?crid=2GHAK85O0QYUF&keywords=intel+cpu+lga+1700&qid=1645102140&sprefix=intel+cpu+lga+17%2Caps%2C640&sr=8-2"),(7,"Intel Core i5 12400F","C07","LGA1700",2.5,4.4,"Yes",6,65,12,128,19999,"https://www.amazon.in/Intel-Generation-Desktop-Processor-Warranty/dp/B09MDFH5HY/ref=sr_1_1?crid=2GHAK85O0QYUF&keywords=intel+cpu+lga+1700&qid=1645102140&sprefix=intel+cpu+lga+17%2Caps%2C640&sr=8-1"),(8,"Intel Core i7 12700","C08","LGA1700",2.1,4.9,"No",12,65,12,128,41999,"https://www.amazon.in/Intel-Generation-Processor-Warranty-Required/dp/B09MDJDSGH/ref=sr_1_3?crid=2GHAK85O0QYUF&keywords=intel+cpu+lga+1700&qid=1645102140&sprefix=intel+cpu+lga+17%2Caps%2C640&sr=8-3");""")

print("CPU Table Created and Values inserted!")

#(iv)RAM table creation 
cur.execute(r"create table RAM (SNo int Unique key,Name varchar(80) not null,PNo char(3) primary key,Size int not null,Frequency int not null, Module_amount int not null, Colour varchar(20),Price int not null,Link varchar(500));")

# Inserting Records into the table
cur.execute(r"""insert into RAM values(1,"Crucial 32GB DDR4-2666 UDIMM","R01",32,2666,1,"Green","12081","https://www.amazon.in/dp/B07ZLD38TY/?cstrackid=0debe8e5-3082-40c4-81a7-58292d79340c&tag=micronin-21&th=1"),(2,"Crucial 64GB Kit (2 x 32GB) DDR4-2666 UDIMM","R02",64,2666,2,"Green",41861,"https://www.amazon.in/dp/B07ZLDCYYS/?cstrackid=1af7275c-3a71-4ac5-af98-75908e896028&tag=micronin-21&th=1"),(3,"Crucial Ballistix RGB 3200 MHz DDR4 DRAM  8GB CL16 BL8G32C16U4RL ","R03",8,3200,1,"RGB",3903,"https://www.amazon.in/Crucial-Ballistix-Desktop-Gaming-BL2K8G36C16U4WL/dp/B08FX45VXJ?th=1"),(4,"Corsair Vengeance LPX 8GB (1x8GB) DDR4 3200MHZ C16 Desktop RAM","R04",8,3200,1,"Black",3144,"https://www.amazon.in/CORSAIR-Vengeance-1x8GB-3200MHZ-Desktop/dp/B07PNW4Q3F/ref=sr_1_5?crid=63SU9XKW2GY0&keywords=ddr4+ram&qid=1643910039&s=electronics&sprefix=ddr4+ram%2Celectronics%2C259&sr=1-5"),(5,"XPG ADATA GAMMIX D30 DDR4  3200MHz U-DIMM -AX4U320038G16A-SR30","R05",8,3200,1,"Red",3250,"https://www.amazon.in/XPG-GAMMIX-3200MHz-Desktop-AX4U320038G16A-SR30/dp/B085HSGQ1Y/ref=sr_1_7?crid=63SU9XKW2GY0&keywords=ddr4+ram&qid=1643910039&s=electronics&sprefix=ddr4+ram%2Celectronics%2C259&sr=1-7"),(6,"G.SKILL Trident Z Neo RAM - F4-3600C16D-32GTZNC","R06",16,3600,2,"RBG",18500,"https://www.amazon.in/G-Skill-F4-3600C16D-32GTZNC-Trident-DDR4-3600MHz-CL16-19-19-39/dp/B07VRLBXLR/ref=sr_1_2?crid=2SFXQUKIU0262&keywords=ddr4%2Bgaming%2Bram&qid=1643910418&s=electronics&sprefix=ddr4%2Bgaming%2Bram%2Celectronics%2C240&sr=1-2&th=1"),(7,"TEAMGROUP T-Force Xtreem ARGB CL18 PC4-32000 ARGB Dual Channel SDRAM","R07",8,4000,2,"Black",15999,"https://www.amazon.in/TEAMGROUP-T-Force-4000MHz-PC4-32000-Channel/dp/B082HCM81P/ref=sr_1_16?crid=2SFXQUKIU0262&keywords=ddr4%2Bgaming%2Bram&qid=1643910418&s=electronics&sprefix=ddr4%2Bgaming%2Bram%2Celectronics%2C240&sr=1-16&th=1"),(8,"Corsair Vengeance DDR5 DRAM 4800MHz C40 Memory Kit","R08",16,4800,2,"Black",28999,"https://www.amazon.in/Corsair-Vengeance-2x16GB-4800MHz-Memory/dp/B09MTS5YH1/ref=sr_1_1?crid=RVBZ92WFPYEX&keywords=ddr5+ram&qid=1643910752&s=electronics&sprefix=ddr5+ram%2Celectronics%2C234&sr=1-1"),(9,"Crucial RAM 4GB DDR4 2666 MHz CL19 Desktop Memory CT4G4DFS8266","R09",4,2666,1,"Green",1890,"https://www.amazon.in/Crucial-4gb-ddr4-2666-Desktop/dp/B07GMRJTS9/ref=sr_1_2?crid=2B213B098EPQT&keywords=ddr4%2Bram&qid=1643911043&s=electronics&sprefix=ddr4%2Bram%2Celectronics%2C234&sr=1-2&th=1"),(10,"Crucial RAM 8GB DDR4 2666 MHz CL19 Laptop Memory CT8G4SFRA266","R10",8,2666,1,"Green",2899,"https://www.amazon.in/Crucial-DDR4-Laptop-Memory-CT8G4SFRA266/dp/B08C56KXQJ/ref=sr_1_3?crid=2B213B098EPQT&keywords=ddr4+ram&qid=1643911043&s=electronics&sprefix=ddr4+ram%2Celectronics%2C234&sr=1-3");""")

print("RAM Table Created and Values inserted!")

#(v)Storage table creation 

cur.execute(r"create table Storage(SNo int unique key auto_increment not null,Name varchar(200) Not null,PNo char(3) primary key,Size int not null,Type char(3) Not null,Transfer_Speed int not null,Price int not null,Link varchar(1000));")

cur.execute(r"""insert into Storage Values(1,"Seagate Firecuda 520 SSD 2TB-Internal M.2 (ZP2000GM3A002)","S01",2000,"SSD",5000,29499,"https://www.amazon.in/Seagate-FireCuda-Performance-Internal-ZP2000GM3A002/dp/B07ZZLDTP6/ref=sr_1_3?keywords=gaming%2Bssd%2Bfor%2Bpc&qid=1643959878&sprefix=Gaming%2BSSD%2Caps%2C258&sr=8-3&th=1"),(2,"Western Digital SN850 500GB, PCIe Gen 4 SSD 7000MB/s R W WD for Gaming & Content Creators","S02",500,"SSD",7000,8832,"https://www.amazon.in/dp/B08KFN1KT1?tag=georiot-in-default-21&th=1&ascsubtag=pcg-in-5367911523935961000-21&geniuslink=true"),(3,"Samsung 970 EVO Plus Series - 500GB PCIe NVMe - M.2 Internal SSD","S03",500,"SSD",3200,12028,"https://www.amazon.in/dp/B07M7Q21N7?tag=georiot-in-default-21&th=1&psc=1&ascsubtag=pcg-in-1337186895929311700-21&geniuslink=true"),(4,"Seagate Barracuda Internal Hard Drive HDD - 3.5 Inch SATA 6 Gb/s 5400 RPM 256 MB Cache for Computer Desktop PC (ST2000DM005)","S04",2000,"HDD",6000,4299," https://www.amazon.in/Seagate-Barracuda-2TB-HDD-ST2000DM005/dp/B07GWRP5LN/ref=sr_1_1_sspa?crid=1G9D7XC0S4N7N&keywords=Seagate%2BBarraCuda&qid=1643960322&s=electronics&sprefix=seagate%2Bbarracuda%2Celectronics%2C195&sr=1-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE1T0tZMFpNSzVNRkgmZW5jcnlwdGVkSWQ9QTA0Mjk1NzExU0oxTTgxVTYwNTlDJmVuY3J5cHRlZEFkSWQ9QTA2MTk5ODYzNFpUMUJPT09STjFQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1 "),(5,"Seagate FireCuda 530 1TB Internal Solid State Drive - M.2 PCIe Gen4 x4 NVMe 1.4 (ZP1000GM3A013), Orange","S05",1000,"SSD",7300,16999,"https://www.amazon.in/Seagate-FireCuda-Performance-Internal-ZP2000GM3A002/dp/B0971FN5MV/ref=sr_1_3?keywords=gaming%2Bssd%2Bfor%2Bpc&qid=1643959878&sprefix=Gaming%2BSSD%2Caps%2C258&sr=8-3&th=1 "),(6,"Seagate FireCuda 530 500GB Internal Solid State Drive - M.2 PCIe Gen4 ×4 NVMe 1.4 (ZP500GM3A023), Black","S06",500,"SSD",7300,12499," https://www.amazon.in/Seagate-FireCuda-Performance-Internal-ZP2000GM3A002/dp/B0977KZN4L/ref=sr_1_3?keywords=gaming%2Bssd%2Bfor%2Bpc&qid=1643959878&sprefix=Gaming%2BSSD%2Caps%2C258&sr=8-3&th=1");""")
print("Storage Table Created and Values inserted!")

print("Program Finished")