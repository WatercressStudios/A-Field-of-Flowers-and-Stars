label scene_2:

    #birds chirping SFX
    scene white with dissolve
    pause 1.0
    scene black with vpunch
    pause 2.0

    voice "voice/2-scene_2-1.ogg" #Raine (Nat)
    mc satisfied "Ugh..."
    na "What the hell happened?"
    na "There was a wormhole and then I saw a planet and..."

    scene spaceship_crashed with wipeup:
        yzoom -1
    #iris open
    #show BG_outdoors_upside_down
    play env "Amb/Outdoors.ogg" fadein 2.0

    na "And now I'm upside down."
    na "Feels like I'm hanging by the ankles, something is brushing up against my back and I'm definitely up off the ground."
    na "It's a tree then. I'm stuck in a fuckin' tree."
    na "Juneau must have ejected me right before I blacked out."
    na "Then my parachute got snagged on the way down."
    na "Ugh, something hurts."
    na "No, actually, everything hurts."
    show spaceship_crashed:
        ease 0.5 yoffset -20
        ease 0.5 yoffset 0
    na "I can't reach the buckle to free me from the harness, thanks to my arms being tied up by the parachute cables."
    show spaceship_crashed:
        ease 0.5 yoffset -20
        ease 0.5 yoffset 0
    na "At least I can wiggle around, so I won't be bored as I slowly die of exposure."
    na "Could be worse, though. The wormhole itself could have popped the ship like a giant metal pimple."

    mc onfire "Well, this blows."

    na "Alright, Raine. You gotta get out of this somehow."

    scene black with wipedown
    na "I close my eyes and meditate on the situation."
    na "If I can wiggle around maybe a line will fray and drop me out of the tree?"
    na "...Or drop me on my head, breaking my neck and squashing any chance of survival."

    ###
    # SFX - SOUND OF A MOTORCYCLE APPROACHING THEN STOPPING A LITTLE WAYS AWAY
    # SFX - FOOTSTEPS BEGIN AFTER 3 SECONDS, VERY FAINT BUT GRADUALLY GETTING LOUDER OVER THE COURSE OF ANOTHER 5 SECONDS. FOLLOWED BY ANOTHER PAUSE FOR A SECOND BEFORE LEONA SPEAKS
    ###

    play sound "sfx/footsteps.ogg"

    pause 3.0

    #pause for ten or so seconds

    $ hide_sides = ["Leona"]

    voice "voice/2-scene_2-4.ogg" #Leona (Dot)
    le "Eo'ahola! I'akiam eo'ahap?!?"
    #iris open, fast
    #show BG_outdoors_upside_down

    scene spaceship_crashed with wipeup:
        yzoom -1

    na "What was that?"
    na "That was definitely a voice I heard just now. Where is it?"
    na "Straining my neck, I try to look around."

    show cgTree with dissolve

    na "There's someone at the base of the tree. A girl?"

    voice "voice/2-scene_2-5.ogg" #Leona (Dot)
    le "Ahola? U'ai ehol ek u'ai ikih?"
    na "She's definitely there."

    voice "voice/2-scene_2-6.ogg" #Raine (Nat)
    mc shyspeak "Hey! You!"
    mc upset "H-help!"

    voice "voice/2-scene_2-7.ogg" #Leona (Dot)
    le "Olal i ohi e u'ai eo' ea' e, a'ap e!"
    scene spaceship_crashed with Dissolve(2.0):
        yzoom -1.0
        zoom 1.2
        yalign 1.0

    na "The girl climbs up the tree with surprising speed. Within seconds she's out of sight. Behind me?"

    voice "voice/2-scene_2-8.ogg" #Leona (Dot)
    le "Ulo'ulo' e, uamo'oh e!"

    na "She's messing with something. Is she cutting me down?"

    #cable tearing SFX
    play sound "sfx/tree.ogg"

    na "The cables fall away..."

    play sound "sfx/falling.ogg"

    show spaceship_crashed:
        linear 0.6 yalign 0.0
    pause 0.6
    show black

    voice "voice/2-scene_2-9.ogg" #Raine (Nat)
    mc "W-Woah!"

    na "...as I fall to the ground."

    voice "voice/2-scene_2-10.ogg" #Leona (Dot)
    le @ catching "Ohaw i ānān!"

    na "The girl leaps down from the branch and grabs me midair."
    na "Perhaps it's because of the planet's reduced gravity, but we seem to float down, rather than fall."
    na "Or maybe the adrenaline is slowing my perception of time?"

    scene spaceship_crashed with vpunch
    pause 0.5

    mc blech "AuUuoghhh..."
    na "I'm gonna go with the latter. If I wasn't sore before, I am now."

    mc thankful "Thanks. Thought I was done for..."

    show le sassyquestioning with dissolve:
        stage_right

    voice "voice/2-scene_2-11.ogg" #Leona (Dot)
    le "Ikah iwi uam eh? Anomom eli?"
    na "A thought occurs to me. This girl isn't speaking anything resembling Galactic Standard."
    na "Did my translation chip break during the crash?"
    na "My head definitely feels like it got banged into something."

    le " Uo said iwi aum okay?"
    na "It seems like it's starting to work though."

    voice "voice/2-scene_2-12.ogg" #Raine (Nat)
    mc thankful "S-Sorry, can you say that again?"

    voice "voice/2-scene_2-14.ogg" #Leona (Dot)
    le questioning a1 "Did you break anything? No broken bones, right?"
    play music "music/meeting leona.ogg" fadein 2.0
    na "I check myself over. Nothing broken, but I've got a nasty scrape on my leg and it feels like I was put through a wood chipper."

    voice "voice/2-scene_2-15.ogg" #Raine (Nat)
    mc @ yawn "I'm okay. Mostly."
    na "At least the ship is close. Hopefully there's still a usable medpack in there."

    voice "voice/2-scene_2-16.ogg" #Leona (Dot)
    le smug a3 "Good! I'm glad you're okay."

    voice "voice/2-scene_2-18.ogg" #Raine (Nat)
    mc questioning "I didn't realize there were other humans on this planet. What sector am I in?"

    voice "voice/2-scene_2-19.ogg" #Leona (Dot)
    le questioning a2 "'Sector'? 'Human'? What are those?" with bounce

    voice "voice/2-scene_2-20.ogg" #Raine (Nat)
    mc surprised "Uh..."

    voice "voice/2-scene_2-21.ogg" #Raine (Nat)
    mc shocked armraised "Ah! Y-You're..."

    voice "voice/2-scene_2-22.ogg" #Leona (Dot)
    le questioning a1 "Hm?"
    na "There's a pair of horns on this girl's head. Honest-to-goodness horns, like you'd see on a goat or a ram."

    voice "voice/2-scene_2-23.ogg" #Raine (Nat)
    mc "H-Horns..."

    voice "voice/2-scene_2-24.ogg" #Leona (Dot)
    le concerned "Oh? Oh!"
    le "You don't have any horns?"

    na "The girl thinks for a moment."

    voice "voice/2-scene_2-40.ogg" #Leona (Dot)
    le speakingthink "You're... an alien?"

    voice "voice/2-scene_2-41.ogg" #Raine (Nat)
    mc amused "No, I'm --"

    na "Wait, yeah. She's right. I'm technically the alien here."

    voice "voice/2-scene_2-43.ogg" #Raine (Nat)
    mc "Yeah. I'm Raine. A human from a planet called Lumin. Ever heard of it?"

    voice "voice/2-scene_2-44.ogg" #Leona (Dot)
    le surprised "That's not a planet I've heard of... Is it close?"

    voice "voice/2-scene_2-45.ogg" #Raine (Nat)
    mc speaking "I don't really know. My ship has all the info, but it's uh, not exactly in good shape right now."

    voice "voice/2-scene_2-46.ogg" #Leona (Dot)
    le happy a2 "Well whatever, it's nice to meet you. I'm Leona!"

    voice "voice/2-scene_2-27.ogg" #Leona (Dot)
    le concerned "You're injured, so we should get you to the city and patch you up."

    voice "voice/2-scene_2-29.ogg" #Raine (Nat)
    mc "City? Where are we anyway?"

    voice "voice/2-scene_2-30.ogg" #Leona (Dot)
    le explaining "Hmm? A forest just south of Aster."

    voice "voice/2-scene_2-30.ogg" #Leona (Dot)
    le happy a1 "You picked a pretty bad spot to land, I won't sugar coat it."

    voice "voice/2-scene_2-33.ogg" #Raine (Nat)
    mc surprised "No, I mean WHERE are we?"

    voice "voice/2-scene_2-30.ogg" #Leona (Dot)
    le explaining "Oh, right, planet. You're on Fireside."

    voice "voice/2-scene_2-29.ogg" #Raine (Nat)
    mc speaking "Fireside? Strange name for a rock."

    voice "voice/2-scene_2-46.ogg" #Leona (Dot)
    le happy a2 "Really? Seems normal to me, but then again, I live here."

    voice "voice/2-scene_2-46.ogg" #Leona (Dot)
    le "We call ourselves Dawnese. We're from Dawne, a few light years away from here. This is our first colony world."

    voice "voice/2-scene_2-48.ogg" #Leona (Dot)
    le speaking a2 "I gotta say, I was more than a little surprised to see a ship come down here."

    voice "voice/2-scene_2-49.ogg" #Leona (Dot)
    le speaking a1 "We don't know how to make space ships that small yet."

    voice "voice/2-scene_2-50.ogg" #Leona (Dot)
    le explaining "I thought it was just a shooting star at first, but I saw something else trailing behind it."

    voice "voice/2-scene_2-51.ogg" #Leona (Dot)
    le happy a2 "I came to have a peek and look what I found! An honest-to-goodness alien!"

    voice "voice/2-scene_2-51.ogg" #Leona (Dot)
    le speakingthink "Though, I've never seen an alien look so much like me before..."

    voice "voice/2-scene_2-52.ogg" #Raine (Nat)
    mc questioning "Likewise, actually."

    voice "voice/2-scene_2-53.ogg" #Leona (Dot)
    le happy a2 "Well, let's get you somewhere safe. We should really make sure you're okay too."

    scene sky with dissolve

    na "Leona walks us over to her ride, a primitive hoverbike with room for two."

    stop env fadeout 2.0

    na "After a relatively short ride, the trees begin to thin and the terrain flows into a wide open plain, where the first sign of civilization on this planet comes into view."

    $ hide_sides = []
    mc speaking "What's that tower?"
    le happy a2 "That's the ark ship that brought us here! We're still dependent on it for it's atmosphere processors and power systems."
    mc "Ark ship? Didn't you say your homeworld was only a few lightyears from here?"
    le "Yeah. Like I said, we're not that advanced yet."
    le happy a1 "I was born here, but there are people still alive here in Aster who came here from Dawne originally."

    na "As we ride towards the ship, a cluster of small buildings come into view at the base of the tower."

    scene street onlayer master with dissolve:
        subpixel True xpos 0.85 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None

    $ hide_sides = ['Leona']

    show le happy a1 at stage_right with dissolve
    voice "voice/2-scene_2-55.ogg" #Leona (Dot)
    le happy a2 "We're here! Welcome to the city of Aster!"
    scene street onlayer master with None:
            subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
            parallel:
                xpos 1.00
                ease 15 xpos 0.56

    $ hide_sides = []

    play env "amb/City Day.ogg" fadein 1.0
    na "Leona disembarks, helping me down from the bike."

    le happy a2 "Whaddya think?"

    na "If I didn't know any better, I'd say the town felt almost human in design."

    voice "voice/2-scene_2-56.ogg" #Raine (Nat)
    mc shocked armraised "Wow, you've built quite a little settlement here."

    voice "voice/2-scene_2-57.ogg" #Leona (Dot)
    le speaking a2 "And it's still growing! This world is just full of new things to find."

    le "I was surveying the terrain for a new exploration path when I found you in the tree."

    voice "voice/2-scene_2-58.ogg" #Raine (Nat)
    mc "Oh, you're an explorer?"

    le smug a3 "Yep! You're looking at the captain of Fireside's first explorers guild!"
    le happy a1 "I can tell you all about us later, let's get you healed up first."

    na "Leona walks us and her bike over to a small metal box affixed to one of the buildings."

    voice "voice/2-scene_2-59.ogg" #Leona (Dot)
    le happy a2 "All right, take a seat and show me where it hurts."

    na "She retrieves some gauze and a tube of green paste from the box on the wall."
    na "I'm assuming this is their version of a first aid kit."

    mc thankful "My leg, firstly. Shoulders are pretty banged up too, and I've got a headache."
    mc weary "I wouldn't be surprised if I had a concussion."

    voice "voice/2-scene_2-60.ogg" #Leona (Dot)
    le speakingthink "A conk-a-what?"

    voice "voice/2-scene_2-61.ogg" #Leona (Dot)
    mc "I hit my head."

    le kind a2 "Ouchie."

    le happy a1 "Okay, hold still…"

    na "She takes the paste and applies it to my scraped knee."

    voice "voice/2-scene_2-62.ogg" #Raine (Nat)
    show street with vpunch
    mc blech "Ow!"

    na "It stings a lot. Instinctually I pull away."

    le "Easy there, just give it a bit."

    na "She carefully places the gauze on top and wraps it up, letting the paste underneath stick and spread."
    na "Sure enough, the pain is replaced by a cool, soothing sensation."

    mc shocked m2 "Oh… Okay."

    na "She's clearly done this before."

    le kind a2 "Feeling better? You okay?"

    na "She gives me a tender look, like a mother looking after her kid."
    na "All for someone she just met."
    na "For me."
    na "It's… really sweet."

    mc thankful "Yeah, the pain's pretty much gone now."

    le "As for your shoulders and head, hold out your hand."

    na "Doing as instructed, she takes hold of my finger and squeezes out a drop of the green paste onto it."

    le happy a2 "Lick it just enough to taste it. It does funny stuff to your stomach if you try to swallow."
    mc shocked m2 "But... Didn't you just put that on my leg?"
    le "It works differently on the outside, trust me."

    mc speaking "Well, you've proven trustworthy so far..."
    na "..."

    show street with vpunch
    mc blech "HYECH!"

    mc upset "God, that tastes terrible!!"

    le happy2 a1 "I know, right?"
    le happy a2 "Once, when I was a kid, I had a really bad toothache and tried rubbing some onto it."
    le happy a1 "The pain went away, but I couldn't get the taste out for days."
    le smug a2 "And then the tummy problems began..."
    mc speaking "Isn't youth wonderful?"
    le happy a2 "Hehe!"
    le kind a2 "So, how's your head?"
    mc "Feels better. My shoulders aren't as sore either."
    le "I'm glad I was able to help!"
    mc "Yeah, you really saved me. First Juneau, then-"
    le speakingthink "Juneau?"
    mc shocked armraised "Oh! Juneau!"
    mc "Shit! I hope she survived the crash!"
    le concernedspeaking "...There was someone else on your ship?"
    mc thankful "Yes - well, no. Not exactly. She's part of my ship. My AI navigator. I need to see if she made it. Can you take me there? Back to the crash site?"
    le happy a2 "Sure, I can take you back."
    le "But not right now."
    mc "Huh?"
    le "I don't think we should go back to your ship just yet."
    le shylook "Those woods aren't exactly safe after the sun goes down."
    le "And in your condition…"
    mc sighing "Without my ship, I uh...don't really have anywhere else to go."
    le happy a2 "Well, why don't you rest at my place, then? We can look into your ship tomorrow."
    na "I guess I don't really have much of a choice."
    mc amused "Yes, please."
    le happy2 a1 "Right, scootch over and we'll head in!"

    scene sky with dissolve
    pause 0.5
    ###
    # ART - BG bg_leonahouse
    ###
    scene house with wipeleft

    $ hide_sides = ["Leona"]
    show le happy a2 with dissolve:
        stage_right

    le "Ta-dahhh! Welcome to my little house."
    mc happy "Ah, I feel cozy already."
    na "There's a shelf of knick-knacks, a messy pile of papers on a desk, and a small kitchenette in the corner."
    na "But none of those things are even remotely as interesting as the centerpiece of the room."
    na "I immediately target the bed, or what I assume to be the bed -- a huge pile of cushions and blankets lining the back wall beneath more rows of shelving."
    le questioning a3 "Oh, you'll probably --"
    ###
    # SFX - POMF
    ###
    show house with vpunch
    le "-want to sleep off the medicine."
    le kind a2 "I figured this would happen."
    mc yawn2 "Sorry... "
    le "Rest up, we can talk later."
    mc satisfied "Thanks, you're the best~"
    na "It doesn't take much time before the day's trauma catches up to me and the urge to pass right the hell out envelops me completely."

    scene black with wipedown
    ###
    # VFX - EYES CLOSE
    ###

    na "But before I conk out, I hear something."
    le "Logdate 2301: Today was interesting. I found an alien! She -- or at least, I think it's a she -- crash-landed..."
    na "Huh... She has... a diary..."
    na "I guess... we're not... that... diff..."

    jump scene_3
