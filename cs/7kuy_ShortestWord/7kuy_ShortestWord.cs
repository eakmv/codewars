using System;
using System.Text.RegularExpressions;

public class Kata
{
    static public void Main()
    {
        int size = Regexp("https://v1810devsfp6b2ca5deed6a5b3a7devaos.cloudax.dynamics.com/?cmp=USMF&mi=DefaultDashboard");
        Console.WriteLine(size);
    }

    public static int Regexp(string s)
  {
      string pattern = @"(\w)*devaos.cloudax.dynamics.com/";
      if (Regex.IsMatch(s, pattern, RegexOptions.IgnoreCase))
        return 1;
      else
        return 0;
  }
}