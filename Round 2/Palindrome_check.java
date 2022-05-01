import java.util.*;

class Palindrome_check{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String s1 = new String();
        s1 = sc.nextLine();
        String s2 = "";
        for(int i=0; i<s1.length(); i++){
            s2 += s1.charAt(s1.length()-i-1);
        } 
        if(s1.equals(s2)){
            System.out.println("yes");
        }
        else{
            System.out.println("no");
        }
    }
}