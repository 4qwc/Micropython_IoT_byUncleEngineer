from cgitb import text
from email.utils import decode_rfc2231
from tkinter import *
from PIL import Image, ImageTk #python3 -m pip install pillow

GUI = Tk()
GUI.geometry('1000x900')
GUI.title('Dashboard ระบบ IoT ควบคุบ Smart Farm')
GUI.state('zoomed')

# Canvas กระดานวาดภาพ
canvas = Canvas(GUI,width=1500,height=900)
canvas.place(x=0,y=0)

background = ImageTk.PhotoImage(Image.open('farm.png'))
canvas.create_image(200,200,anchor=NW,image=background)

# วาดรูป
canvas.create_polygon([50,50,100,25,200,50],fill='red',outline='black')

# ใส่ข้อความ
canvas.create_text(300,300,text='ประตูกำลังเปิด',fill='green',font=('Angsana New',30,'bold'),tags='d1')

# ใส่ Line
canvas.create_line(425,320,640,455,fill='gray',width=4,tags='d1')

door_state = True # สถานะประตู
def DoorOnOff():
    global door_state # เปลี่ยนตัวแปรด้านนอกฟังก์ชั่น
    door_state = not door_state # สลับสถานะ
    canvas.delete('d1')
    if door_state == True:
        canvas.create_polygon([630,425,675,450,200,50],fill='red',outline='black')





GUI.mainloop()