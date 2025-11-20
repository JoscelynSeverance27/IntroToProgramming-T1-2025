#This is for the first choice in the game. It's also the start of the story vv
#Game is very inspired by Secrets of Mana, Omori, OneShot, Bad End Theatre and more
#even though there is more than one death sequence, I'll be sure to add at least 5 endings other than death
#Sorry if it sucks, I literally went from 440 lines of code or so to 200 because i didn't like the branching...
def start_game():
    print("The chilly autumn winds gently blow your hair as you skip and hop along the cobblestone road. As most 5 year olds, you don't have much to worry about. Most of the things you need are given to you, in return for only your basic manners and spirit. However, you are unfortunate enough to not have parents. The village, naturally, protect you on their own, letting you run around and stay where you please. They even let you take what you want from them. On this breezy day, you find a lavender scarf. When you pick it up, a pit opens underneath you, amd you fall into a completely different world from the sky. Do you:")
    print("A: Aim for the lake")
    print("B: Aim for the boat")
    print("C: Aim for the stone island")
    print("D: Scream")
    
    answer1 = input("> ")

    if answer1.lower == "a":
         lake_fall()
    if answer1.lower == "b":
         boat_fall()
    if answer1.lower == "c":
         stone_island()
    if answer1.lower == "d": 
         scream_fall()
    else: 
         print("Please type a valid response...")
         start_game()



#These are the first branchings in the game vv

def lake_fall():
    print("You land straight into the lake, but the water tension is near nothing, for when you land, it doesn't hurt. You sink under the water and see the glowing fish under you, some even brushing against you. Someone dives in after you and grabs you, pulling you on their boat.")
    print('"Hey, kid! Are you okay?!" The person gasps, slightly worried for your wellbeing as they lift you up and hold you above water. The person has a large sword sheathed on their back, and their hair is a long dark purple. They look weary amd old in spirit, yet still young enough to be considered a father figure for children, and they look oddly familiar. Do you:')
    print("A: Ask where you are")
    print("B: Introduce yourself")
    print("C: Cry")
    print("D: Ask who they are")

    answer2 = input("> ")

    if answer2.lower == "a":
         where_hero()
    if answer2.lower == "b":
         intro_hero()
    if answer2.lower == "c":
         cry1()
    if answer2.lower == "d": 
         ask_heroident()
    if answer2.lower == "restart": 
         start_game()
    if answer2.lower == "undo last choice": 
         start_game()
    else:
         print("Please type a valid response...")
         lake_fall()


#this is for falling in the boat
def boat_fall():
     print("You fall and land in the boat, hitting your head on one of the seats. The person in the boat looks at you in sheer surprise, and keeps looking back up at the voided sky where you fell.")
     print('"Holy hell, a whole CHILD this time?!" they exclaim. They sigh, humming a simple lullaby while sitting you up and tending to you. The glowing fish linger under the boat and some try to nudge them while pink fireflies swarm and fly around them like fairies, but the stranger ignore them, bust tending to you first')
     print('"Can ya see okay, kid? You look kinda familiar..." What do you say?:')
     print('A: "Yeah..."')
     print('B: "Where am I...')
     print('C: "Ow...')

     ans3 = input("> ")

     if ans3 == "A" or "a":
          see_okay()
     if ans3 == "B" or "b":
          where_hero()
     if ans3 == "C" or "c":
          ouch_head()
     if ans3.lower == "dest?":
          secret_ending()
     if ans3.lower == "restart": 
         start_game()
     if ans3.lower == "undo last choice": 
         start_game()
     else:
          print("Please type a valid response...")
          boat_fall()

#This one is for falling on the island (DEATH 1)
def stone_island():
     print("THE STORY ENDS HERE: You land painfully on the rocks and sand. Tough fall! Your vision is blurry and your blood coats the sea glass path your head landed on. The person in the boat sees you and rushes to you, but it all fades out before they reach you. (BAD ENDING 1: ROCKY DOWNSIDES)")
     print("Retry or Restart?")

     da1 = input("> ")

     if da1.lower == "restart": 
         start_game()
     if da1.lower == "retry": 
         start_game()
     else:
          print("Please type restart or retry...")
          stone_island()

#This one is for screaming and falling
def scream_fall():
     print("You scream as you fall, hoping someone hears you. The person in the boat below unsheathes their sword and runs out of the boat. A strange magic surrounds them, allowing them to run on the water and jump up high enough to catch you. Their sword opens to a parachute as they grab you, and they bring you to the boat.")
     print('"Okay, I got you. You sit tight, little fella. I can take you to my humble abode." Do you:')
     print("A: Go with them")
     print("B: Resist")
     print("C: Ask")
     print("D: Talk")

     ans4 = input("> ")

     if ans4.lower == "a":
          hero_home()
     if ans4.lower == "b":
          fight_hero()
     if ans4.lower == "c":
          where_hero()
     if ans4.lower == "d":
          talk_hero()
     if ans4 == "restart" or "undo last choice": 
         start_game()
     else:
          print("Please type a valid response...")
          scream_fall()

#This one is for asking where you are
def where_hero():
     print('"Oh, what do you mean, kid? You asking where you are or where you gonna go?" The person asks patiently.')
     print('A: "Where are we...?"')
     print('B: "Where are we headed...?"')
     
     a5 = input("> ")

     if a5.lower == "a":
          where_now()
     if a5.lower == "b":
          where_later()
     if a5.lower == "restart": 
         start_game()
     else:
          print("Please type a valid response...")
          where_hero()

#This is for introducing yourself
def intro_hero():
     print("Of course, being an orphan with a whole village caring for you, not everyone calls you the same name. You simply say you're a 5 year old orphan, and that was all the person needed to suddenly shift from worried to almost sad. After a long minute of silence, they sit towards you.")
     print('"Hey, kid...This is gonna sound like a weird question...but do I know you?" they ask quietly. What do you say?:')
     print('A: No, sorry...')
     print('B: What do you mean..?')

     a5 = input("> ")

     if a5.lower == "a":
          cont_intro()
     if a5.lower == "b":
          cont_intro()
     if a5.lower == "dest?" or "dest":
          secret_ending()
     if a5.lower == "restart": 
         start_game()
     if a5.lower == "undo last choice": 
         lake_fall()
     else:
          print("Please type a valid response...")
          intro_hero()

#this one is for crying
def cry1():
     print("The stranger flinches a bit and looks around at the fireflies and fish, as if looking for advice. He then turns to you")
     print('"Hey kid, something wrong? Am I scaring you at all? I promise I aint scary..."') 
     print('The stranger hugs you and pats your back, letting you cry on them. After a while, he takes out a small sweet treat')
     print('"I can try to get you back home, but you should take a break first..." Do you')
     print("A: Calm down")
     print("B: Cry")

     a6 = input("> ")
     if a6.lower == "a":
          hero_home()
     if a6.lower == "b":
          cry2()
     if a6.lower == "restart": 
         start_game()
     if a6.lower == "undo last choice": 
         lake_fall()
     else:
          print("Please type a valid response...")
          cry1()

#this one is for asking who they are
def ask_heroident():
     print('"Me? Oh, uh..."')
     print("The stranger seems to be thinking, looking away from you and sighing a heavy sigh") 
     print('"Well, no ones ever been around to ask me that in a long minute, kid...For now, er..."')
     print("They try to remember something, but give up easily")
     print('"Just call me Stranger. Just like how I call ya kid. Deal?')
     print('A: "Deal"')
     print('B: "Stranger..?"')

     a7 = input("> ")

     if a7.lower == "a":
          deals()
     if a7.lower == "b":
          alt_deal()
     if a7.lower == "restart": 
         start_game()
     if a7.lower == "undo last choice": 
         lake_fall()
     else:
          print("Please type a valid response...")
          ask_heroident()

#this one is for seeing alright
def see_okay():
     print("You nod, but your head still hurts. The person seems slightly relieved, but not quite reassured. They look at your face and cup it, trying to see if you're lying")
     print('"Well, if you say so...Even if I aint no doctor, I can tell when enough is enough. Stay still..."')
     print("The stranger bandages your head carefully, not wanting to make you cry. They mess up your hair and laugh")
     print('"At least you made it. Never thought a kid like you would end up here like me..." The stranger tilts his head a bit at you, wondering something. They speak up..')
     print('"Say...How DID you end up here...?" What do you say:')
     print("A: (explain what happened)")
     print('B: "Long story..."')

     a8 = input("> ")

     if a8.lower == "a":
          explain()
     if a8.lower == "b":
          long_story()
     if a8.lower == "restart": 
         start_game()
     if a8.lower == "retry": 
         boat_fall()
     else:
          print("Please type a valid response...")
          see_okay()

#this one is for not being able to see well (ow!!)
def ouch_head():
     print('"Shucks, kid...You aint looking too hot..."')
     print("The stranger helps you the best they can, but your head still hurts. You fall asleep on the boat for a few hours and wake up in the same boat, though it's tied to the dock and the stranger is gone. Your head doesn't hurt anymore, but now you're alone. Do you:")
     print("A: Look for the stranger (leave boat)")
     print("B: Wait in the boat")
     print("C: Call out for the stranger")

     a9 = input("> ")

     if a9.lower == "a":
          leave_boat()
     if a9.lower == "b":
          wait_boat()
     if a9.lower == "c":
          call_losthero()
     if a9.lower == "undo last choice":
          boat_fall()
     if a9.lower() == "restart":
          start_game()
     else:
          print("Please type a valid response...")
          ouch_head()

#this one is for the secret ending...ooooooooo
def secret_ending():
     print("The person's arms go to their sides, and they look at you in shock, then grabs your hands carefully and shake you a bit")
     print('"Kid, where did you get that name..?! Are you...no..."')
     print("Dest hugs you tightly and hugs you, crying. You live with them in this mystical land where they had stayed alone for so long. The both of you live happily ever after together and keep each other company until the end of time. (SECRET ENDING: REUNION!!)")
     print("Reset?")

     se = input("> ")

     if se.lower == "yes" or "reset":
          start_game()
     if se.lower == "no":
          print("fine")
          secret_ending()
     if se.lower == "that's all?":
          print("yeah, but a happy ending is a happy ending, isn't it? if you want more you can ask me another time")
          secret_ending()
     else:
          ("Please type a valid response...")
          secret_ending()

#this is for Dest's house
def hero_home():
     print("The stranger sails you to the dock, walking on the path slow enough so you wouldn't fall behind. There's a cozy, apple-red house at the highest hill of the stone island, and a little crystal chimney. The windows are large peices of sea glass, and the wood seems to be from the forest nearby. The house is nicely decorated and clean, like no one stays there often. It smells like candy and baked goods.")
     print('"Welp, this is my place. Feel free to stay as long as you want. It aint like this place is gonna get an easy exit anytime soon, anyway..." The stranger sighs. It looks as if they hate being in their own house, like the house itself is a burden. They help you take off your coat and shoes. Do you:')
     print("A: Give them the scarf")
     print("B: Go to the living room")
     print("C: Follow them")
     print("D: Go to the kitchen")

     a10 = input("> ")

     if a10.lower == "a":
          scarf_return()
     if a10.lower == "b":
          living_room()
     if a10.lower == "c": 
          hero_room()
     if a10.lower == "d":
          kitchen()
     if a10.lower == "restart":
          start_game()
     else:
          print("Please type a valid response...")
          hero_home()

#this one is for resisting Dest
def fight_hero():
     print('"Aw, kid..." The stranger sighs "Ya have nothing to be afraid of here. Course, I appreciate whoever takes care of you for teaching you not to trust strangers, but there aint anything to do to you"')
     print("They don't pester you anymore, but they look at you deeply with worry")
     print('"Just helping is all. Only ones here is me and you, so there aint another folk to help you but me" Do you:')
     print("A: Comply")
     print("B: Physically fight them")
     print("C: Jump off the boat")
     print("D: Sit in silence")

     a20 = input("> ")

     if a20.lower == "a":
          hero_home()
     if a20.lower == "b": 
          kill_dest()
     if a20.lower == "c":
          drowned()
     if a20.lower == "d":
          awkward_silence()
     if a20 == "restart":
          start_game()
     else:
          print("Please type a valid response...")
          fight_hero()

#this one is for talking with Dest when he saves you the first time (will there be another time? idk)
def talk_hero():
     print('"Mister? How did you do that?" You find yourself asking. The stranger laughs a bit at the question, like theyve heard it a million times.')
     print('"Honestly, it aint me, kid. I guess you could say I still have a little magic in me after all..."')
     print("You feel safe around them. Suddenly, they ask")
     print('"Kid, you should stay with me for now. Just until I can get you back where you belong..." Do you:')
     print("A: Go with him")
     print("B: Don't go")

     a21 = input("> ")

     if a21.lower == "a":
          hero_home()
     if a21.lower == "b":
          fight_hero()
     if a21.lower == "restart":
          start_game()
     if a21.lower == "undo last choice":
          scream_fall()
     else:
          print("Please type a valid response...")
          talk_hero()

#this is for asking where you are
def where_now():
     print("When you tell them, they look around at the voided sky")
     print('"Honestly, I couldnt lie to you, kid. We may never know where this place is. For now, just call it the Graveyard of Heros. All the ancient text calls it that anyway. Sometimes things fall down here by accident, but a whole kid like you? What heroic act did you do, little guy? Did something happen?" Do you:')
     print("A: Tell")
     print("B: Don't tell")

     a = input("> ")

     if a.lower == "a":
          explain()
     if a.lower == "b":
          awkward_silence()
     if a.lower == "undo last choice":
          where_hero()
     if a.lower == "reset":
          start_game()
     else:
          print("Please type a valid response...")
          where_now()

#this is for asking where you're going
def where_later():
     print('"On route to my house, kid. Little red one on the tall hill up there, see?" They point to the cozy, apple-red house on the tallest hill of the stone island. "Not much, but better than nothing.."')
     hero_home()

#this is for intro pt2
def cont_intro():
     print('"Sorry, you just look so much like..." The stranger stops and looks out at the black horizon sadly "It aint anything important, kid. Just an old memory is all"')
     hero_home()

#this is for crying again 
def cry2():
     print('"Oh boy.." The stranger stresses out slightly, picking you up and putting you on their lat as they sit down. The pink fireflies land on the boat around you and watch, some picking at the stranger. They ignore the bugs. "Something got you all sad, little guy? Youre alright..."')
     print("Later on, they carry you to their house and lay you in a twin sized bed. The room is meant for a child about your age. You fall asleep. When you wake up again, the sky is a bright white with a black sun. The stranger is reading an old book with no cover on it, It's a red color similar to the house, but lighter. Do you:")
     print("A: Look at him")
     print("B: Go back to sleep")
     print("C: Nudge them") 

     a23 = input("> ")

     if a23.lower == "a":
          wake_up()
     if a23.lower == "b":
          sleep_more()
     if a23.lower == "c":
          wake_hero()
     if a23.lower == "undo last choice":
          cry1()
     if a23.lower == "reset":
          start_game()
     else:
          print("Please type a valid response...")
          cry2()

#this is for making a deal with Dest
def deals():
     print('"Thanks, kid. You seem pretty easy to reason with, aint ya kid?" They laugh and pet your head. "Kid, seems your village is gonna miss a little one like you. I can get you to my place and we can help you there. Sound good?" What do you say?:')
     print("A: Yes")
     print("B: No")

     a24 = input("> ")

     if a24.lower == "a":
          hero_home()
     if a24.lower == "b":
          fight_hero()
     if a24.lower == "restart": 
         start_game()
     if a24.lower == "undo last choice": 
         ask_heroident()
     else:
          print("Please type a valid response...")
          deals()

#This one is for the alternative
def alt_deal():
     print('"Yeah, like that. Bit weird, I know, but itll do..." The stranger sees drops of glass drip from the dark sky."Come now, the storm aint gonna wait for you out here!"')
     hero_home()

#This one is for explaining everything
def explain(): 
     print("When you explain your story, you expect the stranger to look at you like you kicked a puppy, but they just sit and listen, avoiding eye contact as you tell the events of picking up a scarf.")
     print('"Must be one of em cursed items or something. Happens mostly to stuff it falls on, which might explain that pit forming." The stranger says dryly in reply. "Sounds like quite the adventure for a little guy like you!" The stranger gives you a sweet treat. "Thanks for telling me kid, youre awfully familiar, but I can tell we were meant to meet."')
     hero_home()

#This one is for the story explaining altrernative
def long_story():
     print('"Um...Its a long story, Stranger...How did YOU end up here?" you ask. The person is surprised by the question, then recalls the events')
     print('It wasnt a very pleasant journey, thats for sure. One of em sad tales that makes the ladies cry for a week, or at least my wife anyway." They say, the last part slipping out by accident. They get embarrassed. "WELL I MEAN-! It aint all that sad or anything, nothing that bad..." The stranger sighs "Oh well, so ya heard it. We didnt do all that much that wasnt PG..."')
     print('They dust themself off and sit down. "Maybe if I like you enough, I can tell you the full of it..."')
     hero_home()

#this one is for leaving the boat 
def leave_boat():
     print("In hopes of finding the stranger, or even a way out, you leave the boat. The closest thing to the dock is the Crimson Woods. You know because you see a sign that says so. When you go in, you hear lots of strange sounds that aren't there. You hear hospital sounds and sirens despite there being nothing, and the sound of crying when no one is there. You eventually find the stranger laying on the ground unconscious. They do not get up when you talk to them. They only wake up when you poke them. They look up at you and cry.")
     print('"Hey, kid..."')
     print("The person stands up and holds your hand, escorting you out of the forest, and hiding something in their pocket. They dont make eye contact with you nor talk on the way out of the woods")
     print('A: "Is something wrong?"')
     print('B: "Why are you crying?"')
     print('C: "Its okay...')
     print('D: "..."')

     a25 = input("> ")

     if a25.lower == "a":
          silent_walk()
     if a25.lower == "b":
          silent_walk()
     if a25.lower == "c":
          comfort_hero1()
     if a25.lower == "d":
          silent_walk()
     if a25.lower == "restart": 
         start_game()
     if a25.lower == "undo last choice": 
         ouch_head()
     else:
          print("Please type a valid response...")
          leave_boat()

#This one is for waiting in the boat
def wait_boat():
     print("You wait in the boat until your head hurts again. You sit for countless hours, but they don't show up. After falling asleep and waking up again for the 10th time, the stranger comes back to the boat heavily wounded. They give you some medicine they made")
     print('"Here kid, this is gonna help your head feel better..." When you take it, what they say is true, and you feel better. The person, after you look at them and smile, smiles back tiredly')
     print('"Feeling better? Come on now, get up..."')
     print("The stranger helps you into their house, and lays you on a twin sized bed. When you say you aren't tired, they get you some coloring books and a set of crayons. After a while, you notice the stranger leaving the house. Do you:")
     print("A: Go with them")
     print("B: Stay at the house")
 

     a26 = input("> ")

     if a26.lower == "a":
          journey_start1()
     if a26.lower == "b":
          patient_ending()
     if a26.lower == "restart": 
         start_game()
     if a26.lower == "undo last choice": 
         ouch_head()
     else:
          print("Please type a valid response...")
          wait_boat()

#This one is for calling out to Dest from the boat (death2)
def call_losthero():
     print("THE STORY ENDS HERE: At first, only silence greets you. Then, you hear something rushing out of the forest. A large orange snake speeds out of the forest, the size of a train. It sees you and kills you, then relaxes when it's quiet again. (BAD ENDING 2: SNAKE AWAKENING)")
     print("Retry or Reset?")

     da2 = input("> ")

     if da2.lower == "restart": 
         start_game()
     if da2.lower == "retry": 
         ouch_head()
     else:
          print("Please type restart or retry...")
          call_losthero()

#This one is for returning the scarf
def scarf_return():
     print("The stranger looks at the scarf in recognition, then gently takes it from you")
     print('"Where did you get this..? Is it how you got here...?" They ask, barely able to contain their surprise')
     print("When you nod, the person holds your hand and takes you to a room similar to the ones the people in the village set up for you. The stranger sits on the chair and stares at the scarf in slight exasperation and disbelief")
     print('"Well, that explains how ya got here to begin with..." The stranger sighs and pats your head "Cheeky little bastard...')
     print("While you color on the coloring books in the room, you see the hero leaving the house. Do you:")
     print("A: Go with them")
     print("B: Stay at the house")

     a27 = input("> ")

     if a27.lower == "a":
          journey_start1()
     if a27.lower == "b":
          patient_ending() 
     if a27.lower == "restart": 
         start_game()
     if a27.lower == "undo last choice": 
         hero_home()
     else:
          print("Please type a valid response...")
          scarf_return()

#this one is for going to the living room
def living_room():
     print("The furniture is very soft and new, like it's unused. Dust flies up when you jump on it, and you can't help but cough and wave away the ashy cloud. The stranger winces with embarrassment.")
     print('"Sorry, I aint really around this room much. No point in a living room that aint lively anyway...Make yourself as comfortable as possible, kid. Ill be in the kitchen getting you a snack." The stranger leaves you alone. Do you:')
     print("A: Sleep")
     print("B: Go outside (The stranger will follow)")

     a28 = input("> ")


     if a28.lower == "a":
          sleep_living()
     if a28.lower == "b":
          journey_start1
     if a28.lower == "restart": 
         start_game()
     if a28.lower == "undo last choice": 
         hero_home()
     else:
          print("Please type a valid response...")
          scarf_return()

#This one is for Dest's room
def hero_room():
     print("You climb up the stranger's bed and jump on it. The bounce it gives you is so high you almost hit the ceiling. The stranger catches you and laughs")
     print('"Hey, that was dangerous!" They hold you up by your underarms "Are you tryna scare me now? I hope not!" They toss you back gently on the bed and you go back to bouncing. The stranger sits down at the overflowing desk and watches you quietly, a slight sadness shining in their expression.')
     print('"You really are somethin, huh kid? I didnt think anything could make me remember back before I was here. This void was just my life, but clearly my repression aint working much anymore..."')
     print("A: Ask them about them")
     print("B: Take him outside")
     a29 = input("> ")

     if a29.lower == "a":
          wake_hero()
     if a29.lower == "b":
          journey_start1()
     if a29.lower == "restart": 
         start_game()
     if a29.lower == "undo last choice": 
         hero_home()
     else:
          print("Please type a valid response...")
          hero_room()

#This one is for going to the kitchen
def kitchen():
     print("In the kitchen, the sink and counter is clean, and all the dishes are in the cabinets. Cups made of cut sea glass and stone are stacked in another cabinet. You notice some of the dishes are meant for children, and some knives are rounded so much it isn't sharp anymore. There's child safety on the cabinets and the sharp corners. The stranger gets you a small chair and seats you at a little table. After a snack, you fall asleep and wake up in a twin sized bed. The room is decorated nicely and fits you well. The stranger is gone. Do you:")
     print("A: Look for the stranger")
     print("B: Call out for the stranger")
     print("C: Wait for their return")

     a30 = input("> ")

     if a30.lower == "a":
          empty_house()
     if a30.lower == "b":
          empty_house()
     if a30.lower == "c":
          patient_ending()
     if a30.lower == "restart": 
         start_game()
     if a30.lower == "undo last choice": 
         hero_home()
     else:
          print("Please type a valid response...")
          kitchen()

#This one is for killing dest (great, i hate this)
def kill_dest():
     print("THE STORY ENDS HERE: As anybody would be, The stranger was very surprised by your reaction. They step back a bit and try to stop you carefully")
     print('"Woah! Kid!" You fight them as hard as you can, but the stranger doesnt fight back.')
     print("You climb on their back and tug at them. Suddenly, the sword, unsheathing, flies up as you pull at them. The stranger out of reflex, grabs you and holds you down, protecting you from the sword. The sword ultimately cuts through and stabs the stranger's lower back, piercing their gut from the back. The stranger lets go of you and falls dead on the boat")
     print("Eventually, the boat goes to the dock on its own, and you find his house. It rains heavily from the black sky, and you're left alone with what remains of the stranger (NEUTRAL ENDING 1: MURDER IN THE GRAVES)")
     print("Retry or Reset?")

     ne1 = input("> ")

     if ne1.lower == "restart": 
         start_game()
     if ne1.lower == "retry": 
         fight_hero()
     else:
          print("Please type restart or retry...")
          kill_dest()

#This one is for drowning
def drowned():
     print("You jump off the boat. Why? No one knows but you. The stranger goes in the water to try and save you, but soon you can't see their sillouete anymore. The glowing fish around you become less appealing and the world fades around you. (DEATH ENDING 3: DARK ABYSS)")
     print("Retry or Reset?")

     da3 = input("> ")

     if da3.lower == "restart": 
         start_game()
     if da3.lower == "retry": 
         fight_hero()
     else:
          print("Please type restart or retry...")
          drowned()

#This one is for an awkward silence
def awkward_silence():
     print("The stranger stares at you blankly, expecting an answer. As a period of time passes, They sit back and sight, looking back at you occasionally.")
     print('Kid, its boutta storm soon. You want to go or not?" They ask, but their words just make it more embarrassing to say anything. After a while, they choose to just take you home anyway')
     hero_home()

#This one is for looking at Dest whe you wake up
def wake_up():
     print("You notice how restless they seem, like the people on TV back in the nursing home that try and solve mysteries. They don't notice you looking at them until they accidentally make eye contact with you. They jump up a bit.")
     print('"Gracious, kid!! How long were ya staring at me for? Was it at least not hours?" The stranger acts carefully around you "Feeling better at all? I gotta take you home, so you better be okay..."')
     journey_start1()

#this one is for sleeping again after crying
def sleep_more():
     print("When you wake up again, the person is asleep, the book on the nightstand. They're sleeping on the chair and likely won't wake up for a while unless you wake them. Do you:")
     print("A: Wake them up")
     print("B: Look at the book")
     print("C: Get up and go elsewhere")

     a32 = input("> ")

     if a32.lower == "a":
          wake_hero()
     if a32.lower == "b":
          dest_book()
     if a32.lower == "c":
          stopped_dest()
     if a32.lower == "restart": 
         start_game()
     if a32.lower == "undo last choice": 
         cry2()
     else:
          print("Please type a valid response...")
          sleep_more()

#this one is for dest not talking back from the forest
def silent_walk(): 
     print("They don't speak to you, and it doesn't seem like they want to talk to you either. They follow you out of the forest and take you hime. They open the door for you and let you rest, but something seems different from before. They feel cold and distant. Hours later, they come back to you")
     print('"Kid..." They barely start talking before losing track of what they want to say. "Sometimes life aint fair. you get that, dontcha? Ever miss anyone?"')
     print("A: Parents")
     print("B: Friends")
     print("C: Village")

     a30 = input("> ")

     if a30.lower == "a":
          dest_mourn()
     if a30.lower == "b":
          dest_mourn()
     if a30.lower == "c":
          dest_mourn()
     if a30.lower == "restart": 
         start_game()
     if a30.lower == "undo last choice": 
          leave_boat()
     else:
          print("Please type a valid response...")
          silent_walk()

#this one is for comforting dest
def comfort_hero1():
     print("The stranger looks down at you and cries")
     print('"Maybe it is, but I get tired too..."')
     print("After a while, they take you to their house.")
     dest_mourn()

def dest_mourn():
     print('"I just miss a special someone is all. I guess two someones, but its complicated..." They sigh. "See, I was up on that world too. The mortal world is a thin eggshell when you see it from down here. Used to be a simple townsperson. Made clothes in my freetime, and did anything you could think of. I even had a wife, you know.."')
     print('Their voice shakes a bit at the word. Had is a powerless word. "I lost her. I was fending off the monsters from entering the village. I died then...and there was nothing she could do."')
     print('"You remind me of our kid, you know. We adopted a little guy about your age when it all happened. Here, how bout we go now? It may not be much, but it can get ya home"')
     journey_start1()

def journey_start1():
     print("After hours or walking, you both reach a temple. Inside is a long staircase with different floors. You both go in together.")
     print('"Nothing can hurt you with me here by your side, okay kid?"')
     print("You hear screaming, but the stranger holds your hand tighter.")
     print('"Ignore those. Those are just..."')
     print("As the stranger talks, you both hear a loud scream")
     print('"DEST!!!"')
     print('The stranger goes pale and holds you closer. "Those aint real, its okay..." They murmur to themself. You see a woman holding something you cannot recognize. The stranger freezes and watches the scene. Stay with them?')
     print("A: Yes")
     print("B: No")

     at = input("> ")

     if at.lower == "a":
          destamy()
     if at.lower == "b":
          return_alone()
     if at.lower == "restart": 
         start_game()
     else:
          print("Please type a valid response...")
          journey_start1()

def patient_ending():
     print("THE STORY ENDS HERE: You wait for hours. Then days. Then weeks. Surely, they'll come back, right? They'll return? You wait forever, never seeing the stranger again... (NEUTRAL ENDING 2: PATIENCE IS A VIRTUE)")
     print("Retry or Restart?")
     ne2 = input("> ")

     if ne2.lower == "restart": 
         start_game()
     if ne2.lower == "retry": 
         wait_boat()
     else:
          print("Please type restart or retry...")
          patient_ending()

def sleep_living():
     print("You dream of life on the surface, but in an older light than you remember. Blurry faces of your parents playing with you, and how much you miss them. You wake up to the stranger waking you up")
     print('"Kid, I havent been honest with ya...I know how to leave, it just...I dont got enough courage to go...Heard ya mumblin in your sleep about home and I may as well take ya..')
     print("They pick you up with one arm and take you outside")
     journey_start1()

def empty_house():
     print("THE STORY ENDS HERE: Despite your efforts, the stranger is gone. You look for any sigh of them, but it's like they were never there. You stay alone forever (NEUTRAL ENDING 3: A BLUNT LOSS)")
     print("Retry or Restart?")
     ne3 = input("> ")

     if ne3.lower == "restart": 
         start_game()
     if ne3.lower == "retry": 
         kitchen()
     else:
          print("Please type restart or retry...")
          empty_house()

def dest_book():
     print('"Entry 1093: I was thinking on my boat again when a whole KID fell from the sky. I guess I couldnt wallow in loneliness forever. Something about this kid is familiar to me. Ever since I died so long ago, I feel like I aint in my own head again. Please dont make me remember..."')
     print("The stranger wakes up and sees you.")
     print('"Hey, why are ya going though my stuff? Theres adult talks in there!" They take it from you and set it on a shelf "I guess I cant keep ya here forever, come on...')
     journey_start1()

def stopped_dest():
     ('"Where ya goin, kid...?" They ask suddenly. "Didnt think you could be louder when you got up..."')
     print("A: Home")
     print("B: Don't know")

     a30 = input("> ")

     if a30.lower == "a":
          journey_trig()
     if a30.lower == "b":
          journey_trig()
     if a30.lower == "restart": 
         start_game()
     if a30.lower == "undo last choice": 
          sleep_more()
     else:
          print("Please type a valid response...")
          silent_walk()

def wake_hero():
     print("The hero jerks in surprise and looks at you tiredly")
     print('"Jeez, kid...Let a stranger sleep..." They smile a bit "You want something?" When you say you want to go home, they sigh "Okay...fine, we can go...."')
     journey_start1()

def return_alone():
     print("You go home alone. The village claims you fell asleep wandering off into the woods, and they celebrate your return. Everything is back to normal, but you still remember the stranger deep down. (MAIN ENDING 1: DREAM OF THE DEEP)")
     print("Retry or Restart?")

     ma1 = input("> ")

     if ma1.lower == "retry": 
          journey_start1()
     if ma1.lower == "restart":
          start_game()
     else:
          print("Please type a valid response...")
          return_alone()
def journey_trig():
     print('"You wanna go home...huh..? The stranger sighs "Alright, kid...Since I love ya too much, I can take ya home..."')
     journey_start1()

def destamy():
     print("The stranger sighs")
     print('"Amy...." They whisper "Kid, you see her too? That aint right....You shouldnt be able to, unless..."')
     print("The stranger is stunned, then they look at you")
     print('"You were there...Does that mean...You...')
     print("The stranger points at you, then themself")
     print('"That means youre MY kid..." they say. When they hear it come out their mouth, they slap their mouth shut in surprise "Jeez, time really has passed, huh...?')
     print('"They take your hand and continue walking down the hallway. Sounds of war play all around you, but they cover your eyes "Dont look, kid. I got ya..."')
     print("You make it to the surface. At first, the village people are scared of the stranger, then they see you. The stranger steps forward")
     print('"I remember my name...You people may call me Dest..."')
     print('They rest their hand on your shoulder "And this is my kid...We named you Ori..."')
     print("They take you somewhere in the forest")
     true_ending()

def true_ending():
     print("THE STORY ENDS HERE: Dest shows you the old windmill in the forest, which was their old home. They protect you and teach you everything they know, from how to protect yourself to stories of back then. The protector's statue in the forest breaks, and a woman emerges from the petrified stone. The woman is the same one from the long hallway out. That woman is Dest's wife, Amy, and the three of you live together. Years later, when Dest dies, you bury him with the scarf around their tombstone, and the story lives on in your bloodline. (TRUE ENDING: DESTINY OF TIME)")
     print("Retry or Restart?")

     te = input("> ")

     if te.lower == "retry": 
          journey_start1()
     if te.lower == "restart":
          start_game()
     else:
          print("Please type a valid response...")
          destamy()