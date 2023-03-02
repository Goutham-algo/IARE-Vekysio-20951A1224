import java.util.Scanner;
public class ReverseStringExample1   
{  
public String reverseString(String str)
{  
if(str.isEmpty())  
{  
return str;  
}   
else   
{  
return reverseString(str.substring(1))+str.charAt(0);  
}  
}  
public static void main(String[] args)   
{  
ReverseStringExample1 rs = new ReverseStringExample1(); 
Scanner sc = new Scanner(System.in);
String obj = sc.nextLine();
String resultantSting1 = rs.reverseString(obj);  
System.out.println(resultantSting1);    
}  
}
