import streamlit as st 
import pickle
import numpy as np
import pandas as pd


data=pickle.load(open("data9.pkl","rb"))
# print(data)
pipe=pickle.load(open("pipe9.pkl","rb"))
# print(pipe)

st.title("Laptop Price Predictor")


company=data["Company"].unique()
# print(company)
sec=st.selectbox("Select Company",company)

type=data["TypeName"].unique()
sety=st.selectbox("select Type",type)

gpu=data["Gpu"].unique()
seg=st.selectbox("Select GPU",gpu)

opsys=data["OpSys"].unique()
seo=st.selectbox("Select OS",opsys)

cpu=data["cpu"].unique()
secp=st.selectbox("Select CPU",cpu)

y=[2,4,6,8,12,16,24,32,64]
ram=st.selectbox("RAM in GB",y)
ser=ram

Weight=st.number_input("Weight of the Laptop(kg)")

z=["Yes","No"]
TouchScreen=st.selectbox("TouchScreen (TP=1,TN=0)",[1,0])
set=TouchScreen

w=["Yes","No"]
ips=st.selectbox("IPS(IP=1,IN=0)",[1,0])
sei=ips

screensize=st.number_input("Screen Size(inch)")

t=["1920 x 1080","1366 x 768","1600 x 900","3840 x 2160","3200 x 1800",
"2880x1800","2560 x 1600","2560x1440","2304x1440"]
resolution = st.selectbox("Screen Resolution",t)
sere=resolution

a=[0,128,256,512,1024,2048]
hdd=st.select_slider("HDD (GB)",a)
sehdd=hdd

b=[0,8,128,256,512,1024]
ssd=st.select_slider("SSD (GB)",b)
sessd=ssd


if st.button("Predict Price"):
    ppi=None

    # if TouchScreen=="Yes":
    #     TouchScreen=1
        
    # else:
    #    TouchScreen=0

    # if ips=="Yes":
    #    ips==1
    # else:
    #    ips==0

    x_r=int(sere.split("x")[0])
    y_r=int(sere.split("x")[1])
#     
    # x_r, y_r = map(int, resolution.split("x"))
    ppi=np.sqrt((x_r)**2 + (y_r)**2)/screensize
#     # ram=str(ram)


#     # Weight=str(Weight)


#     # ppi=str(ppi)

#     # hdd=str(hdd)
#     # ssd=str(ssd)
#     print(pipe)

    
    # x=np.array([[company,type,ram,gpu,opsys,Weight,TouchScreen,ips,ppi,cpu,hdd,ssd]])

    
    # pipe.Predict(x)
    quary=np.array([sec,sety,ser,seg,seo,Weight,set,sei,ppi,secp,sehdd,sessd])
    quary=quary.reshape(1,12)
    # print(x)
    
    st.title(str(int(np.exp(pipe.predict(quary)[0])))+" ₹")
 