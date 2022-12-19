import java.util.Random;
public class Game{
	Player p1;
	Player p2;
	int turnCnt;
	public Random rand;
	
	public Game(){
		rand = new Random();
		p1 = new Player(0);
		p2 = new Player(1);
	}
	
	public void setUp(){
		
		
	}
	
}