import random
def main():
    """Guess the periodic table elemen."""
    print("*********************************************")
    print("Hello welcome to our amazing game")
    print("Guess the periodic table elemen!")
    print("1.Oxygen")
    print("2.Hydrogen")
    print("3.Cobalt")
    print("4.Nickle")
    print("5.Gold")
    print("6.Palladium")
    print("7.Iron")
    print("8.Magnesium")
    print("9.Calcium")
    print("10.Titanium")
    print("(Use Capital letter for the first letter)")
    y = ["Titanium","Hydrogen","Calcium","Iron","Oxygen","Palladium","Nickle","Magnesium","Gold","Cobalt"]
    x = random.choice(y)
       
    guess = None
    while x != guess:
         guess =str(input("Pick a element: "))
         print("--------------------------------------------------------------")
         
         if x == guess:
             print("You won..Great Job!")
         elif x!=guess:
             print("Unfortunately!!! You got it wrong.")
             
             if x=="Titanium":
                 print("The chemical element of atomic number 22, a hard silver-grey metal of the transition series, used in strong, light, corrosion-resistant alloys.")
             elif x=="Hydrogen":
                 print("A colourless, odourless, highly flammable gas, the chemical element of atomic number")
             elif x=="Calcium":
                 print("The chemical element of atomic number 20, a soft grey metal.")
             elif x=="Cobalt":
                 print("The chemical element of atomic number 27, a hard silvery-white magnetic metal.")
             elif x=="Palladium":
                 print("The chemical element of atomic number 46, a rare silvery-white metal resembling platinum.")
             elif x=="Iron":
                 print("Mineral that the body needs for growth and development")
             elif x=="Nickel":
                 print("A silvery-white metal, the chemical element of atomic number 28.")
             elif x=="Gold":
                 print("It is a member of the coinage metals.")
             elif x=="Oxygen":
                 print("Used for breathing gas")
             elif x=="Magnesium":
                 print("It is used to make strong lightweight alloys, and is also used in flash bulbs and pyrotechnics.")
            
             

                  
main()