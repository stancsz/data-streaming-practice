# Use Case 1: Social Media Sentiment Analysis (SM)

##### Analyze the problem

Customers are using social media to express their feedback on your company's website and products. Your business needs a real-time social media tracking system to identify negative posts and alert your customer service. The goals for this architecture are: provide real- time monitoring of social media. Scale horizontally to accommodate future growth in posts and additional analytics.

##### Outline the solution

Twitter provides a real-time streaming API that can be used to listen to tweets happening for a specific user, handle or hashtag. We need areal-time subscriber that will subscribe to Twitter and receive tweets coming in for specific hashtags. Almost all social media platforms, like Instagram and Gooogle Plus, support streaming interfaces. A text mining engine will use a sentiment analysis engine for identifying sentiment of the posts.

##### Consider technologies

Search engines can do real time data stream processing. Apache Storm and Apache Samza are popular engines for sentiment analysis. Storm and Samza both use Apache Kafka and Hadoop Yarn to process data. Strom is capable of doing parallel processing, and can provide very good throughput. It can be deployed in a cluster, which can then be horizontally scaled, as the load goes up. 

Samza is programmed through a simple API, and any programming language can be used to work with Samza. Moving data between Samza, and local data structures is manual, and that increases programming load. 

Samza's integrations are limited to management frameworks like Yarn and Mesos, and streaming ques like Kafka. Apache Spark is a general purpose compute engine that supports streaming, which has been greatly improved, in the latest versions. Message queues play an important part in real-time analytics, by providing a buffering zone. RabbitMQ, ActiveMQ, and Apache Kafka, are the most popular of the list. 

R and Python provide excellent multiple, sentiment analysis packages, that will do the job for us. We will build a web service, around Python, to provide sentiment analysis service, for any client.

##### Lay out the architecture

Social media sentiment analysis architecture can be built for Twitter, Facebook and other social networks. The architecture will allow for both Twitter and Facebook subscribers to be built within the same JVM with different threads monitoring different platforms and hashtags. The real-time streaming queue will be built on Kafka with a text mining engine built in Apache Spark. It will use Python's sentiment analysis packages to predict sentiment.

##### Design key elements

Designing Apache Spark components for real-time processing. Each post received in the queue is independent of other posts. The sentiment of the tweets can be summarized through a reduce function for every micro batch. For 100K per day load, very small batch sizes might not be optimal. We will use the NTLK Python package for sentiment analysis.

##### Best practices: Real-time streaming

Streaming should guarantee delivery of messages pushed into the streaming queue. Ordering of messages may or may not be important for your use case. Solution should support failover in case of individual node or partition failures. Streaming solution should be capable of horizontally scaling to handle big data.