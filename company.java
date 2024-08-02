class company
{
 public static void main(String args[])
 {
    int year=2020,age=18;
    if(age>=18)                           //checks if age is greater than are equal to 18 
    {
      if(year<=2020)                      //check year of graduation 
      {
          System.out.println("Eligible for drive");
          if(age>50)                     //check age senior citizen or not
          {
           System.out.println("Senior Citizen");
          }
          else                          //optional statements in  nested if 
          {
          System.out.println("Not a Senior Citizen");
          }
      }
     else
     {
       System.out.println("year of pass not matched ");
     }
   }
   else
   {
    System.out.println("under age ");
   }
}
}

