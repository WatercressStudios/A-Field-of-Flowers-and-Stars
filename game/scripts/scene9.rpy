label scene_9:

    #ART Inside ship, Garage BG
    #VFX We're at red alert status
    #SFX Sirens going off
    scene cockpit_ground with dissolve:
        zoom 0.75
    scene cockpit_ground with hpunch:
        zoom 0.75

    show ju annoyed a1 at stage_right with dissolve
       
    ju "Get up! You {i}absolute{/i} child!"

    mc annoyed "Hell no! Leave me alone and turn off that thing off! It's too damn loud!!"

    ju "Then get your act together already!"

    ju "All you've done since you got back yesterday is shovel ice cream into your face and whine about your alien goat girl!"

    ju annoyed a2 "I'm sick of it! I have things to do, so get out of my way! Who cares if she lied!?"

    mc upset "I do!"

    ju annoyed a1 "If she hadn't, you woulda been blown to bits in that cave and then ground into a fine paste by 100 billion tons of rock!"

    ju "Zapped 'n slapped while drooling over a light bulb, you moth!"

    mc onfire "I am a beautiful butterfly and I deserve respect!"

    ju annoyed a2 "Are you really going to spend the rest of your life complaining about not being obliterated?!"

    mc upset "{b}Yes!{/b}"

    mc "It's my life and my choices!"

    mc "She'd still have betrayed me regardless of the circumstances! I wouldn't be here if I wanted people making my mistakes for me."

    ju annoyed a1 "And I'm telling you, you're full of shit. Who the hell cares about {i}whatever{/i} she did?"

    ju snarky a1 "You could be doing {b}literally anything else!{/b} What she did doesn't matter!"

    ju annoyed a1 "If you want to make your own choices then get up and {i}do{/i} something with your life!"

    ju "So rather than moping into a bucket of ice cream, either suck it up and make amends with her or get shit done on your own!"

    mc annoyed "And I'm telling you, I don't want to!"

    ju "Idiot! Buffoon! Moron!"

    ju snarky a2 "I'm done!"

    ju annoyed a1 "You made me do this!"

    mc shocked armraised  "What are you doing? Get your hands off of me!"

    mc shocked m2 "When the hell did you fix the hard light projector?!"

    ju annoyed a1 "Out!"

    mc shocked m2 "Actually, {i}how{/i} did y-!?"

    ju "{b}Ouuuuuut!{/b}"

    #ART Garage
    #SFX Raine gets tossed from the ship
    #VFX BG Shakes as she lands
    scene street onlayer master with hpunch:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.22
            ease 1.0 xpos 0.09
        parallel:
            zoom 1.48
            ease 1.0 zoom 1.0
    show ju snarky a2 with dissolve:
            xalign 0.5
    ju "And don't come back until you're done moping over every little thing that goes wrong!"
    ju "'Beautiful butterfly' my ass, Raine!"
    hide ju snarky a2 with dissolve
    
    #SFX Door slamming
    play sound "sfx/door.ogg"

    na "Well."
    na "The nerve of some people."
    na "I peel my butt off the floor and march back to the door of {i}my{/i} ship."

    mc annoyed "Never should have brought you back!"

    mc "You're the one who told Leona and I to go rooting around in that dark ass cave, you damn-"

    #SFX Kicking metal
    play sound "sfx/Kicking panel.ogg"

    mc "Ow! Juneau!"

    mc "You could have {i}at least{/i} let me put on my boots!"

    #SFX Door opening
    #SFX Boot being chucked out, a small crash
    #SFX Door slamming

    mc "I'm surrounded by assholes!"

    na "As I turn to see where my boots were chucked, I see a lone figure peering around the corner."

    mc unimpressed "Oh. And what are you looking at?"

    show le concerned with Dissolve(2.0):
        xalign 0.75

    le "...Nothin'."

    mc sighing "Good. 'Cause there's nothin' to see."

    na "Leona says nothing, putting some things into a bag instead."

    mc unimpressed "...What are you doing?"

    le crying "...Packing my things."

    le concerned "I won't be coming back. So don't worry about it."

    mc surprised "Leona? What do you mean?"

    le crying "It means I was fired."

    le concerned "So I'm packing my things up."

    mc questioning "Fired? They can't fire you, can they?"

    mc questioning2 "Aren't you the Captain? Isn't this your garage?"

    le questioning a2 "We're funded by the city. It was either I go, or the expedition team goes."

    le "We blew up a mountain, ya know?."

    le crying "Just saying 'it was an accident' doesn't cut it for something like that."

    mc annoyed "That's bullshit! I lit the fuse! Why didn't anybody talk to me about it?"

    le concerned "You were my responsibility."

    le "Did you really think anyone would just let an alien set up shop without some sort of oversight?"

    mc upset "It's still bullshit!"

    na "Leona sighs as she continues putting items into her bag."

    le "Whatever. As long as something like that doesn't happen again, nobody will bother you here."

    le crying "You'll have to put up with the crew coming and going, but they'll leave you be if that's what you want."

    na "Leona closes up her bag and walks for the door."

    show le concerned with move:
        xalign 0.77
        xzoom -1
    le "Take care, Raine. I hope you get home safe."

    show le crying with move:
        xalign 0.79
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
    na "A sigh escapes my lips, as I lay down aimlessly on the ground."
    na "What a hell of a week this has been. I need a nap..."

    #SFX Door opening
    show ju annoyed a1 with dissolve:
        xalign 0.5

    
    ju "Get your butt back in here, pronto!"

    mc annoyed "The hell is it now? I need some rest!"

    ju snarky a2  "Apparently not. We got rads, emo kid. Haul ass and get in here!"

    mc shocked armraised "Rads?!"

    ju concerned a2 "Radiation, Raine! Radiation!"

    mc unimpressed "Clear the door, I'm coming in!"

    na "I leap up from the floor and dash for the ship."

    #ART Inside ship, Garage BG
    hide ju concerned a2 with dissolve 

    scene cockpit_ground with dissolve:
        zoom 0.75

    show ju annoyed a1 at stage_right with dissolve
    ju "Take a look at these readings."

    ju "I tapped into the city's information grid through the power lines, but the interference was making a mess of just about everything."

    ju concerned a2 "Interference that looked a lot like-"

    mc questioning2 "-Nuclear radiation. But if the bomb was atomic, we would have known instantly. We'd all be dead, right?"

    ju snarky a2 "No shit, Sherlock. Look closer."

    ju "It's not from the blast site."

    mc questioning "They're from… the center of town?"

    ju concerned a1 "And there's two other readings I can't identify."

    ju "One of which is coming from this ship."

    mc neutral "Let me take a look at that. There are a few things I know of that might not be in your databanks."

    na "I scroll through the data Juneau has up on the screen, running through the reams of information as quickly as I can."

    mc unimpressed "Well, shit."

    mc "I think this is a unique form of radiation. How the hell does that end up here?"

    ju concerned a2 "Where does something like that come from?"

    mc "We don't even know. Last I heard it's only existed once or twice in a locked down test chamber."

    mc questioning2 "I read those textbooks a dozen times, but it only came up once in a section about mutated radioisotopes."

    ju snarky a2 "Can we assume this has something to do with the unknown readings from where the bomb went off?"

    mc unimpressed "You're sure they're coming from the southwest?"

    ju "Yeah."

    mc "Then there's our answer. I believe something with the bomb may have forced an unstable interaction between our ship and the ship at the center of this city."

    mc questioning2 "Next question: what do we do?"

    ju snarky a1 "Well, we can't just leave it alone. People will get sick."

    ju snarky a2 "Or, more likely, it'll get exponentially stronger and we could all be dead, rotting husks within a couple of days. Myself included."

    mc unimpressed "That's a lovely thought, but it doesn't answer the question."

    mc "There are a ton of isolated subsystems the radiation could be coming from. We don't have the equipment to check even half of them!"

    ju "Look, I'm not quantum by any stretch of what you call the imagination."

    ju "But I'm willing to bet the only thing that's gonna stop this is getting one of these ships very far from here. Say, half the planet-"

    ju snarky a1 "-Or destroying one before it can destroy us all."

    ju "None of which, I might add, we can do right now."

    mc upset "Well that's just great!"

    mc "I really am stuck here now!"

    mc annoyed "What the hell did I do for the universe to shit on me so badly!?"

    ju annoyed a1 "Maybe if you stopped being such a self-pitying, cynical jerk for two minutes you'd realize it is your own damn fault!"

    ju sarcastic a1 e1 b4 "Oh, look at me, I'm Raine! I'm socially inept! My girlfriend loved me too much and I have a fear of rejection, so I shit on everybody who cares about me even a little bit so they never get the chance to be as disappointed in me as I am of myself!"

    ju annoyed a1 "Especially my girlfriend who has been {i}nothing{/i} but amazing to me and I'd be lucky to find another person in the entire fuckin' universe who can put up with my selfish {b}bullshit{/b}!"

    ju "Pull the tree out of your ass already and make it right with that poor girl, or so help me I will put you out of your misery {i}long{/i} before a little radiation can!"

    mc unimpressed "...Fine."

    ju "'Fine' what?"

    mc annoyed "Fine, I will, yes."

    ju snarky a2 "'Yes' who?"

    mc questioning2 "You?"

    ju annoyed a1 "Say. My. Name."

    mc upset "Yes, Juneau! I will apologise to Leona, beg for her help and get us out of this disaster!"

    ju annoyed a1 "About time."

    mc questioning "Remind me to look at your subroutines when I get back, you've got a hell of an attitude today."

    ju annoyed a2 "I'm blaming it on the rads, roll with it."

    ju annoyed a1 "Now get going!"

    mc annoyed "Yes, Juneau. Thank you, Juneau."

    mc upset "Blah blah blah..."

    scene street onlayer master with fade:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.22
            ease 1.0 xpos 0.09
        parallel:
            zoom 1.48
            ease 1.0 zoom 1.0

    na "All the vitriol aside, Juneau is right."
    na "I've been such an asshole to Leona. Even if I'm upset, I was too hard on her."
    na "God, what was I thinking?"
    na "No, I guess I wasn't thinking at all."
    na "I overreacted and did something wrong."
    na "But right now, that doesn't matter."
    na "There's plenty more at stake than just how I feel right now."
    na "And if I have to get my shit together and work with her, then that's a small price to pay compared to what could happen otherwise."
    na "Buckle up, Raine. It's gonna be a rough ride."

    jump scene_10
