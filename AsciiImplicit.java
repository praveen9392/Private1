class AsciiImplicit
{
 public static void main(String args[])
 {
   char  ch=' '; //it can hold one character 
 
     if (ch>='A' && ch<='z') 
     {
     System.out.println("Upper case");
     }
     else if (ch>='a' && ch<='z')
     {
      System.out.println("lower case");
     }
     else if (ch>='0' && ch<='9')
     { 
     System.out.println("number");
     }
     else
     {
      System.out.println("Symbols");
     }
   
 }
}
     