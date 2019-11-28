label scene_2:

    #birds chirping SFX
    scene testbg with dissolve
    mc "Ugh..."
    na "What the hell happened? I recall entering the atmosphere of that planet..."

    #iris open
    #show BG_outdoors_upside_down

    mc "Shit."
    na "I'm upside down in what appears to be a... tree?"
    na "I guess Juneau must have ejected me before the crash."
    na "My parachute is tangled up in the branches, my seat, and me."
    mc "Can't... move..."
    na "My arms are trapped above my head."
    na "I'm tangled in the mess of cables in such a way that makes it impossible for me to free myself."
    na "This is it. Great. This is how I die. On some godforsaken planet. Entangled by my own parachute."
    na "All alone, with no one to mourn me."
    na "Well, this fucking sucks."

    na "The last thing I recall from the ship is that this planet is not registered on any starmap."
    na "So, I'm most likely the only human on this planet."
    na "I'd probably cry, if I weren't so bitter with how this day turned out."
    #iris close
    na "I close my eyes and wait to die. Dehydration will most likely take me in a few days."
    na "Well, can't say it wasn't fun. Goodbye cruel world."
    #pause for ten or so seconds
    le "Eo'ahola! I'akiam eo'ahap?!?"
    #iris open, fast
    #show BG_outdoors_upside_down
    na "What was that?"
    na "That was definitely a voice I heard just now. Where is it?"
    na "Straining my neck, I try to look around."
    na "And there, I see it. Or, rather, {i}her{/i}."

    #show CG_02a

    na "There's someone at the base of the tree. A girl?"
    le "Ahola? U'ai ehol ek u'ai ikih?"
    na "She's definitely there."
    na "For the first time in what feels like several hours, I speak."
    mc "H-help!"
    le "Olal i ohi e u'ai eo' ea' e, a'ap e!"

    #show CG_02b
    show le curious onlayer master:
        bounce
        xflip
        subpixel True ypos 100 xanchor None yanchor None xzoom -1.0 rotate None
        parallel:
            xpos -743
            power_in2 1.0 xpos -743
            power_in2 0.63 xpos 212
    na "The girl climbs up the tree with surprising speed. Within seconds she's at my side."
    le "Ulo'ulo' e, uamo'oh e!"

    #cable tearing SFX

    na "The cables fall away..."
    mc "W-Woah!"
    mc "...Leaving me to fall to the ground."
    le "Ohaw i ānān!"
    na "The girl leaps forward from the branch and catches me mid-air."
    na "Perhaps it's because of the planet's reduced gravity, but we seem to float down, rather than fall."
    na "Or maybe I'm just relieved that I'm not going to die."

    #landing on ground SFX

    le "Ikah iwi uam eh? Anomom eli?"
    na "A thought occurs to me. My translator implant should be kicking in..."
    na "It's not English. Or Lucoan, or Halcynth either. She must be speaking a language the system doesn't recognize."
    mc "S-Sorry, can you say that again?"
    na "I need her to keep speaking. Any second now it should begin to translate her words."
    le "Ohaw i ānān!"
    le "Did you break anything? No broken bones, right?"
    na "Finally, my implant starts to work and I can understand her words."
    na "I check myself over. Aside from some rope burn and some really sore spots, I seem to be alright."
    mc "I'm okay. Mostly."
    na "There's the issue of my ship, too."
    na "I look around but I don't see it. It must have come down some distance away."
    le "Good! I'm glad you're okay."
    mc "Thanks for cutting me down. I didn't think there'd be any other humans this far out."
    mc "What sector are we in anyway?"
    le "'Sector'? 'Human'? What are those?"
    mc "Uh..."
    mc "Ah! Y-You're..."
    le "Hm?"
    na "At first glance the girl appears to be human but..."
    na "There's a pair of horns on this girl's head. Honest-to-goodness horns, like you'd see on a goat or a ram."
    mc "H-Horns..."
    le "Oh? Oh! You don't have any horns? They must have broken off in the crash. You poor thing."
    mc "N-No, wait! I never had any horns to begin with! I'm human!"
    na "The girl thinks for a moment."
    le "Okay! Hello, Human! It's nice to meet you. I'm Leona!"
    le "Come on, you must be a new arrival! I'll take you back to the city!"
    le "Welcome to Fireside!"
    mc "Fireside?"
    le "Yeah, you know? Cuz' of the cozy warmth given by the planet's position in the binary system?"
    le "When we finally vote on a name, I think we should give it one that sounds cozy!"
    mc "Fireside."
    mc "Hang on. What planet do you think I'm from again?"

    le "Oh man, you must have hit your head. I should definitely take you to the city and get you patched up."
    mc "Hold on..."
    le "We're from Dawne, a few light years away from here. This is our first colony!"
    mc "I'm trying to tell you, I'm not one of... you guys."
    mc "I'm from another planet. And my name isn't 'Human', it's 'Raine'!"
    le "..."
    na "Finally, it hits her."
    le "You're... an alien?"
    mc "No, I'm --"
    na "Wait, yeah. She's right. I'm technically the alien here."
    le "You mean you're not from Dawne? You're from...somewhere else?"

    mc "Yeah. I'm from a planet called Lumin. Ever heard of it?"
    le "That's not a planet I've heard of... How far away are you from home?"
    mc "I don't really know. My ship had all the info, but it crashed."
    le "Ah, so that's what that thing was!"
    mc "You've seen it?"
    le "Yeah, my team saw something enter the atmosphere a while ago, so they went to check it out."
    le "Lucky for me, I saw something else falling from the ship."
    le "And look what I found! An honest-to-goodness alien!"
    le "Though, I've never seen an alien look so much like me before..."
    mc "Likewise, actually."

    le "Well, let's get you to my place. We should really make sure you're okay."
    na "Thankfully, Leona has a ride back into town, a primitive hoverbike with extra space for me and the few meager belongings I had on my person."
    na "For a second, I thought we'd be walking the whole way back."
    na "After a relatively short trip, we arrive."

    le "We're here!"
    na "Leona disembarks, helping me down from the bike."
    le "Welcome to the city of Aster!"
    na "The city is a massive sprawl, all centered on a large tower about a mile away."
    mc "What's that tower?"
    le "That's the colony ship we arrived on several decades ago! Nowadays it's been refitted as a government office and communications relay."
    mc "Decades? So this is a new colony?"
    le "More or less. I was born here, so I hear a lot of stories about our homeworld."
    le "But this place is growing a lot! We want to expand to make another small city out west for some researchers and stuff."
    le "That's where I come in! I help survey and explore new areas that we might be able to live in!"
    mc "By yourself?"
    le "Nah, I've got a whole crew who helps out. Maybe you'll meet them!"
    na "Leona goes on for a few more minutes about her background and past expeditions while I silently nod and listen."
    na "While our civilization made first contact centuries ago, I don't think Leona's species has ever been encountered."
    na "We've mostly encountered non-humanoid species, so for Leona to look so humanlike is really surprising."
    na "We arrive at what appears to be a small first-aid station a few minutes later."
    le "All right, we're here!"
    le "Hey, stay here, Raine. I'll get you something that'll make you feel better instantly!"
    na "She returns with gauze and a strange paste."
    le "Okay, hold still…"
    na "She takes the paste and applies it to my scraped knee."
    mc "Ow!"
    le "Easy there, just give it a bit."
    na "It stings a lot, but it's quickly replaced by a soothing sensation."
    na "She carefully places the gauze on top and massages it, letting the paste underneath stick to it."
    na "She's clearly done this before."
    le "Feeling better? You okay?"
    na "She gives me a tender look, like a mother looking after her kid."
    na "All for someone she just met."
    na "It's… really sweet."
    mc "Yeah, the pain's pretty much gone now."
    le "Great! So, I was thinking... you'll need a place to stay, right?"
    mc "You're not wrong. I don't know where my ship is, so I can't exactly leave just yet."
    le "Well, why don't you rest at my place, then? We can try to find your ship tomorrow."
    na "After the various traumas of today, I think I deserve a break."
    mc "Sure. I could use the rest."
    le "Right, then! Hop on and I'll take you home!"
    na "Entering the large gate to the city, we travel down the main street, turning at an intersection. It only takes us a few more minutes to reach her house."
    #show bg_leonahouse


    le "Ta-dahhh! Welcome to my little plot of land."
    na "While it looks like one of those old prefabricated shelters, the inside is surprisingly cozy."
    na "There's a shelf of knick-knacks, a messy pile of papers on a desk, and a small kitchenette in the corner."
    le "Oh, you'll probably --"
    na "I immediately target the bed, or what I assume to be the bed -- a pile of cushions and blankets seems to be where Leona sleeps."

    #POMF

    na "Without another word, I flop down onto the 'bed' and turn to Leona."
    mc "I'm going to sleep for a bit. Sorry."
    le "No problem! Sleep well!"
    na "It doesn't take much effort before I pass out completely."

    #iris close

    na "But before I do, I hear something."
    le "Logdate 2301: Today was interesting. I found an alien! She -- or at least, I think it's a she -- crash-landed..."
    na "How funny. Guess she isn't that much different from the girls on my home planet if she keeps a diary."

    jump scene_3
