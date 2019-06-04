import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;

import java.util.Set;
import java.util.TreeSet;

public class XStreamUsage {

    private String string = "Sample string field";

    private int integer = 1337;

    public static void main(String[] args) {
        XStream xStream = new XStream(new DomDriver());
        String serialized = xStream.toXML(new TreeSet<String>());
        System.out.println(serialized);
        TreeSet<String> set = (TreeSet<String>) xStream.fromXML(serialized);
        set.add("Test");
        System.out.println(set.toString());
    }

}
