SELECT COUNT(*) AS total_customers
FROM customer_churn_data;

#curned customers
SELECT COUNT(*) AS churned_customers
FROM customer_churn_data
WHERE churned = 1;

#total active customers
SELECT COUNT(*) AS active_customers
FROM customer_churn_data
WHERE churned = 0;

#churn rate
SELECT 
COUNT(CASE WHEN churned = 1 THEN 1 END) * 100.0 / COUNT(*) AS churn_rate
FROM customer_churn_data;

#churn distribution
SELECT churned, COUNT(*) AS total_customers
FROM customer_churn_data
GROUP BY churned;

#churn by gender
SELECT gender, COUNT(*) AS churned_customers
FROM customer_churn_data
WHERE churned = 1
GROUP BY gender;

#customer by subscription type
SELECT subscription_type, COUNT(*) AS customers
FROM customer_churn_data
GROUP BY subscription_type;

#churn by subscription type
SELECT subscription_type, COUNT(*) AS churned_customers
FROM customer_churn_data
WHERE churned = 1
GROUP BY subscription_type;

#average age of customers
SELECT AVG(age) AS average_age
FROM customer_churn_data;

#average watch per day
SELECT AVG(avg_watch_time_per_day) AS avg_watch_time
FROM customer_churn_data;

#churn by region
SELECT region, COUNT(*) AS churned_customers
FROM customer_churn_data
WHERE churned = 1
GROUP BY region;

#most popular favorite genre
SELECT favorite_genre, COUNT(*) AS users
FROM customer_churn_data
GROUP BY favorite_genre
ORDER BY users DESC;

#churn by favorite genre
SELECT favorite_genre, COUNT(*) AS churned_customers
FROM customer_churn_data
WHERE churned = 1
GROUP BY favorite_genre
ORDER BY churned_customers DESC;

#average watch time of churned customers
SELECT AVG(avg_watch_time_per_day) AS avg_watch_time_churned
FROM customer_churn_data
WHERE churned = 1;

#average watch time of active customers
SELECT AVG(avg_watch_time_per_day) AS avg_watch_time_active
FROM customer_churn_data
WHERE churned = 0;

#churn by number of profiles
SELECT number_of_profiles, COUNT(*) AS churned_customers
FROM customer_churn_data
WHERE churned = 1
GROUP BY number_of_profiles;

#Customers with highest watch time
SELECT customer_id, avg_watch_time_per_day
FROM customer_churn_data
ORDER BY avg_watch_time_per_day DESC
LIMIT 10;

#region with most costomers
SELECT region, COUNT(*) AS customers
FROM customer_churn_data
GROUP BY region
ORDER BY customers DESC;

#churn percentage by subscription type
SELECT subscription_type,
COUNT(CASE WHEN churned = 1 THEN 1 END) * 100.0 / COUNT(*) AS churn_percentage
FROM customer_churn_data
GROUP BY subscription_type;

#top 5 segments with highest churn rate
SELECT region, subscription_type, COUNT(*) AS churned_customers
FROM customer_churn_data
WHERE churned = 1
GROUP BY region, subscription_type
ORDER BY churned_customers DESC
LIMIT 5;