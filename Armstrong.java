class Armstrong
{
 public static void main(String args[])
 {
  int num=153,rem,count=0,b=num,sum=0,d=b;
  while(num>0)
  {
   rem = num%10;
   count++;
   num=num/10;
  }
  while(b>0)
  {
   rem=b%10;
   int pow =(int)Math.pow(rem,count);
   sum=sum+pow;
   b=b/10;
  }
  if(d==sum)
  {
   System.out.print("Armstrong");
  }
  else
  {
   System.out.print("not");
  }
}
}