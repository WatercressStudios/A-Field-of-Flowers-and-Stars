
label scene_7:
    #ART - FOREST BG (NO SHIP)
    #VFX - BG Should be super zoomed in too. See end of this scene for clarity.
    ###

    scene sky with Dissolve(1.5)

    pause 0.5

    play env "Amb/forest.ogg" fadein 2.0


    scene forest with  Dissolve(1.5):
        anchor (0.5, 0.5) align (0.5, 0.5) zoom 0.75

    voice "voice/7-scene_7-1.ogg" #Raine (Nat)
    mc sighing "Lovely. I was sort of hoping I'd never see this neck of the woods again."
    voice "voice/7-scene_7-2.ogg" #Raine (Nat)
    mc "Why are we here again?"

    $ hide_sides = ['Leona']
    show le explaining at stage_right with dissolve
    voice "voice/7-scene_7-3.ogg" #Leona (Dot)
    le explaining "Remember the alien tech we found while bringing in your ship?"
    voice "voice/7-scene_7-4.ogg" #Leona (Dot)
    le "I was thinking the crash uncovered some supplies that got left behind by the previous inhabitants, but then we found all that crate inside the cave."
    voice "voice/7-scene_7-5.ogg" #Leona (Dot)
    le questioning a3 "Why is there stuff all the way out here when the cave base would suffice?"
    voice "voice/7-scene_7-6.ogg" #Leona (Dot)
    le "Think about it; a hidden base inside a cave, things buried underground-"
    voice "voice/7-scene_7-7.ogg" #Raine (Nat)
    mc questioning2 "Rooms full of bodies?"
    voice "voice/7-scene_7-8.ogg" #Leona (Dot)
    le concerned "Y-Yeah."
    voice "voice/7-scene_7-9.ogg" #Raine (Nat)
    mc "You might be onto something."
    voice "voice/7-scene_7-10.ogg" #Leona (Dot)
    le "What's more, why haven't we found anything out in the open?"
    voice "voice/7-scene_7-11.ogg" #Leona (Dot)
    le questioning a1 "Was this place really colonized at some point if there are no other structures?"
    voice "voice/7-scene_7-12.ogg" #Raine (Nat)
    mc "Assume it wasn't a populated planet then."
    voice "voice/7-scene_7-13.ogg" #Raine (Nat)
    mc questioning "What else would someone be doing here, living in a cave and hiding stuff underground so far away?"
    voice "voice/7-scene_7-14.ogg" #Leona (Dot)
    le explaining "I'm pretty sure whoever was here before us was a criminal, perhaps a smuggler."
    voice "voice/7-scene_7-15.ogg" #Raine (Nat)
    mc "That would make some sense, but it doesn't explain why there's stuff all the way out here."
    voice "voice/7-scene_7-16.ogg" #Leona (Dot)
    le "That's just it, isn't it?"
    voice "voice/7-scene_7-17.ogg" #Leona (Dot)
    le questioning a1 "We didn't find much of anything in the cave, except some old books."
    voice "voice/7-scene_7-18.ogg" #Leona (Dot)
    le "And it's not like we can read them anyway."
    voice "voice/7-scene_7-19.ogg" #Raine (Nat)
    mc satisfied "Actually, I might be able to help with that!"
    voice "voice/7-scene_7-20.ogg" #Leona (Dot)
    le happy a1 "You can? How?"
    voice "voice/7-scene_7-21.ogg" #Raine (Nat)
    mc "I can't actually speak your language, remember?"
    voice "voice/7-scene_7-22.ogg" #Leona (Dot)
    le happy a2 "Oooh, your translator! I didn't think about it, but that must be why you can use the mediapad I gave you."
    voice "voice/7-scene_7-23.ogg" #Raine (Nat)
    mc neutral "Yeah, works just as well for the written word. Gimme one of the books and I'll take a look-see."
    na "Leona quickly shuffles through the hoverbike's storage compartment, coming out with one of the dusty books we'd brought back with us."
    voice "voice/7-scene_7-24.ogg" #Leona (Dot)
    le concerned "Careful, it might fall apart if you're too rough with them."
    voice "voice/7-scene_7-25.ogg" #Raine (Nat)
    mc satisfied "If it can survive in a cave for a thousand years and then make it through your deathtrap of a bike in one piece, I doubt my delicate hands will be enough to leave a scratch."
    play sound "sfx/book.ogg"
    voice "voice/7-scene_7-26.ogg" #Raine (Nat)
    mc speaking "Looks like nothing but random squiggles."
    play sound "sfx/book.ogg"
    voice "voice/7-scene_7-27.ogg" #Raine (Nat)
    mc "More squiggles..."
    voice "voice/7-scene_7-28.ogg" #Raine (Nat)
    mc surprised "Squig- Wait! Here we go, finally kicking in!"
    voice "voice/7-scene_7-29.ogg" #Raine (Nat)
    mc questioning2 "Eh? Looks like a manifest of some sort."
    voice "voice/7-scene_7-30.ogg" #Raine (Nat)
    mc speaking "Food, water, all sorts of supplies and components like batteries and computer chips."
    voice "voice/7-scene_7-31.ogg" #Raine (Nat)
    mc "The whole thing is just that. Every page a different list. No names, just numbers."
    voice "voice/7-scene_7-32.ogg" #Raine (Nat)
    mc "Get me a different one."
    voice "voice/7-scene_7-33.ogg" #Leona (Dot)
    le questioning a2 "Here."
    voice "voice/7-scene_7-34.ogg" #Raine (Nat)
    mc questioning2 "...Nope. Just more manifests. Are they all like this?"
    na "One by one Leona brings out the other handful of books we'd brought with us."
    voice "voice/7-scene_7-35.ogg" #Raine (Nat)
    mc "It's just the same boring shit in all of 'em. They're useless!"
    voice "voice/7-scene_7-36.ogg" #Leona (Dot)
    le "But this lends credence to it being a smuggler, doesn't it?"
    voice "voice/7-scene_7-37.ogg" #Raine (Nat)
    mc "How do you figure that?"
    voice "voice/7-scene_7-38.ogg" #Leona (Dot)
    le sassyquestioning "Well, whoever these belonged to obviously didn't care about them."
    voice "voice/7-scene_7-39.ogg" #Leona (Dot)
    le "If they were real, they wouldn't have been left behind like that."
    voice "voice/7-scene_7-40.ogg" #Leona (Dot)
    le "Record keeping is an important part of trade, so leaving them there would be a really bad move for an employee and a nightmare for an employer."
    voice "voice/7-scene_7-41.ogg" #Leona (Dot)
    le "But if they were a smuggler, they could just cook up another set of books."
    voice "voice/7-scene_7-42.ogg" #Raine (Nat)
    mc unimpressed "Or they were intending to get rid of evidence of smuggling, thinking nobody would find it there."
    voice "voice/7-scene_7-43.ogg" #Leona (Dot)
    le questioning a2 "That leads me back to the stuff we found with your ship though."
    voice "voice/7-scene_7-44.ogg" #Leona (Dot)
    le "Why go through the trouble of building something so deep inside a cave, hiding evidence of smuggling there but not leaving the smuggled cargo with it?"
    voice "voice/7-scene_7-45.ogg" #Raine (Nat)
    mc "I think you're onto something. It doesn't quite make sense, does it?"
    play music "music/Smugglers and Bombs.ogg" fadein 2.0
    voice "voice/7-scene_7-46.ogg" #Raine (Nat)
    mc "Come to think of it, we found the cave because the power source inside shows up on sensors."
    voice "voice/7-scene_7-47.ogg" #Raine (Nat)
    mc "You might as well leave a giant arrow pointing straight to it."
    voice "voice/7-scene_7-48.ogg" #Leona (Dot)
    le questioning a3 "...Huh. That's a really good point."
    voice "voice/7-scene_7-49.ogg" #Raine (Nat)
    mc surprised "What if it's not a decoy, but a trap?"
    voice "voice/7-scene_7-50.ogg" #Leona (Dot)
    le surprised "A trap? Why would-"
    voice "voice/7-scene_7-51.ogg" #Raine (Nat)
    mc questioning2 "Leona, what about the bodies you found?"
    voice "voice/7-scene_7-52.ogg" #Raine (Nat)
    mc "A room full of corpses halfway through the cave. At the back of the cave there's a sealed room and a crate full of cargo manifests just sitting there for anyone to find."
    voice "voice/7-scene_7-53.ogg" #Raine (Nat)
    mc surprised "That entire cave had to have been a trap. Whoever those people were must have been killed before they could find these manifests!"
    voice "voice/7-scene_7-54.ogg" #Leona (Dot)
    le speakingsurprised a1 "W-Well, I don't know about-"
    voice "voice/7-scene_7-55.ogg" #Raine (Nat)
    mc neutral "We found them though!"
    voice "voice/7-scene_7-56.ogg" #Raine (Nat)
    mc "But then we couldn't get the door open right away, so we decided to come back with something to power the control panel."
    voice "voice/7-scene_7-57.ogg" #Leona (Dot)
    le "No, I-"
    voice "voice/7-scene_7-58.ogg" #Leona (Dot)
    le "Wait. What are you getting at?"
    voice "voice/7-scene_7-59.ogg" #Raine (Nat)
    mc questioning2 "What if the door is a trap set for whoever wanted to find the smuggled cargo?"
    voice "voice/7-scene_7-60.ogg" #Raine (Nat)
    mc "Let's consider that there isn't actually anything inside. The cargo they were looking for was actually all the way out here, buried in the middle of a forest."
    voice "voice/7-scene_7-61.ogg" #Raine (Nat)
    mc neutral "Think about it. A beacon to draw people in, trapped doors to kill off intruders and at the very back of the cave there's a pressurized room."
    voice "voice/7-scene_7-62.ogg" #Raine (Nat)
    mc questioning "Leona, what if it's a bomb?"
    voice "voice/7-scene_7-63.ogg" #Leona (Dot)
    le concerned "A bomb? I don't understand, how can a room be a bomb?"
    voice "voice/7-scene_7-64.ogg" #Raine (Nat)
    mc "I don't know. Maybe there's something inside set to go off as soon as..."
    voice "voice/7-scene_7-65.ogg" #Raine (Nat)
    mc "...as soon as..."
    voice "voice/7-scene_7-66.ogg" #Raine (Nat)
    mc questioning2 "...the pressure is released when the door opens."
    voice "voice/7-scene_7-67.ogg" #Leona (Dot)
    le questioning a3 "Raine, didn't that hole start making a whistling noise when you pulled that bolt out?"
    voice "voice/7-scene_7-68.ogg" #Raine (Nat)
    mc unimpressed "Crap."
    voice "voice/7-scene_7-69.ogg" #Leona (Dot)
    le speakingsurprised a1 "What do we do?!"
    voice "voice/7-scene_7-70.ogg" #Raine (Nat)
    mc "Absolutely nothing."
    voice "voice/7-scene_7-71.ogg" #Leona (Dot)
    le speakingsurprised a1 "What? No! A bomb is gonna go off!"
    voice "voice/7-scene_7-72.ogg" #Raine (Nat)
    mc yawn "Relax, it can't be that strong."
    voice "voice/7-scene_7-73.ogg" #Raine (Nat)
    mc "Why set up traps to kill people before they can even get to the door, if opening it is just going to kill everyone anyway?"
    voice "voice/7-scene_7-74.ogg" #Leona (Dot)
    le concerned "...Uh, R-Raine?"
    voice "voice/7-scene_7-75.ogg" #Raine (Nat)
    mc neutral "Yeah?"
    voice "voice/7-scene_7-76.ogg" #Leona (Dot)
    le "I have a bit of confession and you're not going to like it."
    voice "voice/7-scene_7-77.ogg" #Raine (Nat)
    mc questioning "Go on...?"
    voice "voice/7-scene_7-78.ogg" #Leona (Dot)
    le "Promise me you won't be mad?"
    voice "voice/7-scene_7-79.ogg" #Raine (Nat)
    mc annoyed "...That depends, Leona. What are you confessing to?"
    voice "voice/7-scene_7-80.ogg" #Leona (Dot)
    le "That room? With the bodies?"
    voice "voice/7-scene_7-81.ogg" #Leona (Dot)
    le "It uh... It didn't actually, sort of, have... any?"
    na "..."
    voice "voice/7-scene_7-82.ogg" #Raine (Nat)
    mc unimpressed "What?"
    voice "voice/7-scene_7-83.ogg" #Leona (Dot)
    le "I miiight have l-lied..."
    voice "voice/7-scene_7-84.ogg" #Raine (Nat)
    mc upset "Why would you- Wait, what was glowing then?"
    voice "voice/7-scene_7-85.ogg" #Leona (Dot)
    le speakingsurprised a1 "There was a room, but it didn't have any corpses inside."
    voice "voice/7-scene_7-86.ogg" #Raine (Nat)
    mc annoyed "Leona, what did you see?"
    voice "voice/7-scene_7-87.ogg" #Leona (Dot)
    le "It was this big, green glowy canister like thing sitting in the middle of the room with a bunch of wires coming out of it."
    voice "voice/7-scene_7-88.ogg" #Raine (Nat)
    mc "That could have been the power source we were looking for."
    voice "voice/7-scene_7-89.ogg" #Raine (Nat)
    mc unimpressed "But why would you...?"
    voice "voice/7-scene_7-90.ogg" #Raine (Nat)
    mc "Waaait a second. If there aren't any traps before the door at the back-"
    voice "voice/7-scene_7-91.ogg" #Raine (Nat)
    mc questioning "That means the bomb might not be as small as I thought."
    voice "voice/7-scene_7-92.ogg" #Leona (Dot)
    le concerned "How big do you think it could be?"
    voice "voice/7-scene_7-93.ogg" #Raine (Nat)
    mc unimpressed "I don't know. Big enough to blow away the entire cave, I imagine."
    voice "voice/7-scene_7-94.ogg" #Leona (Dot)
    le "Or anyone foolish enough to get close to it, looking for the smuggled cargo."
    voice "voice/7-scene_7-95.ogg" #Leona (Dot)
    le "Raine, those mountains have {i}tons{/i} of cave systems."
    voice "voice/7-scene_7-96.ogg" #Leona (Dot)
    le speakingsurprised a1 "A big enough explosion could cause them all to collapse at once!"
    voice "voice/7-scene_7-97.ogg" #Raine (Nat)
    stop music fadeout 2.0
    mc upset "Get on the horn, warn everyone to get away from those mountains!"
    play sound "sfx/Explosion.ogg"
    stop env fadeout 1.0
    play sound3 "amb/Explosion After.ogg" fadein 1.0
    show forest with vpunch
    na "Leona and I look to the horizon as we feel the ground shake beneath our feet, a burst of sound echoing through the air."
    na "And in the distance, visible through the treetops…"
    na "Was a large chunk of a mountain torn right from the earth."
    voice "voice/7-scene_7-98.ogg" #Raine (Nat)
    mc shocked armraised "Oh my god."
    #voice "voice/7-scene_7-99.ogg" #Leona (Dot)
    le surprised "{nw}"
    na "Leona stands there, stunned in place with a terrified look."
    voice "voice/7-scene_7-100.ogg" #Raine (Nat)
    mc unimpressed "Leona, the radio! Quick!"
    play sound4 "sfx/wind.ogg" fadein 1.0
    na "A gust of wind barrels through the forest, thrusting into my face as it batters the trees in its wake."
    voice "voice/7-scene_7-101.ogg" #Raine (Nat)
    mc annoyed "Aah!"
    hide le with moveoutright
    stop sound4 fadeout 3.0
    na "By the time the wind dies down, Leona rushes to the radio on her bike, sweat dripping from her face."
    $ hide_sides = []
    voice "voice/7-scene_7-102.ogg" #Leona (Dot)
    le frustrated a2 "This is Captain Leona broadcasting on all emergency channels!"
    voice "voice/7-scene_7-103.ogg" #Leona (Dot)
    le "I need reports from all units detailing locations and status on frequency 88.9, prioritizing vicinity to Southwest Mountain range!"
    na "One by one the reports roll in."
    na "Minor injuries, a number of scrapes and bruises."
    na "A single man knocked unconscious. Fortunately, everyone is still alive."
    na "Those closest to the explosion said it sounded like a storm was coming in before they saw rocks flying everywhere."
    na "The mountain just sort of caved in on itself, followed by a huge amount of smoke."
    na "Beyond that and what will eventually be a better view of the horizon, Aster only had minor damage from the shockwave."
    voice "voice/7-scene_7-104.ogg" #Leona (Dot)
    le concernedspeaking "I need people out there keeping an eye on it. I'll be making a stop in Aster then I'll be out to assess the situation."
    voice "voice/7-scene_7-105.ogg" #Leona (Dot)
    le "All other units report to base and await our return. Captain Leona signing off."
    stop sound3 fadeout 2.0
    play env "amb/forest.ogg" fadein 2.0
    na "Leona stands there a moment, staring into the radio."
    voice "voice/7-scene_7-106.ogg" #Raine (Nat)
    mc neutral "Can we talk about this?"

    $ hide_sides = ['Leona']
    show le crying2 at stage_right with easeinright

    voice "voice/7-scene_7-107.ogg" #Leona (Dot)
    le concerned "Um…"
    na "She opens her mouth to speak."
    na "But then turns her face away from me."
    na "..."
    play music "music/Trust In You.ogg" fadein 3.0
    voice "voice/7-scene_7-108.ogg" #Raine (Nat)
    mc "If you're not going to talk, then listen."
    voice "voice/7-scene_7-109.ogg" #Raine (Nat)
    mc "Everyone makes mistakes. There isn't a person in the universe who goes through life flawlessly."
    voice "voice/7-scene_7-110.ogg" #Leona (Dot)
    le concernedspeaking "...I'm sorry."
    voice "voice/7-scene_7-111.ogg" #Raine (Nat)
    mc upset "But you lied to me. I trusted you, and you lied to me."
    voice "voice/7-scene_7-112.ogg" #Leona (Dot)
    le "...I'm sorry…"
    voice "voice/7-scene_7-113.ogg" #Raine (Nat)
    mc unimpressed "I want to know why."
    na "Head still hung low, she turned her head to me, unable to look me in the eye."
    voice "voice/7-scene_7-114.ogg" #Raine (Nat)
    mc "Why?"
    voice "voice/7-scene_7-115.ogg" #Leona (Dot)
    le concerned "I-I was afraid."
    voice "voice/7-scene_7-116.ogg" #Leona (Dot)
    le "I only wanted to keep you safe."
    voice "voice/7-scene_7-117.ogg" #Leona (Dot)
    le "The room I found... I saw the power sources and got scared."
    voice "voice/7-scene_7-118.ogg" #Leona (Dot)
    le "For a moment I saw you back up in that tree."
    voice "voice/7-scene_7-119.ogg" #Leona (Dot)
    le "I thought about you being sucked into a wormhole and crashing into a planet."
    voice "voice/7-scene_7-120.ogg" #Leona (Dot)
    le "Not this one though. Not Fireside."
    voice "voice/7-scene_7-121.ogg" #Leona (Dot)
    le "Some random, lifeless rock somewhere a million miles away from any another person."
    voice "voice/7-scene_7-122.ogg" #Leona (Dot)
    le crying "I didn't..."
    na "She takes a step back into the bike, setting herself down on the seat."
    voice "voice/7-scene_7-123.ogg" #Leona (Dot)
    le "I don't want you to get hurt again."
    voice "voice/7-scene_7-124.ogg" #Raine (Nat)
    mc "Is that so?"
    voice "voice/7-scene_7-125.ogg" #Raine (Nat)
    mc annoyed "And the easiest way to do that is to keep me from leaving."
    voice "voice/7-scene_7-126.ogg" #Leona (Dot)
    le "I'm sorry! I was scared!"
    voice "voice/7-scene_7-127.ogg" #Raine (Nat)
    mc "That isn't your choice to make."
    voice "voice/7-scene_7-128.ogg" #Leona (Dot)
    le "But-"
    voice "voice/7-scene_7-129.ogg" #Raine (Nat)
    mc upset "That isn't your fucking choice to make!"
    voice "voice/7-scene_7-130.ogg" #Raine (Nat)
    mc "It's my life! I'm the one who decides what to do with it!"
    voice "voice/7-scene_7-131.ogg" #Raine (Nat)
    mc "If I wanted to spend my life huddled up in the corner of my room on some backwater planet I wouldn't be in fucking space to begin with!"
    voice "voice/7-scene_7-132.ogg" #Raine (Nat)
    mc "And I don't need your help if I can't trust you to understand that."
    voice "voice/7-scene_7-133.ogg" #Raine (Nat)
    mc unimpressed "Get the rocks."
    voice "voice/7-scene_7-134.ogg" #Leona (Dot)
    le speakingsurprised a1 "R-Raine, what are you-"
    voice "voice/7-scene_7-135.ogg" #Leona (Dot)
    mc "The ones I told you to hold on to. Right now."

    hide le with dissolve
    na "Looking more than a little sheepish, Leona fishes the rocks out of her bag."
    na "They're decently sized, a handful even. Much bigger than the pebbles around here."

    show forest:
        anchor (0.5, 0.5) align (0.0, 0.5)
        ease 2.0 zoom 1.2

    na "I grab one out of her hand, then point towards a big tree in the distance."
    voice "voice/7-scene_7-136.ogg" #Raine (Nat)
    mc "I want you to hit it."

    $ hide_sides = []

    voice "voice/7-scene_7-137.ogg" #Leona (Dot)
    le "Hit? Like, go up and-?"
    voice "voice/7-scene_7-138.ogg" #Raine (Nat)
    mc "No, I mean throw it. As hard as you can. Hit that tree."
    voice "voice/7-scene_7-139.ogg" #Leona (Dot)
    le concerned "I-I don't think I can-"
    voice "voice/7-scene_7-140.ogg" #Raine (Nat)
    mc annoyed "I don't care. Throw the rock."
    na "Still looking nervous, she reels back and lets it fly."
    na "The rock sails through the air, but barely makes it halfway to the tree."
    voice "voice/7-scene_7-141.ogg" #Leona (Dot)
    le "R-Raine, what is this about?"
    na "I don't give her an answer. I simply take aim and fire."
    play sound  "sfx/Stone.ogg"
    na "It sails straight like a bullet, and the bark explodes at the center of impact.."
    voice "voice/7-scene_7-142.ogg" #Leona (Dot)
    le speakingsurprised "Oh my god-!"
    voice "voice/7-scene_7-143.ogg" #Leona (Dot)
    le "What was that?!"
    voice "voice/7-scene_7-144.ogg" #Raine (Nat)
    mc satisfied "I could do that the whole time. I didn't figure it out until earlier today."
    voice "voice/7-scene_7-145.ogg" #Raine (Nat)
    mc "The gravity here is weaker than what my species is used to, so my body can handle more punishment than yours."
    voice "voice/7-scene_7-146.ogg" #Raine (Nat)
    mc "Stronger too, since my muscles are more dense."
    voice "voice/7-scene_7-147.ogg" #Raine (Nat)
    mc unimpressed "That reminds me. I have a gift for you."
    na "From my own bag I fetch the neatly wrapped box I'd prepared the night before as Leona slept."
    voice "voice/7-scene_7-148.ogg" #Raine (Nat)
    mc "Your present. As promised; A little \"thanks\" for all the help."
    voice "voice/7-scene_7-149.ogg" #Raine (Nat)
    mc neutral "It's a music player. Brought it with me from Lumin. You just hit the button in the middle when you want to start it."
    voice "voice/7-scene_7-150.ogg" #Raine (Nat)
    mc "I had Juneau translate the interface and attach lyrics to all the songs."
    voice "voice/7-scene_7-151.ogg" #Leona (Dot)
    le concernedspeaking "Raine..."
    voice "voice/7-scene_7-152.ogg" #Raine (Nat)
    mc unimpressed "But, as you know, I won't be needing any more help from now on."
    voice "voice/7-scene_7-153.ogg" #Raine (Nat)
    mc "I'll see you around, Leona."

    show forest:
        linear 40 zoom 3.0 align (0.8, 0.5)

    na "I turn away from her and start walking."
    #VFX - BG and Leona sprite zooms out a step with every following line until end of scene.
    #
    ###
    voice "voice/7-scene_7-154.ogg" #Leona (Dot)
    le "Raine?"
    na "Just walking."
    voice "voice/7-scene_7-155.ogg" #Leona (Dot)
    le concerned "R-Raine...?"
    na "Back to my ship."
    voice "voice/7-scene_7-156.ogg" #Leona (Dot)
    le crying "{b}Raine{/b}?!"
    na "Back to Aster."

    voice "voice/7-scene_7-157.ogg" #Leona (Dot)
    le crying2 "{b}Raaaine{/b}!"
    stop music fadeout 3.0
    stop env fadeout 2.0
    na "Back to a prison."

    scene black with Dissolve(2.0)
    jump scene_8



    #VFX - Quickly cut to black
    #Timing - add an extra couple seconds of nothing but black before next line
    #VFX - Journal entry added - 4
