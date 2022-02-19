import mysql.connector as run
from tkinter import *
import pickle

def table_gpu(data): #this is used to create the GPU table in tkinter
    fetched_data=data
    global window
    try:
        window.destroy()
        window=Tk()
    except:
        window=Tk()
    Label(window,fg="blue",text="S. No.",relief='ridge',borderwidth=5,font="none 12 bold").grid(row=0,column=0)
    Label(window,fg="blue",text="Name",relief='ridge',borderwidth=5,width=60,font="none 12 bold").grid(row=0,column=1)
    Label(window,fg="blue",text="Part",relief='ridge',borderwidth=5,width=9,font="none 12 bold").grid(row=0,column=2)
    Label(window,fg="blue",text="Base Clock",relief='ridge',borderwidth=5,width=9,font="none 12 bold").grid(row=0,column=3)
    Label(window,fg="blue",text="Boost Clock",relief='ridge',borderwidth=5,width=9,font="none 12 bold").grid(row=0,column=4)
    Label(window,fg="blue",text="VRAM",relief='ridge',borderwidth=5,width=9,font="none 12 bold").grid(row=0,column=5)
    Label(window,fg="blue",text="Price",relief='ridge',borderwidth=5,width=9,font="none 12 bold").grid(row=0,column=6)
    x=1
    for i in fetched_data:
        for j in range(len(i)):
            if j==1:
                e= Label(window,fg="black",text=i[j],width=86,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            elif j==0:
                e= Label(window,fg="black",text=i[j],width=7,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            e= Label(window,fg="black",text=i[j],width=14,relief='ridge',borderwidth=2)
            e.grid(row=x,column=j,sticky=W)
        x=x+1
    but1= Button(window,text="Exit",command=exit_window,font="15")
    but1.grid(sticky=W)

def table_cpu(data): #this is used to create the CPU table in tkinter
    fetched_data=data
    global window
    try:
        window.destroy()
        window=Tk()
    except:
        window=Tk()
    Label(window,fg="blue",text="S. No.",relief='ridge',borderwidth=5,font="none 12 bold").grid(row=0,column=0)
    Label(window,fg="blue",text="Name",relief='ridge',borderwidth=5,width=13,font="none 12 bold").grid(row=0,column=1)
    Label(window,fg="blue",text="Part",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=2)
    Label(window,fg="blue",text="Socket",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=3)
    Label(window,fg="blue",text="Base Clock",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=4)
    Label(window,fg="blue",text="Boost Clock",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=5)
    Label(window,fg="blue",text="GPU Needed?",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=6)
    Label(window,fg="blue",text="Cores",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=7)
    Label(window,fg="blue",text="TDP",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=8)
    Label(window,fg="blue",text="Generation",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=9)
    Label(window,fg="blue",text="Max Ram",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=10)
    Label(window,fg="blue",text="Price",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=11)
    x=1
    for i in fetched_data:
        for j in range(len(i)):
            if j==1:
                e= Label(window,fg="black",text=i[j],width=20,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            elif j==0:
                e= Label(window,fg="black",text=i[j],width=7,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            e= Label(window,fg="black",text=i[j],width=16,relief='ridge',borderwidth=2)
            e.grid(row=x,column=j,sticky=W)
        x=x+1
    but1= Button(window,text="Exit",command=exit_window,font="15")
    but1.grid(sticky=W)

def table_mobo(data): #this is used to create the Motherboard table in tkinter
    fetched_data=data
    global window
    try:
        window.destroy()
        window=Tk()
    except:
        window=Tk()
    Label(window,fg="blue",text="S. No.",relief='ridge',borderwidth=5,font="none 12 bold").grid(row=0,column=0)
    Label(window,fg="blue",text="Name",relief='ridge',borderwidth=5,width=20,font="none 12 bold").grid(row=0,column=1)
    Label(window,fg="blue",text="Part",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=2)
    Label(window,fg="blue",text="Socket",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=3)
    Label(window,fg="blue",text="Chipset",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=4)
    Label(window,fg="blue",text="Form_Factor",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=5)
    Label(window,fg="blue",text="Max Memory",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=6)
    Label(window,fg="blue",text="Ram type",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=7)
    Label(window,fg="blue",text="Max Ram Speed",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=8)
    Label(window,fg="blue",text="Ram Slots",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=9)
    Label(window,fg="blue",text="PCIE Slots",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=10)
    Label(window,fg="blue",text="Price",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=11)
    x=1
    for i in fetched_data:
        for j in range(len(i)):
            if j==1:
                e= Label(window,fg="black",text=i[j],width=30,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            elif j==0:
                e= Label(window,fg="black",text=i[j],width=7,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            e= Label(window,fg="black",text=i[j],width=16,relief='ridge',borderwidth=2)
            e.grid(row=x,column=j,sticky=W)
        x=x+1
    but1= Button(window,text="Exit",command=exit_window,font="15")
    but1.grid(sticky=W)

def table_ram(data): #this is used to create the Motherboard table in tkinter
    fetched_data=data
    global window
    try:
        window.destroy()
        window=Tk()
    except:
        window=Tk()
    Label(window,fg="blue",text="S. No.",relief='ridge',borderwidth=5,font="none 12 bold").grid(row=0,column=0)
    Label(window,fg="blue",text="Name",relief='ridge',borderwidth=5,width=42,font="none 12 bold").grid(row=0,column=1)
    Label(window,fg="blue",text="Part",relief='ridge',borderwidth=5,width=15,font="none 12 bold").grid(row=0,column=2)
    Label(window,fg="blue",text="Size",relief='ridge',borderwidth=5,width=15,font="none 12 bold").grid(row=0,column=3)
    Label(window,fg="blue",text="Speed/Frequency",relief='ridge',borderwidth=5,width=15,font="none 12 bold").grid(row=0,column=4)
    Label(window,fg="blue",text="No. of Ram Sticks",relief='ridge',borderwidth=5,width=15,font="none 12 bold").grid(row=0,column=5)
    Label(window,fg="blue",text="Ram Type",relief='ridge',borderwidth=5,width=15,font="none 12 bold").grid(row=0,column=6)
    Label(window,fg="blue",text="Price",relief='ridge',borderwidth=5,width=15,font="none 12 bold").grid(row=0,column=7)
    x=1
    for i in fetched_data:
        for j in range(len(i)):
            if j==1:
                e= Label(window,fg="black",text=i[j],width=60,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            elif j==0:
                e= Label(window,fg="black",text=i[j],width=7,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            e= Label(window,fg="black",text=i[j],width=22,relief='ridge',borderwidth=2)
            e.grid(row=x,column=j,sticky=W)
        x=x+1
    but1= Button(window,text="Exit",command=exit_window,font="15")
    but1.grid(sticky=W)

def table_storage(data): #this is used to create the Storage table in tkinter
    fetched_data=data
    global window
    try:
        window.destroy()
        window=Tk()
    except:
        window=Tk()
    Label(window,fg="blue",text="S. No.",relief='ridge',borderwidth=5,font="none 12 bold").grid(row=0,column=0)
    Label(window,fg="blue",text="Name",relief='ridge',borderwidth=5,width=87,font="none 12 bold").grid(row=0,column=1)
    Label(window,fg="blue",text="Part",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=2)
    Label(window,fg="blue",text="Size",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=3)
    Label(window,fg="blue",text="Type",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=4)
    Label(window,fg="blue",text="Transfer Speed",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=5)
    Label(window,fg="blue",text="Price",relief='ridge',borderwidth=5,width=11,font="none 12 bold").grid(row=0,column=6)
    x=1
    for i in fetched_data:
        for j in range(len(i)):
            if j==1:
                e= Label(window,fg="black",text=i[j],width=126,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            elif j==0:
                e= Label(window,fg="black",text=i[j],width=7,relief='ridge',borderwidth=2)
                e.grid(row=x,column=j,sticky=W)
                continue
            e= Label(window,fg="black",text=i[j],width=16,relief='ridge',borderwidth=2)
            e.grid(row=x,column=j,sticky=W)
        x=x+1
    but1= Button(window,text="Exit",command=exit_window,font="15")
    but1.grid(sticky=W)



def exit_window(): #used by tkinter
    window.destroy()

con=run.connect(host="localhost",user="root",passwd="Gurjot@2004",database="pc_parts")

cur=con.cursor(buffered=True)
additional=""
where_command=""

################################MAIN LOOP##################################

while True:
    print("1.Display Tables\n2.Load/Save Builds\n3.See the selected components")
    uc=int(input(">"))

    if uc==1:
        print("Which table?\n1.CPU\n2.Motherboard\n3.RAM\n4.GPU\n5.Storage")
        uc=int(input(">"))
        if uc==4:            
            table_name="GPU"
            column_names="Sno,Name,pno,Base_Clock,Boost_Clock,vram,price"
            while True:
                print("\n1.Display GPU Table\n2.Filter\n3.Sort\n4.Select GPU\n5.Go Back")
                uc=int(input(">"))
                if uc==1:
                    cur.execute(f"select {column_names} from {table_name} {where_command} {additional};")
                    data=cur.fetchall()
                    table_gpu(data)
                    window.mainloop()
                elif uc==3:
                    print("1.by Price\n2.by Clockspeed\n3.by VRAM\n4.Clear")
                    uc=int(input(">"))
                    if uc==1:
                        additional="order by price"
                        continue
                    elif uc==2:
                        additional="order by boost_clock,base_clock"
                        continue
                    elif uc==3:
                        additional="order by vram"
                        continue
                    else:
                        additional=""
                        continue
                elif uc==2:
                    print("1.by Vram amount\n2.by Clockspeed\n3.by Price\n4.Clear")
                    uc=int(input(">"))
                    if uc==1:
                        col1="vram"
                    elif uc==2:
                        col1="base_clock"
                    elif uc==3:
                        col1="price"
                    elif uc==4:
                        where_command=""
                        continue
                    print("1.Less than\n2.Greater than")
                    uc=int(input(">")) 
                    if uc==1:
                        filt1=int(input("less than: "))
                        where_command=f"where {col1}<{filt1}"   
                    elif uc==2:
                        filt1=int(input("greater than: "))
                        where_command=f"where {col1}>{filt1}"
                elif uc==5:
                    table_name=""
                    column_names=""
                    additional=""
                    where_command=""
                    break
                elif uc==4:
                    GPU_selection=input("Enter the Part no.:")
                    cur.execute(f'select * from gpu where pno="{GPU_selection}"')
                    gpu_data=cur.fetchall()[0]
                    print(gpu_data[1],"Selected!")
                    
        elif uc==1:
            table_name="CPU"
            column_names="SNo,Name,Pno,Socket,Base_Clock,Boost_clock,GPU_Requirment,core_count,TDP,Generation,max_memory,price"
            while True:
                print("\n1.Display CPU Table\n2.Filter\n3.Sort\n4.Select CPU\n5.Go Back")
                uc=int(input(">"))
                if uc==1:
                    cur.execute(f"select {column_names} from {table_name} {where_command} {additional};")
                    data=cur.fetchall()
                    table_cpu(data)
                elif uc==2:
                    print("1.by Power Consumed per hour(TDP)\n2.by Clockspeed\n3.by Price\n4.by Socket\n5.Clear")
                    uc=int(input(">"))
                    if uc==1:
                        col1="tdp"
                    elif uc==2:
                        col1="base_clock"
                    elif uc==3:
                        col1="price"
                    elif uc==4:
                        print("Which Socket?\n1.LGA1151\n2.LGA1200\n3.LGA1700")
                        uc=int(input(">"))
                        if uc==1:
                            where_command='where socket="LGA1151"'
                        elif uc==2:
                            where_command='where socket="LGA1200"'
                        elif uc==3:
                            where_command='where socket="LGA1700"'
                        continue
                    elif uc==5:
                        where_command=""
                        continue
                    print("1.Less than\n2.Greater than")
                    uc=int(input(">")) 
                    if uc==1:
                        filt1=int(input("less than: "))
                        where_command=f"where {col1}<{filt1}"   
                    elif uc==2:
                        filt1=int(input("greater than: "))
                        where_command=f"where {col1}>{filt1}"
                elif uc==3:
                    print("1.by Price\n2.by Clockspeed\n3.by TDP\n4.Clear")
                    uc=int(input(">"))
                    if uc==1:
                        additional="order by price"
                        continue
                    elif uc==2:
                        additional="order by boost_clock,base_clock"
                        continue
                    elif uc==3:
                        additional="order by TDP"
                        continue
                    else:
                        additional=""
                        continue
                elif uc==5:
                    table_name=""
                    column_names=""
                    additional=""
                    where_command=""
                    break
                elif uc==4:
                    CPU_selection=input("Enter the Part no.:")
                    cur.execute(f'select * from cpu where pno="{CPU_selection}"')
                    cpu_data=cur.fetchall()[0]
                    Cpu_socket=cpu_data[3]
                    print(cpu_data[1],"Selected!")
                    print("Socket-",Cpu_socket)
                    
        elif uc==2:
            table_name="motherboard"
            column_names="Sno,Name,pno,Socket,Chipset,Form_Factor,Max_Memory,Ram_type,Max_Ram_Speed,Ram_Slots,PCIE_Slots,Price"     
            while True:
                print("\n1.Display all motherboards\n2.Display Compatible motherboards\n3.Select Motherboard\n4.Go Back")
                #Sort and Filter not included for motherboard because too few records for compatible motherboards
                uc=int(input(">"))
                if uc==1:
                    cur.execute(f'select {column_names} from {table_name} {where_command} {additional};')
                    data=cur.fetchall()
                    table_mobo(data)
                elif uc==2:
                    cur.execute(f'select {column_names} from {table_name} where socket="{Cpu_socket}" {where_command} {additional};')
                    data=cur.fetchall()
                    table_mobo(data)
                elif uc==3:
                    mobo_selection=input("Enter the Part no.: ")
                    cur.execute(f'select * from motherboard where pno="{mobo_selection}"')  
                    mobo_data=cur.fetchall()[0]
                    print(mobo_data[1],"Selected!")
                    mobo_ram_type=mobo_data[7]
                    if mobo_data[3]!=cpu_data[3]:
                        print("\nWARNING! CPU AND MOTHERBOARD NOT COMPATIBLE\n")
                    else:
                        print("\nMotherboard compatible with CPU!\n")
                elif uc==4:
                    table_name=""
                    column_names=""
                    additional=""
                    where_command=""
                    break
                    
        elif uc==3:
            table_name="ram"
            column_names="Sno,Name,pno,size,frequency,module_amount,ram_type,Price"
            while True:
                print("1.Display compatible RAM modules\n2.Display all the RAM modules\n3.Filter\n4.Sort\n5.Select Ram Modules\n6.Go Back")
                uc=int(input(">"))
                if uc==1:
                    cur.execute(f'select {column_names} from {table_name} where ram_type="{mobo_ram_type}";')
                    data=cur.fetchall()
                    table_ram(data)
                elif uc==2:
                    cur.execute(f"select {column_names} from {table_name} {where_command} {additional};")
                    data=cur.fetchall()
                    table_ram(data)
                elif uc==3:
                    print("1.by Ram Size\n2.by Speed\n3.by Price\n4.Clear")
                    uc=int(input(">"))
                    if uc==1:
                        col1="size"
                    elif uc==2:
                        col1="frequency"
                    elif uc==3:
                        col1="price"
                    elif uc==4:
                        where_command=""
                        continue
                    print("1.Less than\n2.Greater than")
                    uc=int(input(">")) 
                    if uc==1:
                        filt1=int(input("less than: "))
                        where_command=f"where {col1}<{filt1}"   
                    elif uc==2:
                        filt1=int(input("greater than: "))
                        where_command=f"where {col1}>{filt1}"
                elif uc==4:
                    print("1.by Price\n2.by Speed\n3.by Size\n4.Clear")
                    uc=int(input(">"))
                    if uc==1:
                        additional="order by price"
                        continue
                    elif uc==2:
                        additional="order by frequency"
                        continue
                    elif uc==3:
                        additional="order by size"
                        continue
                    else:
                        additional=""
                        continue
                elif uc==5:
                    Slots_Used=int(input(f"Your selected motherboard has {mobo_data[9]} RAM Slots.\nHow Many would you like to use: "))
                    Ram_data=dict()
                    i=0
                    while i<Slots_Used:
                        RAM_selection=input("Enter the part no.: ")
                        cur.execute(f'select * from ram where pno="{RAM_selection}";')
                        Ram_data_single=cur.fetchall()[0]
                        if Ram_data_single[5]==2:
                            i+=2
                            Ram_data[i]=Ram_data_single
                            Ram_data[i+1]=Ram_data_single
                            print(f"For Slot {i-1} and {i} {Ram_data_single[1]}Selected!")
                            continue
                        Ram_data[i]=Ram_data_single
                        print(f"For Slot {i+1} {Ram_data_single[1]}Selected!")
                        i+=1
                        total_ram_size=0
                        for i in range(len(Ram_data)):
                            total_ram_size+=Ram_data[i][3]
                        print("Total Ram size is",total_ram_size)
                        if total_ram_size>mobo_data[6] or total_ram_size>cpu_data[10]:
                            print("Warning TOTAL RAM SIZE IS OVER THE LIMIT")
                elif uc==6:
                    table_name=""
                    column_names=""
                    additional=""
                    where_command=""
                    break
        elif uc==5:
            column_names="sno,name,pno,size,type,transfer_speed,price"
            table_name="storage"
            while True:
                print("1.Display Storage Devices\n2.Filter\n3.Sort\n4.Select Storage Device\n5.Go Back")
                uc=int(input(">"))
                if uc==1:
                    cur.execute(f"select {column_names} from {table_name} {where_command} {additional};")
                    data=cur.fetchall()
                    table_storage(data)
                elif uc==2:
                    print("1.by Size\n2.by Speed\n3.by Price\n4.by type\n5.Clear")
                    uc=int(input(">"))
                    if uc==1:
                        col1="size"
                    elif uc==2:
                        col1="transfer_speed"
                    elif uc==3:
                        col1="price"
                    elif uc==4:
                        print("1.SSD\n2.HDD")
                        uc=int(input(">"))
                        if uc==1:
                            where_command="where type=SSD"
                        elif uc==2:
                            where_command="where type=HDD"
                        continue
                    elif uc==5:
                        where_command=""
                        continue
                    print("1.Less than\n2.Greater than")
                    uc=int(input(">")) 
                    if uc==1:
                        filt1=int(input("less than: "))
                        where_command=f"where {col1}<{filt1}"   
                    elif uc==2:
                        filt1=int(input("greater than: "))
                        where_command=f"where {col1}>{filt1}"
                elif uc==3:
                    print("1.by Price\n2.by Speed\n3.by Size\n4.Clear")
                    uc=int(input(">"))
                    if uc==1:
                        additional="order by price"
                        continue
                    elif uc==2:
                        additional="order by transfer_speed"
                        continue
                    elif uc==3:
                        additional="order by size"
                        continue
                    else:
                        additional=""
                        continue
                elif uc==4:
                    storage_selection=input("Enter the Part no.:")
                    cur.execute(f'select * from storage where pno="{storage_selection}"')
                    storage_data=cur.fetchall()[0]
                    print(storage_data[1],"Selected!")
                elif uc==5:
                    table_name=""
                    column_names=""
                    additional=""
                    where_command=""
                    break
    elif uc==2:
        while True:
            print("1.Load\n2.Save\n3.Go Back")
            uc=int(input(">"))
            if uc==1:
                print("1.Pre-selected Gaming Build\n2.Your own\n3.Go Back")
                uc=int(input(">"))
                if uc==1:
                    file=open("premade Gaming Build.bin","rb")
                    cpu_data=pickle.load(file)
                    mobo_data=pickle.load(file)
                    Ram_data=pickle.load(file)
                    gpu_data=pickle.load(file)
                    storage_data=pickle.load(file)
                    file.close()
                elif uc==2:
                    filename=input("Enter the Name of the file: ")
                    file=open(filename,"rb")
                    cpu_data=pickle.load(file)
                    mobo_data=pickle.load(file)
                    Ram_data=pickle.load(file)
                    gpu_data=pickle.load(file)
                    storage_data=pickle.load(file)
                    file.close()
                elif uc==3:
                    continue
            elif uc==2:
                filename=input("Enter the Name of the file: ")
                file=open(filename,"wb")
                pickle.dump(cpu_data,file)
                pickle.dump(mobo_data,file)
                pickle.dump(Ram_data,file)
                pickle.dump(gpu_data,file)
                pickle.dump(storage_data,file)
                file.close()
            elif uc==3:
                break
    elif uc==3:
        print("CPU: ",cpu_data[1])
        print("Motherboard: ",mobo_data[1])
        print("GPU: ",gpu_data[1])
        print("Storage: ",storage_data[1])

    else:
        break