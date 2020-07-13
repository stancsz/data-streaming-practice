# Use Case 2: Real-Time Fraud Detection (FD)

##### Analyze the problem
We are going to focus on using big data and predictive analytics in preventing e-commerce payment fraud. The identification of a fraudulent transaction should happen within a matter of minutes after the order is placed. The goals for this solution are as follows. Architect a real-time payment fraud prediction system to identify fraudulent transactions before order shipment.

##### Outline the solution
We will outline the solution for real-time fraud detection in this video. The e-commerce system is used to collect orders from the customer. The orders are pushed into a transactions database with customer details. Transactions identified as fraudulent will then be pushed to a real time fraud queue.

##### Consider technologies

| Goals                   | R/Python | TensorFlow | Spark |
| ----------------------- | -------- | ---------- | ----- |
| ML Algorithm            | good     | okay       | okay  |
| scalability             | bad      | bad        | good  |
| third-party integration | good     | bad        | good  |
| code management         | bad      | good       | good  |

Overall, spark is the most well rounded solution for this use case.

##### Lay out the architecture

for real-time fraud detection in this video. We will use Apache Kafka as the streaming queue. The prediction engine to be used would be Apache Spark.

##### Design key elements

Fraud detection pipeline design includes Apache Spark predictions and Kafka clusters. Each transaction is independent so it is easy to process that transaction inside map operations. Design the system for frequent model updates. Average response time for this pipeline is expected to be a few minutes.

##### Best practices: Predictive analytics

Big data architects should care about prediction efficiency, and data scientists should care About prediction effectiveness. Scalability is an important architectural component in predictions, and it should be possible to run predictions on a number of transactions simultaneously. We will leave the finer details of model building to data scientists.