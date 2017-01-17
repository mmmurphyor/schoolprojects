using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//overloading and overriding

namespace item23_1
{
   class Animal
   {
      public int NumLegs { get; set; } //all animals have legs, make noise(mostly), eat
      public string Sound { get; set; }
      public string Name { get; set; }
      public int choice = 0;

      public void Eat(string name)
      {
         //do something
      }

      class Dog : Animal
      {
         public string Breed { get; set; }
         public string Praise { get; set; }
         private string praise = "good dog!";
         private string food = "kibble";
         private string breed = "Pomeranian";
         //need constructors

         public void Tricks()//dog method
        
         {
            //do something
            Console.WriteLine(praise);
         }

      }

      class Bird : Animal
      {
         public string Type { get; set; }
         public string Movement { get; set; }
         private string movement = "flap flap";
         private string food = "seeds";
         private string type = "Parrot";
         //need constructors
         // only applies to birds(overloaded)

         private void Fly() //bird method
         {
            Console.WriteLine(movement);
         }

      }    
      
         static void Main(string[] args)
         {

         
         Dog Dog1 = new Dog();
         Bird Bird1 = new Bird();

         Console.WriteLine("A {0} is a type of dog, and has {1} legs, eats{2}, and can do tricks, {3}");
         Console.WriteLine("A {0} is a type of bird, has {1} legs, eats {2}, and flies, {3}.")
            //need to get the variables and method calls in here, then do an override example.
         }
}
}  