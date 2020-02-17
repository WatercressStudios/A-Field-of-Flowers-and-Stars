label scene_2:

    #birds chirping SFX
    scene white with dissolve
    pause (2)
    scene black with vpunch
    pause (4)

    voice "voice/2-scene_2-1.ogg" #Raine (Nat)
    mc "Ugh..."
    na "What the hell happened? I recall entering the atmosphere of that planet..."
    scene spaceship_crashed with wipeup:
        yzoom -1
    #iris open
    #show BG_outdoors_upside_down
    play env "Amb/Outdoors.ogg" fadein 2.0

    voice "voice/2-scene_2-2.ogg" #Raine (Nat)
    mc "Shit."
    na "I'm upside down in what appears to be a... tree?"
    na "I guess Juneau must have ejected me before the crash."
    na "My parachute is tangled up in the branches, my seat, and me."

    voice "voice/2-scene_2-3.ogg" #Raine (Nat)
    mc "Can't... move..."
    na "My arms are trapped above my head."
    na "I'm tangled in the mess of cables in such a way that makes it impossible for me to free myself."
    na "This is it. Great. This is how I die. On some godforsaken planet. Entangled by my own parachute."
    na "All alone, with no one to mourn me."
    na "Well, this fucking sucks."

    na "I'd probably cry, if I weren't so bitter with how this day turned out."
    scene black with wipedown
    na "I close my eyes and wait to die. Dehydration will most likely take me in a few days."
    na "Well, can't say it wasn't fun. Goodbye cruel world."
    scene black with fade
    pause 5.0

    play sound "sfx/footsteps.ogg"

    pause 5.0

    #pause for ten or so seconds

    voice "voice/2-scene_2-4.ogg" #Leona (Dot)
    le "Eo'ahola! I'akiam eo'ahap?!?"
    #iris open, fast
    #show BG_outdoors_upside_down
    na "What was that?"
    na "That was definitely a voice I heard just now. Where is it?"
    na "Straining my neck, I try to look around."
    na "And there, I see it. Or, rather, {i}her{/i}."

    #show CG_02a

    na "There's someone at the base of the tree. A girl?"

    voice "voice/2-scene_2-5.ogg" #Leona (Dot)
    le "Ahola? U'ai ehol ek u'ai ikih?"
    na "She's definitely there."
    na "For the first time in what feels like several hours, I speak."

    voice "voice/2-scene_2-6.ogg" #Raine (Nat)
    mc "H-help!"

    voice "voice/2-scene_2-7.ogg" #Leona (Dot)
    le "Olal i ohi e u'ai eo' ea' e, a'ap e!"
    scene spaceship_crashed with Dissolve(2.0)
    #show CG_02b
    show le curious onlayer master:
        stage_right
        bounce
    na "The girl climbs up the tree with surprising speed. Within seconds she's at my side."
    show le questioning a1 with dissolve

    voice "voice/2-scene_2-8.ogg" #Leona (Dot)
    le "Ulo'ulo' e, uamo'oh e!"

    #cable tearing SFX
    play sound "sfx/tree.ogg"

    na "The cables fall away..."

    voice "voice/2-scene_2-9.ogg" #Raine (Nat)
    mc "W-Woah!"

    na "...Leaving me to fall to the ground."

    voice "voice/2-scene_2-10.ogg" #Leona (Dot)
    le @ catching "Ohaw i ānān!"
    na "The girl leaps forward from the branch and catches me mid-air."
    hide le with dissolve
    na "Perhaps it's because of the planet's reduced gravity, but we seem to float down, rather than fall."
    na "Or maybe I'm just relieved that I'm not going to die."

    play sound "sfx/falling.ogg"

    show le sassyquestioning with dissolve:
        stage_right

    voice "voice/2-scene_2-11.ogg" #Leona (Dot)
    le "Ikah iwi uam eh? Anomom eli?"
    na "A thought occurs to me. My translator implant should be kicking in..."
    na "It's not English. Or Lucoan, or Halcynth either. She must be speaking a language the system doesn't recognize."

    voice "voice/2-scene_2-12.ogg" #Raine (Nat)
    mc thankful "S-Sorry, can you say that again?"
    na "I need her to keep speaking. Any second now it should begin to translate her words."

    voice "voice/2-scene_2-13.ogg" #Leona (Dot)
    le questioning a2 "Ohaw i ānān!"

    voice "voice/2-scene_2-14.ogg" #Leona (Dot)
    le questioning a1 "Did you break anything? No broken bones, right?"
    play music "music/meeting leona.ogg" fadein 2.0
    na "Finally, my implant starts to work and I can understand her words."
    na "I check myself over. Aside from some rope burn and some really sore spots, I seem to be alright."

    voice "voice/2-scene_2-15.ogg" #Raine (Nat)
    mc @ yawn "I'm okay. Mostly."
    na "There's the issue of my ship, too."
    na "I look around but I don't see it. It must have come down some distance away."

    voice "voice/2-scene_2-16.ogg" #Leona (Dot)
    le smug a3 "Good! I'm glad you're okay."

    voice "voice/2-scene_2-17.ogg" #Raine (Nat)
    mc neutral "Whew! I thought I was a goner."

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
    na "At first glance the girl appears to be human but..."
    na "There's a pair of horns on this girl's head. Honest-to-goodness horns, like you'd see on a goat or a ram."

    voice "voice/2-scene_2-23.ogg" #Raine (Nat)
    mc "H-Horns..."

    voice "voice/2-scene_2-24.ogg" #Leona (Dot)
    le concerned "Oh? Oh! You don't have any horns? They must have broken off in the crash. You poor thing."

    voice "voice/2-scene_2-25.ogg" #Raine (Nat)
    mc unimpressed "N-No, wait! I never had any horns to begin with! I'm human!"
    show le curious
    na "The girl thinks for a moment."

    voice "voice/2-scene_2-26.ogg" #Leona (Dot)
    le happy a2 "Okay! Hello, Human! It's nice to meet you. I'm Leona!"

    voice "voice/2-scene_2-27.ogg" #Leona (Dot)
    le a1 "Come on, you must be a new arrival to Fireside. Let me take you back to the city!"

    voice "voice/2-scene_2-29.ogg" #Raine (Nat)
    mc "Fireside?"

    voice "voice/2-scene_2-30.ogg" #Leona (Dot)
    le explaining "You know, the name of this planet?"

    voice "voice/2-scene_2-33.ogg" #Raine (Nat)
    mc surprised "Hang on. What planet do you think I'm from again?"

    voice "voice/2-scene_2-34.ogg" #Leona (Dot)
    le concerned "Oh man, you must have hit your head. I should definitely take you to the city and get you patched up."

    voice "voice/2-scene_2-35.ogg" #Raine (Nat)
    mc @ speaking  "Hold on..."

    voice "voice/2-scene_2-36.ogg" #Leona (Dot)
    le "We're from Dawne, a few light years away from here. This is our first colony!"

    voice "voice/2-scene_2-37.ogg" #Raine (Nat)
    mc annoyed "I'm trying to tell you, I'm not one of... you guys."

    voice "voice/2-scene_2-38.ogg" #Raine (Nat)
    mc upset "I'm from another planet. And my name isn't 'Human', it's 'Raine'!"

    voice "voice/2-scene_2-39.ogg" #Leona (Dot)
    le "..."
    na "Finally, it hits her."

    voice "voice/2-scene_2-40.ogg" #Leona (Dot)
    le "You're... an alien?"

    voice "voice/2-scene_2-41.ogg" #Raine (Nat)
    mc amused "No, I'm --"

    na "Wait, yeah. She's right. I'm technically the alien here."

    voice "voice/2-scene_2-43.ogg" #Raine (Nat)
    mc "Yeah. I'm from a planet called Lumin. Ever heard of it?"

    voice "voice/2-scene_2-44.ogg" #Leona (Dot)
    le surprised "That's not a planet I've heard of... How far away are you from home?"

    voice "voice/2-scene_2-45.ogg" #Raine (Nat)
    mc speaking "I don't really know. My ship had all the info, but it crashed."

    voice "voice/2-scene_2-46.ogg" #Leona (Dot)
    le happy a2 "Ah, so that's what that thing was!"

    voice "voice/2-scene_2-47.ogg" #Raine (Nat)
    mc surprised "You've seen it?"

    voice "voice/2-scene_2-48.ogg" #Leona (Dot)
    le speaking a2 "Yeah, my team saw something enter the atmosphere a while ago, so they went to check it out."

    voice "voice/2-scene_2-49.ogg" #Leona (Dot)
    le explaining "Lucky for me, I saw something else falling from the ship."

    voice "voice/2-scene_2-50.ogg" #Leona (Dot)
    le speaking a1 "And look what I found! An honest-to-goodness alien!"

    voice "voice/2-scene_2-51.ogg" #Leona (Dot)
    le questioning a1 "Though, I've never seen an alien look so much like me before..."

    voice "voice/2-scene_2-52.ogg" #Raine (Nat)
    mc questioning "Likewise, actually."

    voice "voice/2-scene_2-53.ogg" #Leona (Dot)
    le "Well, let's get you to my place. We should really make sure you're okay."

    na "Thankfully, Leona has a ride back into town, a primitive hoverbike with extra space for me and the few meager belongings I had on my person."

    na "For a second, I thought we'd be walking the whole way back."
    hide le with dissolve
    stop env fadeout 2.0

    scene street onlayer master with wiperight:
        subpixel True xpos 0.85 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None

    voice "voice/2-scene_2-54.ogg" #Leona (Dot)
    le "We're here!"

    na "After a relatively short trip, we arrive."

    na "Leona disembarks, helping me down from the bike."

    voice "voice/2-scene_2-55.ogg" #Leona (Dot)
    le happy a2 "Welcome to the city of Aster!"
    scene street onlayer master with None:
            subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
            parallel:
                xpos 0.85
                ease 15 xpos 0.59
    show le happy a1 at le_side with dissolve
    play env "amb/City Day.ogg" fadein 1.0
    na "The city is a massive sprawl, all centered on a large tower about a mile away."

    voice "voice/2-scene_2-56.ogg" #Raine (Nat)
    mc "What's that tower?"

    voice "voice/2-scene_2-57.ogg" #Leona (Dot)
    le speaking a1 "That's the colony ship we arrived on several decades ago! Nowadays it's been refitted as a government office and communications relay."

    voice "voice/2-scene_2-58.ogg" #Raine (Nat)
    mc "Decades? So this is a new colony?"

    voice "voice/2-scene_2-59.ogg" #Leona (Dot)
    le curious "More or less. I was born here, so I hear a lot of stories about our homeworld."

    voice "voice/2-scene_2-60.ogg" #Leona (Dot)
    le happy a1 "But this place is growing a lot! We want to expand to make another small city out west for some researchers and stuff."

    voice "voice/2-scene_2-61.ogg" #Leona (Dot)
    le "That's where I come in! I help survey and explore new areas that we might be able to live in!"

    voice "voice/2-scene_2-62.ogg" #Raine (Nat)
    mc "By yourself?"

    voice "voice/2-scene_2-63.ogg" #Leona (Dot)
    le happy2 a1  "Nah, I've got a whole crew who helps out. Maybe you'll meet them!"

    show le happy2 a1:
        subpixel True xpos 0.67 ypos 577 xanchor 1.55 yanchor 1 xzoom -1.0 zoom 1.13 rotate None alpha 1.0
        parallel:
            ypos 525
            ease_back 0.5 ypos 1109
    na "Leona goes on for a few more minutes about her background and past expeditions while I silently nod and listen."
    na "While our civilization made first contact centuries ago, I don't think Leona's species has ever been encountered."
    na "We've mostly encountered non-humanoid species, so for Leona to look so humanlike is really surprising."
    na "We arrive at what appears to be a small first-aid station a few minutes later."

    show le happy a1 at stage_left with dissolve

    voice "voice/2-scene_2-64.ogg" #Leona (Dot)
    le "All right, we're here!"

    voice "voice/2-scene_2-65.ogg" #Leona (Dot)
    le happy2 a1 "Hey, stay here, Raine. I'll get you something that'll make you feel better instantly!"
    na "She returns with gauze and a strange paste."

    voice "voice/2-scene_2-66.ogg" #Leona (Dot)
    le "Okay, hold still…"
    na "She takes the paste and applies it to my scraped knee."

    voice "voice/2-scene_2-67.ogg" #Raine (Nat)
    mc "Ow!"

    voice "voice/2-scene_2-68.ogg" #Leona (Dot)
    le kind a2 "Easy there, just give it a bit."
    na "It stings a lot, but it's quickly replaced by a soothing sensation."
    na "She carefully places the gauze on top and massages it, letting the paste underneath stick to it."
    na "She's clearly done this before."

    voice "voice/2-scene_2-69.ogg" #Leona (Dot)
    le "Feeling better? You okay?"
    na "She gives me a tender look, like a mother looking after her kid."
    na "All for someone she just met."
    na "It's… really sweet."

    voice "voice/2-scene_2-70.ogg" #Raine (Nat)
    mc "Yeah, the pain's pretty much gone now."

    voice "voice/2-scene_2-71.ogg" #Leona (Dot)
    le speakingsurprised a1 "Great! So, I was thinking... you'll need a place to stay, right?"

    voice "voice/2-scene_2-72.ogg" #Raine (Nat)
    mc "You're not wrong. I don't know where my ship is, so I can't exactly leave just yet."

    voice "voice/2-scene_2-73.ogg" #Leona (Dot)
    le speaking a2 "Well, why don't you rest at my place, then? We can try to find your ship tomorrow."
    na "After the various traumas of today, I think I deserve a break."

    voice "voice/2-scene_2-74.ogg" #Raine (Nat)
    mc "Sure. I could use the rest."

    voice "voice/2-scene_2-75.ogg" #Leona (Dot)
    le smug a1 "Right, then! Hop on and I'll take you home!"
    hide le
    scene black with fade
    #show bg_leonahouse
    stop env fadeout 2.0
    stop music fadeout 2.0
    play sound3 "amb/Leonas house.ogg" fadeout 2.0

    scene house onlayer master with fade:
        subpixel True xpos 0.5 ypos 1.25 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.35
            ease 10 xpos 0.66

    show le happy2 a1 at le_side with dissolve

    voice "voice/2-scene_2-76.ogg" #Leona (Dot)
    le "Ta-dahhh! Welcome to my little plot of land."
    na "While it looks like one of those old prefabricated shelters, the inside is surprisingly cozy."
    na "There's a shelf of knick-knacks, a messy pile of papers on a desk, and a small kitchenette in the corner."

    voice "voice/2-scene_2-77.ogg" #Leona (Dot)
    le explaining "Oh, you'll probably --"
    na "I immediately target the bed, or what I assume to be the bed -- a pile of cushions and blankets seems to be where Leona sleeps."

    #POMF
    play sound "sfx/bed fall.ogg"
    show le surprised with vpunch
    na "Without another word, I flop down onto the 'bed' and turn to Leona."

    voice "voice/2-scene_2-78.ogg" #Raine (Nat)
    mc "I'm going to sleep for a bit. Sorry."

    voice "voice/2-scene_2-79.ogg" #Leona (Dot)
    le relaxed "No problem! Sleep well!"
    stop sound3 fadeout 2.0
    na "It doesn't take much effort before I pass out completely."

    scene black with Dissolve(2.0)
    hide le with dissolve

    #iris close

    na "But before I do, I hear something."

    voice "voice/2-scene_2-80.ogg" #Leona (Dot)
    le "Logdate 2301: Today was interesting. I found an alien! She -- or at least, I think it's a she -- crash-landed..."
    na "How funny. Guess she isn't that much different from the girls on my home planet if she keeps a diary."
    scene black with fade
    jump scene_3
