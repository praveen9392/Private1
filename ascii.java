class ascii
{
 public static void main(String args[])
 {
  int  A=20; 
 
     if (A>=60 && A<=90) 
     {
     System.out.println("Upper case");
     }
     else if (A>=97 && A<=122)
     {
      System.out.println("lower case");
     }
     else if (A>=48 && A<=57)
     { 
     System.out.println("number");
     }
     else
     {
      System.out.println("Symbols");
     }
   
 }
}
     