import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.File;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class java_regex{
    public static void main(String[]args){
        String file = "../../files/results.csv";
        Pattern pattern = Pattern.compile("^2018\\-.*[zk].*");

        try {
            BufferedReader br = new BufferedReader(new FileReader(file));
            String line;
            while((line=br.readLine())!=null){
                Matcher matcher = pattern.matcher(line);
                if(matcher.find()){
                    System.out.println(line);
                }
            }
        } catch (Exception e) {
            System.out.println(e);
        }finally{
            System.out.println("--FINISHED--");
        }
    }
}
