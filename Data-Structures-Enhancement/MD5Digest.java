

import java.security.MessageDigest;

public class MD5Digest

{

     public static String md5HashCode(String input)

     {

          StringBuilder sb = new StringBuilder();

          MessageDigest md;

          try

          {

              md = MessageDigest.getInstance("MD5");

              md.update(input.getBytes());

              byte[] digest = md.digest();

              for (byte b : digest)

              {

                   sb.append(String.format("%02x", b & 0xff));

              }            

          } catch (Exception e) {
              System.out.println(e.getMessage());
          }

         return sb.toString();
         //return "0d107d09f5bbe40cade3de5c71e9e9b7";//bruce.grizzlybear
         //return "108de81c31bf9c622f76876b74e9285f";//griffin.keyes
         //return "a584efafa8f9ea7fe5cf18442f32b07b";//bernie.gorilla
     }

}