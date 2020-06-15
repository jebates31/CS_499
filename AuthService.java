import java.io.File;
import java.util.Scanner;

public class AuthService {

    private final String adminMessageLoc = "Admin.txt";
    private final String zookeeperMessageLoc = "Zookeeper.txt";
    private final String veterinarianMessageLoc = "veterinarian.txt";

    private String adminMessage = "";
    private String zookeeperMessage = "";
    private String veterinarianMessage = "";

    private Scanner authScanner =null;

    public AuthService() {
        try {

            //admin
            authScanner = new Scanner(new File(adminMessageLoc));
            adminMessage = System.lineSeparator();
            if (authScanner != null) {
                while (authScanner.hasNextLine()) {
                    adminMessage =  adminMessage + authScanner.nextLine() + System.lineSeparator();
                }
            }

            //zookeeper
            authScanner = new Scanner(new File(zookeeperMessageLoc));
            zookeeperMessage = System.lineSeparator();
            if (authScanner != null) {
                while (authScanner.hasNextLine()) {
                    zookeeperMessage =  zookeeperMessage + authScanner.nextLine() + System.lineSeparator();
                }
            }

            //veterinarian1
            authScanner = new Scanner(new File(veterinarianMessageLoc));
            veterinarianMessage = System.lineSeparator();
            if (authScanner != null) {
                while (authScanner.hasNextLine()) {
                    veterinarianMessage =   veterinarianMessage + authScanner.nextLine() + System.lineSeparator();
                }
            }

        } catch (Exception ex) {
            System.out.println(ex.toString());
        }
    }

    public String authorizedInfo(String autherized) {

        String  authMessage = "";
        switch (autherized) {
            case "admin":  authMessage = adminMessage;
                break;
            case "zookeeper":  authMessage = zookeeperMessage;
                break;
            case "veterinarian":  authMessage = veterinarianMessage;
                break;
            default: authMessage = null;
                break;
        }

        return authMessage;

    }
}
