label scene6:

    scene black with dissolve #return to this later regarding coding in blackness or whater
    play sound "sfx/footsteps 2.ogg"
    show le happy a1 with dissolve:
        xalign 0.5
    #voice "voice/6-scene6-1.ogg" #Leona (Dot)
    le "See? It's not {i}that{/i} hot."
    #voice "voice/6-scene6-2.ogg" #Raine (Nat)
    mc surprised "It has to be at least 35c in here!"
    show le happy speaking a2 with dissolve
    "Whatever that means. I think it's nice 'n' toasty."
    #voice "voice/6-scene6-3.ogg" #Leona (Dot)
    le "Much better than outside, it's always freezing out there."
    #voice "voice/6-scene6-4.ogg" #Raine (Nat)
    mc unimpressed "I think I'd rather be out there in the direct sunlight, thanks."
    #voice "voice/6-scene6-5.ogg" #Raine (Nat)
    mc "Besides, if you think it's freezing outside, you'd hate Lumin."
    #voice "voice/6-scene6-6.ogg" #Leona (Dot)
    le questioning a3 "The sun and exercise is good for you! You're so pale... and thin? What's a good word for it...?"
    show le happy speaking a2 with hpunch:
        xalign 0.5
    na "Leona pokes at my arms through the shroud of darkness." #later program some kind of screenshake or vpunch maybe
    #voice "voice/6-scene6-7.ogg" #Raine (Nat)
    mc blech "NYuUugH, no touchy. I can already feel my skin crawling, it's so humid in here."
    #voice "voice/6-scene6-8.ogg" #Raine (Nat)
    mc blech "Please, PLEASE tell me there’s no blood-sucking bugs in here, eyuckh..."
    hide le questioning a3 with dissolve
    na "Leona and I make our way through the deep, deep cave."
    play sound "sfx/footsteps.ogg"
    na "The floor is rocky and uneven, slippery with some sort of slimy mess. I can barely keep my footing, not to mention the awful smell."
    #voice "voice/6-scene6-9.ogg" #Raine (Nat)
    mc questioning2 "How does a species from a bright desert planet even get off having such good night vision anyway?"
    show le explaining with dissolve:
        xalign 0.5
    #voice "voice/6-scene6-10.ogg" #Leona (Dot)
    le "I dunno. I've always liked small, dark corners, but so does everyone else I know."
    #voice "voice/6-scene6-11.ogg" #Leona (Dot)
    le explaining "Mom always said Dad loved these sorts of places when the colony arrived."
    #voice "voice/6-scene6-12.ogg" #Raine (Nat)
    mc sighing "I'll take your word for it..."
    na "I give a small sigh as we move deeper in."
    #voice "voice/6-scene6-13.ogg" #Leona (Dot)
    le concerned "Are you sure you don't want to use the flashlight?"
    #voice "voice/6-scene6-14.ogg" #Raine (Nat)
    mc thankful "It's fine, I can't tell how much charge the battery has in it anyway. Better to save it for an emergency."
    #voice "voice/6-scene6-15.ogg" #Raine (Nat)
    mc happy "I mean, I've got you! Be my eyes. Can't think of anyone else better suited to lead us through a dark, damp, disturbing tunnel."
    #voice "voice/6-scene6-16.ogg" #Leona (Dot)
    le questioning a2 "Hmm... Oh!"
    #voice "voice/6-scene6-17.ogg" #Leona (Dot)
    le happy speaking a3 "I found the word I was looking for. You’re scrawny!"
    #voice "voice/6-scene6-18.ogg" #Raine (Nat)
    mc annoyed "I'll show you scrawny, ya dingbat."
    #voice "voice/6-scene6-19.ogg" #Leona (Dot)
    le sassyquestioning "Oho? And how will you do that?"
    na "A playful smirk comes across my face."
    #voice "voice/6-scene6-20.ogg" #Raine (Nat)
    mc satisfied "Let's just say I have a little secret."
    #voice "voice/6-scene6-21.ogg" #Leona (Dot)
    le curious "I like secrets. Tell me."
    #voice "voice/6-scene6-22.ogg" #Raine (Nat)
    mc questioning "Do you remember when you cut me down out of that tree?"
    #voice "voice/6-scene6-23.ogg" #Raine (Nat)
    mc "Specifically the part when you jumped to catch me?"
    #voice "voice/6-scene6-24.ogg" #Leona (Dot)
    le questioning p2 "Yeah, what of it?"
    #voice "voice/6-scene6-25.ogg" #Raine (Nat)
    mc questioning "Well, something about that seemed off."
    #voice "voice/6-scene6-26.ogg" #Raine (Nat)
    mc "I thought it was just the adrenaline at the time, but it didn't seem like we fell very hard."
    #voice "voice/6-scene6-27.ogg" #Leona (Dot)
    le concerned "...I don't follow."
    #voice "voice/6-scene6-28.ogg" #Raine (Nat)
    mc questioning2 "Are there any rocks you can pick up around us?"
    #voice "voice/6-scene6-29.ogg" #Leona (Dot)
    le "Plenty."
    #voice "voice/6-scene6-30.ogg" #Raine (Nat)
    mc satisfied "Grab two that are roughly the same size and weight and hold onto them for me."
    #voice "voice/6-scene6-31.ogg" #Raine (Nat)
    mc "Once we get out of here, remind me to show you how good my throwing arm is."
    #voice "voice/6-scene6-32.ogg" #Leona (Dot)
    le curious "Weird, but alright."
    hide le curious with dissolve
    na "We continue our trek into the caves, the air growing ever more humid."
    na "As we navigate the caves, the temperature slowly drops and damp water settles on my skin."
    na "Great, first it was hot and now I'm nearly shivering."
    na "Leona continues forward, ahead of me. I walk quietly and carefully behind her, trusting her as the expert here."
    na "I may be able to navigate an asteroid belt and maneuver around a pulsar, but down here, she's queen."
    na "She's a little airheaded, but… she knows what she's doing. I have more faith in her than I do myself in a place like this."
    show le suspicious a2:
        xpos -0.5
        easein 1.0 xpos 0.3
    #voice "voice/6-scene6-33.ogg" #Leona (Dot)
    le "Smell that?"
    #voice "voice/6-scene6-34.ogg" #Raine (Nat)
    mc questioning2 "What?"
    show le happy a2:
        xalign 0.5
        bounce
    "Rust! We're getting close to something." #i wanted to put a bounce but couldnt figure out the right format since i keep getting errors
    #voice "voice/6-scene6-35.ogg" #Raine (Nat)
    mc neutral "I can't smell anything. Maybe a little bit of sulphur from the caves, but that's it." 
    hide le with easeoutright
    na "But, if she's right about the rust, then we're getting close to something man made."
    na "Er, well. Not {i}man{/i} made. Alien made?"
    na "Artificial. Let's go with that. Speaking of…"
    na "A glint on the cave wall catches my eye."
    na "Bioluminescence? A button or lightbulb covered in something?"
    na "I move off, my curiosity getting the better of me. It's probably just my mind playing tricks on me."
    na "It's like… some sort of glowing moss? Something sticking out of the wall?"
    na "Putting my hand on it, I feel something give way, ever so slightly, and hear a small click from further inside."
    #voice "voice/6-scene6-36.ogg" #Raine (Nat)
    mc "Hey, I think I found something--"



    ###
   # BG goes completely dark, just a black screen. Maybe a spooky cave sound effect?
    ###

    na "And then, the light fades from sight."
    na "..."
    #voice "voice/6-scene6-37.ogg" #Raine (Nat)
    mc shocked armraised "Leona?"
    na "..."
    na "Where'd Leona go?"
    na "Crap, I should have said something. Rule number one: Stay with the guide!"
    na "Okay, okay, okay, let's think about this."
    na "When lost, those who wander are dead. If I sit still Leona will notice that I'm gone, and come and find me."
    na "She can probably smell me, too."
    na "I'm tempted to yell out, but maybe that'd confuse her? I'm sure my voice echoing through the cave would hurt her little goat ears."
    na "But, then again, if I yell out, she'd know that I'm not with her."
    na "Screw it."
    #voice "voice/6-scene6-38.ogg" #Raine (Nat)
    mc shocked m2 "...Leona? I, uhh, I think I'm lost."
    na "Stay calm. A clear, moderate voice will travel without confusing her."
    #voice "voice/6-scene6-39.ogg" #Raine (Nat)
    mc thankful "I'll stay put, okay?"
    na "I get no answer."
    na "It's so dark that I can't even see my hand in front of me."
    na "Flashlight, emergency!"
    na "Just gonna grab it out of the bag and-"
    na"-and..."
    na "...Leona has my bag."
    na "I gave it to her before we came in so I wouldn't snag it on anything. Son of a bitch!"
    na "I hold onto the wet, slightly slimy wall to keep my bearings."
    na "The last thing I want to do is walk around and lose the one thing grounding me."
    na "Well, more than I already have."
    na "My breath becomes more tense as it bounces around the chamber and my head begins to spin with worry."
    na "After everything I've been through, this is what gets me, huh?"
    na "Surviving many, many years in the cold vacuum of space, falling through a wormhole onto an alien planet, only to die alone in a cold, wet cave."
    na "I sit down, holding my legs in front of me, leaning back on the wall."
    na "You're such a moron, Raine..."
    na "Stupid little girl always pawning off her responsibilities to others."
    na "Maybe Juneau is right; I am just a lazy ass."
    na "Just a pathetic girl who can't get anything fucking done on her own."
    na "..."
    na "I feel tears fall from my eyes, as quiet sobs echo through the cavern."

    ###
    #Pause for effect.
    #ART - Load Cave1 BG but really dark (Cave1 BG just cave, not the same as Cave2BG which has the door and panel and whatnot.)
    #VFX - slowly increase the light
    ###

    na "Slowly, the cave begins to light up. A figure enters the tunnel to my right, its radiance blinding me."
    #voice "voice/6-scene6-40.ogg" #Raine (Nat)
    mc shocked m2  "Leona!?"
    show le concerned:
        xpos -0.5
        easein 1.0 xpos 0.3
    #voice "voice/6-scene6-41.ogg" #Leona (Dot)
    le "RAINE!"
    na "She dashes over to me and pulls me into her arms, squeezing me tightly with all of her strength."
    #voice "voice/6-scene6-42.ogg" #Leona (Dot)
    le sad "Are you okay? Are you hurt? I'm so sorry! I should have been paying more attention, I'm sorry, I'm sorry, I'm so sorry!"
    #voice "voice/6-scene6-43.ogg" #Leona (Dot)
    le concerned "Need something to drink? Something to eat? Need a break? You're not hurt, right?"
    #voice "voice/6-scene6-44.ogg" #Raine (Nat)
    mc thankful "I-ack! I'm fine! Just a little cold!"
    na "She tightens her grip on me, crushing me a little."
    na "Maybe I should follow her advice and bulk up a bit..."
    na "Leona produces a blanket from her pack, wiping me down and wrapping it gently around my shoulders."
    #voice "voice/6-scene6-45.ogg" #Leona (Dot)
    le sad_lee "I was so worried…"
    show le crying with dissolve
    na "She looks at me with a pained expression, her breathing erratic and her heart beating fast. I think she's about to cry."
    na "Crap, now I feel bad."
    #voice "voice/6-scene6-46.ogg" #Raine (Nat)
    mc "No, it's my fault. I'm stupid. We should have used the flashlight from the start, I should have stuck with you, and said something rather than just walking away."
    #voice "voice/6-scene6-47.ogg" #Raine (Nat)
    mc "I guess I'm just used to doing stuff on my own."
    #voice "voice/6-scene6-48.ogg" #Leona (Dot)
    le "It's okay, it's okay. I'm just happy you're okay. You're with me now, right?"
    #voice "voice/6-scene6-49.ogg" #Raine (Nat)
    mc sighing "R-right."
    na "She pulls me back in, and we share a quiet embrace."
    #voice "voice/6-scene6-50.ogg" #Raine (Nat)
    mc thankful "Thank you, Leona. If it weren't for you, I'd be a goner."
    na "Leona remains quiet, attached to me."
    na "I really do have to rely on her. Not only is she my ticket out of here, but…"
    na "I don't have to go it alone."
    na "I am with her, now."
    na "Slowly, she catches her breath and lets go, however reluctantly."
    #voice "voice/6-scene6-51.ogg" #Leona (Dot)
    le relaxed "So, uh…"
    #voice "voice/6-scene6-52.ogg" #Raine (Nat)
    mc questioning2"Yeah?"
    #voice "voice/6-scene6-53.ogg" #Leona (Dot)
    le kind a2 "Please hold my hand."
    #voice "voice/6-scene6-54.ogg" #Raine (Nat)
    mc "R-Right."
    hide le kind a2 with easeoutright

    ###
    #ART - CaveBG2 (the one with the door and panel)
    ###
    scene cave with Dissolve(2.0) 
    na "After about half an hour of walking, we finally reach our destination; a large alcove with a door and panel at the very back of the cave. "
    na "Everything here looks to be scaled up compared to human or dawnese standards."
    na "Whoever built this must have been pretty tall."
    show le happy a2 with dissolve:
        xalign 0.5
    "Here we go!"
    #voice "voice/6-scene6-55.ogg" #Raine (Nat)
    mc questioning2 "Yeah, this is a biggun. Why would anyone build something like that inside a cave though?"
    #voice "voice/6-scene6-56.ogg" #Leona (Dot)
    le curious "Maybe they needed to hide something in it? It's weird that they'd leave this crate outside though."
    #voice "voice/6-scene6-57.ogg" #Raine (Nat)
    mc "Why all the effort if you're just gonna leave the goods where anyone can waltz in and snatch it up?"
    #voice "voice/6-scene6-58.ogg" #Leona (Dot)
    le "What if they had to leave in a hurry? Maybe they left something special here?"
    na "I rummage around in the half-rotten box, in search of treasure."
    #voice "voice/6-scene6-59.ogg" #Raine (Nat)
    mc questioning "Nope, I don't think that's it."
    #voice "voice/6-scene6-60.ogg" #Raine (Nat)
    mc "The whole thing smells like crap, and the only thing I've found so far is some old books."
    #voice "voice/6-scene6-61.ogg" #Raine (Nat)
    mc "Yeah, you have fun with that. I'll take a crack at this big ol' door I guess."
    na "As Leona gingerly flips through muddied pages, I saunter towards the panel adjacent to the metal behemoth."
    na "It's a digital lock alright. I'd be surprised if it still had any juice left in it."
    #voice "voice/6-scene6-62.ogg" #Raine (Nat)
    mc "One thing's for sure, this control panel's as old as dirt. Wanna take a guess at how long it's been here?"
    show le happy a2 with dissolve:
        align 0.5
        bounce
    #voice "voice/6-scene6-63.ogg" #Leona (Dot)
    le "Books? Lemme see!"#vary it up a bit here
    #voice "voice/6-scene6-64.ogg" #Raine (Nat)
    mc "Yeah, you have fun with that. I'll take a crack at this big ol' door I guess."
    hide le happy a2 with dissolve
    na "As Leona gingerly flips through muddied pages, I saunter towards the panel adjacent to the metal behemoth."
    na "It's a digital lock alright. I'd be surprised if it still had any juice left in it."
    #voice "voice/6-scene6-65.ogg" #Raine (Nat)
    mc "One thing's for sure, this control panel's as old as dirt. Wanna take a guess at how long it's been here?"
    #voice "voice/6-scene6-66.ogg" #Leona (Dot)
    le questioning a3 "A while?"
    na "Leona continues to study her books, eyes only occasionally glancing back in my direction."
    #voice "voice/6-scene6-67.ogg" #Leona (Dot)
    le "At least a few decades? With all the rot and stuff."
    #voice "voice/6-scene6-68.ogg" #Leona (Dot)
    le curious "What do you think?"
    #voice "voice/6-scene6-69.ogg" #Raine (Nat)
    mc satisfied "Spitballing it, a couple hundred years or so?"
    #voice "voice/6-scene6-70.ogg" #Raine (Nat)
    mc "The point is this has been here for a long, long time."
    #voice "voice/6-scene6-71.ogg" #Leona (Dot)
    le speakingsurprised a1 "So whatever's inside might still be in good condition?"
    #voice "voice/6-scene6-72.ogg" #Raine (Nat)
    mc questioning2 "If it's airtight, probably."
    #voice "voice/6-scene6-73.ogg" #Raine (Nat)
    mc "Hopefully we'll find some amazing stuff! Or garbage, probably garbage."
    #voice "voice/6-scene6-74.ogg" #Raine (Nat)
    mc "Still gotta get it open though. Leona! Could you give me my bag for a second?"
    na "I walk over to Leona, taking the bag in my hand and digging through it."
    #voice "voice/6-scene6-75.ogg" #Raine (Nat)
    mc satisfied "And… there it is!"
    na "I pull out a small energy detector from my bag. It's not as good as the one I had on my ship, but it's fortunate Fireside's tech has this."
    na "I turn it on and scan it around the door."
    #voice "voice/6-scene6-76.ogg" #Raine (Nat)
    mc questioning2 "There's definitely something like a generator behind this, but…"
    #voice "voice/6-scene6-77.ogg" #Raine (Nat)
    mc "There's a lot of energy noise floating around. The detector's going kind of crazy."
    #voice "voice/6-scene6-78.ogg" #Raine (Nat)
    mc "Not a good sign."
    #voice "voice/6-scene6-79.ogg" #Raine (Nat)
    mc "If that generator's unstable this is going to be a lot harder than I'd hoped."
    hide le speakingsurprised a1 with dissolve
    na "If it'll even fit in our ship to begin with. The door's massive, so whatever's inside might be as well."
    na "I move forward to investigate, working through the details in my mind."
    na "There are some bolts bulging out of the door's frame. Giving one a yank proves fruitless."
    na "The rust on the bolt seems to become thinner the closer to the frame it is."
    na "It's almost as if the bolt has slowly been crawling out of it's hole over the years."
    na "Could the room beyond this door be pressurized?"
    na "An imperfect seal on the other side of the bolt could be what's causing it to slide out over time."
    na "But there's no way to tell exactly how much pressure there is."
    #voice "voice/6-scene6-80.ogg" #Raine (Nat)
    mc questioning "Leona, do you have any sort of lubricant I can use here?"
    #voice "voice/6-scene6-81.ogg" #Leona (Dot)
    le curious "Lube? How much do you need? I have a little bit of moisturizer that might work. "
    #voice "voice/6-scene6-82.ogg" #Raine (Nat)
    mc "Just a drop or two will do, I hope."
    #voice "voice/6-scene6-83.ogg" #Leona (Dot)
    le "Show me where you want it."
    #voice "voice/6-scene6-84.ogg" #Raine (Nat)
    mc "See this bolt sticking out of the frame? Put a bit right at the base of the threads."
    #voice "voice/6-scene6-85.ogg" #Leona (Dot)
    le speakingsurprised a1 "There ya go. What are you gonna do with it if it comes out?"
    #voice "voice/6-scene6-86.ogg" #Raine (Nat)
    mc "Just doing an experiment. I doubt we'll be getting inside this door either way."
    #voice "voice/6-scene6-87.ogg" #Raine (Nat)
    mc "The control panel doesn't have any power and I'm not about to waste my flashlight battery on the off chance it's enough to do the trick."
    #voice "voice/6-scene6-88.ogg" #Leona (Dot)
    le "We could come back later with a bike battery. I have a few extras at the garage."
    #voice "voice/6-scene6-89.ogg" #Raine (Nat)
    mc satisfied "Worth a shot."
    #voice "voice/6-scene6-90.ogg" #Raine (Nat)
    mc "Start gathering up whatever you want to keep from that crate, we'll get out of here in a minute."
    #voice "voice/6-scene6-91.ogg" #Leona (Dot)
    le happy a2 "Okey-doke."
    hide le happy a2 with dissolve
    na "Leona returns to her books, and I to my bolt."
    na "I lean in and blow on it a bit, hoping the lubricant will seep in enough to gain leeway."
    na "Then, I grab and pull. When that doesn't work, I try twisting."
    na "With a pop, the bolt comes free and a gentle whistle can be heard coming from the hole."
    na "Just as I'm about to lean back in to see what might be on the other side-"
    play sound "sfx/rustle.ogg"
    na "My ears shoot up at a sound from higher up in the cave."
    na "Something heavy. Stone scrawling against stone, echoing against the walls."
    #voice "voice/6-scene6-92.ogg" #Leona (Dot)
    le surprised "Hey, did you hear that?"
    #voice "voice/6-scene6-93.ogg" #Raine (Nat)
    mc questioning2 "I'd be surprised if I didn't. What the hell was that?"
    #voice "voice/6-scene6-94.ogg" #Leona (Dot)
    le concerned "Ssh! Don't be so loud, please!"
    na "Leona looks around cautiously, keeping her eyes and ears open."
    #voice "voice/6-scene6-95.ogg" #Leona (Dot)
    le suspicious a2 "I think it was back the way we came?"
    #voice "voice/6-scene6-96.ogg" #Raine (Nat)
    mc "Are you sure?"
    #voice "voice/6-scene6-97.ogg" #Leona (Dot)
    le "No, but the cave is just a straight path. One way in, one way out."
    #voice "voice/6-scene6-98.ogg" #Leona (Dot)
    le "I think we should get out of here, just to be safe."
    #voice "voice/6-scene6-99.ogg" #Raine (Nat)
    mc "Do you smell anything?"
    #voice "voice/6-scene6-100.ogg" #Leona (Dot)
    le questioning a3 "What does that matter?"
    #voice "voice/6-scene6-101.ogg" #Raine (Nat)
    mc "It matters. Is there more sulfur than before? Anything that might be a gas?"
    #voice "voice/6-scene6-102.ogg" #Leona (Dot)
    le "No, aside from the sound I think we're fine."
    #voice "voice/6-scene6-103.ogg" #Leona (Dot)
    le concerned "C'mon, let's go back. I'll walk a little bit ahead of you in case we run into something."
    #voice "voice/6-scene6-104.ogg" #Raine (Nat)
    mc "Okay... But don't get too far away. Talk to me so I don't lose you again."
    #voice "voice/6-scene6-105.ogg" #Leona (Dot)
    le "Good idea."
    na "Leona and I quickly gather up the old books she'd set aside and head out."
    hide le concerned with fade 
    scene cave with dissolve
    na "Walking back the way we came, Leona and I got to talking about something she said earlier."
    na "About how everyone she knows including herself likes small, dark corners."
    na "Looking at the city of Aster, and even Leona's home, I can see it. Their architecture is downright utilitarian, edging on brutalist."
    na "She herself isn't too happy about that, saying pictures of cities back on Dawne she saw in school were much more colorful and warm than the grayscale mess here on Aster."
    na "To me, this felt like a contradiction, but as I'm about to say something..."
    #voice "voice/6-scene6-106.ogg" #Raine (Nat)
    mc questioning "Everything alright up there?"
    #voice "voice/6-scene6-107.ogg" #Leona (Dot)
    le happy speaking a3 "Yeah! Just need to check something out, won't take me long!"
    show le happy a2:
        xalign 0.5
        bounce
    #voice "voice/6-scene6-108.ogg" #Leona (Dot)
    le "H-Hey, Raine! Can you stay there for a second?"
    #voice "voice/6-scene6-109.ogg" #Raine (Nat)
    mc questioning "Everything alright up there?"
    #voice "voice/6-scene6-110.ogg" #Leona (Dot)
    le happy speaking a3 "Yeah! Just need to check something out, won't take me long!"
    hide le happy speaking a3 with easeoutright
    na "I look ahead into the darkness."
    na "In the distance… lies a hallway that wasn't there before. With sharp, edged corners, and a green glow illuminating its form."
    #voice "voice/6-scene6-111.ogg" #Raine (Nat)
    mc questioning2 "You'll be alright, right!?"
    #voice "voice/6-scene6-112.ogg" #Leona (Dot)
    le "I'll be fine! Just stay there!"
    play sound "sfx/door.ogg" 
    na "A sudden loud, mechanical grinding forces an audible wince out of me."
    na "About as bad as nails on a chalkboard."
    #voice "voice/6-scene6-113.ogg" #Leona (Dot)
    le speakingsurprised a1 "...Oops. That was louder than I thought."
    #voice "voice/6-scene6-114.ogg" #Raine (Nat)
    mc questioning2 "Everything alright? I think my ears are ringing."
    #voice "voice/6-scene6-115.ogg" #Leona (Dot)
    le concerned "Y-Yeah. God, that hurt."
    #voice "voice/6-scene6-116.ogg" #Raine (Nat)
    mc shocked m2 "Are you alright?! What the hell was that!?"
    #voice "voice/6-scene6-117.ogg" #Leona (Dot)
    le happy a2 "I'm fine, I'm fine! I just had to close a door."
    #voice "voice/6-scene6-118.ogg" #Raine (Nat)
    mc questioning2 "You found a door? Why didn't you just say so?"
    #voice "voice/6-scene6-119.ogg" #Leona (Dot)
    le suspicious a2 "Because... well..."
    na "..."
    #voice "voice/6-scene6-120.ogg" #Raine (Nat)
    mc "...Leona?"
    #voice "voice/6-scene6-121.ogg" #Leona (Dot)
    le explaining "Bodies. We must have done something back in the alcove that opened a door over here."
    #voice "voice/6-scene6-122.ogg" #Leona (Dot)
    le "There was a pile of bones n stuff and I didn't want you to see it."
    #voice "voice/6-scene6-123.ogg" #Raine (Nat)
    mc shocked m2 "Bodies? You mean, like {i}people{/i} bodies?"
    #voice "voice/6-scene6-124.ogg" #Leona (Dot)
    le "I couldn't tell. The room was full of them. Not a pretty sight."
    #voice "voice/6-scene6-125.ogg" #Leona (Dot)
    le sad_lee "I don't think we should open that door again. Ever."
    #voice "voice/6-scene6-126.ogg" #Raine (Nat)
    mc questioning "If you say so..."
    #voice "voice/6-scene6-127.ogg" #Raine (Nat)
    mc questioning2"But now I'm really curious about whoever was here before us."
    #voice "voice/6-scene6-128.ogg" #Raine (Nat)
    mc "At least we know what that noise was."
    #voice "voice/6-scene6-129.ogg" #Leona (Dot)
    le concerned "Can we please move on now? Just knowing what's on the other side of this door is giving me the shivers."
    #voice "voice/6-scene6-130.ogg" #Raine (Nat)
    mc neutral "Yeah, let's go back home. I don't want to hang around any longer either."
    #voice "voice/6-scene6-131.ogg" #Raine (Nat)
    mc "Let's walk together and finish our conversation, okay?"
    #voice "voice/6-scene6-132.ogg" #Leona (Dot)
    le "I'd like that, but before that I'm thinking we should make a little detour on the way home."
    #voice "voice/6-scene6-133.ogg" #Raine (Nat)
    mc questioning2 "Detour? To where?"
    #voice "voice/6-scene6-134.ogg" #Leona (Dot)
    le speaking a1 "There's something I want to check out. These books gave me an idea."
    na "I quickly catch up to Leona, my nerves calming down now that she's beside me once again."
    #voice "voice/6-scene6-135.ogg" #Raine (Nat)
    mc happy "Well, alright. We have daylight to burn anyway. Besides, I have a little present I've been meaning to give you."
    #voice "voice/6-scene6-136.ogg" #Leona (Dot)
    le curious "Oooh, I never get presents!"
    #voice "voice/6-scene6-137.ogg" #Raine (Nat)
    mc satisfied "Then I'm sure you'll love it."
    #voice "voice/6-scene6-138.ogg" #Raine (Nat)
    mc "Now, what were we talking about before? Architecture?"
    #voice "voice/6-scene6-139.ogg" #Leona (Dot)
    le happy a1 "Right, as I was saying, the family and the home are equally important-"
    hide le happy a1 with dissolve

    jump scene7

###
#VFX - JOURNAL ENTRY ADDED - 3
###

