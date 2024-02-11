Question 1
SELECT count(*) FROM `de-ibphilippov.de_shvetsov.week3_green_taxi_2022` 

Q2
SELECT count(distinct(PULocationID)) FROM `de-ibphilippov.de_shvetsov.week3_green_taxi_2022` 

Q3
SELECT count(*) FROM `de-ibphilippov.de_shvetsov.week3_green_taxi_2022` where fare_amount = 0

Q4
create table

Q5
SELECT distinct(PULocationID) FROM `de-ibphilippov.de_shvetsov.week3_green_taxi_2022` where cast(lpep_pickup_datetime as date) between "2022-06-01" and "2022-06-30"
