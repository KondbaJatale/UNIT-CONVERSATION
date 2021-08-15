from tkinter import*
from functools import partial
def Click(event):
	global lenvalue
	text=event.widget.cget("text")
	print(text)
	if text=="Clear":
		lenvalue.set("")
		screen.update()
def calsum():
    mm=" milimeter  "
    cm=" centimeter  "
    m=" meter  "
    km=" kilometer  "
    ft=" feet  "
    i=" inch  "
    v1=value_inside.get() 
    v2=value_inside1.get() 
    if v1=="kilometer" and v2=="meter":
    	b=int(lenvalue.get())
    	b=b*1000
    	c=str(lenvalue.get())+km
    	d=str(b)+m
    	len=(c+' = '+d)
    
    	print("in meter",len)
    elif v1=="meter" and v2=="kilometer":
    	b=int(lenvalue.get())
    	b=b*0.001
    	c=str(lenvalue.get())+m
    	d=str(b)+km
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="meter" and v2=="meter":
    	b=int(lenvalue.get())
    	len=str(b)+m
    	print("in meter",len)
    elif v1=="kilometer" and v2=="kilometer":
    	b=int(lenvalue.get())
    	len=str(b)+km
    	print("in meter",len)
    elif v1=="centimeter" and v2=="centimeter":
    	b=int(lenvalue.get())
    	len=str(b)+cm
    	print("in meter",len)
    elif v1=="milimeter" and v2=="milimeter":
    	b=int(lenvalue.get())
    	len=str(b)+mm
    	print("in meter",len)
    elif v1=="feet" and v2=="feet":
    	b=int(lenvalue.get())
    	len=str(b)+ft
    	print("in meter",len)
    elif v1=="inch" and v2=="inch":
    	b=int(lenvalue.get())
    	len=str(b)+i
    	print("in meter",len)
    elif v1=="meter" and v2=="centimeter":
    	b=int(lenvalue.get())
    	b=b*100
    	c=str(lenvalue.get())+m
    	d=str(b)+cm
    	len=(c+' = '+d)
    
    	print("in meter",len)
    elif v1=="centimeter" and v2=="meter":
    	b=int(lenvalue.get())
    	b=b*0.01
    	c=str(lenvalue.get())+cm
    	d=str(b)+m
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="centimeter" and v2=="milimeter":
    	b=int(lenvalue.get())
    	b=b*10
    	c=str(lenvalue.get())+cm
    	d=str(b)+m
    	len=(c+' = '+d)
    	print("in meter",len)
    elif v1=="milimeter" and v2=="centimeter":
    	b=int(lenvalue.get())
    	b=b*0.1
    	c=str(lenvalue.get())+mm
    	d=str(b)+cm
    	len=(c+' = '+d)
   
    	print("in meter",len)
    elif v1=="feet" and v2=="inch":
    	b=int(lenvalue.get())
    	b=b*12
    	c=str(lenvalue.get())+ft
    	d=str(b)+i
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="inch" and v2=="feet":
    	b=int(lenvalue.get())
    	b=b*0.0833
    	c=str(lenvalue.get())+i
    	d=str(b)+ft
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="milimeter" and v2=="feet":
    	b=int(lenvalue.get())
    	b=b*0.0032
    	c=str(lenvalue.get())+mm
    	d=str(b)+ft
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="centimeter" and v2=="feet":
    	b=int(lenvalue.get())
    	b=b*0.0328
    	c=str(lenvalue.get())+cm
    	d=str(b)+ft
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="centimeter" and v2=="inch":
    	b=int(lenvalue.get())
    	b=b*0.3937
    	c=str(lenvalue.get())+cm
    	d=str(b)+i
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="centimeter" and v2=="kilometer":
    	b=int(lenvalue.get())
    	b=b*0.00001
    	c=str(lenvalue.get())+cm
    	d=str(b)+km
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="meter" and v2=="feet":
    	b=int(lenvalue.get())
    	b=b*3.2808
    	d=str(b)+ft
    	c=str(lenvalue.get())+m
    	len=(c+' = '+d)
    	print("in meter",len)
    elif v1=="meter" and v2=="inch":
    	b=int(lenvalue.get())
    	b=b*39.3700
    	d=str(b)+i
    	c=str(lenvalue.get())+m
    	len=(c+' = '+d)
    	print("in meter",len)
    elif v1=="meter" and v2=="milimeter":
    	b=int(lenvalue.get())
    	b=b*1000
    	c=str(lenvalue.get())+m
    	d=str(b)+mm
    	len=(c+' = '+d)
    	print("in meter",len)
    elif v1=="feet" and v2=="centimeter":
    	b=int(lenvalue.get())
    	b=b*30.48
    	c=str(lenvalue.get())+ft
    	d=str(b)+cm
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="feet" and v2=="kilometer":
    	b=int(lenvalue.get())
    	b=b*0.0003048
    	c=str(lenvalue.get())+ft
    	d=str(b)+km
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="feet" and v2=="meter":
    	b=int(lenvalue.get())
    	b=b*0.3048
    	c=str(lenvalue.get())+ft
    	d=str(b)+m
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="feet" and v2=="milimeter":
    	b=int(lenvalue.get())
    	b=b*304.8
    	c=str(lenvalue.get())+ft
    	d=str(b)+mm
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="inch" and v2=="centimeter":
    	b=int(lenvalue.get())
    	b=b*2.54
    	c=str(lenvalue.get())+i
    	d=str(b)+cm
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="inch" and v2=="kilometer":
    	b=int(lenvalue.get())
    	b=b*0.0000254
    	c=str(lenvalue.get())+i
    	d=str(b)+km
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="inch" and v2=="milimeter":
    	b=int(lenvalue.get())
    	b=b*25.4
    	c=str(lenvalue.get())+i
    	d=str(b)+mm
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="inch" and v2=="meter":
    	b=int(lenvalue.get())
    	b=b*0.0254
    	c=str(lenvalue.get())+i
    	d=str(b)+m
    	len=(c+' = '+d)
  
    	print("in meter",len)
    elif v1=="milimeter" and v2=="inch":
    	b=int(lenvalue.get())
    	b=b*0.0393
    	c=str(lenvalue.get())+mm
    	d=str(b)+i
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="milimeter" and v2=="meter":
    	b=int(lenvalue.get())
    	b=b*0.001
    	c=str(lenvalue.get())+mm
    	d=str(b)+m
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="milimeter" and v2=="kilometer":
    	b=int(lenvalue.get())
    	b=b*0.000001
    	c=str(lenvalue.get())+mm
    	d=str(b)+km
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="kilometer" and v2=="inch":
    	b=int(lenvalue.get())
    	b=b*39370.0787
    	c=str(lenvalue.get())+km
    	d=str(b)+i
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="kilometer" and v2=="feet":
    	b=int(lenvalue.get())
    	b=b*3280.8398
    	c=str(lenvalue.get())+km
    	d=str(b)+ft
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="kilometer" and v2=="centimeter":
    	b=int(lenvalue.get())
    	b=b*100000
    	c=str(lenvalue.get())+km
    	d=str(b)+cm
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    elif v1=="kilometer" and v2=="milimeter":
    	b=int(lenvalue.get())
    	b=b*1000000
    	c=str(lenvalue.get())+km
    	d=str(b)+mm
    	len=(c+' = '+d)
    	
    	print("in meter",len)
    else:
        len=0
    txt=len
    ans.config(text=txt,fg="white",pady=44,width=65,font="lucida 8 bold",height=0,bg="black")
		


def print_answers(): 
      print("Selected Option: {}".format(value_inside.get())) 
      return None

root=Tk()

root.title("My Unit Convertor")
root.geometry("700x740")

root.config(bg="grey")




f1=Frame(root,bg="black")
f1.pack(side=TOP,fill=X)

f2=Frame(root,bg="black",relief=SUNKEN,borderwidth=2,height=44)
f2.pack(side=TOP,fill=X)

f3=Frame(root,bg="black",relief=SUNKEN,borderwidth=2,height=44)
f3.pack(side=TOP,fill=X)

f4=Frame(root,bg="black",relief=SUNKEN,borderwidth=2,height=44)
f4.pack(side=TOP,fill=X)

f5=Frame(root,bg="black",relief=SUNKEN,borderwidth=2,height=55)
f5.pack(side=TOP,fill=X)


Label(f1,text="Unit Convertor",font=("Helvetica" ,14,"bold italic"),relief=SUNKEN,bg="black",fg="white",padx=33,pady=115).pack(side=TOP,fill=X)


lenvalue=StringVar()
e1=Entry(f1,textvariable=lenvalue,font="lucida 12 bold",relief=SUNKEN).pack(ipadx=15,ipady=19,padx=6,pady=10,fill=X)

l4=Label(f5,text="ANS:",font="Comicsansns 10 bold",padx=18,pady=40,fg="white",bg="black")
l4.pack(side=LEFT)

l2=Label(f2,text="FROM:",font="Comicsansns 10 bold",padx=3,pady=2,fg="white",bg="black")
l2.place(x=20,y=8)

l3=Label(f3,text="TO:",font="Comicsansns 10 bold",padx=3,pady=2,fg="white",bg="black").place(x=20,y=4)


l1=["centimeter","feet","kilometer","meter","inch","milimeter"]
value_inside = StringVar(f2) 
value_inside.set("Select an Option")
value_inside.set("Centimeter") 
question_menu = OptionMenu(f2, value_inside, *l1) 
question_menu.pack()	

value_inside1= StringVar(f3) 
value_inside1.set("Select an Option")
value_inside1.set("meter") 
question_menu = OptionMenu(f3, value_inside1, *l1) 
question_menu.pack()

calsum = partial(calsum)
ans= Label(f5)
ans.pack()

b1= Button(f4, text='Calculate',fg="black",bg="white",command=calsum) 
b1.place(x=500,y=0) 

b2= Button(f4, text='Clear',fg="black",bg="white", command=print_answers,width=8) 
b2.pack(side=BOTTOM,anchor="w")
b2.bind("<Button-1>",Click) 

root.mainloop()