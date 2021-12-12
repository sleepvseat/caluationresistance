import tkinter as tk
import tkinter.messagebox
#提示颜色选择  计算

win=tk.Tk()
win.geometry('570x500')
win.title('caluationresistance')
win.resizable(0,0)
d=3
b=0

cl=(('0','whitesmoke'),('黑色','black'),('棕色','brown'),('红色','red'),('橙色','orange'),('黄色','yellow'),('绿色','green'),('蓝色','blue'),('紫色','purple'),('灰色','gray'),('白色','white'),('金色','gold'),('银色','silver'),('无色','ghostwhite'))
for a in cl:
    tk.Label(win,text=a[0],bg=a[1],justify='left',padx=6).place(x=b,y=10,anchor='nw')
    b+=40




#误差判断公式
def errors(err):
    error0='0.5%'
    error1 = '1%'
    error2 = '5%'
    error3 = '10%'
    error4 = '20%'
    if err==5:
        return error0
    elif err == 1:
        return error1
    elif err==10:
        return error2
    elif err==11:
        return error3
    elif err==12:
        return error4
    else:
        tkinter.messagebox.showinfo('提示','电阻可能输入错误')


def caluas():
    b1=a1.get()-1
    b2 = a2.get() - 1
    b3 = a3.get() - 1
    b4 = a4.get() - 1
    b5 = a5.get() - 1
    b6 = a6.get() - 1

    if b5>=0:
    #5环或六环
        tt=(b1*100+b2*10+b3)*10**b4
        dd=errors(b5)
        if b6>=0:
            tem=('空','1000','500','250','150','空','100','50','空','10','空','空')
            gettem=tem[b6]
            tkinter.messagebox.showinfo('提示', '电阻值为%s,误差为%s，电阻温度%s' % (tt, dd,gettem))
        else:
            tkinter.messagebox.showinfo('提示','电阻值为%s,误差为%s'%(tt,dd))
    else:
    #四环
    #第三环为金色#
        if b3==10 :
            tt=(b1*10+b2)*0.1
            dd=errors(b4)
            tkinter.messagebox.showinfo('提示','电阻值为%s,误差为%s' % (tt, dd))
    #第三环为银色#
        elif b3==11:
            tt=(b1*10+b2)*0.01
            dd=errors(b4)
            tkinter.messagebox.showinfo('提示','电阻值为%s,误差为%s' % (tt, dd))
    #第三环其他色
        else:
            tt=(b1*10+b2)*10**b3
            dd=errors(b4)
            tkinter.messagebox.showinfo('提示','电阻值为%s,误差为%s' % (tt, dd))

a1=tk.IntVar()
a2=tk.IntVar()
a3=tk.IntVar()
a4=tk.IntVar()
a5=tk.IntVar()
a6=tk.IntVar()

sc_list=(('第一段颜色',a1),('第二段颜色',a2),('第三段颜色',a3),('第四段颜色',a4),('第五段颜色',a5),('第六段颜色',a6))
for c in sc_list:
    d+=60
    tk.Scale(win,label=c[0],from_=0,to=13,variable=c[1],length=550,orient='horizontal',showvalue=0,tickinterval=1,resolution=1,).place(y=d,x=0)

tk.Button(win,text='计算色环电阻阻值',width=30,height=3,font=('times',10,'bold',),command=caluas).place(x=170,y=430)

win.mainloop()