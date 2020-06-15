import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.io.FileNotFoundException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class SecurityService {

    public static void AuthorizedInfo (String roll)

    {

        Scanner autherizersRoll = null;

        try

        {

            // define the scanner object pointing to the text

            autherizersRoll = new Scanner(new File(roll.trim() + ".txt"));

            System.out.println();

            // loop until end of the file

            while (autherizersRoll.hasNextLine());

            {



                System.out.println(autherizersRoll.nextLine());

            }

            System.out.println();


        } catch (FileNotFoundException ex)

                {




                }



    }



    public static String CredentialsValid (String userName, String password)
    {

        String md5ConvertedPassWord = MD5Digest.md5HashCode(password);


        Scanner fileReader;

        // boolean
        String AutherizationRecord = "";


        try {

            // define the scanner class object to point to the Credentials.txt

            fileReader = new Scanner(new File("Credentials.txt"));

            // loop until the last line of the file
            while (fileReader.hasNextLine()) {
            AutherizationRecord = fileReader.nextLine();


                // get the record information into AutherizationRecord

                //AutherizationRecord = fileReader.nextLine();

                // split the data
                //String credentialsCols[] = AutherizationRecord.split("([^\"]\\S*|\".+?\")\\s*");
                //String splitter = "^\\S+\\s+\\S+\\s+([\"].+[\"])\\s+\\S+$";
                //String splitter = "\\s+";
                //String credentialsCols[] = AutherizationRecord.split(splitter);

                //List<String> list = new ArrayList<String>();
                List<String> credentialsCols = new ArrayList<String>();
                String splitter = "([^\"]\\S*|\".+?\")\\s*";
                Matcher m = Pattern.compile(splitter).matcher(AutherizationRecord);
                String userNameFromFile = "";
                String passNameFromFile = "";
                while (m.find()) {
                    credentialsCols.add(m.group(1));
                }

                // check whether the userName(parameter) and the value in
                userNameFromFile = credentialsCols.get(0).trim();
                if (userNameFromFile.equals(userName)) {
                    // if valid, then check for the md5ConvertedPassWord with
                    passNameFromFile =credentialsCols.get(1).trim();
                    if (passNameFromFile.equals(md5ConvertedPassWord)) {
                        // if valid, call the method
                        // displayAuthorizedInformation()
                        //loop
                        String credText = credentialsCols.get(3);
                        return credText;
                    }
                }
            }

            // close the file
            fileReader.close();

        } catch (FileNotFoundException e) {
        }

        // return null value
        return null;

    }

    public static String authorizedInfo(String autherized) {




        String authMessage = "";
        switch (autherized) {
            case "admin":  authMessage = "January";
                break;
            case "zookeeper":  authMessage = "February";
                break;
            case "veterinarian":  authMessage = "February";
                break;
            default: authMessage = "Not found";
                break;
        }

        return authMessage;

    }
}
