import glob
import pandas as pd
import os


file_root = '/Users/tm/PycharmProjects/pythonProject1/data'
file = glob.glob(file_root+'/*')
# print('printed:'+file[100])
with open(file[0] , "r" , encoding='euc_jp') as f:
     html = f.read()
df = pd.read_html(html)
df


#


# _df=pd.DataFrame()
# def open(path: object) -> object:
#      with open(path,"rb",encoding='euc_jp') as f:
#           html= f.read()
#     df = pd.read_html(html)
#     print(df)
# #
# open(file[100])


#
# def open(i):
#      with open(i,"r",encoding='euc_jp') as f:
#           ok= f.read()
#
# def read(i):
#      df = pd.read_html(data)[0]
#      _df = pd.concat([df, _df])
#
# def mining():
#      for i in file:
#           open(i)
#           try:
#                read(i)
#           except ImportError:
#                os.remove(i)
#                open(i+1)
#
# if __name__=='__main__':
#      mining()
