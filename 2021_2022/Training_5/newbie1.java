public class Rotate
{
	public static void main(String[] args)
	{
		String s = args[0];
		for(int i = 0; i < s.length(); i++)
		{
			char c = s.charAt(i);
			if	(c >= ' ' && c <= 'P') c += 47;
			else if	(c >= 'O' && c <= '~') c -= 47;
			
			System.out.print(c);
		}
		System.out.println();
	}
}

//5@??Fr%uL;FDE0Cb250D_FC4bDN
//
