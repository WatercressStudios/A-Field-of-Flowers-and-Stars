label scene_9:

    #ART Inside ship, Garage BG
    #VFX We're at red alert status
    #SFX Sirens going off

    scene street_open_garage with dissolve:
        zoom 3.8 anchor (0.5, 0.5) align (0.86, 0.81)
    show cockpitoverlay2 with dissolve:
        zoom 0.75

    $ hide_sides = ['Juneau']
    show ju annoyed a1 at stage_right with dissolve
    play sound4 "amb/workshop.ogg"fadein 2.0
    play sound3 "sfx/Alarm.ogg"
    voice "voice/9-default-1.ogg" #Juneau (Lily)
    ju "Get up! You {i}absolute{/i} child!" with hpunch

    voice "voice/9-default-2.ogg" #Raine (Nat)
    mc annoyed "Hell no! Leave me alone and turn off that thing off! It's too damn loud!!"

    voice "voice/9-default-3.ogg" #Juneau (Lily)
    ju "Then get your act together already!"

    stop sound3 fadeout 1.0

    voice "voice/9-default-4.ogg" #Juneau (Lily)
    ju "All you've done since you got back yesterday is shovel ice cream into your face and whine about your alien goat girl!"

    voice "voice/9-default-5.ogg" #Juneau (Lily)
    ju annoyed a2 "I'm sick of it! I have things to do, so get out of my way! Who cares if she lied!?"

    voice "voice/9-default-6.ogg" #Raine (Nat)
    mc upset "I do!"

    voice "voice/9-default-7.ogg" #Juneau (Lily)
    ju annoyed a1 "If she hadn't, you woulda been blown to bits in that cave and then ground into a fine paste by 100 billion tons of rock!"

    voice "voice/9-default-8.ogg" #Juneau (Lily)
    ju "Zapped 'n slapped while drooling over a light bulb, you moth!"

    voice "voice/9-default-9.ogg" #Raine (Nat)
    mc onfire "I am a beautiful butterfly and I deserve respect!"

    voice "voice/9-default-10.ogg" #Juneau (Lily)
    ju annoyed a2 "Are you really going to spend the rest of your life complaining about not being obliterated?!"

    voice "voice/9-default-11.ogg" #Raine (Nat)
    mc upset "{b}Yes!{/b}"

    voice "voice/9-default-12.ogg" #Raine (Nat)
    mc "It's my life and my choices!"

    voice "voice/9-default-13.ogg" #Raine (Nat)
    mc "She'd still have betrayed me regardless of the circumstances! I wouldn't be here if I wanted people making my mistakes for me."

    voice "voice/9-default-14.ogg" #Juneau (Lily)
    ju annoyed a1 "And I'm telling you, you're full of shit. Who the hell cares about {i}whatever{/i} she did?"

    voice "voice/9-default-15.ogg" #Juneau (Lily)
    ju snarky a1 "You could be doing {b}literally anything else!{/b} What she did doesn't matter!"

    voice "voice/9-default-16.ogg" #Juneau (Lily)
    ju annoyed a1 "If you want to make your own choices then get up and {i}do{/i} something with your life!"

    voice "voice/9-default-17.ogg" #Juneau (Lily)
    ju "So rather than moping into a bucket of ice cream, either suck it up and make amends with her or get shit done on your own!"

    voice "voice/9-default-18.ogg" #Raine (Nat)
    mc annoyed "And I'm telling you, I don't want to!"

    voice "voice/9-default-19.ogg" #Juneau (Lily)
    ju "Idiot! Buffoon! Moron!"

    voice "voice/9-default-20.ogg" #Juneau (Lily)
    ju snarky a2 "I'm done!"

    voice "voice/9-default-21.ogg" #Juneau (Lily)
    ju annoyed a1 "You made me do this!"

    voice "voice/9-default-22.ogg" #Raine (Nat)
    mc shocked armraised  "What are you doing? Get your hands off of me!"

    voice "voice/9-default-23.ogg" #Raine (Nat)
    mc shocked m2 "When the hell did you fix the hard light projector?!"

    voice "voice/9-default-24.ogg" #Juneau (Lily)
    ju annoyed a1 "Out!"

    voice "voice/9-default-25.ogg" #Raine (Nat)
    mc shocked m2 "Actually, {i}how{/i} did y-!?"

    voice "voice/9-default-26.ogg" #Juneau (Lily)
    ju "{b}Ouuuuuut!{/b}"

    #ART Garage
    #SFX Raine gets tossed from the ship
    play sound "sfx/Throw.ogg"
    #VFX BG Shakes as she lands
    scene street_open_garage onlayer master with hpunch:
        subpixel True xpos 0.5 ypos 1.1 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.22
            ease 0.2 xpos 0.09
        parallel:
            zoom 1.48
            ease 0.2 zoom 0.95
            ease 0.1 zoom 1.0
    pause 0.5

    $ hide_sides = []
    voice "voice/9-default-27.ogg" #Juneau (Lily)
    ju snarky a2 "And don't come back until you're done moping over every little thing that goes wrong!"
    voice "voice/9-default-28.ogg" #Juneau (Lily)
    ju "'Beautiful butterfly' my ass, Raine!"
    hide ju snarky a2 with dissolve

    #SFX Door slamming
    play sound "sfx/ship door 2.ogg"

    na "Well."
    na "The nerve of some people."
    na "I peel my butt off the floor and march back to the door of {i}my{/i} ship."

    voice "voice/9-default-29.ogg" #Raine (Nat)
    mc annoyed "Never should have brought you back!"

    voice "voice/9-default-30.ogg" #Raine (Nat)
    mc "You're the one who told Leona and I to go rooting around in that dark ass cave, you damn-"

    #SFX Kicking metal
    play sound "sfx/Kicking panel.ogg"

    voice "voice/9-default-31.ogg" #Raine (Nat)
    mc "Ow! Juneau!"

    voice "voice/9-default-32.ogg" #Raine (Nat)
    mc "You could have {i}at least{/i} let me put on my boots!"

    play sound "sfx/boots.ogg"

    pause 5.0
    voice "voice/9-default-33.ogg" #Raine (Nat)
    mc "I'm surrounded by assholes!"

    na "As I turn to see where my boots were chucked, I see a lone figure peering around the corner."

    show street_open_garage:
        ease 1.0 ypos 1.0 xpos 0.25 zoom 0.75
    pause 1.0

    voice "voice/9-default-34.ogg" #Raine (Nat)
    mc unimpressed "Oh. And what are you looking at?"

    $ hide_sides = ['Leona']
    show le concerned with Dissolve(2.0):
        xalign 0.75

    voice "voice/9-default-35.ogg" #Leona (Dot)
    le "...Nothin'."

    voice "voice/9-default-36.ogg" #Raine (Nat)
    mc sighing "Good. 'Cause there's nothin' to see."

    na "Leona says nothing, putting some things into a bag instead."

    voice "voice/9-default-37.ogg" #Raine (Nat)
    mc unimpressed "...What are you doing?"

    voice "voice/9-default-38.ogg" #Leona (Dot)
    le crying "...Packing my things."

    voice "voice/9-default-39.ogg" #Leona (Dot)
    le concerned "I won't be coming back. So don't worry about it."

    voice "voice/9-default-40.ogg" #Raine (Nat)
    mc surprised "Leona? What do you mean?"

    voice "voice/9-default-41.ogg" #Leona (Dot)
    le crying "It means I was fired."

    voice "voice/9-default-42.ogg" #Leona (Dot)
    le concerned "So I'm packing my things up."

    voice "voice/9-default-43.ogg" #Raine (Nat)
    mc questioning "Fired? They can't fire you, can they?"

    voice "voice/9-default-44.ogg" #Raine (Nat)
    mc questioning2 "Aren't you the Captain? Isn't this your garage?"

    voice "voice/9-default-45.ogg" #Leona (Dot)
    le questioning a2 "We're funded by the city. It was either I go, or the expedition team goes."

    voice "voice/9-default-46.ogg" #Leona (Dot)
    le "We blew up a mountain, ya know?."

    voice "voice/9-default-47.ogg" #Leona (Dot)
    le crying "Just saying 'it was an accident' doesn't cut it for something like that."

    voice "voice/9-default-48.ogg" #Raine (Nat)
    mc annoyed "That's bullshit! I lit the fuse! Why didn't anybody talk to me about it?"

    voice "voice/9-default-49.ogg" #Leona (Dot)
    le concerned "You were my responsibility."

    voice "voice/9-default-50.ogg" #Leona (Dot)
    le "Did you really think anyone would just let an alien set up shop without some sort of oversight?"

    voice "voice/9-default-51.ogg" #Raine (Nat)
    mc upset "It's still bullshit!"

    na "Leona sighs as she continues putting items into her bag."

    voice "voice/9-default-52.ogg" #Leona (Dot)
    le "Whatever. As long as something like that doesn't happen again, nobody will bother you here."

    voice "voice/9-default-53.ogg" #Leona (Dot)
    le crying "You'll have to put up with the crew coming and going, but they'll leave you be if that's what you want."

    na "Leona closes up her bag and walks for the door."

    show le concerned with move:
        xalign 0.77
        xzoom -1
    voice "voice/9-default-54.ogg" #Leona (Dot)
    le "Take care, Raine. I hope you get home safe."

    show le crying with move:
        xalign 0.79
    voice "voice/9-default-55.ogg" #Leona (Dot)
    le "...I'm sorry for all the trouble."
    show le crying with move:
        xalign 0.82
    show le crying with move:
        xalign 0.84
    show le crying with move:
        xalign 0.86
    show le crying with move:
        xalign 0.88
    hide le concerned with easeoutright
    na "She vanishes from sight around the corner, heading off to god knows where."
    na "I should feel good about it, but I don't."
    na "Of all the people to take a dump on my feelings throughout my life, that stinging feeling is strongest here most of all."
    na "At least when dad sold off my first ship, I knew he was a piece of shit to begin with."

    $ hide_sides = []
    scene sky with dissolve
    na "A sigh escapes my lips, as I lay down aimlessly on the ground."
    na "What a hell of a week this has been. I need a nap..."


    voice "voice/9-default-56.ogg" #Juneau (Lily)
    ju annoyed a1 "Get your butt back in here, pronto!"

    voice "voice/9-default-57.ogg" #Raine (Nat)
    mc annoyed "The hell is it now? I need some rest!"

    voice "voice/9-default-58.ogg" #Juneau (Lily)
    ju snarky a2  "Apparently not. We got rads, emo kid. Haul ass and get in here!"

    voice "voice/9-default-59.ogg" #Raine (Nat)
    mc shocked armraised "Rads?!"
    play music "music/Fading Glow.ogg" fadein 2.0
    voice "voice/9-default-60.ogg" #Juneau (Lily)
    ju concerned a2 "Radiation, Raine! Radiation!"



    voice "voice/9-default-61.ogg" #Raine (Nat)
    mc unimpressed "Clear the door, I'm coming in!"

    scene street_open_garage with dissolve:
        zoom 0.75 anchor (0.5, 0.2) xalign 0.9 yalign 0.8
        pause 0.5
        parallel:
            ease 2.0 zoom 3.8 xalign 0.86

    na "I leap up from the floor and dash for the ship."

    scene street_open_garage with Dissolve(0.1):
        zoom 3.8 anchor (0.5, 0.2) xalign 0.86 yalign 0.8
    show cockpitoverlay2 with dissolve:
        zoom 0.75

    $ hide_sides = ['Juneau']

    show ju annoyed a1 at stage_right with dissolve
    voice "voice/9-default-62.ogg" #Juneau (Lily)
    ju "Take a look at these readings."

    voice "voice/9-default-63.ogg" #Juneau (Lily)
    ju "I tapped into the city's information grid through the power lines, but the interference was making a mess of just about everything."

    voice "voice/9-default-64.ogg" #Juneau (Lily)
    ju concerned a2 "Interference that looked a lot like-"

    voice "voice/9-default-65.ogg" #Raine (Nat)
    mc questioning2 "-Nuclear radiation. But if the bomb was atomic, we would have known instantly. We'd all be dead, right?"

    voice "voice/9-default-66.ogg" #Juneau (Lily)
    ju snarky a2 "No shit, Sherlock. Look closer."

    voice "voice/9-default-67.ogg" #Juneau (Lily)
    ju "It's not from the blast site."

    voice "voice/9-default-68.ogg" #Raine (Nat)
    mc questioning "They're from...the center of town?"

    voice "voice/9-default-69.ogg" #Juneau (Lily)
    ju concerned a1 "And there's two other readings I can't identify."

    voice "voice/9-default-70.ogg" #Juneau (Lily)
    ju "One of which is coming from this ship."

    voice "voice/9-default-71.ogg" #Raine (Nat)
    mc neutral "Let me take a look at that. There are a few things I know of that might not be in your databanks."

    na "I scroll through the data Juneau has up on the screen, running through the reams of information as quickly as I can."

    voice "voice/9-default-72.ogg" #Raine (Nat)
    mc unimpressed "Well, shit."

    voice "voice/9-default-73.ogg" #Raine (Nat)
    mc "I think this is a unique form of radiation. How the hell does that end up here?"

    voice "voice/9-default-74.ogg" #Juneau (Lily)
    ju concerned a2 "Where does something like that come from?"

    voice "voice/9-default-75.ogg" #Raine (Nat)
    mc "We don't even know. Last I heard it's only existed once or twice in a locked down test chamber."

    voice "voice/9-default-76.ogg" #Raine (Nat)
    mc questioning2 "I read those textbooks a dozen times, but it only came up once in a section about mutated radioisotopes."

    voice "voice/9-default-77.ogg" #Juneau (Lily)
    ju snarky a2 "Can we assume this has something to do with the unknown readings from where the bomb went off?"

    voice "voice/9-default-78.ogg" #Raine (Nat)
    mc unimpressed "You're sure they're coming from the southwest?"

    voice "voice/9-default-79.ogg" #Juneau (Lily)
    ju "Yeah."

    voice "voice/9-default-80.ogg" #Raine (Nat)
    mc "Then there's our answer. I believe something with the bomb may have forced an unstable interaction between our ship and the ship at the center of this city."

    voice "voice/9-default-81.ogg" #Raine (Nat)
    mc questioning2 "Next question: what do we do?"

    voice "voice/9-default-82.ogg" #Juneau (Lily)
    ju snarky a1 "Well, we can't just leave it alone. People will get sick."

    voice "voice/9-default-83.ogg" #Juneau (Lily)
    ju snarky a2 "Or, more likely, it'll get exponentially stronger and we could all be dead, rotting husks within a couple of days. Myself included."

    voice "voice/9-default-84.ogg" #Raine (Nat)
    mc unimpressed "That's a lovely thought, but it doesn't answer the question."

    voice "voice/9-default-85.ogg" #Raine (Nat)
    mc "There are a ton of isolated subsystems the radiation could be coming from. We don't have the equipment to check even half of them!"

    voice "voice/9-default-86.ogg" #Juneau (Lily)
    ju "Look, I'm not quantum by any stretch of what you call the imagination."

    voice "voice/9-default-87.ogg" #Juneau (Lily)
    ju "But I'm willing to bet the only thing that's gonna stop this is getting one of these ships very far from here. Say, half the planet-"

    voice "voice/9-default-88.ogg" #Juneau (Lily)
    ju snarky a1 "-Or destroying one before it can destroy us all."

    voice "voice/9-default-89.ogg" #Juneau (Lily)
    ju "None of which, I might add, we can do right now."

    voice "voice/9-default-90.ogg" #Raine (Nat)
    mc upset "Well that's just great!"



    voice "voice/9-default-91.ogg" #Raine (Nat)
    mc "I really am stuck here now!"

    voice "voice/9-default-92.ogg" #Raine (Nat)
    mc annoyed "What the hell did I do for the universe to shit on me so badly!?"

    voice "voice/9-default-93.ogg" #Juneau (Lily)
    ju annoyed a1 "Maybe if you stopped being such a self-pitying, cynical jerk for two minutes you'd realize it is your own damn fault!"

    voice "voice/9-default-94.ogg" #Juneau (Lily)
    ju sarcastic a1 e1 b4 "Oh, look at me, I'm Raine! I'm socially inept! My girlfriend loved me too much and I have a fear of rejection, so I shit on everybody who cares about me even a little bit so they never get the chance to be as disappointed in me as I am of myself!"

    voice "voice/9-default-95.ogg" #Juneau (Lily)
    ju annoyed a1 "Especially my girlfriend who has been {i}nothing{/i} but amazing to me and I'd be lucky to find another person in the entire fuckin' universe who can put up with my selfish {b}bullshit{/b}!"

    voice "voice/9-default-96.ogg" #Juneau (Lily)
    ju "Pull the tree out of your ass already and make it right with that poor girl, or so help me I will put you out of your misery {i}long{/i} before a little radiation can!"

    voice "voice/9-default-97.ogg" #Raine (Nat)
    mc unimpressed "...Fine."

    voice "voice/9-default-98.ogg" #Juneau (Lily)
    ju "'Fine' what?"

    voice "voice/9-default-99.ogg" #Raine (Nat)
    mc annoyed "Fine, I will, yes."

    voice "voice/9-default-100.ogg" #Juneau (Lily)
    ju snarky a2 "'Yes' who?"

    voice "voice/9-default-101.ogg" #Raine (Nat)
    mc questioning2 "You?"

    voice "voice/9-default-102.ogg" #Juneau (Lily)
    ju annoyed a1 "Say. My. Name."

    voice "voice/9-default-103.ogg" #Raine (Nat)
    mc upset "Yes, Juneau! I will apologise to Leona, beg for her help and get us out of this disaster!"

    voice "voice/9-default-104.ogg" #Juneau (Lily)
    ju annoyed a1 "About time."

    voice "voice/9-default-105.ogg" #Raine (Nat)
    mc questioning "Remind me to look at your subroutines when I get back, you've got a hell of an attitude today."

    voice "voice/9-default-106.ogg" #Juneau (Lily)
    ju annoyed a2 "I'm blaming it on the rads, roll with it."

    stop music fadeout 4.0
    voice "voice/9-default-107.ogg" #Juneau (Lily)
    ju annoyed a1 "Now get going!"

    voice "voice/9-default-108.ogg" #Raine (Nat)
    mc annoyed "Yes, Juneau. Thank you, Juneau."

    voice "voice/9-default-109.ogg" #Raine (Nat)
    mc upset "Blah blah blah..."

    play music "music/There's No Time.ogg" fadein 4.0

    scene street_open_garage:
        subpixel True xpos 0.5 ypos 1.1 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.22
            ease 0.5 xpos 0.09
        parallel:
            zoom 1.48
            ease 0.5 zoom 1.0
    pause 0.5
    na "All the vitriol aside, Juneau is right."
    na "I've been such an asshole to Leona. Even if I'm upset, I was too hard on her."
    na "God, what was I thinking?"
    na "No, I guess I wasn't thinking at all."
    na "I overreacted and did something wrong."
    na "But right now, that doesn't matter."
    na "There's plenty more at stake than just how I feel right now."
    na "And if I have to get my shit together and work with her, then that's a small price to pay compared to what could happen otherwise."
    na "Buckle up, Raine. It's gonna be a rough ride."
    stop sound4 fadeout 2.0
    play env "amb/City Night.ogg" fadein 2.0
    jump scene_10
