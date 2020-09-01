# Use Case 4: Mobile Couponing (MC)

##### Analyze the problem
Real-time mobile couponing is about putting coupons on consumers' cell phones in real-time. Coupons are usually available for companies in the city where the consumer is based. The aim of this use case is to push coupons to the customer's phone within a few seconds of obtaining location information. The solution should be scalable to accommodate hundreds of thousands of active cell phones at any time.


##### Outline the solution
Predictive analysis would classify the types of services and goods that the consumer will be interested in purchasing. The user's location will be monitored from his or her cell phone in real time. The Data Science Team will create models to predict user preferences based on the user history database. The preferences will then be stored in a database of user preferences in the location services database. An online directory of programmes and existing coupons accessible at different locations will be updated.


##### Consider technologies
Coupon recommendation engine can look up user interests and location services to determine which coupons to print. We will use Apache Spark for this engine based on assumptions made in previous use cases. Second, we 're looking at the real-time stream and coupon queues.

##### Lay out the architecture
We 're developing a custom mobile gateway solution. We 're going to use Kafka for the real-time queue. Apache Spark will be used as the preferred coupon engine. This will help to scale the solution horizontally.

##### Design key elements
User preferences and location services should be designed in a specific way to allow easy query and caching. The mobile gateway we are developing should also be horizontally scalable, so it has to be designed as a stateless infrastructure. Coupons that have been found to have a time to live during the process. If the location information received from cell phones is trapped in the queue for long periods of time, the customer must have transferred to another location when the coupons eventually arrive.

##### Best practices: Pipeline management
We also need to make it easier for the working staff to handle the system. Your pipeline usually has clusters, Kafka clusters, Spark clusters, database clusters, and custom service clusters. It's a smart idea to use best-in - class cluster managers like YARN and Mesos to handle clusters.

