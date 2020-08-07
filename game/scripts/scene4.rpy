label scene_4:
    play env "amb/workshop.ogg" fadein 2.0
    #ART - GARAGE BG
    show street_open onlayer master:
        subpixel True xpos 1.0 ypos .5 xanchor 0.5 yanchor 0.5 zoom 1.3 rotate None
        parallel:
            easeout2 3.0 xpos -.2
        parallel:
            easein_back 3.0 ypos 0.2

    na "After a brief tour, we complete a loop around the neighborhood and approach a garage just around the corner from Leona's house."
    na "I hope Juneau is okay..."

    $ hide_sides = ['Leona']
    show le kindly at stage_right with dissolve:
        xalign 1.3
    voice "voice/4-scene_4-1.ogg" #Leona (Dot)
    le "So, how's it look?"
    na "Leona snaps me out of my thoughts as I rest my eyes on what's left of my ship."
    show le concerned at stage_right with dissolve:
        xalign 1.3
    voice "voice/4-scene_4-2.ogg" #Raine (Nat)
    mc onfire "Oh man, what a stinking mess!"

    na "I run over, pushing aside some people investigating it. They shoot me dirty looks, but upon seeing Leona, they take the hint and leave."

    voice "voice/4-scene_4-3.ogg" #Leona (Dot)
    le concerned "So what's wrong with it? As I said when we met, we don't exactly have ships like yours."
    voice "voice/4-scene_4-4.ogg" #Raine (Nat)
    mc grr "Well... first of all, it's upside down. It's going to be a pain to flip over."
    voice "voice/4-scene_4-5.ogg" #Leona (Dot)
    le look "But can you fix it?"
    na "I lean down to look at the roof of the ship, now pressed firmly against the ground, metal jutting out every which way."
    voice "voice/4-scene_4-6.ogg" #Raine (Nat)
    mc sighing "Huh. Not sure. The hardware will be a real bitch to repair, but I can do it."
    voice "voice/4-scene_4-7.ogg" #Raine (Nat)
    mc grumpy "The software is the issue. If it's trashed, I'm not sure if it can be fixed."
    na "Juneau... please be alright."
    voice "voice/4-scene_4-8.ogg" #Leona (Dot)
    le concerned "Hey, don't look so down!"
    voice "voice/4-scene_4-9.ogg" #Leona (Dot)
    le kind a2 "I'm sure you'll get it fixed! You're a high-tech alien, This must be nothing for you!"
    voice "voice/4-scene_4-10.ogg" #Raine (Nat)
    mc hmm "Heh. While your baseless confidence is flattering, I think you might be overestimating me."
    play sound "sfx/Metal fix.ogg"
    na "I push together two pieces of metal, one of which was mildly bent. Holding them in place, I grab a nearby tool and try to turn the screw that originally held them together."
    voice "voice/4-scene_4-11.ogg" #Leona (Dot)
    le questioning a3 "Regardless, you'll be staying with me until you've got your ship back together."
    na "I stand up, brushing myself off."
    voice "voice/4-scene_4-12.ogg" #Raine (Nat)
    mc "I guess I don't have much of a choice, do I? Guess I'm stuck with you."
    voice "voice/4-scene_4-13.ogg" #Leona (Dot)
    le sassyquestioning "Excuse you, I'm a delight to live with!"
    voice "voice/4-scene_4-14.ogg" #Raine (Nat)
    mc "And a wonderful chef."
    voice "voice/4-scene_4-15.ogg" #Leona (Dot)
    le hmm "Aww, that's not fair at all."
    voice "voice/4-scene_4-16.ogg" #Raine (Nat)
    mc satisfied "Nah, I'm serious. The egg was great."
    voice "voice/4-scene_4-17.ogg" #Leona (Dot)
    le happy2 a1 "I can pick some more up, if you'd like."
    voice "voice/4-scene_4-18.ogg" #Raine (Nat)
    mc smugly "...Yes!"
    voice "voice/4-scene_4-19.ogg" #Leona (Dot)
    le happy a1 "We'll make a stop at the store later then."
    voice "voice/4-scene_4-20.ogg" #Leona (Dot)
    le "Anywho, there are more tools in the storage room. There's a guy working in there that can help you find something useful."
    voice "voice/4-scene_4-21.ogg" #Leona (Dot)
    le speakingthink "Well, I hope he can at least."
    voice "voice/4-scene_4-22.ogg" #Raine (Nat)
    mc speaking "You're not coming?"
    voice "voice/4-scene_4-23.ogg" #Leona (Dot)
    le happy a2 "I kinda wanna look at your ship. It's alien technology! I've never seen anything like it."
    voice "voice/4-scene_4-24.ogg" #Raine (Nat)
    mc hmm "Sure, just don't go pressing any random buttons."

    hide le with dissolve
    $ hide_sides = []

    show street_open:
        ease 2.0 zoom 2.0 xalign 0.95 yalign 0.9

    na "I smile to myself as I turn and make towards the door in the corner with the sign above it that reads 'STORAGE'."
    na "Behind me, Leona talks to herself as she prods about the ship."

    voice "voice/4-scene_4-25.ogg" #Leona (Dot)
    le speakingthink "This is really amazing stuff, even when it's in shambles."
    voice "voice/4-scene_4-26.ogg" #Leona (Dot)
    le kindly "Oh, uh, thanks! I never could have imagined this type of metal could be used like this."
    voice "voice/4-scene_4-27.ogg" #Leona (Dot)
    le curious "Or that this shape would make for a good space ship."
    voice "voice/4-scene_4-28.ogg" #Leona (Dot)
    le "Or that, or..."
    play sound "sfx/metal break.ogg"
    na "..."

        #SFX - METALLIC POP

    voice "voice/4-scene_4-29.ogg" #Leona (Dot)
    le awk "Oops."
    voice "voice/4-scene_4-30.ogg" #Leona (Dot)
    le shylook "Uhhh... And she just fixed that too..."
    voice "voice/4-scene_4-31.ogg" #Leona (Dot)
    le "Not a great start."
    na "Leona notices me watching from the doorway."
    na "I've caught her red handed."
    voice "voice/4-scene_4-32.ogg" #Raine (Nat)
    mc "Uhhh... Everything okay?"
    voice "voice/4-scene_4-33.ogg" #Leona (Dot)
    le "Yeah! Totally! Um, actually no, it's not..."
    voice "voice/4-scene_4-34.ogg" #Raine (Nat)
    mc onfire "Leona?"
    voice "voice/4-scene_4-35.ogg" #Leona (Dot)
    le "Well, I, uh..."
    voice "voice/4-scene_4-36.ogg" #Leona (Dot)
    le awk "Maybe I shouldn't try to help. I'm all thumbs."
    voice "voice/4-scene_4-37.ogg" #Raine (Nat)
    mc happy "No use fussing over it. It was gonna do that anyway."
    voice "voice/4-scene_4-38.ogg" #Leona (Dot)
    le happy a2 "Did you find anything useful back there?"
    voice "voice/4-scene_4-39.ogg" #Raine (Nat)
    mc sighing "I looked around, but I didn't know what any of them did. They all looked like strange toys."
    voice "voice/4-scene_4-40.ogg" #Leona (Dot)
    le concerned "Was there nobody there to help you?"
    voice "voice/4-scene_4-41.ogg" #Raine (Nat)
    mc speaking "Someone was working, but I don't think they could help..."
    voice "voice/4-scene_4-42.ogg" #Raine (Nat)
    mc questioning2 "No offense, but the stuff you have here is more than a little bit out of date."
    voice "voice/4-scene_4-43.ogg" #Leona (Dot)
    le curious "Hmmm, I suppose it might be for the best."
    voice "voice/4-scene_4-44.ogg" #Leona (Dot)
    le look "Everyone's a little nervous about having you here. It's not every day an alien crash-lands in your backyard."
    voice "voice/4-scene_4-45.ogg" #Raine (Nat)
    mc happy "Haha, I'll bet."
    voice "voice/4-scene_4-46.ogg" #Raine (Nat)
    mc questioning "As soon as everyone realized who I was, they cleared out of there really quick."
    voice "voice/4-scene_4-47.ogg" #Raine (Nat)
    mc "I bet the one in the storage room is only still there because he felt a bit trapped."
    voice "voice/4-scene_4-48.ogg" #Leona (Dot)
    le happy a2 "We do some of our best work when we feel like that though."
    voice "voice/4-scene_4-49.ogg" #Leona (Dot)
    le "Did I tell you why we decided to found a colony to begin with?"
    voice "voice/4-scene_4-50.ogg" #Raine (Nat)
    mc oho "No, but I'd love to hear more."
    voice "voice/4-scene_4-51.ogg" #Leona (Dot)
    le speaking a2 "Tell you what, you tell me what kind of tools you need and I'll get them for ya."
    voice "voice/4-scene_4-52.ogg" #Leona (Dot)
    le smug a3 "And while you work, I'll give you a rundown!"
    voice "voice/4-scene_4-53.ogg" #Raine (Nat)
    mc "You've got a deal."
    stop env fadeout 2.0
    scene sky with dissolve


    na "..."
    na "After a couple of hours listening to Leona's stories while working on the ship, I decide to take a break."
    na "I won't be able to determine Juneau's condition for awhile yet, and I'm hungry."

    #ART - LEONA'S HOUSE
    play sound2 "amb/Leonas house.ogg"
    scene house with dissolve:
        zoom 1.25 xalign 1.0


    na "After a short trip to a nearby convenience store in search of eggs, we return to Leona's abode."
    na "It's already mid-afternoon."
    na "If I go back to the base to work on my ship now, I'll be there all night."
    na "Juneau..."
    voice "voice/4-scene_4-54.ogg" #Leona (Dot)
    le surprised "Did you hear me? Helloooo?"
    play music "music/Missing Juneau.ogg" fadein 3.0

    voice "voice/4-scene_4-55.ogg" #Raine (Nat)
    mc shocked armraised "Oh! Ah, what?"

    show house:
        ease 0.5 zoom 0.75 xalign 0.5
    pause 0.5
    show le happy a2 at stage_right with dissolve

    $ hide_sides = ['Leona']

    voice "voice/4-scene_4-56.ogg" #Leona (Dot)
    le concerned "I asked if you wanted dinner. Are you okay?"

    voice "voice/4-scene_4-57.ogg" #Raine (Nat)
    mc onfire "Yeah, just thinking about the ship."
    voice "voice/4-scene_4-58.ogg" #Leona (Dot)
    le thinky "You said you'd have trouble if the software was busted. I thought you'd know how to simply redo it."
    voice "voice/4-scene_4-59.ogg" #Raine (Nat)
    mc blech "It's not recreating the software I can't do. It's getting back the programs I had."

    hide le with dissolve
    show house:
        ease 0.5 zoom 1.0 xalign 0.0 yalign 1.0
    na "Leona sets food down in front of me. I'm not entirely sure what it's supposed to be, but it seems she used ingredients based on what she knew I could eat."
    na "As expected, it's delicious."

    $ hide_sides = []

    voice "voice/4-scene_4-60.ogg" #Leona (Dot)
    le questioning a2 "So what's so important about the program?"
    voice "voice/4-scene_4-61.ogg" #Raine (Nat)
    mc annoyed "She's an AI companion. She's way more than just a program."
    voice "voice/4-scene_4-62.ogg" #Raine (Nat)
    mc weary "As far as I'm concerned she's a real person."
    voice "voice/4-scene_4-63.ogg" #Leona (Dot)
    le concerned "...She must be very important to you."
    voice "voice/4-scene_4-64.ogg" #Raine (Nat)
    mc shyspeak "Well, we had our fights, but she's the closest I have to family."
    voice "voice/4-scene_4-65.ogg" #Raine (Nat)
    mc happy "Like an annoying little sister."
    na "Leona's long ears seem to perk up, but she covers her expression by taking another bite of food."
    voice "voice/4-scene_4-66.ogg" #Raine (Nat)
    mc grumpy "This sucks."
    voice "voice/4-scene_4-67.ogg" #Leona (Dot)
    le tired "Yeah..."
    voice "voice/4-scene_4-68.ogg" #Leona (Dot)
    le happyspeaking a3 "But!"
    na "Leona's sudden change of tone catches me off guard."
    voice "voice/4-scene_4-69.ogg" #Leona (Dot)
    le kindly "You're gonna need rest if you'll be spending tomorrow fixing your ship!"
    na "She gestures towards the bed excitedly."
    na "Sitting on top of the bed pile, neatly folded, is one slightly singed blanket I recognize as part of my ship's bedding."
    na "For a brief moment, I feel... sad."
    na "Sad, but grateful?"
    na "How strange."
    voice "voice/4-scene_4-72.ogg" #Raine (Nat)
    mc shyspeak "Thanks, Leona. I really appreciate it. You've been amazing, I really don't deserve your help."
    na "Leona turns from me."
    voice "voice/4-scene_4-73.ogg" #Leona (Dot)
    le kind a2 "Just doing what anyone would do. Now, make sure you get some rest! Ya need a strong and healthy mind to get her back!"

    na "I want to say something more, but I can't put it into words. I abandon the notion and let my thoughts return to the repair of my ship."
    na "But there's nothing I can do until I have Juneau back, and that has to wait till tomorrow."
    na "The wormhole that brought me here is more likely than not long gone."
    na "Would it really be so bad to slow down a bit? Take in the sights, get a feel for the place?"

    show house:
        ease 1.5 zoom 1.3 xalign 0.5 yalign 1.0

    na "Resigned to the facts, I follow Leona's advice and head to bed."
    na "As I lay in bed, I remember the stories Leona told me earlier."
    na "If I'm going to be here for a while, I guess it wouldn't hurt to document some things."
    voice "voice/4-scene_4-74.ogg" #Raine (Nat)
    mc speaking "Hey, Leona?"
    na "Leona, who is now cleaning up after our meal, pokes her head out from the kitchen."
    voice "voice/4-scene_4-75.ogg" #Leona (Dot)
    le happy a1 "Yes?"
    voice "voice/4-scene_4-76.ogg" #Raine (Nat)
    mc shyspeak "Do you have anything I can write on?"
    voice "voice/4-scene_4-77.ogg" #Leona (Dot)
    le curious "Is digital alright?"
    voice "voice/4-scene_4-78.ogg" #Raine (Nat)
    mc shyspeak "That would be wonderful."
    voice "voice/4-scene_4-79.ogg" #Leona (Dot)
    le happy a2 "Check the shelf on the back wall. There are a bunch of mediapads I bought a while ago for next to nothing, so you can keep one if you want."
    voice "voice/4-scene_4-80.ogg" #Raine (Nat)
    mc "Whoa, thanks!"
    voice "voice/4-scene_4-81.ogg" #Raine (Nat)
    mc satisfied "I'd feel a little guilty taking something else from you for nothing in return, so I'll make you a trade."
    voice "voice/4-scene_4-82.ogg" #Raine (Nat)
    mc shyspeak "How does a copy of my music collection sound?"
    voice "voice/4-scene_4-83.ogg" #Leona (Dot)
    le happy2 a1 "Alien music? That sounds exciting!"
    voice "voice/4-scene_4-84.ogg" #Raine (Nat)
    mc smug "I thought that might interest you. I'll get you hooked up tomorrow."
    voice "voice/4-scene_4-85.ogg" #Leona (Dot)
    le "You know how to drive a hard bargain!"
    voice "voice/4-scene_4-86.ogg" #Leona (Dot)
    le happy a1 "Oh, and I'm done with dishes here but I need to go check on something at the base. I'll be back in a little while."
    voice "voice/4-scene_4-87.ogg" #Leona (Dot)
    le "Will you be okay on your own for a bit?"
    voice "voice/4-scene_4-88.ogg" #Raine (Nat)
    mc happy "Sure, I just want to write some things down before I go to sleep. See you in the morning?"
    voice "voice/4-scene_4-89.ogg" #Leona (Dot)
    le kind a2 "Alrighty, g'night Raine."
    voice "voice/4-scene_4-90.ogg" #Raine (Nat)
    mc satisfied "Night night~"
    na "Leona takes her leave and I set about making notes of what I've seen and heard so far."
    na "When we were talking in the garage earlier she told me an interesting story about their homeworld; Dawne."
    na "I figure that's as good a place as any to start before I decide to nod off."
    #VFX - JOURNAL ENTRY ADDED - 1
    stop music fadeout 2.0
    stop env fadeout 2.0
    scene black with Dissolve(2.0)
    pause 0.5

    jump scene_5
