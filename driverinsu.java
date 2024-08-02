class driverinsu
{
 public static void main(String args[])
 {
  int age=32;
  String driver="Married", gender="male",insurance="yes";
  if(driver=="Married")
  {
   System.out.println("Insurance is appplicable");
  }
  else if(driver=="Unmarried" && gender=="male" && age>30)   
  {
   System.out.println("Insurance is appplicable");
  }
  else if(driver=="Unmarried" && gender=="female" && age>25)
  {
   System.out.println("Insurance is appplicable");
  }
  else
  {
    System.out.println("Insurance is  Not appplicable");
  }
}
}