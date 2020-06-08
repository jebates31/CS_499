
/**
 *
 * @author Jared
 */

import java.util.Scanner;


public class FinalProject2 {

    public static void main(String args[]) {
        // variables

        Scanner uInput = null;
        int numAttempts = 0;
        String userName;
        String password;
        AuthService authService = new AuthService();

        boolean logout = false;

        // loop until it is true
        while (true) {

            logout = false;

            // user Input Scanner
            uInput = new Scanner(System.in);

            // Prompt for Username
            System.out.print("Enter user name: ");
            //store Username
            userName = uInput.nextLine();
            //userName = "bruce.grizzlybear";  //admin
            //userName = "griffin.keyes";      //zookeeper
            //userName = "bernie.gorilla";     //veterinarian

            //Prompt Password
            System.out.print("Enter password: ");
            // store password
            password = uInput.nextLine();
            //password = "letmein";
            //password = "alphabet soup";
            //password = "secret password";

            // set up autherrized users
            String autherized = null;

            autherized = SecurityService.CredentialsValid(userName, password);

            // Loop for autherized users
            if (autherized != null && autherized.length() > 0) {

                //logout loop
                while (true) {
                    System.out.println(System.lineSeparator());
                    System.out.println(authService.authorizedInfo(autherized));

                    //prompt the user for logout
                    System.out.print("Enter \"LogOut\" to logout: ");

                    String choice = uInput.nextLine();

                    if (choice.equalsIgnoreCase("LogOut")) {

                        // if so, successfully logout the system
                        System.out.println("\nSuccessfully logged out...");

                        numAttempts = 0;

                        logout = true;

                        break;

                    }

                    System.out.println();

                }

            } else {

                // Increses number of attems
                numAttempts++;

                // When Number of attmpts = 3 exit
                if (numAttempts == 3) {

                    System.out.println("You have reached the maximum number of attempts!");
                    System.out.println("Exiting the System");

                    break;

                } // otherwise, display the information about the invalid
                // credentials
                else {

                    System.out.println("Invalid User Name or Password!");

                    System.out.println("You only have " + (3 - numAttempts) + " attempts left to login.");

                }

            }

            String proceed = null;

            if (logout) {

                System.out.println("Would you like to exit the application? Press y: ");

                proceed = uInput.nextLine();

                if (proceed.equalsIgnoreCase("y")) ;
                {
                }

                System.out.println("Successfully exiting the application...");

                break;
            }

        }

        System.out.println();

    }
        
    
        

}

     
