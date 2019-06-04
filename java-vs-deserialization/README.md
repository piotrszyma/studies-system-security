# README #

**BE EXTREMELY CAREFUL! RUNNING THIS CODE MAY EXPOSE YOUR MACHINE TO EXPLOIATION! WHEN RUNNING SERVERS, MAKE SURE THEY ARE ONLY ACCESSIBLE VIA LOCALHOST, AND IDEALLY - TURN OFF INTERNET CONNECTION COMPLETELY!**

This is the source code which was used in series of articles about deserialization vulnerabilities in Java - "Java vs. niezaufana serializacja danych" on http://sekurak.pl/ .

All articles are in Polish.

[Part I - java deserialization basics, commons-collections gadget chain, sample exploitation](http://sekurak.pl/java-vs-deserializacja-niezaufanych-danych-i-zdalne-wykonanie-kodu-czesc-i/)

[Part II - deserialization DoS via JRE classes, RCE via XStream library](https://sekurak.pl/java-vs-deserializacja-niezaufanych-danych-czesc-ii-mozliwosc-dosowania-aplikacji/)

[Part III - defences and mitigations against Java deserialization vulnerabilities](https://sekurak.pl/java-vs-deserializacja-niezaufanych-danych-czesc-iii-jak-sie-zabezpieczyc/)


## Usage ##

### Part I ###

Source code related to the first part is available in directory **[part-i](part-i)**

To start vulnerable server, run:

```bash
mvn clean package && sh target/bin/webapp
```

To generate simple payload (based on apache commons-collections 3.1 library) run:

```bash
export CLASSPATH="<location of commons-collections-3.1 JAR>:."
javac PayloadGenerator.java
java PayloadGenerator
```

### Part II ###

Source code related to second part is available in directory **[part-ii](part-ii)**

#### Java deserialization DoS attacks ####

Source code is in directory **[part-ii/java-dos](part-ii/java-dos)**

##### DoS via recursive sets #####
To generate payload which will cause Java to hang during deserialization, run:

```bash
javac DeserializationDosRecursiveSet.java
java DeserializationDosRecursiveSet
```

You can test generated payload against the server from Part I

To check how long Java would deserialize given payload, run:

```bash
javac DeserializationDosRecursiveSetCustomizable.java
java DeserializationDosRecursiveSetCustomizable <depth of recursion>
```

*Be aware that even with small payloads it might take quite a lot of time. On my machine, running this code with depth of 28 will take almost a minute*.

##### DoS via exceeding max array size #####
To generate payload which will cause Java to hang during deseriaarelization, run:

```bash
javac DeserializationDosMaxArray.java
java DeserializationDosMaxArray
```

You can test generated payload against the server from Part I (although Tomcat won't crash even with `java.lang.OutOfMemoryError`)

#### Java deserialization vulnerabilities with XStream ####

##### XStream deserialization vulnerabilities example 1

XStream deserialization RCE via `java.lang.reflect.Proxy` and `java.beans.EventHandler`

Source code is in directory **[part-ii/xstream-1](part-ii/xstream-1)**

To see how XStream works in practice run:
```bash
cd src/main/java/
export CLASSPATH="<location of XStream JAR>:<location of XML Pull Parser JAR>:."
javac XStreamUsage.java
java XStreamUsage
```

To start vulnerable server, run:

```bash
 mvn clean package && sh target/bin/webapp
```

To generate simple payload (which will work only when deserialized object will be cast to some interface, so it won't work with test vulnerable server) run:

```bash
cd src/main/java/
export CLASSPATH="<location of XStream <= 1.4.6 JAR>:<location of XML Pull Parser JAR>:."
javac SimplePayloadGenerator.java
java SimplePayloadGenerator
```

To generate (try) not-so-simple payload generator (generation won't work, because OS command will be executed first), run:
```bash
cd src/main/java/
export CLASSPATH="<location of XStream <= 1.4.6 JAR>:<location of XML Pull Parser jar:."
javac NotSoSimplePayloadGenerator.java
java NotSoSimplePayloadGenerator
```

##### XStream deserialization vulnerabilities example 2

XStream deserialization RCE via `groovy.util.Expando`

Source code is in directory **[part-ii/xstream-2](part-ii/xstream-2)**

To start vulnerable server, run:

```bash
 mvn clean package && sh target/bin/webapp
```

To generate payload for the server run:

```bash
cd src/main/java/
export CLASSPATH="<location of XStream <= 1.4.6 JAR>:<location of Jettison 1.2.x JAR>:<location of Groovy <= 2.4.3 JAR>:."
javac PayloadGenerator.java
java PayloadGenerator
```

### Part III ###

Source code related to second part is available in directory **[part-iii](part-iii)**

#### SerialKiller demo ####

Source code is in directory **[part-iii/serial-killer](part-iii/serial-killer)**

To start server, run:

```bash
 mvn clean package && sh target/bin/webapp
```

Server uses config from **[part-iii/serial-killer/src/main/resources/serialkiller.xml](part-iii/serial-killer/src/main/resources/serialkiller.xml)** - you can modify this file and redeploy server (or wait 6 seconds) to play with SerialKiller.

#### NotSoSerial demo ####

Source code is in directory **[part-iii/not-so-serial](part-iii/not-so-serial)**

To start server, run:

```bash
 mvn clean package && sh target/bin/webapp
```

In given configuration NotSoSerial agent works in whitelisting dryrun mode with empty whitelist. To play with different settings modify ```extraJvmArguments``` tag in **[part-iii/not-so-serial/pom.xml](part-iii/not-so-serial/pom.xml)** (different config options are available on **[project's homepage](https://github.com/kantega/notsoserial)**).

#### Crypto demo ####

Source code is in directory **[part-iii/crypto](part-iii/crypto)**

To start server, run:

```bash
 mvn clean package && sh target/bin/webapp
```