SELECT * FROM sakthi.df_orders;
select max(List_Price),Sub_Category from df_orders group by Sub_Category having max(List_Price)>5000;
select Category, max(Discount_Percent )from df_orders group by Category;
Select Sub_Category,max(Profit) from df_orders group by Sub_Category having max(Profit)>50;
Select Sub_Category,min(Profit)  as minprofit from df_orders group by Sub_Category limit 10;
select max(sales),Category from df_orders group by Category;
SELECT * FROM sakthi.df_order;
update df_order set Order_ID='22' where Order_ID=10;
select Order_Date,category from df_order join df_orders on df_order.order=df_orders.order;
select Order_ID,category ,State from df_order left join df_orders on df_order.order=df_orders.order;
update df_order set Region=upper(Region); 
select Sub_Category ,sum(Quantity) from df_orders group by Sub_Category  having sum(Quantity)>1000;                                             
Select * from df_order where Segment like 'C%';                         
Select * from df_order where Segment not like 'C%';                      
SELECT * FROM sakthi.df_orders;
select max(Sales)  as revenue ,Product_Id from df_orders group by Product_ID having max(Sales)>=40000 limit 10;
select sum(Discount) as TotalDiscount ,Category from df_orders group by Category;
select sum(Profit) as TotalProfit ,Category from df_orders group by Category;
select Segment, max(Quantity) as highestorders from df_orders join df_order on df_order.order=df_orders.order group by Segment;
select sum(Profit) as highestTotalProfit ,Category from df_orders group by Category having sum(Profit)>100000;
select sum(Profit) as Top5highestprofitpercity ,City from df_orders join df_order on df_order.order=df_orders.order group by City having sum(profit)>10000;
SELECT * FROM sakthi.df_order;
select Order_Date from df_order limit 3;
select sum(Sales) as totalrevenueperyear,
year(str_to_date(Order_Date,'%Y-%m-%d')) as order_year
from df_order join df_orders on df_order.order=df_orders.order group by order_year;
Alter table df_order
modify column Order_Date date;
select avg(Discount_Percent) as Averagediscount ,Region from df_orders        
join df_order on df_order.order=df_orders.order group by Region; 
select Avg(Sales) as highestaveragesellprice,Region from df_orders join df_order on df_order.order=df_orders.order group by Region;
select Avg(Sales) as PerProductCategory ,Category from df_orders  group by Category               


