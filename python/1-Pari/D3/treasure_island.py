print('''
                   e$$$      .c.
                 4$$$$     ^$$$$$.
                 $$$$        $$$$$.
                .$$$$         $$$$$
             z$$$$$$$$       $$$$$$b
            $$$$$$""          *$$$$$$.
            $$$$$                $$$$$r
   \        $$$*     dc    ..    '$$$$b
   4       $$$F      $F    $%     $$$$$       4
   'r     4$$$L  .e$$$$$$$$$$bc    $$$$r      $
    $.    '$$$$z$$$$$$$$$$$$$$$$$..$$$$$     z$
    $$$c   $$$$$$$$$$$$$$$$$$$$$$$$$$$$F  .d$$*
      "$$$. $$$$$$$$$$$$$$$$$$$$$$$$$$P z$$$"
         "$$b$$$$$$$$$$$$$$$$$$$$$$$$$d$$*
            "$$$$$$$$$$$$$$$$$$$$$$$$$P"
^         .d$$$$$$$$$$$$$$$$$$$$$$$$"
 "e   .e$$$$*"$$$$$$$$$$$$$$$$$$$$$$$$$$e..  e"
  *$$$$P"     ^$$$$$$$$$$$$$$$$$$$$P ""**$$$$
   *"          $$$$$$$$$$$$$$$$$$$P
             .$$"*$$$$$$$$$$$$P**$$e
            z$P   J$$$$$$$$$$$e.  "$$c     .
           d$" .$$$$$$*""""*$$$$$F  "$$. .P
    ^%e.  $$   4$$$"          ^$$     "$$"
     "*$*     "$b           $$"       ^
                  $r          $
                   ".        $
                    ^


''')

print("welcome to Treasure island. \nYour mission is find the treasure.")
user_ans = input("left or right")
if user_ans == 'left':
    user_swim_wait = input("swim or wait")
    if user_swim_wait == "wait":
        door_choose = input("which door? blue, red or yellow")
        if door_choose == "red":
            print("Burned by fire\nGame over")
        elif door_choose == "blue":
            print("Eaten by beast\nGame over")
        elif door_choose == "yellow":
            print("You win!!!")
        else:
            print("Game over")
    else:
        print("Attack by Trout.\n Game over")
else:
    print("Fall into a ho,e.\n Game over")

# TODo check for typing lower case and space delete extra
