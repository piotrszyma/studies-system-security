import com.thoughtworks.xstream.XStream;
import com.thoughtworks.xstream.io.json.JettisonMappedXmlDriver;
import org.apache.tomcat.util.codec.binary.Base64;

import java.io.*;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(
        name = "Servlet",
        urlPatterns = {"/"}
    )
public class Servlet extends HttpServlet {

    private XStream xStream;

    public Servlet() {
        this.xStream = new XStream();
        this.xStream.setClassLoader(this.getClass().getClassLoader());
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        Cookie[] cookies = request.getCookies();

        Data data = null;

        if (null != cookies) {
            for (Cookie cookie : cookies) {
                if (cookie.getName().equals("data")) {
                        data = (Data) xStream.fromXML(new String(Base64.decodeBase64(cookie.getValue())));
                }
            }
        }

        if (null == data) {
            data = new Data("Anonymous");
        }

        request.setAttribute("name", data.getName());
        request.getRequestDispatcher("page.jsp").forward(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        if (null != request.getParameter("name")) {
            Data data = new Data(request.getParameter("name"));

            Cookie cookie = new Cookie("data", Base64.encodeBase64String(xStream.toXML(data).getBytes()));
            response.addCookie(cookie);
        }

        response.sendRedirect("/");
    }
}