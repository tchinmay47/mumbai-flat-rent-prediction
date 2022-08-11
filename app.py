import streamlit as st
import numpy as np
import pickle

model_0=pickle.load(open('model_0.pkl','rb'))
model_1=pickle.load(open('model_1.pkl','rb'))
model_2=pickle.load(open('model_2.pkl','rb'))
model_3=pickle.load(open('model_3.pkl','rb'))
model_4=pickle.load(open('model_4.pkl','rb'))
model_5=pickle.load(open('model_5.pkl','rb'))
model_6=pickle.load(open('model_6.pkl','rb'))
model_7=pickle.load(open('model_7.pkl','rb'))
model_8=pickle.load(open('model_8.pkl','rb'))
model_9=pickle.load(open('model_9.pkl','rb'))

st.title("Mumbai Flat Rent Prediction Model")
area=st.slider("Area in Sq.ft", min_value=100, max_value=4000, value=None, step=1)
bathroom_num=st.slider("Number of Bathrooms", min_value=0, max_value=10, value=None, step=1)
bedroom_num=st.slider("Number of Bedrooms", min_value=0, max_value=10, value=None, step=1)

locality = st.selectbox('Location',
('4 Bunglows','Aarey Milk Colony','Agripada','Akurli Nagar','Altamount Road','Andheri East','Andheri West','Antop Hill','Asha Nagar','Ashok Nagar Western Mumbai','Azad Nagar','Bandra','Bandra Band Stand','Bandra East','Bandra Kurla Complex','Bandra Reclamation','Bandra West','Bangur Nagar','BEST Housing Colony','Best Nagar - Goregaon West','Beverly Park','Bhakti Park','Bhandup','Bhandup East','Bhandup Industrial Estate','Bhandup West','Bhavani Nagar','Bhayandar East','Bhayandar West','Bhoiwada','Bimbisar Nagar','Borivali East','Borivali West','Breach Candy','Byculla','CAMA Industrial Estate','Carter Road','Central Area','Central Avenue Road','Chakala','Chakala MIDC','Chandivali','Charkop','Charkop Sector 2','Charkop Sector 8','Charni Road','Chembur','Chembur Colony','Chiku Wadi','Chinchpokli','Chunabhatti','Church Gate','Colaba','Collector Colony','Cuffe Parade','D.N. Nagar','Dadar','Dadar East','Dadar TT Circle','Dadar West','Dahisar East','Dahisar West','Datta Pada','Deonar','Deonar Farm Road','Devi Pada','Dhanukar Wadi','Dindoshi','Ekta Nagar','Ekta Nagar Charkop','Elphinstone','Everard Nagar','Evershine Nagar','Film City','Film City Road','Four Bungalows','Gandhi Nagar','Ghatkopar','Ghatkopar East','Ghatkopar West','Ghatla','Gokul Dham','Gokuldham','Gopal Nagar','Gorai 2','Goregaon East','Goregaon West','Govandi','Govandi Station Road','Grant Road','Gulmohar Road','Haji Ali','Hatkesh Udyog','Hindu Colony','IC Colony','IIT Colony','Ishwar Nagar','Jacob Circle','Jankalyan Nagar','Jayprakash Nagar','JB Nagar','Jogeshwari East','Jogeshwari West','Juhu','Juhu Beach Area','Juhu Tara','Juhu Tara Road','Juhu Versova Link','Juhu Versova Link Road','Juhu Vile Parle Development Scheme','JVLR-Jogeshwari Vikhroli Link Road','JVPD Scheme','Kala Nagar','Kalina','Kalyan','Kamala City','Kanch Pada','Kandarpada','Kandivali East','Kandivali West','Kanjurmarg East','Kanjurmarg West','Kannamwar Nagar 1','Kanya Pada','Kemps Corner','Khar','Khar West','King Circle','Kulup Wadi','Kurar Village','Kurla East','Kurla West','Lakme Road','Lal Baug','LBS Marg','Link Road','Linking Road','Lokhandwala Complex','Lokhandwala Twp','Lower Parel','Madh','Magathane','Mahalakshmi','Mahalaxmi Race Course','Mahatama Gandhi Road','Mahavir Nagar','Mahim','Mahim West','Malabar Hill','Malad East','Malad West','Marol','Marol Maroshi','Marol Maroshi Road','Matunga','Matunga East','Matunga West','Mazgaon','Mehboob Studio','MHADA Colony','MHADA Colony 20','Mindspace','Mira Bhayandar','Mira Road','Motilal Nagar 2','Mount Mary','Mulund Colony','Mulund East','Mulund West','Mumbai Central','Nahur East','Nahur West','Naigaon East','Nalasopara East','Nalasopara West','Nana Chowk','Nansey Colony','Napean Sea Road','Nepeansea Road','New Link Road','Orlem','Oshiwara','Pali Hill','Pali Naka','Parel','Parmanand Wadi','Peddar Road','Pedder Road','Pestom Sagar','Phase D, Shastri Nagar','Piramal Nagar','Pleasant Park','Poonam Gardens','Poonam Nagar','Poonam Sagar','Postal Colony','Powai','Powai lake','Prabhadevi','Pratiksha Nagar','Pratiksha Nagar-Sion','Premier Colony','Raheja Vihar','Rajendra Nagar','Rambaug','Ramdev Park','Royal Palms Estate','Saat Rasta','Sai Baba Complex','Sai Baba Nagar','Sakinaka','Sakinaka Junction','Samata Nagar','Santacruz East','Santacruz West','Sarvodaya Nagar','Seven Bungalows','Sewri','Shantivan','Shastri Nagar','Shell Colony','Sher E Punjab Society','Sher-e-Punjab','Shimpoli','Shivaji Park','Shri Krishana Nagar','Shri Swami Samarth Nagar','Siddhartha Nagar','Sion','Sion East','Sion Trombay Road','Sundar Nagar, Kalina','Sunder Nagar','Swastik Park','Takshila Nagar','Tardeo','Thakur Complex','Thakur Village, Kandivali East','Thane','Thane-Kalyan-Dombivli','Tilak Nagar - Harbour Line','Tilak Nagar â€“ Central Line','Tunga','Turner Road','Udyog Nagar','Union Park','Unnat Nagar','Uppar Colaba','Upper Govind Nagar','Vakola','Vasai','Vasai East','Vasai West','Veena Nagar','Veera Desai Chowk','Veera Desai Road','Versova','Vidya Nagari','Vikhroli','Vikhroli East','Vikhroli West','Vile Parle East','Vile Parle West','Vinay Nagar','Virar','Virar East','Virar West','Vishveshwar Nagar','Wadala','Wadala East','Wadala West','Walkeshwar','Waterfield Road','World Trade Centre','Worli','Worli Hill','Worli Naka Acharaya Atre Chowk','Worli Sea Face','Yari Road','Yeshodham',))

dictforlabel=[]

dictforlabel.append(['Bhayandar West','IC Colony','Kandarpada','Dahisar West','Mira Bhayandar','Bhayandar East','Poonam Sagar','Dahisar East','Ramdev Park','Mira Road','Beverly Park','Poonam Gardens','Naigaon East','Pleasant Park','Hatkesh Udyog','Vinay Nagar'])

dictforlabel.append(['Sion','Sion East','Chunabhatti','Antop Hill','Pratiksha Nagar','Pratiksha Nagar-Sion','Everard Nagar','Kurla West','Takshila Nagar','Bhakti Park','Kurla East','Premier Colony','Swastik Park','Tilak Nagar - Harbour Line','Collector Colony','Postal Colony','Shell Colony','Tilak Nagar â€“ Central Line','Union Park','Central Avenue Road','Chembur'])

dictforlabel.append(['Chakala','Sher E Punjab Society','Andheri East','Ekta Nagar','JB Nagar','Poonam Nagar','Chakala MIDC','Marol Maroshi','Marol Maroshi Road','Aarey Milk Colony','Bhavani Nagar','Marol','Film City','Sakinaka','Sakinaka Junction','Royal Palms Estate','Tunga','Raheja Vihar','JVLR-Jogeshwari Vikhroli Link Road','Rambaug','Chandivali','MHADA Colony 20','Powai lake','IIT Colony','Powai','Ghatkopar West','Central Area','Vikhroli West'])

dictforlabel.append(['Charkop Sector 8','Jankalyan Nagar','Charkop','Charkop Sector 2','Gorai 2','Ekta Nagar Charkop','Evershine Nagar','Mindspace','New Link Road','Malad West','Dhanukar Wadi','Orlem','Kanch Pada','Chiku Wadi','Sunder Nagar','Ashok Nagar Western Mumbai','Kandivali West','Shimpoli','Mahavir Nagar','Sai Baba Nagar','Udyog Nagar','Borivali West','Upper Govind Nagar','Vishveshwar Nagar','Datta Pada','Malad East','Rajendra Nagar','Akurli Nagar','Borivali East','Dindoshi','Kurar Village','Thakur Complex','Nansey Colony','Shantivan','Kulup Wadi','Asha Nagar','Shri Krishana Nagar','Magathane','Devi Pada','Yeshodham','Sai Baba Complex','Gokuldham','Gokul Dham','Kanya Pada','Kandivali East','Lokhandwala Twp','Thakur Village, Kandivali East','Film City Road'])

dictforlabel.append(['Virar West','Virar','Nalasopara West','Vasai West','Virar East','Nalasopara East','Vasai','Vasai East'])

dictforlabel.append(['LBS Marg','Kanjurmarg West','Sarvodaya Nagar','Kanjurmarg East','Ishwar Nagar','Vikhroli East','Vikhroli','Bhandup','Bhandup West','Kannamwar Nagar 1','Veena Nagar','Mulund West','Mulund Colony','Nahur West','Bhandup Industrial Estate','Bhandup East','Nahur East','Mulund East','Samata Nagar','Thane','Thane-Kalyan-Dombivli','Kalyan'])

dictforlabel.append(['Malabar Hill','Napean Sea Road','Nepeansea Road','Walkeshwar','Kemps Corner','Breach Candy','Peddar Road','Pedder Road','Altamount Road','Haji Ali','Tardeo','Nana Chowk','Colaba','Uppar Colaba','Grant Road','Charni Road','World Trade Centre','Mumbai Central','Cuffe Parade','Church Gate','Byculla','Sher-e-Punjab','Mazgaon'])

dictforlabel.append(['Madh','Yari Road','Versova','Seven Bungalows','Lokhandwala Complex','Juhu Versova Link','Juhu Versova Link Road','Shri Swami Samarth Nagar','Juhu','Juhu Beach Area','4 Bunglows','Four Bungalows','Shastri Nagar','Andheri West','D.N. Nagar','Phase D, Shastri Nagar','Bangur Nagar','JVPD Scheme','Juhu Vile Parle Development Scheme','Motilal Nagar 2','Azad Nagar','Vile Parle West','Gulmohar Road','Veera Desai Road','Veera Desai Chowk','Oshiwara','Best Nagar - Goregaon West','Siddhartha Nagar','Jogeshwari West','Goregaon West','Piramal Nagar','Goregaon East','Jayprakash Nagar','Unnat Nagar','CAMA Industrial Estate','Jogeshwari East','MHADA Colony','Bimbisar Nagar'])

dictforlabel.append(['Bandra Band Stand','Carter Road','Mount Mary','Mehboob Studio','Pali Hill','Juhu Tara Road','Juhu Tara','Pali Naka','Bandra West','Bandra','Link Road','Khar West','Linking Road','Waterfield Road','Bandra Reclamation','Turner Road','Khar','Santacruz West','Bandra East','Gandhi Nagar','Vakola','Kala Nagar','Vile Parle East','Mahatama Gandhi Road','Santacruz East','Sundar Nagar, Kalina','Vidya Nagari','Kalina','Bandra Kurla Complex'])

dictforlabel.append(['Worli Hill','Worli Sea Face','Worli Naka Acharaya Atre Chowk','Worli','Mahalakshmi','Mahalaxmi Race Course','Gopal Nagar','Saat Rasta','Agripada','Prabhadevi','Kamala City','Jacob Circle','Elphinstone','Chinchpokli','Parel','Lower Parel','Dadar West','Lal Baug','Shivaji Park','Mahim West','Mahim','Dadar East','Matunga West','Bhoiwada','Dadar TT Circle','Dadar','Hindu Colony','Parmanand Wadi','Sewri','Wadala West','Matunga','Matunga East','King Circle','Wadala East','Wadala'])

# locarr=[0,0,0,0,0,0,0,0,0]
# for i in range(10):
#     if locality in dictforlabel[i]:
#         if i!=0:
#             locarr[i-1]=1
            
# furnishingarr=['Furnished','Semi-furnished','Unfurnished']
# furnishing_locarr=[0,0]
# for i1 in range(3):
#     if furnish in furnishingarr[i1]:
#         if i1!=0:
#             furnishing_locarr[i1-1]=1

btn=st.button("Predict")
if btn:
    other=[]
    ll=0
    other.append(area)
    other.append(bathroom_num)
    other.append(bedroom_num)
    other=np.array(other)
    for i in range(len(dictforlabel)):
        if locality in dictforlabel[i]:
            ll=i
#             st.write(str(i))
    if i==0:
        ans=model_0.predict(np.array([other]).reshape(1,-1))
    elif i==1:
        ans=model_1.predict(np.array([other]).reshape(1,-1))
    elif i==2:
        ans=model_2.predict(np.array([other]).reshape(1,-1))        
    elif i==3:
        ans=model_3.predict(np.array([other]).reshape(1,-1))        
    elif i==4:
        ans=model_4.predict(np.array([other]).reshape(1,-1))        
    elif i==5:
        ans=model_5.predict(np.array([other]).reshape(1,-1))        
    elif i==6:
        ans=model_6.predict(np.array([other]).reshape(1,-1))        
    elif i==7:
        ans=model_7.predict(np.array([other]).reshape(1,-1))        
    elif i==8:
        ans=model_8.predict(np.array([other]).reshape(1,-1))
    elif i==9:
        ans=model_9.predict(np.array([other]).reshape(1,-1))
    else:
        st.write("Somethings wrong")
    if ans < 5000:
        st.write("Insufficient Data to predict(too little observations)")
    else:
        st.write("The predicted rent is Rs.",str(int(ans)))
