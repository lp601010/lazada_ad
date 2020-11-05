import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from read_file import read_file
from pandasql import sqldf
import pandas as pd
import gc
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# showtext = str(ad)
# lab3.insert('insert', showtext + '\n')
p = lambda q: sqldf(q, globals())


def read_file(zd):

    global ad, br
    for root, folds, files in os.walk(os.path.join(r"D:\lazada待处理", zd[:-3], zd)):
        for item in files:
            if "$" not in item and 'Product - Performance' in item:
                br = pd.read_excel(root+'/'+ item,header=None)
                br.drop(br.head(6).index,inplace=True)
                br.columns =['Product_Name','Product_Performance','URL','Product_Visitors','Product_Pageviews','Visitor_Value','Buyers','Order',
                            'Units_Sold','Revenue','Conversion_Rate','Revenue_per_Buyer','Wishlist_Visitor','Wishlists','Add_To_Cart_Visitors','Add_to_Cart_Units']
                br.drop(['Product_Performance','URL'], axis=1,inplace=True)
                br.to_excel(root + '/br.xlsx', index=False)
            elif "$" not in item and '--' in item:
                ad=pd.read_excel(root+'/'+ item,header=None)
                ad.drop(ad.head(1).index, inplace=True)
                ad.columns=['Date','Campaign_Id','Campaign_Name','Promoted_Product_Name','Product_promotion_ID','Product_Name','Spend','Impressions','Clicks',
                            'CTR','CPC','Units_sold','Revenue','Return_on_Investment_(ROI)','Product_Units_sold','Product_Revenue']
                ad.loc[:,['Date', 'Campaign_Name','Promoted_Product_Name','Spend','Impressions','Clicks',
                            'Units_sold','Revenue','Product_Units_sold','Product_Revenue']]
                ad[["Spend", "Revenue", "Product_Revenue"]] = ad[["Spend", "Revenue", "Product_Revenue"]].applymap(
                    lambda x: str(x).replace(',','').replace('-','0').strip('PHP').strip()).astype(float)
                # ad=ad.groupby("Promoted_Product_Name").agg('sum')
                ad.to_excel(root+'/ad.xlsx', index=False)
    gc.collect()

    s=('''
        select s%, sum(Spend),sum(Impressions),sum(Clicks),sum(Units_sold),sum(Revenue),sum(Product_Units_sold),sum(Product_Revenue) from ad 
    ''')%('asda')
    # re.to_excel(root+'/re.xlsx', index=False)
    return ad,br

# def handel(zd):
#     p('''
#         select * from
#     ''')


if __name__ == '__main__':
    read_file('Sweet-123-PH')
    # win = tk.Tk()
    # win.title("lazada广告小程序")  # 添加标题
    # ttk.Label(win, text="站点名称:").grid(column=0, row=0)  # 添加一个标签，并将其列设置为0，行设置为0
    # # Address 文本框
    # address = tk.StringVar()  # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
    # address_entered = ttk.Entry(win, width=40,
    #                             textvariable=address)  # 创建一个文本框，并且将文本框中的内容绑定到上一句定义的address变量上，方便clickMe调用
    # address_entered.grid(column=1, row=0)  # 设置其在界面中出现的位置  column代表列   row 代表行
    # address_entered.focus()  # 当程序运行时,光标默认会出现在该文本框中
    # # 提示信息 Text
    # tip = tk.Label(win, background='seashell', foreground='red',
    #                text='请输入站点')
    # tip.grid(column=1, row=2)
    #
    # # 按钮绑定事件
    # action = ttk.Button(win, text="Ready? Go!",
    #                     command=lambda:read_file(address.get()) )  # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
    # action.grid(column=2, row=0)  # 设置其在界面中出现的位置  column代表列   row 代表行
    # # 输出框
    # showtext = tk.StringVar()
    # lab3 = tk.Text(win, fg='blue')
    # # lab3 = tk.Label(win,textvariable = showtxt,height=10, width=50,fg='blue',bg='yellow')
    # lab3.grid(row=3, column=0, columnspan=3)
    # # 定义关闭按钮
    # win.mainloop()  # 当调用mainloop()时,窗口才会显示出来
    # # win.protocol('WM_DELETE_WINDOW', win.destroy())
