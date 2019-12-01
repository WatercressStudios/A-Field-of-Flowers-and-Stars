label scene_3:

    #iris open
    scene house with dissolve
    play env "amb/Leonas house.ogg"

    na "I wake up to an unfamiliar place. Some kind of hut?"
    na "Oh, wait. I remember now. I crash-landed."
    na "I met an alien named Leona before immediately falling asleep."
    na "Where is she, by the way?"

    #movement SFX
    play sound "sfx/footsteps 2.ogg"

    show le happy a1 at stage_right with dissolve
    #voice "voice/3-scene_3-1.ogg" #Leona (Dot)
    le "Hey Raine! You awake? You've been out for a long time, the sun just came up!"

    #voice "voice/3-scene_3-2.ogg" #Raine (Nat)
    mc unimpressed  "Yeah, I'm kind of a heavy sleeper. How long was I out for?"

    #voice "voice/3-scene_3-3.ogg" #Leona (Dot)
    le curious "About sixty ticks or so."

    #voice "voice/3-scene_3-4.ogg" #Raine (Nat)
    mc questioning "Sixty... hours?"

    #voice "voice/3-scene_3-5.ogg" #Leona (Dot)
    le speakingsurprised a1 "I don't know what an 'hour' is, but you've been out the entire evening."
    na "Ah, it makes sense that they'd had some different units of measurement."
    na "So assuming I landed mid-afternoon, I've probably been out for sixteen hours, give or take."

    #voice "voice/3-scene_3-6.ogg" #Raine (Nat)
    mc unimpressed "I see."

    #voice "voice/3-scene_3-7.ogg" #Leona (Dot)
    le speaking a1 "No problem! Want some food? I'm cooking some stuff right now if you want some!"
    na "The smell of oil and vegetables cooking in a pan is unmistakable."

    #stomach growl SFX

    play sound "sfx/stomach.ogg"
    na "My stomach immediately begs for something edible."


    #voice "voice/3-scene_3-8.ogg" #Raine (Nat)
    mc surprised "Sure, I'd like that."

    #voice "voice/3-scene_3-9.ogg" #Leona (Dot)
    le smug a3 "One plate of grub, coming up!"
    hide le with easeoutright
    na "A few moments later, and Leona slides a dish onto the table."
    na "It's a strange collection of what appears to be purple disks, a deep orange-colored fried egg, and... white jelly?"

    #voice "voice/3-scene_3-10.ogg" #Raine (Nat)
    mc questioning "What's this?"

    #voice "voice/3-scene_3-11.ogg" #Leona (Dot)
    show le happy speaking at stage_right with easeinright
    le "Let's see... sliced inop root, some o'eke'ke, and fresh iwaiwa eggs!"
    na "Huh… those didn't translate. I don't know what these could actually be."
    show le kind a2 with dissolve
    na "Despite the alien nature of these, it smells really good."
    na "Food is food. If we share similar biology then this should go down without much of a fuss, right?"

    #voice "voice/3-scene_3-12.ogg" #Raine (Nat)
    mc "Thanks for the meal, Leona."
    show le relaxed with dissolve
    #voice "voice/3-scene_3-13.ogg" #Raine (Nat)
    mc "..."

    #voice "voice/3-scene_3-14.ogg" #Raine (Nat)
    show le surprised
    mc blech "Blech!" (what_size = 48) with vpunch

    #voice "voice/3-scene_3-15.ogg" #Raine (Nat)

    mc shocked m2 "This inop root... it's so spicy!"
    na "I can't even chew it without an intense wave of heat burning my tongue. "

    #voice "voice/3-scene_3-16.ogg" #Leona (Dot)
    le concerned "Spicy? What do you mean?"

    #voice "voice/3-scene_3-17.ogg" #Raine (Nat)
    mc onfire "Mouth... on f-fire..."

    #voice "voice/3-scene_3-18.ogg" #Leona (Dot)\

    show le concerned onlayer master:
        subpixel True xpos 0.75 xanchor 0.5 yanchor 1 zoom 1.21 rotate None
        parallel:
            xpos 0.75
            linear 0.3 xpos 0.64
        parallel:
            ypos 0
            ease_back 0.2 ypos 1294
            ease_back 0.4 ypos 37
        parallel:
            zoom 1.21
            ease_back .5 zoom 1.76
    le "Oh no!"
    hide le with easeoutright
    na "She runs to the sink for a glass of water and— "
    scene black with vpunch
    na "—splashes my mouth — and the rest of my face — with it."
    scene house with Dissolve(2.0)
    #voice "voice/3-scene_3-19.ogg" #Raine (Nat)
    mc  annoyed "Ack! How can you eat that?!?"

    #voice "voice/3-scene_3-20.ogg" #Raine (Nat)
    mc blech "My eyes are watering and my tongue feels like it's swelling up."

    #voice "voice/3-scene_3-21.ogg" #Leona (Dot)
    show le crying2 at stage_right with dissolve
    le crying2 "I don't know! I don't know what you mean by 'spicy'! Inop root is just a..."
    show le concerned with dissolve
    na "Her eyes widen."

    #voice "voice/3-scene_3-22.ogg" #Leona (Dot)
    le "Oh shoot! None of the animals here on this planet will eat this stuff! That must be it!"

    #voice "voice/3-scene_3-23.ogg" #Leona (Dot)
    le "I didn't realize that! I'm so sorry!"
    hide le with dissolve
    na "Apparently she has no concept of spicy foods. Damn, her species must have one helluva tolerance for that stuff."
    na "Well, now's a better time than any to explain some of this stuff to her."
    na "...I don't want a repeat of this. Hell, who knows what food here is perfectly fine for her kind, but absolutely toxic for mine?"
    na "Better safe than sorry."

    #timeskip

    #voice "voice/3-scene_3-24.ogg" #Raine (Nat)
    mc "So that's why it hurts to eat spicy food."

    #voice "voice/3-scene_3-25.ogg" #Leona (Dot)
    le questioning a2 "Wow, that 'capsaicin' stuff must really hurt your species, then."

    #voice "voice/3-scene_3-26.ogg" #Leona (Dot)
    le surprised "Again, sorry about that. I should have thought about it before giving you our food."

    #voice "voice/3-scene_3-27.ogg" #Raine (Nat)
    mc unimpressed "I'm just surprised that your species isn't affected by it."

    #voice "voice/3-scene_3-28.ogg" #Leona (Dot)
    le concerned "Are you still hungry?"

    #voice "voice/3-scene_3-29.ogg" #Raine (Nat)
    mc "Let me try the other food; surely that's not too bad, right?"

    #voice "voice/3-scene_3-30.ogg" #Leona (Dot)
    le "I guess so..."
    na "She nervously looks at me as I take a bite of the o'eke'ke."

    #voice "voice/3-scene_3-31.ogg" #Raine (Nat)
    mc "..."

    #voice "voice/3-scene_3-32.ogg" #Raine (Nat)
    mc surprised "Oh!"

    #voice "voice/3-scene_3-33.ogg" #Raine (Nat)
    mc "It's good!"
    show le happy a1 at stage_right:
        linear .1 yanchor 10
        linear .1 yanchor 0
    na "The o'eke'ke is almost like a custard or pudding. It's very sweet."

    #voice "voice/3-scene_3-34.ogg" #Leona (Dot)
    le happy2 a1 "Oh, yay!"

    #voice "voice/3-scene_3-35.ogg" #Raine (Nat)
    mc "Now for the egg..."
    #pause 1
    na "My eyes widen. It's incredibly rich, almost like hollandaise sauce."
    na "I quickly wolf it down."

    #voice "voice/3-scene_3-36.ogg" #Raine (Nat)
    mc surprised "Wow, that hit the spot. What's in there?"

    #voice "voice/3-scene_3-37.ogg" #Leona (Dot)
    le explaining "Hm? It's just an egg."

    #voice "voice/3-scene_3-38.ogg" #Raine (Nat)
    mc amused "Sorry, these eggs are... much different than the ones I'm used to."

    #voice "voice/3-scene_3-39.ogg" #Leona (Dot)
    le relaxed "It looks like you can eat those things just fine, though. That's good!"

    #voice "voice/3-scene_3-40.ogg" #Raine (Nat)
    mc "I was worried about that for a second."

    #voice "voice/3-scene_3-41.ogg" #Raine (Nat)
    mc "Glad I won't be starving anytime soon."

    #voice "voice/3-scene_3-42.ogg" #Leona (Dot)
    le happy a2"Need anything else to eat?"

    #voice "voice/3-scene_3-43.ogg" #Raine (Nat)
    mc yawn "I'd love another one of those eggs, actually."

    #voice "voice/3-scene_3-44.ogg" #Leona (Dot)
    le crazy "Coming right up!"

    show le:
        zoom 1.5
        ease_back .5 xpos 1.11

    scene black with fade
    hide le
    #timeskip

    #voice "voice/3-scene_3-45.ogg" #Raine (Nat)
    scene house with Dissolve(2.0)
    mc satisfied "Ahh, that was really good. Thanks for breakfast, Leona."

    #voice "voice/3-scene_3-46.ogg" #Leona (Dot)
    show le relaxed at stage_right with dissolve
    le "I'm glad your fast was broken!"

    #voice "voice/3-scene_3-47.ogg" #Raine (Nat)
    mc neutral "No, that's... what?"

    #voice "voice/3-scene_3-48.ogg" #Leona (Dot)
    le questioning a2 "You were fasting, and now it's broken, right? Is that what that word means?"

    #voice "voice/3-scene_3-49.ogg" #Raine (Nat)
    mc "In the literal sense, I guess. But it's just our name for our morning meal."

    #voice "voice/3-scene_3-50.ogg" #Leona (Dot)
    le happy a1 "Oh, okay!"
    na "She seems to take this in pretty naturally."

    #voice "voice/3-scene_3-51.ogg" #Leona (Dot)
    le smug a3 "Well, then I'm glad I helped!"

    #voice "voice/3-scene_3-52.ogg" #Leona (Dot)
    le curious "That reminds me, you're not from Dawne, but you speak Oleloahak just fine. What's up with that?"

    #voice "voice/3-scene_3-53.ogg" #Raine (Nat)
    mc questioning2 "Oh, I have an implant that automatically translates foreign languages for me. So to me, it sounds like English, but the implant does the talking for your… Oleloahak?"

    #voice "voice/3-scene_3-54.ogg" #Leona (Dot)
    le explaining "I see. That's some impressive technology. Your civilization must be quite advanced!"
    #voice "voice/3-scene_3-55.ogg" #Raine (Nat)
    mc neutral "Yeah, we made a lot of settlements after our native solar system was colonized."
    show le happy a1 with dissolve
    #voice "voice/3-scene_3-56.ogg" #Raine (Nat)
    mc speaking "A few centuries after that we finally mastered the use of faster-than-light travel and we've been expanding ever since."

    #voice "voice/3-scene_3-57.ogg" #Raine (Nat)
    mc "Unfortunately, I didn't get here by FTL travel, though. I got here through a wormhole. Honestly, I'm pretty amazed that I survived the whole ordeal."
    hide le with dissolve
    na "I need to get Juneau back as soon as possible. Wormholes aren't exactly the most stable things in the universe - who knows when this one will close."

    #voice "voice/3-scene_3-58.ogg" #Leona (Dot)
    show le curious at stage_right with dissolve

    le "Woah, wormholes? Those super-unstable gravity wells?"

    #voice "voice/3-scene_3-59.ogg" #Leona (Dot)
    le suspicious a2 "Yeah, you should have died."

    #voice "voice/3-scene_3-60.ogg" #Raine (Nat)
    mc sighing "Y-Yeah..."

    #voice "voice/3-scene_3-61.ogg" #Leona (Dot)
    le questioning a3 "Ah, sorry! What I meant to say is that you're extremely lucky. None of our tests with wormholes have proved successful."

    #voice "voice/3-scene_3-62.ogg" #Leona (Dot)
    le "I'm surprised you took a ship through one to begin with."

    #voice "voice/3-scene_3-63.ogg" #Raine (Nat)
    mc "I didn't really have a choice. I ran into one while I was flying."

    #voice "voice/3-scene_3-64.ogg" #Raine (Nat)
    mc "When I exited the wormhole, I was close to Fireside. My whole system shut down, so I was forced to land.."

    #voice "voice/3-scene_3-65.ogg" #Leona (Dot)
    le surprised "Wow, that's a lot."

    #voice "voice/3-scene_3-66.ogg" #Leona (Dot)
    le kind a2"I'm just glad you're okay after all of that."

    #voice "voice/3-scene_3-67.ogg" #Leona (Dot)
    le concerned "You even went through a wormhole! I never thought that would be possible."

    #voice "voice/3-scene_3-68.ogg" #Raine (Nat)
    mc "Yeah... I guess so."
    play sound "sfx/get up.ogg"
    show le smirk a2 with dissolve

    na "Leona suddenly stands up."

    #voice "voice/3-scene_3-69.ogg" #Leona (Dot)
    le happy speaking a3 "So, I think it's high time I took you on a short tour of Aster!"
    na "Wow, she accepted all of that pretty quickly."

    #voice "voice/3-scene_3-70.ogg" #Leona (Dot)
    le "If you're going to be with us, you might as well make yourself at home, right?"

    #voice "voice/3-scene_3-71.ogg" #Raine (Nat)
    mc "Umm..."
    na "I honestly don't want to stay any longer than I have to. Leona's a wonderful host, but planetary life just isn't for me."

    #voice "voice/3-scene_3-72.ogg" #Raine (Nat)
    mc "Maybe later."

    #voice "voice/3-scene_3-73.ogg" #Leona (Dot)
    le sassyquestioning "Don't you want to go outside? You can't stay cooped up in here forever..."

    #voice "voice/3-scene_3-74.ogg" #Raine (Nat)
    mc happy "Once I fix my ship, I'll be fine."

    show le surprised:

    na "Leona perks up at the mention of my ship."

    #voice "voice/3-scene_3-75.ogg" #Leona (Dot)
    le "Oh, that's right! While you were out, my crew managed to track down the ship."

    #voice "voice/3-scene_3-76.ogg" #Raine (Nat)
    mc "R-Really?"

    #voice "voice/3-scene_3-77.ogg" #Leona (Dot)
    le explaining"Yeah, they've moved it to the base."

    #voice "voice/3-scene_3-78.ogg" #Raine (Nat)
    mc "Well then, what are we waiting for?"

    #voice "voice/3-scene_3-79.ogg" #Leona (Dot)
    le sassyquestioning "Oh? Didn't you just say you could wait until later?"
    na "Leona's giving off the cheekiest grin. She knew I'd jump at this opportunity."

    #voice "voice/3-scene_3-80.ogg" #Raine (Nat)
    mc "I've... changed my mind. Let's go."

    #voice "voice/3-scene_3-81.ogg" #Leona (Dot)
    le smirk a2 "All right!"
    scene black with fade
    scene street onlayer master with wiperight:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.25
            ease 20 xpos 0.85
    stop env fadeout 2.0
    play sound3 "amb/City Day.ogg" fadein 2.0

    na "Leona's neighborhood is full of people just like her, with different horn shapes and a variety of builds."
    na "They're super similar to humans, minus the whole 'having horns' part."
    na "Were I more interested in xenobiology, I'd certainly be interested in how they grow. Are they part of the skull, or are they more like antlers?"

    #voice "voice/3-scene_3-82.ogg" #Leona (Dot)
    show le explaining at le_side with dissolve

    le "And there is Xennia's place, who has the best vegetables this time of year, and over there's my mechanic's house..."
    na "Meanwhile, Leona is dragging me around, pointing at various buildings and landmarks without a care in the world."

    #voice "voice/3-scene_3-83.ogg" #Raine (Nat)
    mc "Just how far away is this base of yours?"

    #voice "voice/3-scene_3-84.ogg" #Leona (Dot)
    le speakingsurprised a1 "Oh, right across the street from my house!"

    #voice "voice/3-scene_3-85.ogg" #Raine (Nat)
    mc "Wait, aren't we walking away from it, then?"

    #voice "voice/3-scene_3-86.ogg" #Leona (Dot)
    le happy a2"Yep!"

    #voice "voice/3-scene_3-87.ogg" #Raine (Nat)
    mc "..."

    #voice "voice/3-scene_3-88.ogg" #Leona (Dot)
    le suspicious a2 "...?"

    #voice "voice/3-scene_3-89.ogg" #Raine (Nat)
    mc "Can I see my ship?"

    #voice "voice/3-scene_3-90.ogg" #Leona (Dot)
    le questioning p2 "Oh! Right, just this way!"

    stop sound3 fadeout 2.0
    scene black with fade

    return
    #jump scene_4
