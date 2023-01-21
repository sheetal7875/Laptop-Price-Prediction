veimport streamlit as from django.conf import settings
import pickle
pipe= pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")

# brand
company= st.selectbox('Brand',df['company'].unique())

#type of laptop
type = st.selectbox('Type',df['TypeName'].unique())

#Ram
type = st.selectbox('RAM(in GB',[2,4,6,8,16,24,64])

# weight of laptop
weight = st.number_input()

# touchscreen
touchsreen = st.selectbox('Touchscreen',['No','Yes'])

# IPS 
ips = st.selectbox('IPS',['No','Yes'])


#screen size
screen_size = st.number_input('Screen Size')

#resolution
resolution = st.selectbox('Screen Resolution',['1920*1080','1366*768','1600*900','3840*2160','2560*1600','2560*1440','2304*1440'])

# cpu
cpu= st.selectbox('CPU',df['Cpu brand'].unique())

# hdd
hdd= st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd= st.selectbox('SDD(in GB)',[0,8,128,256,512,1024])


gpu= st.selectbox('GPU',df['Gpu brand'].unique())

os= st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    pass



