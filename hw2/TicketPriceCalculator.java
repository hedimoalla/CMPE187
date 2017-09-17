import java.util.List;

/**
Ticket Price Calculator class
Calculate ticket price based on age
Adult age = 18 - Children age = 3 -> 18, baby age = free ticket = 3
Giving family discount of 5% if more than 1 adult and 1 children travel (2 adult - 2 child)
*/
public class TicketPriceCalculator {
    // Define age and discount % variable
    private static int ADULT_AGE = 18;
    private static int FREE_TICKET_AGE_BELOW = 3;
    
    public static double FAMILY_DISCOUNT = 0.05;
    
    /** Public method for calculate the price of ticket
     @Param: 
	 List<Passenger>: List of Passenger
	 Integer: adult ticket price
	 Integer: children ticket price
    */
    public double calculatePrice(List<Passenger> passengers, int adultTicketPrice, int childTicketPrice) {
        // Defind local variable
	int totalPrice = 0;
        int childrenCounter = 0;
        int adultCounter = 0;
        double result;
	// For each passenger, check age and calculate ticket price
        for (Passenger passenger : passengers) {
	    // IF passenger > 18, use adult price
	    // ELSE IF 3 < age < 18, use child price
	    // ELSE free
            if (passenger.getAge() > ADULT_AGE) {
                totalPrice += adultTicketPrice;
                adultCounter++;
            } else if (passenger.getAge() > FREE_TICKET_AGE_BELOW) {
                totalPrice += childTicketPrice;
                childrenCounter++;
            }
        }
	// Apply discount if at least 2 adult AND 2 children
        if (childrenCounter > 1 && adultCounter > 1) {
            result = (1 - FAMILY_DISCOUNT) * totalPrice;
        } else {
            result = totalPrice;
        }

        return result;
    }
}



