FILEPATH=/Users/szyma/java1234
CLASSES=.:/Users/szyma/Studies/studies-system-security/java-vs-deserialization/part-ii/xstream-1/jars/xmlpull-1.1.4c.jar:/Users/szyma/Studies/studies-system-security/java-vs-deserialization/part-ii/xstream-1/jars/xstream-1.4.5.jar

make_dir:
	CLASSPATH=${CLASSES} javac NotSoSimplePayloadGenerator.java
	CLASSPATH=${CLASSES} java NotSoSimplePayloadGenerator

simple_usage:
	CLASSPATH=${CLASSES} javac XStreamUsage.java
	CLASSPATH=${CLASSES} java XStreamUsage

rm:
	rm -rf ${FILEPATH}
