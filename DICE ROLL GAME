using System;
namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int playerRandomNum;//player 1
            int enemyRandomNum;//player 2
            int playerPoints = 0;
            int enemyPoints = 0;

            
            Random random = new Random();//to generate random number

            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine("press any key to roll the dice");
               Console.ReadKey();

                playerRandomNum=random.Next(1,7);  //to generate random number between upper and lower limit we use next
                Console.WriteLine("YOU ROLLED A " + playerRandomNum);
                
                Console.WriteLine("...");
                System.Threading.Thread.Sleep(1000); // makes thread wait for 1000 millisecond(making game intEresting)
                
                enemyRandomNum=random.Next(1,7);
                Console.WriteLine("Enemy Ai rolled a " + enemyRandomNum);

                if (playerRandomNum > enemyRandomNum)
                {
                    playerPoints++;
                    Console.WriteLine("Player wins this round!");

                }

                else if(playerRandomNum< enemyRandomNum)
                {
                    enemyPoints++;
                    Console.WriteLine("Enemy wins the round");

                }
                else
                {
                    Console.WriteLine("Draw");
                }
                Console.WriteLine("the score is now - player:" +playerPoints + " enemy:"  +enemyPoints + ".");
                Console.WriteLine();
                }
            if(playerPoints> enemyPoints)
            {
                Console.WriteLine("You win!");
            }
            else if(playerPoints < enemyPoints)
            {
                Console.WriteLine("you loose ");

            }
            else
            {
                Console.WriteLine("It'a draw");
            }
            Console.ReadKey();

            }
    }
}
