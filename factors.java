class factors
{
    public static void main(String args[]) 
    {
        int a = 12;
        int i = 1;

        while (i <= a)
        {
            if (a%i == 0) 
	    {
                System.out.println(i);
            }
            i++;
        }
    }
}