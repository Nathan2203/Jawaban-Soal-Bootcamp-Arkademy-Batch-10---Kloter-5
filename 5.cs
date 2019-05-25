using System;

namespace ReplaceString
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine(ganti_kata("purwakarta", 'a', 'o'));
		}
		
		static string ganti_kata(string kata_awal, char pilih_huruf, char ganti_huruf)
  		{      	     
			string res = "";			
			int count = kata_awal.Length;
      		for (int i = 0; i < count; i++)
      		{
      			if (kata_awal[i] == pilih_huruf)
      			{
      				res += ganti_huruf;
      			}
      			else
      				res += kata_awal[i];
      		}
			
	        return res;
  		}  
	}
}
