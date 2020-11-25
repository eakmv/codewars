public class Kata
{
  public static int FindShort(string s)
  {
      string[] words = s.Split(' ');
      int lowestLenth = int.MaxValue;
      foreach(var item in words)
        {
            if (item.Length < lowestLenth)
            {
                lowestLenth = item.Length;
            }
        }
      return lowestLenth;
  }
}