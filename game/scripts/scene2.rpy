label scene_2:

    #birds chirping SFX
    scene white with dissolve
    pause 1.0
    scene black with vpunch
    pause 2.0

    voice "voice/2-scene_2-1.ogg" #Raine (Nat)
    mc ugh "Ugh..."
    na "What the hell happened?"
    scene spaceship_crashed with wipeup:
        yzoom -1
    #iris open
    #show BG_outdoors_upside_down
    play env "Amb/Outdoors.ogg" fadein 2.0

    na "I feel a sharp pulsing in my head. And sharp pins in my feet."
    na "And the world is upside down..."
    na "...no wait, that's me. Right. I'm stuck in a tree."
    na "Ugh, something hurts."
    na "No, actually, everything hurts."
    na "Juneau must have ejected me right before I blacked out."
    show spaceship_crashed:
        ease 0.5 yoffset -20
        ease 0.5 yoffset 0
    na "I try to move my arms. If I can just reach the buckle..."
    play sound "sfx/tree2.ogg"
    show spaceship_crashed:
        ease 0.5 yoffset -20
        ease 0.5 yoffset 0
    na "..."
    na "Damn."
    na "At least I can wiggle around, so I won't be bored as I slowly die of exposure."
    na "Could be worse, though."
    na "Alright, Raine. Gotta get out of this somehow."
    na "If I can wiggle around, maybe a line will fray and drop me out of the tree..."
    na "...headfirst. Onto the ground. Thirty feet down."
    voice "voice/2-scene_2-2.ogg" #Raine (Nat)
    mc onfire "Well, this blows."
    ###
    # SFX - SOUND OF A MOTORCYCLE APPROACHING THEN STOPPING A LITTLE WAYS AWAY
    # SFX - FOOTSTEPS BEGIN AFTER 3 SECONDS, VERY FAINT BUT GRADUALLY GETTING LOUDER OVER THE COURSE OF ANOTHER 5 SECONDS. FOLLOWED BY ANOTHER PAUSE FOR A SECOND BEFORE LEONA SPEAKS
    ###
    play sound "sfx/footsteps.ogg"
    pause 3.0
    #pause for ten or so seconds
    $ hide_sides = ["Leona"]
    voice "voice/2-scene_2-3.ogg" #Leona (Dot)
    le "Eo'ahola! I'akiam eo'ahap?!?"
    #iris open, fast
    #show BG_outdoors_upside_down
    na "I strain against the ropes and try to turn my head."
    na "The rush makes it hard to find the source of the sound."
    na "There's someone at the base of the tree, I think. A girl?"
    show cgTree with dissolve:
        zoom 1.1
    voice "voice/2-scene_2-4.ogg" #Leona (Dot)
    le "Ahola? U'ai ehol ek u'ai ikih?"
    voice "voice/2-scene_2-5.ogg" #Raine (Nat)
    mc shyspeak "Hey! You!"
    play sound "sfx/tree2.ogg"
    show cgTree:
        ease 0.5 yoffset -20
        ease 0.5 yoffset 0
    voice "voice/2-scene_2-6.ogg" #Raine (Nat)
    mc upset "H-Help!"

    voice "voice/2-scene_2-7.ogg" #Leona (Dot)
    le "Olal i ohi e u'ai eo' ea' e, a'ap e!"
    scene spaceship_crashed with Dissolve(2.0):
        yzoom -1.0
        zoom 1.2
        yalign 1.0

    na "The girl climbs up the tree with surprising speed. Within seconds she's out of sight. Behind me?"

    voice "voice/2-scene_2-8.ogg" #Leona (Dot)
    le "Ulo'ulo' e, uamo'oh e!"

    na "Is she cutting me down?"
    #cable tearing SFX
    play sound "sfx/tree.ogg"
    na "The ropes begin to give..."
    show spaceship_crashed:
        easein 0.6 yalign 0.0
    voice "voice/2-scene_2-9.ogg" #Raine (Nat)
    mc "W-Woah!"
    voice "voice/2-scene_2-10.ogg" #Leona (Dot)
    le @ catching "Ohaw i ānān!"
    na "The girl leaps up from the branch as I fall and catches me in her arms."
    na "We seem to float down rather than plummet."
    na "Or maybe the adrenaline is slowing my perception of time?"
    play sound "sfx/falling.ogg"
    scene spaceship_crashed with vpunch
    pause 0.5
    voice "voice/2-scene_2-11.ogg" #Raine (Nat)
    mc blech "AuUuoghhh..."
    na "I'm gonna go with the latter. If I wasn't sore before, I am now."

    voice "voice/2-scene_2-12.ogg" #Raine (Nat)
    mc thankful "Thanks. Thought I was done for..."

    show le concerned with dissolve:
        stage_right

    voice "voice/2-scene_2-13.ogg" #Leona (Dot)
    le "Ikah iwi uam eh? Anomom eli?"
    na "A thought occurs to me; This girl isn't speaking anything resembling English."
    na "Did my translation chip break during the crash?"
    na "My head definitely feels like it got banged on something."

    voice "voice/2-scene_2-14.ogg" #Leona (Dot)
    le " Uo said iwi aum okay?"
    na "It seems like it's starting to work though."

    voice "voice/2-scene_2-15.ogg" #Raine (Nat)
    mc thankful "S-Sorry, can you say that again?"

    voice "voice/2-scene_2-16.ogg" #Leona (Dot)
    le hmm "Did you break anything? No broken bones, right?"
    play music "music/meeting leona.ogg" fadein 2.0
    na "I check myself over. Nothing broken, but I've got a nasty scrape on my leg and it feels like I was put through a wood chipper."

    voice "voice/2-scene_2-17.ogg" #Raine (Nat)
    mc @ yawn "I'm okay. Mostly."
    na "At least the ship is close. Hopefully there's still a usable medpack in there."

    voice "voice/2-scene_2-18.ogg" #Leona (Dot)
    le awk "Good! I'm glad you're okay."

    voice "voice/2-scene_2-19.ogg" #Raine (Nat)
    mc questioning "I didn't realize there were other Humans on this planet. What sector am I in?"

    voice "voice/2-scene_2-20.ogg" #Leona (Dot)
    le thinky "'Sector'? 'Human'? What are those?" with bounce

    voice "voice/2-scene_2-21.ogg" #Raine (Nat)
    mc surprised "Uh..."

    voice "voice/2-scene_2-22.ogg" #Raine (Nat)
    mc shocked armraised "Ah! Y-You're..."

    voice "voice/2-scene_2-23.ogg" #Leona (Dot)
    le questioning a1 "Hm?"
    na "There's a pair of horns on this girl's head. Honest-to-goodness horns, like you'd see on a goat or a ram."

    voice "voice/2-scene_2-24.ogg" #Raine (Nat)
    mc "H-Horns..."

    voice "voice/2-scene_2-25.ogg" #Leona (Dot)
    le concerned "Oh? Oh!"
    voice "voice/2-scene_2-26.ogg" #Leona (Dot)
    le "You don't have any horns?"

    na "The girl thinks for a moment."

    voice "voice/2-scene_2-27.ogg" #Leona (Dot)
    le speakingthink "You're... an alien?"

    voice "voice/2-scene_2-28.ogg" #Raine (Nat)
    mc amused "No, I'm --"

    na "Wait, yeah. She's right. I'm technically the alien here."

    voice "voice/2-scene_2-29.ogg" #Raine (Nat)
    mc "Yeah. I'm Raine. A human from a planet called Lumin. Ever heard of it?"

    voice "voice/2-scene_2-30.ogg" #Leona (Dot)
    le surprised "That's not a planet I've heard of... Is it close?"

    voice "voice/2-scene_2-31.ogg" #Raine (Nat)
    mc speaking "I don't really know. My ship has all the info, but it's uh, not exactly in good shape right now."

    voice "voice/2-scene_2-32.ogg" #Leona (Dot)
    le happy a2 "Well whatever, it's nice to meet you. I'm Leona!"

    voice "voice/2-scene_2-33.ogg" #Leona (Dot)
    le concerned "You're injured, so we should get you to the city and patch you up."

    voice "voice/2-scene_2-34.ogg" #Raine (Nat)
    mc "City? Where are we anyway?"

    voice "voice/2-scene_2-35.ogg" #Leona (Dot)
    le explaining "Hmm? A forest just south of Aster."

    voice "voice/2-scene_2-36.ogg" #Leona (Dot)
    le happy a1 "You picked a pretty bad spot to land, I won't sugar coat it."

    voice "voice/2-scene_2-37.ogg" #Raine (Nat)
    mc surprised "No, I mean WHERE are we?"

    voice "voice/2-scene_2-38.ogg" #Leona (Dot)
    le explaining "Oh, right, planet. You're on Fireside."

    voice "voice/2-scene_2-39.ogg" #Raine (Nat)
    mc speaking "Fireside? Strange name for a rock."

    voice "voice/2-scene_2-40.ogg" #Leona (Dot)
    le happy a2 "Really? Seems normal to me, but then again, I live here."

    voice "voice/2-scene_2-41.ogg" #Leona (Dot)
    le "We call ourselves Dawnese. We're from Dawne, a few light years away from here. This is our first colony world."

    voice "voice/2-scene_2-42.ogg" #Leona (Dot)
    le speaking a2 "I gotta say, I was more than a little surprised to see a ship come down here."

    voice "voice/2-scene_2-43.ogg" #Leona (Dot)
    le speaking a1 "We don't know how to make space ships that small yet."

    voice "voice/2-scene_2-44.ogg" #Leona (Dot)
    le explaining "I thought it was just a shooting star at first, but I saw something else trailing behind it."

    voice "voice/2-scene_2-45.ogg" #Leona (Dot)
    le happy a2 "I came to have a peek and look what I found! An honest-to-goodness alien!"

    voice "voice/2-scene_2-46.ogg" #Leona (Dot)
    le speakingthink "Though, I've never seen an alien look so much like me before..."

    voice "voice/2-scene_2-47.ogg" #Raine (Nat)
    mc questioning "Likewise, actually."

    voice "voice/2-scene_2-48.ogg" #Leona (Dot)
    le happy a2 "Well, let's get you somewhere safe. We should really make sure you're okay too."

    scene sky with dissolve

    na "Leona walks us over to her ride, a primitive hoverbike with room for two."

    stop env fadeout 2.0

    na "After a relatively short ride, the trees begin to thin and the terrain flows into a wide open plain, where the first sign of civilization on this planet comes into view."

    $ hide_sides = []
    voice "voice/2-scene_2-49.ogg" #Raine (Nat)
    mc speaking "What's that tower?"
    voice "voice/2-scene_2-50.ogg" #Leona (Dot)
    le happy a2 "That's the ark ship that brought us here! We're still dependent on it for it's atmosphere processors and power systems."
    voice "voice/2-scene_2-51.ogg" #Raine (Nat)
    mc "Ark ship? Didn't you say your homeworld was only a few lightyears from here?"
    voice "voice/2-scene_2-52.ogg" #Leona (Dot)
    le "Yeah. Like I said, we're not that advanced yet."
    voice "voice/2-scene_2-53.ogg" #Leona (Dot)
    le happy a1 "I was born here, but there are people still alive here in Aster who came here from Dawne originally."

    na "As we ride towards the ship, a cluster of small buildings come into view at the base of the tower."

    scene street onlayer master with dissolve:
        subpixel True xpos 0.56 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None

    $ hide_sides = ['Leona']

    show le happy a1 at stage_right with dissolve
    play env "amb/City Day.ogg" fadein 5.0
    voice "voice/2-scene_2-54.ogg" #Leona (Dot)
    le happy a2 "We're here! Welcome to the city of Aster!"
    show street:
        ease 15 xpos 1.0

    hide le with dissolve
    $ hide_sides = []


    na "Leona disembarks, helping me down from the bike."

    voice "voice/2-scene_2-55.ogg" #Leona (Dot)
    le happy a2 "Whaddya think?"

    na "If I didn't know any better, I'd say the town felt almost human in design."

    voice "voice/2-scene_2-56.ogg" #Raine (Nat)
    mc shocked armraised "Wow, you've built quite a little settlement here."

    voice "voice/2-scene_2-57.ogg" #Leona (Dot)
    le speaking a2 "And it's still growing! This world is just full of new things to find."

    voice "voice/2-scene_2-58.ogg" #Leona (Dot)
    le "I was surveying the terrain for a new exploration path when I found you in the tree."

    voice "voice/2-scene_2-59.ogg" #Raine (Nat)
    mc "Oh, you're an explorer?"

    voice "voice/2-scene_2-60.ogg" #Leona (Dot)
    le smug a3 "Yep! You're looking at the captain of Fireside's first explorers guild!"
    voice "voice/2-scene_2-61.ogg" #Leona (Dot)
    le happy a1 "I can tell you all about us later, let's get you healed up first."

    na "Leona walks us and her bike over to a small metal box affixed to one of the buildings."

    voice "voice/2-scene_2-62.ogg" #Leona (Dot)
    le happy a2 "All right, take a seat and show me where it hurts."

    na "She retrieves some gauze and a tube of green paste from the box on the wall."
    na "I'm assuming this is their version of a first aid kit."

    voice "voice/2-scene_2-63.ogg" #Raine (Nat)
    mc thankful "My leg, firstly. Shoulders are pretty banged up too, and I've got a headache."
    voice "voice/2-scene_2-64.ogg" #Raine (Nat)
    mc weary "I wouldn't be surprised if I had a concussion."

    voice "voice/2-scene_2-65.ogg" #Leona (Dot)
    le speakingthink "A conk-a-what?"

    voice "voice/2-scene_2-66.ogg" #Raine (Nat)
    mc "I hit my head."

    voice "voice/2-scene_2-67.ogg" #Leona (Dot)
    le kind a2 "Ouchie."

    voice "voice/2-scene_2-68.ogg" #Leona (Dot)
    le happy a1 "Okay, hold still…"

    na "She takes the paste and applies it to my scraped knee."

    show street with vpunch
    voice "voice/2-scene_2-69.ogg" #Raine (Nat)
    mc blech "Ow!"

    na "It stings a lot. Instinctually I pull away."

    voice "voice/2-scene_2-70.ogg" #Leona (Dot)
    le "Easy there, just give it a bit."

    na "She carefully places the gauze on top and wraps it up, letting the paste underneath stick and spread."
    na "Sure enough, the pain is replaced by a cool, soothing sensation."

    voice "voice/2-scene_2-71.ogg" #Raine (Nat)
    mc shocked m2 "Oh… Okay."

    na "She's clearly done this before."

    voice "voice/2-scene_2-72.ogg" #Leona (Dot)
    le kind a2 "Feeling better? You okay?"

    na "She gives me a tender look, like a mother looking after her kid."
    na "All for someone she just met."
    na "For me."
    na "It's… really sweet."

    voice "voice/2-scene_2-73.ogg" #Raine (Nat)
    mc thankful "Yeah, the pain's pretty much gone now."

    voice "voice/2-scene_2-74.ogg" #Leona (Dot)
    le "As for your shoulders and head, hold out your hand."

    na "Doing as instructed, she takes hold of my finger and squeezes out a drop of the green paste onto it."

    voice "voice/2-scene_2-75.ogg" #Leona (Dot)
    le happy a2 "Lick it just enough to taste it. It does funny stuff to your stomach if you try to swallow."
    voice "voice/2-scene_2-76.ogg" #Raine (Nat)
    mc shocked m2 "But... Didn't you just put that on my leg?"
    voice "voice/2-scene_2-77.ogg" #Leona (Dot)
    le "It works differently on the outside, trust me."

    voice "voice/2-scene_2-78.ogg" #Raine (Nat)
    mc speaking "Well, you've proven trustworthy so far..."
    na "..."

    show street with vpunch
    voice "voice/2-scene_2-79.ogg" #Raine (Nat)
    mc blech "HYECH!"

    voice "voice/2-scene_2-80.ogg" #Raine (Nat)
    mc upset "God, that tastes terrible!!"

    voice "voice/2-scene_2-81.ogg" #Leona (Dot)
    le happy2 a1 "I know, right?"
    voice "voice/2-scene_2-82.ogg" #Leona (Dot)
    le happy a2 "Once, when I was a kid, I had a really bad toothache and tried rubbing some onto it."
    voice "voice/2-scene_2-83.ogg" #Leona (Dot)
    le happy a1 "The pain went away, but I couldn't get the taste out for days."
    voice "voice/2-scene_2-84.ogg" #Leona (Dot)
    le smug a2 "And then the tummy problems began..."
    voice "voice/2-scene_2-85.ogg" #Raine (Nat)
    mc speaking "Isn't youth wonderful?"
    voice "voice/2-scene_2-86.ogg" #Leona (Dot)
    le happy a2 "Hehe!"
    voice "voice/2-scene_2-87.ogg" #Leona (Dot)
    le kind a2 "So, how's your head?"
    voice "voice/2-scene_2-88.ogg" #Raine (Nat)
    mc "Feels better. My shoulders aren't as sore either."
    voice "voice/2-scene_2-89.ogg" #Leona (Dot)
    le "I'm glad I was able to help!"
    voice "voice/2-scene_2-90.ogg" #Raine (Nat)
    mc "Yeah, you really saved me. First Juneau, then-"
    voice "voice/2-scene_2-91.ogg" #Leona (Dot)
    le speakingthink "Juneau?"
    voice "voice/2-scene_2-92.ogg" #Raine (Nat)
    mc shocked armraised "Oh! Juneau!"
    voice "voice/2-scene_2-93.ogg" #Raine (Nat)
    mc "Shit! I hope she survived the crash!"
    voice "voice/2-scene_2-94.ogg" #Leona (Dot)
    le concernedspeaking "...There was someone else on your ship?"
    voice "voice/2-scene_2-95.ogg" #Raine (Nat)
    mc thankful "Yes - well, no. Not exactly. She's part of my ship. My AI navigator. I need to see if she made it. Can you take me there? Back to the crash site?"
    voice "voice/2-scene_2-96.ogg" #Leona (Dot)
    le happy a2 "Sure, I can take you back."
    voice "voice/2-scene_2-97.ogg" #Leona (Dot)
    le "But not right now."
    voice "voice/2-scene_2-98.ogg" #Raine (Nat)
    mc "Huh?"
    voice "voice/2-scene_2-99.ogg" #Leona (Dot)
    le "I don't think we should go back to your ship just yet."
    voice "voice/2-scene_2-100.ogg" #Leona (Dot)
    le shylook "Those woods aren't exactly safe after the sun goes down."
    voice "voice/2-scene_2-101.ogg" #Leona (Dot)
    le "And in your condition…"
    voice "voice/2-scene_2-102.ogg" #Raine (Nat)
    mc sighing "Without my ship, I uh...don't really have anywhere else to go."
    voice "voice/2-scene_2-103.ogg" #Leona (Dot)
    le happy a2 "Well, why don't you rest at my place, then? We can look into your ship tomorrow."
    na "I guess I don't really have much of a choice."
    voice "voice/2-scene_2-104.ogg" #Raine (Nat)
    mc amused "Yes, please."
    voice "voice/2-scene_2-105.ogg" #Leona (Dot)
    le happy2 a1 "Right, scootch over and we'll head in!"
    stop music fadeout 2.0
    stop env fadeout 3.0
    scene sky with dissolve
    pause 0.5
    ###
    # ART - BG bg_leonahouse
    ###
    scene house with wipeleft
    play env "Amb/Leonas house.ogg" fadein 3.0
    $ hide_sides = ["Leona"]
    show le happy a2 with dissolve:
        stage_right

    voice "voice/2-scene_2-106.ogg" #Leona (Dot)
    le "Ta-dahhh! Welcome to my little house."
    voice "voice/2-scene_2-107.ogg" #Raine (Nat)
    mc happy "Ah, I feel cozy already."
    na "There's a shelf of knick-knacks, a messy pile of papers on a desk, and a small kitchenette in the corner."
    na "But none of those things are even remotely as interesting as the centerpiece of the room."
    na "I immediately target the bed, or what I assume to be the bed -- a huge pile of cushions and blankets lining the back wall beneath more rows of shelving."
    voice "voice/2-scene_2-108.ogg" #Leona (Dot)
    le questioning a3 "Oh, you'll probably --"
    ###
    # SFX - POMF
    ###
    play sound "sfx/bed fall.ogg"
    show house with vpunch
    voice "voice/2-scene_2-109.ogg" #Leona (Dot)
    le "-want to sleep off the medicine."
    voice "voice/2-scene_2-110.ogg" #Leona (Dot)
    le kind a2 "I figured this would happen."
    voice "voice/2-scene_2-111.ogg" #Raine (Nat)
    mc yawn2 "Sorry... "
    play music "music/First Night.ogg" fadein 2.0
    voice "voice/2-scene_2-112.ogg" #Leona (Dot)
    le "Rest up, we can talk later."
    voice "voice/2-scene_2-113.ogg" #Raine (Nat)
    mc satisfied "Thanks, you're the best~"
    na "It doesn't take much time before the day's trauma catches up to me and the urge to pass right the hell out envelops me completely."

    scene black with wipedown
    stop env fadeout 2.0
    ###
    # VFX - EYES CLOSE
    ###

    na "But before I conk out, I hear something."
    voice "voice/2-scene_2-114.ogg" #Leona (Dot)
    le "Logdate 2301: Today was interesting. I found an alien! She -- or at least, I think it's a she -- crash-landed..."
    na "Huh... She has... a diary..."
    stop music fadeout 2.0
    na "I guess... we're not... that... diff..."

    jump scene_3
