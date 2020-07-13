# Kafka Lab Notes

This is a concise lab notes for Kafka quick start, if you prefer the full length article official quick start tutorial: https://kafka.apache.org/quickstart#quickstart_download

## Quick Start

### Local install

Kafka local installation will work on Mac with OSX or beyond, and Windows, as well as Linux. Make sure that you have the latest Java development kit, the JDK, installed. Then download the latest version of Kafka: https://www.apache.org/dyn/closer.cgi?path=/kafka (To find the latest release)

**If you didn't have the JDK installed, you may get an error.**

in a nutshell:

```bash
$ # Download Kafka
$ wget https://mirror.dsrg.utoronto.ca/apache/kafka/2.6.0/kafka_2.13-2.6.0.tgz
$ tar -xzf kafka_2.13-2.6.0.tgz
$ cd kafka_2.13-2.6.0
$ # Start Kafka Env
$ bin/zookeeper-server-start.sh config/zookeeper.properties
$ # In another terminal tab
$ bin/kafka-server-start.sh config/server.properties
$ # Create a topic
$ bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092
$ # Describe a topic
$ bin/kafka-topics.sh --describe --topic quickstart-events --bootstrap-server localhost:9092
$ # write some events to a topic
$ # Enter: "This is my first event" and "This is my second event"
$ bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
This is my first event
This is my second event
$ # Read the events
$ bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```

### Kafka Connect

[Kafka Connect](https://kafka.apache.org/documentation/#connect), [Kafka Connect section](https://kafka.apache.org/documentation/#connect)

Kafka Connect allows you to ingest data from external systems into Kafka. It is thus very easy to integrate existing systems with Kafka. There are hundreds of connectors readily available.

### Kafka Streams

#### [Kafka Streams](https://kafka.apache.org/documentation/streams)

Kafka Streams is a Java/Scala client library for Kafka. It allows you to implement mission-critical real-time applications and microservices. It combines the simplicity of writing and deploying standard Java and Scala applications on the client side.

#### `WordCount` algorithm taken from official kafka site

```bash
KStream<String, String> textLines = builder.stream("quickstart-events");

KTable<String, Long> wordCounts = textLines
            .flatMapValues(line -> Arrays.asList(line.toLowerCase().split(" ")))
            .groupBy((keyIgnored, word) -> word)
            .count();

wordCounts.toStream().to("output-topic"), Produced.with(Serdes.String(), Serdes.Long()));
```

The [Kafka Streams demo](https://kafka.apache.org/25/documentation/streams/quickstart) and the [app development tutorial](https://kafka.apache.org/25/documentation/streams/tutorial) demonstrate how to code and run such a streaming application from start to finish.

### Kill the Kafka Environment

```bash
$ rm -rf /tmp/kafka-logs /tmp/zookeeper
```
