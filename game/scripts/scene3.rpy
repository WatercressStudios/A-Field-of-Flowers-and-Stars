label scene_3:

    #iris open
    scene house with wipeup
    play env "amb/Leonas house.ogg"

    na "As I wake, I feel a mountain of pillows and blankets all around me."
    mc blech "Nhyegh-"
    na "Digging myself out and sitting up, I look around the room and am reminded of my situation."
    na "Leona, was it? What a life saver."
    na "I don't know what I would have done if she didn't show up."
    na "Her and that green healing gunk."
    na "Where is she, by the way?"

    #movement SFX
    play sound "sfx/footsteps 2.ogg"
    play music "music/Aster.ogg" fadein 2.0

    voice "voice/3-scene_3-1.ogg" #Leona (Dot)
    le "Hey Raine! Good morning!"

    show le happy a1 at stage_right with dissolve
    na "Leona emerges from the kitchenette."

    le "You've been out for a long time, the sun just came up!"

    voice "voice/3-scene_3-2.ogg" #Raine (Nat)
    mc satisfied "Yeah, I slept like a rock. How long was I out?"

    voice "voice/3-scene_3-3.ogg" #Leona (Dot)
    le curious "About sixteen hours or so."

    voice "voice/3-scene_3-4.ogg" #Raine (Nat)
    mc questioning "Sixteen? Dang."

    voice "voice/3-scene_3-6.ogg" #Raine (Nat)
    mc unimpressed  "I must have been pretty tired after yesterday."

    voice "voice/3-scene_3-7.ogg" #Leona (Dot)
    le speaking a1 "It's alright, both body and mind need rest after a traumatic experience, you know?"
    le "Want some food? I'm cooking some stuff right now if you want some!"

    na "The smell of oil and vegetables cooking in a pan is unmistakable."

    #stomach growl SFX

    play sound "sfx/stomach.ogg"
    pause 1.0

    le smug a2 "Is that a yes?"


    voice "voice/3-scene_3-8.ogg" #Raine (Nat)
    mc surprised "Sure, I'd like that."

    voice "voice/3-scene_3-9.ogg" #Leona (Dot)
    le smug a3 "One plate of grub, coming up!"
    hide le with easeoutright

    na "A few moments later, and Leona slides a dish onto the table."
    na "It's a strange collection of what appears to be purple disks, a deep orange-colored fried egg, and... white jelly?"

    voice "voice/3-scene_3-10.ogg" #Raine (Nat)
    mc questioning "What's this?"

    voice "voice/3-scene_3-11.ogg" #Leona (Dot)
    show le happy a2 at stage_right with easeinright
    le "Let's see... sliced inop root, some o'eke'ke, and fresh iwaiwa eggs!"
    na "Huh… those didn't translate. I don't know what these could actually be."
    show le kind a2 with dissolve
    na "Despite the alien nature of them, it smells really good."
    na "Food is food. If we share similar enough biology that her medicine works then this should go down without much of a fuss, right?"

    voice "voice/3-scene_3-12.ogg" #Raine (Nat)
    mc "Thanks for the meal, Leona."
    show le relaxed with dissolve
    voice "voice/3-scene_3-13.ogg" #Raine (Nat)
    mc "..."

    voice "voice/3-scene_3-14.ogg" #Raine (Nat)
    show le surprised
    mc blech "Blech!" (what_size = 48) with vpunch

    voice "voice/3-scene_3-15.ogg" #Raine (Nat)

    mc shocked m2 "This… -i-i-in-op ro-ot is… is..."
    na "I can't even chew it without an intense wave of pain coursing through my tongue."

    mc onfire "It’s so spicy… I-I c-can’t!"

    voice "voice/3-scene_3-16.ogg" #Leona (Dot)
    le concerned "What do you mean?"

    voice "voice/3-scene_3-17.ogg" #Raine (Nat)
    mc onfire "Mouth... on f-fire..."

    voice "voice/3-scene_3-18.ogg" #Leona (Dot)\

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
    na "She grabs a glass of water and-"
    scene black with vpunch
    play sound "sfx/water splash.ogg"
    na "-splashes my mouth — and the rest of my face — with it."
    scene house with Dissolve(2.0)
    voice "voice/3-scene_3-19.ogg" #Raine (Nat)
    mc annoyed "Ack! How can you eat that?!?"

    voice "voice/3-scene_3-20.ogg" #Raine (Nat)
    mc blech "My eyes are watering and my tongue feels like it's swelling up."

    voice "voice/3-scene_3-21.ogg" #Leona (Dot)
    show le crying2 at stage_right with dissolve
    le crying2 "I don't know! I don't know what you mean by 'spicy'! Inop root is just a..."
    show le concerned with dissolve
    na "Her eyes widen."

    voice "voice/3-scene_3-22.ogg" #Leona (Dot)
    le frustrated a2 "Oh shoot!"
    le "I forgot, none of the animals here will touch the stuff!"
    le tired "This must be why! I'm so sorry!"

    na "Apparently she has no concept of spicy foods. Damn, her species must have one helluva tolerance for that stuff."
    na "Well, now's a better time than any to explain some of this stuff to her."
    na "...I don't want a repeat of this. Hell, who knows what food here is perfectly fine for her kind, but absolutely toxic for mine?"
    na "Better safe than sorry."

    mc upset "Can I get some more water?"
    le frustrated a2 "The fire isn't out yet?!"
    mc blech "It's out, but it still stings. Drinking water helps."
    le frustratedshout "I see... I'll fetch some more, just a second-"
    hide le with easeoutright

    mc satisfied "Capsaicin is a strange thing, I tell you."
    mc "Some plants use it as a defensive mechanism. It kills insects and causes pain in animals that try to eat it."

    show le concerned at stage_right with easeinright
    le "Here, water."
    mc "Thanks-"
    na "Taking a sip, the burning continues to subside."
    mc unimpressed "Would you believe there are those who actually love this stuff?"
    le surprised "You mean people eat it intentionally?"
    mc "Some can't get enough. I've heard people say some crazy things too."
    mc blech "If it doesn't make you cry, it ain't worth eating."
    mc "Who doesn't want to eat fire?"
    mc speaking "'No pain, no gain.'"
    mc blech "Bunch of idiots, if you ask me."
    mc happy "This root could sell for a lot back home, now that I think about it."

    voice "voice/3-scene_3-26.ogg" #Leona (Dot)
    le shylook "Again, I'm sorry about that. I should have thought about it before giving you our food."

    voice "voice/3-scene_3-27.ogg" #Raine (Nat)
    mc unimpressed "I'm just surprised that your species isn't affected by it."

    voice "voice/3-scene_3-28.ogg" #Leona (Dot)
    le concerned "Are you still hungry?"

    voice "voice/3-scene_3-29.ogg" #Raine (Nat)
    mc "Let me try the other food; surely that's not too bad, right?"

    voice "voice/3-scene_3-30.ogg" #Leona (Dot)
    le "I hope so..."
    na "She nervously looks at me as I take a bite of the o'eke'ke."

    voice "voice/3-scene_3-31.ogg" #Raine (Nat)
    mc "..."

    voice "voice/3-scene_3-32.ogg" #Raine (Nat)
    mc shocked armraised "Oh!"

    voice "voice/3-scene_3-33.ogg" #Raine (Nat)
    mc happy "It's good!"
    show le happy a1 at stage_right:
        zoom 1
        linear .1 yoffset 10
        linear .1 yoffset 0

    na "The o'eke'ke is almost like a custard or pudding. It's very sweet."

    voice "voice/3-scene_3-34.ogg" #Leona (Dot)
    le happy2 a1 "Oh, yay!"

    voice "voice/3-scene_3-35.ogg" #Raine (Nat)
    mc "Now for the egg..."
    #pause 1
    na "My eyes widen. It's incredibly rich, almost like hollandaise sauce."
    na "I quickly wolf it down."

    voice "voice/3-scene_3-36.ogg" #Raine (Nat)
    mc surprised "Wow, that hit the spot. What's in there?"

    voice "voice/3-scene_3-37.ogg" #Leona (Dot)
    le explaining "Hm? It's just an egg."

    voice "voice/3-scene_3-38.ogg" #Raine (Nat)
    mc amused "Sorry, these eggs are... much different than the ones I'm used to."

    voice "voice/3-scene_3-39.ogg" #Leona (Dot)
    le relaxed "It looks like you can eat those things just fine, though. That's good!"

    voice "voice/3-scene_3-40.ogg" #Raine (Nat)
    mc "I was worried about that for a second."

    voice "voice/3-scene_3-41.ogg" #Raine (Nat)
    mc "Glad I won't be starving anytime soon."

    voice "voice/3-scene_3-42.ogg" #Leona (Dot)
    le happy a2 "Need anything else to eat?"

    voice "voice/3-scene_3-43.ogg" #Raine (Nat)
    mc yawn "I'd love another one of those eggs, actually."

    voice "voice/3-scene_3-44.ogg" #Leona (Dot)
    le crazy "Coming right up!"
    stop music fadeout 2.0

    show le at stage_right:
        ease_back .5 xpos 1.11

    scene black with fade
    hide le
    #timeskip

    voice "voice/3-scene_3-45.ogg" #Raine (Nat)
    scene house with Dissolve(2.0)
    mc satisfied "Ahh, that was really good. Thanks for breakfast, Leona."

    $ hide_sides = []
    voice "voice/3-scene_3-46.ogg" #Leona (Dot)
    le relaxed "Break fast? Is that a religious thing?"

    voice "voice/3-scene_3-47.ogg" #Raine (Nat)
    mc thankful "It's just our name for our morning meal."
    mc "We eat 3 times a day, give or take."

    voice "voice/3-scene_3-48.ogg" #Leona (Dot)
    le questioning a2 "Oh, okay!"
    le "We do something similar, but don't have names for them."

    na "She seems to take all this in pretty naturally."

    le happy a2 "Well, I'm glad you can at least eat some of our food!"

    le speakingthink "That reminds me, you're not from Dawne, but you speak Oleloahak just fine. What's up with that?"

    voice "voice/3-scene_3-49.ogg" #Raine (Nat)
    mc speaking "Oh, I have an implant that automatically translates foreign languages for me. So to me, it sounds like English, but the implant does the talking for your… Oleloahak?"

    voice "voice/3-scene_3-50.ogg" #Leona (Dot)
    le happy a1 "I see. That's some impressive technology."

    voice "voice/3-scene_3-51.ogg" #Leona (Dot)
    le smug a3 "I wonder what other goodies you have that we don't?"

    mc happy "Yeah, we're a pretty curious species. We've got a lot of different things figured out."

    mc sighing "Including personal space flight."

    mc "Unfortunately, I didn't get here by normal space travel."
    mc surprised "I got here through a wormhole. Honestly, I'm pretty amazed that I survived the whole ordeal."
    na "I need to get Juneau back as soon as possible. Wormholes aren't exactly the most stable things in the universe."
    na "Chances are it closed the moment I was spit out by it."

    voice "voice/3-scene_3-58.ogg" #Leona (Dot)
    le curious "Are you really telling me you went through a wormhole to get here?"

    voice "voice/3-scene_3-59.ogg" #Leona (Dot)
    le suspicious a2 "Anything could’ve happened. You could have... You know..."

    voice "voice/3-scene_3-60.ogg" #Raine (Nat)
    mc sighing "Y-Yeah..."

    voice "voice/3-scene_3-61.ogg" #Leona (Dot)
    le questioning a3 "Ah, sorry! What I meant to say is that you're extremely lucky. None of our tests with wormholes have been fruitful."

    voice "voice/3-scene_3-62.ogg" #Leona (Dot)
    le "I'm surprised you took a ship through one to begin with."

    voice "voice/3-scene_3-63.ogg" #Raine (Nat)
    mc "I didn't really have a choice. I ran into one while I was flying."

    voice "voice/3-scene_3-64.ogg" #Raine (Nat)
    mc "When I exited the wormhole, I was close to Fireside. My ship was damaged and I…"

    mc blech "...had a really rough day."

    voice "voice/3-scene_3-65.ogg" #Leona (Dot)
    le surprised "Sounds like it."

    voice "voice/3-scene_3-66.ogg" #Leona (Dot)
    le kind a2 "I'm just glad you're okay after all of that."

    voice "voice/3-scene_3-67.ogg" #Leona (Dot)
    le concerned "You even went through a wormhole! I never thought that would be possible."

    voice "voice/3-scene_3-68.ogg" #Raine (Nat)
    mc "Yeah... I guess so."
    play sound "sfx/get up.ogg"

    $ hide_sides = ['Leona']
    show le smirk a2:
        xanchor .5
        yanchor 1
        zoom 1.0
        ypos 0.5
        xpos 0.9
        ease 0.3 zoom 1.21 ypos 0.0 xpos 0.75

    na "Leona suddenly stands up."

    voice "voice/3-scene_3-69.ogg" #Leona (Dot)
    le happy speaking a3 "So, I think it's high time I took you on a short tour of Aster!"

    voice "voice/3-scene_3-70.ogg" #Leona (Dot)
    le "If you're going to be stuck with us for awhile, you might as well get the lay of the land."

    voice "voice/3-scene_3-71.ogg" #Raine (Nat)
    mc "Umm..."
    na "I honestly don't want to stay any longer than I have to. Leona's a wonderful host, but planetary life just isn't for me."

    voice "voice/3-scene_3-72.ogg" #Raine (Nat)
    mc "Maybe later."

    voice "voice/3-scene_3-73.ogg" #Leona (Dot)
    le sassyquestioning "Don't you want to go outside? You can't stay cooped up in here forever..."

    voice "voice/3-scene_3-74.ogg" #Raine (Nat)
    mc happy "Once I fix my ship, I'll be fine."

    show le surprised at stage_right:
        zoom 1.0

    na "Leona perks up at the mention of my ship."

    voice "voice/3-scene_3-75.ogg" #Leona (Dot)
    le "Oh, that's right! While you were out, my crew rushed over to your ship and spent the night hauling it back to the base."

    voice "voice/3-scene_3-76.ogg" #Raine (Nat)
    mc shocked armraised "R-Really? What about the creatures you told me about?"

    voice "voice/3-scene_3-77.ogg" #Leona (Dot)
    le happy a1 "We have ways of dealing with them, so no worries."

    voice "voice/3-scene_3-78.ogg" #Raine (Nat)
    le  "Anyway, it was surprisingly light, so they hooked it up to a squad of bikes and brought it in."

    mc happy "Well then, what are we waiting for?"

    le smug a3 "Oh? Didn't you just say you could wait until later?"
    na "Leona's giving off the cheekiest grin. She knew I'd jump at this opportunity."
    mc unimpressed "I've... changed my mind. Let's go."
    le kind a2 "All righty, but first, let me take a look at your leg."
    mc blech "Oh, I had completely forgotten about that."
    na "I stamp my foot a couple times to determine if there are any problems."
    le smug a2 "Calm down there, killer. I just wanna take a peek!"
    na "Leona scoots a chair up beside me and sets about unwrapping the gauze."
    na "Shockingly, the green paste peels off cleanly."
    na "Better still, the skin is completely healed."
    le happy a2 "Lookin' good! With that, you're cleared to return to duty."
    le "Let's go take a look at that ship of yours now. It'll only take a couple minutes to get there, so don't worry about gearing up."
    mc happy "Lead the way, Captain."


    #hide screen flower_menu_button

    #$ renpy.music.play(config.main_menu_music)
    #call screen tobecontinued_announce
    #call screen demo_letter with dissolve
    #call screen credits with dissolve
    #pause 2.0

    ##This is where the demo is ending

    #return

    scene street_open onlayer master with wipeleft:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 1.00
            ease 30 xpos 0.56
    stop env fadeout 2.0
    play sound3 "amb/City Day.ogg" fadein 2.0

    na "Leona's neighborhood is full of people just like her, with differently shaped horns and a variety of builds."
    na "They're super similar to humans, minus the horns."
    na "Were I more interested in xenobiology, I'd certainly be interested in how they grow. Are they part of the skull, or are they more like antlers?"

    #Voice lines are not implimented yet

    $ hide_sides = []
    #voice "voice/3-scene_3-82.ogg" #Leona (Dot)
    le explaining "There's Lua's place, she has the best vegetables this time of year, and over there's my mechanic's house..."
    na "Meanwhile, Leona is dragging me around, pointing at various buildings and landmarks without a care in the world."

    #voice "voice/3-scene_3-83.ogg" #Raine (Nat)
    mc "Just how far away is this base of yours?"

    #voice "voice/3-scene_3-84.ogg" #Leona (Dot)
    le speakingsurprised a1 "Oh, right around the corner from my house!"

    #voice "voice/3-scene_3-85.ogg" #Raine (Nat)
    mc "...Aren't we walking away from it, then?"

    #voice "voice/3-scene_3-86.ogg" #Leona (Dot)
    le happy a2 "Yep!"

    #voice "voice/3-scene_3-87.ogg" #Raine (Nat)
    na "..."

    #voice "voice/3-scene_3-88.ogg" #Leona (Dot)
    na "...?"

    #voice "voice/3-scene_3-89.ogg" #Raine (Nat)
    mc "Can I see my ship?"

    #voice "voice/3-scene_3-90.ogg" #Leona (Dot)
    le questioning p2 "Oh! Right, just this way!"

    stop sound3 fadeout 2.0
    stop music fadeout 2.0
    #scene black with fade

    jump scene_4
