class fibo
{
 public static void main(String args[])
 {
  int a=0,b=1,n=10,c;
  int i=1;
  while(i<=n)
  { 
   System.out.println(a+" ");
   c=a+b;    
   a=b;      
   b=c;     
   i++;     
  }

}
}
    
 