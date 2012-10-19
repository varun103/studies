package sample;

//import java.nio.channels.Channel;

//import org.jboss.*;
import org.jboss.netty.buffer.ChannelBuffer;
import org.jboss.netty.channel.Channel;
import org.jboss.netty.channel.ChannelHandlerContext;
import org.jboss.netty.channel.ExceptionEvent;
import org.jboss.netty.channel.MessageEvent;
import org.jboss.netty.channel.SimpleChannelHandler;


//SimpleChannelHandler provides various handler events
public class DiscardServerHandler extends SimpleChannelHandler{
	
	//Message received event handler is to 
	public void messageReceived(ChannelHandlerContext ctx, MessageEvent e){
		
		ChannelBuffer buf = (ChannelBuffer) e.getMessage();
		Channel ch = e.getChannel();
		StringBuilder st = new StringBuilder();
		
//		while (buf.readable()){
//			System.out.println((char) buf.readByte());
//			//st.append((char) buf.readByte());
//			//System.out.flush();
//		}
//		System.out.println(st);
//		System.out.flush();
//		
		ch.write(buf);
		
		
	}
	
	public void exceptionCaught(ChannelHandlerContext ctx, ExceptionEvent e){

		e.getCause().printStackTrace();
		Channel ch = e.getChannel();
		ch.close();
		
		
	}

}
