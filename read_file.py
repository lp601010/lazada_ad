import os
import gc
import sys
import io
from pandasql import sqldf
import pandas as pd
pysqldf = lambda q: sqldf(q, globals())
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
def read_file(zd):
    for root, folds, files in os.walk(os.path.join(r"D:\lazada待处理", zd[:-3], zd)):
        for item in files:
            if "$" not in item and 'Product - Performance' in item:
                br = pd.read_excel(root+'/'+ item,header=None)
                br.drop(br.head(6).index,inplace=True)
                br.columns =['Product_Name','Product_Performance','URL','Product_Visitors','Product_Pageviews','Visitor_Value','Buyers','Order',
                            'Units_Sold','Revenue','Conversion_Rate','Revenue_per_Buyer','Wishlist_Visitor','Wishlists','Add_To_Cart_Visitors','Add_to_Cart_Units']
            elif "$" not in item and 'Product - Performance' not in item:
                ad=pd.read_excel(root+'/'+ item,header=None)
                ad.drop(ad.head(1).index, inplace=True)
                ad.columns=['Date','Campaign_Id','Campaign_Name','Promoted_Product_Name','Product_promotion_ID','Product_Name','Spend','Impressions','Clicks',
                            'CTR','CPC','Units_sold','Revenue','Return_on_Investment_(ROI)','Product_Units_sold','Product_Revenue']
                ad["Spend", "Revenue", "Product_Revenue"] = ad["Spend", "Revenue", "Product_Revenue"].apply(
                    lambda x: x.strip('PHP').strip())
    # gc.collect()
    return ad,br
if __name__ == '__main__':
    # print(sys.argv)
    print(read_file('Sweet-123-PH'))