import java.utils.Scanner;
public class ReverseStringExample1   
{  
//recursive function to reverse a string      
public String reverseString(String str)  
{  
//checks if the string is empty   
if(str.isEmpty())  
{  
System.out.println("String is empty.")  
//if the above condition is true returns the same string      
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
