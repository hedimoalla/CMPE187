import java.util.ArrayList;
import java.util.List;

/**
Ticket Price Calculator - Test cases
This file includes a calculator and several test cases as methods
Each test method will print out the coressponding ticket price in the TicketCalculator 
*/
public class TicketPriceCalculatorTest {
    // Ticket Price for adult - child
    private static int ADULT_TICKET_PRICE = 40;
    private static int CHILD_TICKER_PRICE = 20;
    // The calculator object
    private static TicketPriceCalculator calculator = new TicketPriceCalculator();
    // Main object that calls other testing methods
    public static void main(String[] args){
	System.out.println("Test case for 1 adult: ");
	System.out.println("Ticket Price for one adult = " + calculatePriceForOneAdult());

	System.out.println("Test case for 1 child: ");
	System.out.println("Ticket Price for one child = " + calculatePriceForChild());

	System.out.println("Test case for big family: ");
	System.out.println("Ticket price for family of 4 = " + calculatePriceForFamily()); 
    }
    // Calculate the price for one adult - age 20
    public static double calculatePriceForOneAdult() {
        List<Passenger> passengers = new ArrayList<>();
        Passenger passenger = new Passenger(20);
        passengers.add(passenger);
        double price = calculator.calculatePrice(passengers, ADULT_TICKET_PRICE, CHILD_TICKER_PRICE);
	return price;
    }

    // Calculate the price for one child - age 15
    public static double calculatePriceForChild() {
        List<Passenger> passengers = new ArrayList<>();
        Passenger childPassenger = new Passenger(15);
        passengers.add(childPassenger);
        double price = calculator.calculatePrice(passengers, ADULT_TICKET_PRICE, CHILD_TICKER_PRICE);
	return price;
    }

    // Calculate the price for one family - 4 member
    // This case will have discount
    public static double calculatePriceForFamily() {
        List<Passenger> passengers = new ArrayList<>();
        Passenger adultPassenger1 = new Passenger(20);
        Passenger adultPassenger2 = new Passenger(20);
        Passenger childPassenger3 = new Passenger(12);
        Passenger childPassenger4 = new Passenger(4);
        passengers.add(adultPassenger1);
        passengers.add(adultPassenger2);
        passengers.add(childPassenger3);
        passengers.add(childPassenger4);
        double price = calculator.calculatePrice(passengers, ADULT_TICKET_PRICE, CHILD_TICKER_PRICE);
	return price;
    }
    // Calculate price for the child-narrow case 
    // Age = 18 -> Adult or child case
    public static double calculatePriceForChildNarrowCase() {
        List<Passenger> passengers = new ArrayList<>();
        Passenger childPassenger = new Passenger(18);
        passengers.add(childPassenger);
        double price = calculator.calculatePrice(passengers, ADULT_TICKET_PRICE, CHILD_TICKER_PRICE);
        return price;
    }
	
    // Calculate ticket for the free-ticket case
    // Age = 3 -> Eligible for free ticket or not ?
    public static double calculatePriceForFreeTicketNarrowCase() {
        List<Passenger> passengers = new ArrayList<>();
        Passenger childPassenger = new Passenger(3);
        passengers.add(childPassenger);
        double price = calculator.calculatePrice(passengers, ADULT_TICKET_PRICE, CHILD_TICKER_PRICE);
        return price;
    }
	
    // Test case for Family discount with adult
    public static double shouldNotCalculatePriceForFamilyEdgeCaseWithAdults() {
        List<Passenger> passengers = new ArrayList<>();
        Passenger adultPassenger1 = new Passenger(20);
        Passenger adultPassenger2 = new Passenger(20);
        Passenger childPassenger1 = new Passenger(12);
        passengers.add(adultPassenger1);
        passengers.add(adultPassenger2);
        passengers.add(childPassenger1);
        double price = calculator.calculatePrice(passengers, ADULT_TICKET_PRICE, CHILD_TICKER_PRICE);
        return price;
    }
    // Test case for family with children - Discount or not ?
    public static double shouldNotCalculatePriceForFamilyEdgeCaseWithChildren() {
        List<Passenger> passengers = new ArrayList<>();
        Passenger adultPassenger1 = new Passenger(20);
        Passenger childPassenger1 = new Passenger(12);
        Passenger childPassenger2 = new Passenger(12);
        passengers.add(adultPassenger1);
        passengers.add(childPassenger1);
        passengers.add(childPassenger2);
        double price = calculator.calculatePrice(passengers, ADULT_TICKET_PRICE, CHILD_TICKER_PRICE);
	return price;
    }

}



