public abstract class Card{
	// might implement as an interface
	private String cID; 
	private String cName;
	
	//private int cColor; // (red, blue, yellow, green, white, purple, black)
	// maybe set color to be an array cause card can have many colors
	
	
	// image var using JavaFX?
	
	
	public Card(cID, cName){
		this.cID = cID;
		this.cName = cName;
	}
	
	public String getCID(){
		return this.cID;
	}
	
	public String getCName(){
		return this.cName;
	}
}