import mysql.connector
import streamlit as st
import pandas as pd

# Example code to check connection (change with actual credentials)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kannadi@123",
    database="sakthi")
st.markdown("""
    <style>
        
        .stApp {
            background-color:  #90EE90;  
        }
        
        
    </style>
""", unsafe_allow_html=True)
myquery=conn.cursor()
r=st.sidebar.selectbox("SELECT THE TABS",["ABOUT","QUERY1_TO_10","QUERY10_TO_20"])

if r == "ABOUT":
    st.title("Hello Teammates I am kannan")
    st.markdown("""
    :moon:
    ## Description :
     
    """)
    st.title("Retail_Order_Analysis")
    st.snow()
    st.markdown("""


    ### PROBLEM STATEMENT :
    ### OBJECTIVE:
    To analyze and optimize sales performance by identifying key trends, top-performing products, and growth opportunities using a dataset of sales transactions.
    ### GOALS:
    Analyze the dataset to find the valuable insights .
    ### MENTOR : Mrs.GOMATHI 

    """)
    st.balloons()
    st.success("ONCE AGAIN THANKYOU GUVI")

if r=="QUERY1_TO_10":
  r1=st.sidebar.radio("SELECT THE QUERIES",['Query1','Query2','Query3','Query4',"Query5","Query6","Query7","Query8","Query9","Query10"])
  if r1=="Query1":
    st.snow()
    myquery.execute("Select * from df_order where Segment like 'C%'")
    data=myquery.fetchall()
    st.title(" Order the segment column starting like c?")
    df=pd.DataFrame(data,columns=myquery.column_names)
    st.dataframe(df)
  if r1=="Query2":
    st.balloons()
    myquery.execute("Select Sub_Category,min(Profit)  as minprofit from df_orders group by Sub_Category limit 10")
    data=myquery.fetchall()
    st.title("Find minimum profit based on the Sub_category limit 10?")
    df=pd.DataFrame(data,columns=myquery.column_names)
    st.dataframe(df)
  if r1=="Query3":
      myquery.execute("select max(List_Price),Sub_Category from df_orders group by Sub_Category having max(List_Price)>5000")
      data=myquery.fetchall()
      st.title("Find maximum list_price based on sub_category ?")
      df=pd.DataFrame(data,columns=myquery.column_names)
      st.dataframe(df)
  if r1=="Query4":
      st.balloons()
      myquery.execute("select Category, max(Discount_Percent )from df_orders group by Category")
      data=myquery.fetchall()
      st.title("find max discount based on category?")
      df=pd.DataFrame(data,columns=myquery.column_names)
      st.dataframe(df)
  if r1=="Query5":
      st.snow()
      myquery.execute("Select Sub_Category,max(Profit) from df_orders group by Sub_Category having max(Profit)>50")
      data=myquery.fetchall()
      st.title("Find maximum profit based on sub_category?")
      df=pd.DataFrame(data,columns=myquery.column_names)
      st.dataframe(df)
  if r1=="Query6":
      myquery.execute("select Sub_Category ,sum(Quantity) from df_orders group by Sub_Category  having sum(Quantity)>1000")
      data=myquery.fetchall()
      st.title("Find Quantity,sub_category greater than 1000?")
      df=pd.DataFrame(data,columns=myquery.column_names)
      st.dataframe(df)
  if r1=="Query7":
      st.snow()
      myquery.execute("select max(sales),Category from df_orders group by Category")
      data=myquery.fetchall()
      st.title("Find maximum sales based on Category")
      df=pd.DataFrame(data,columns=myquery.column_names)
      st.dataframe(df)
  if r1=="Query8":
      st.balloons()
      myquery.execute("select Order_Date,category from df_order join df_orders on df_order.order=df_orders.order")
      data=myquery.fetchall()
      st.title("Find order_date and category?")
      df=pd.DataFrame(data,columns=myquery.column_names)
      st.dataframe(df)
  if r1=="Query9":
      myquery.execute("select Order_ID,category ,State from df_order left join df_orders on df_order.order=df_orders.order")
      data=myquery.fetchall()
      st.title("find  order_id,category,state from the dataset?")
      df=pd.DataFrame(data,columns=myquery.column_names)
      st.dataframe(df)
  if r1=="Query10":
      st.snow()
      myquery.execute("Select * from df_order where Segment not like 'C%' ")
      data=myquery.fetchall()
      st.title("Find the segment not starting like C?")
      df=pd.DataFrame(data,columns=myquery.column_names)
      st.dataframe(df)
if r=="QUERY10_TO_20":
   r2=st.sidebar.radio("SELECT THE QUERIES",["Query11","Query12","Query13","Query14","Query15","Query16","Query17","Query18","Query19","Query20"])
   if r2=="Query15":
       st.snow()
       myquery.execute("select max(Sales)  as revenue ,Product_Id from df_orders group by Product_ID having max(Sales)>=40000 limit 10")
       data=myquery.fetchall()
       st.title("Find top 10 highest revenue generating products")
       df=pd.DataFrame(data,columns=myquery.column_names)
       st.dataframe(df)
   if r2 == "Query12":
       myquery.execute("select sum(Discount) as TotalDiscount ,Category from df_orders group by Category")
       data = myquery.fetchall()
       st.title("Calculate the total discount given for each category")
       df = pd.DataFrame(data, columns=myquery.column_names)
       st.dataframe(df)
   if r2 == "Query13":
       st.balloons()
       myquery.execute("select sum(Profit) as TotalProfit ,Category from df_orders group by Category")
       data = myquery.fetchall()
       st.title("Find the total profit per category")
       df = pd.DataFrame(data, columns=myquery.column_names)
       st.dataframe(df)
   if r2 == "Query14":
       myquery.execute("select Segment, max(Quantity) as highestorders from df_orders join df_order on df_order.order=df_orders.order group by Segment")
       data = myquery.fetchall()
       st.title("Identify the top 3 segments with the highest quantity of orders")
       df = pd.DataFrame(data, columns=myquery.column_names)
       st.dataframe(df)
   if r2 == "Query11":
       st.snow()
       myquery.execute("select sum(Profit) as highestTotalProfit ,Category from df_orders group by Category having sum(Profit)>100000")
       data = myquery.fetchall()
       st.title("Find the product category with the highest total profit")
       df = pd.DataFrame(data, columns=myquery.column_names)
       st.dataframe(df)
   if r2 == "Query16":
       st.balloons()
       myquery.execute("select sum(Profit) as Top5highestprofitpercity ,City from df_orders join df_order on df_order.order=df_orders.order group by City having sum(profit)>10000")
       data = myquery.fetchall()
       st.title("Find the top 5 cities with the highest profit margins")
       df = pd.DataFrame(data, columns=myquery.column_names)
       st.dataframe(df)
   if r2 == "Query17":
       myquery.execute("select sum(Sales) as totalrevenueperyear,year(str_to_date(Order_Date,'%Y-%m-%d')) as order_year from df_order join df_orders on df_order.order=df_orders.order group by order_year")
       data = myquery.fetchall()
       st.title("Calculate the total revenue generated per year")
       df = pd.DataFrame(data, columns=myquery.column_names)
       st.dataframe(df)
   if r2 == "Query18":
       st.snow()
       myquery.execute("select avg(Discount_Percent) as Averagediscount ,Region from df_orders join df_order on df_order.order=df_orders.order group by Region ")
       data = myquery.fetchall()
       st.title(" Determine the average discount percentage given per region")
       df = pd.DataFrame(data, columns=myquery.column_names)
       st.dataframe(df)
   if r2 == "Query19":
       st.balloons()
       myquery.execute("select Avg(Sales) as PerProductCategory ,Category from df_orders  group by Category  ")
       data = myquery.fetchall()
       st.title("Find the average sale price per product category")
       df = pd.DataFrame(data, columns=myquery.column_names)
       st.dataframe(df)
   if r2 == "Query20":
       st.snow()
       myquery.execute("select Avg(Sales) as highestaveragesellprice,Region from df_orders join df_order on df_order.order=df_orders.order group by Region")
       data = myquery.fetchall()
       st.title("Find the region with the highest average sale price")
       df = pd.DataFrame(data, columns=myquery.column_names)
       st.dataframe(df)




