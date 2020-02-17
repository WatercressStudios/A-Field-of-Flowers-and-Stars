label scene1:
    scene stars at main_menu_bg_restore_transform
    pause 6.0
    scene cockpit_space with dissolve:
        zoom 0.75
        anchor (0.5, 0.5)
        align (0.5, 0.5)
    show screen flower_menu_button with easeinright
    #This is the start of the game.
    #ART We begin in space. Nothing else is on the screen. "Warp drive particles" move slowly from left to right to imply motion. The stars in the background are still.

    na "All my life I've been looking for something."

    na "No, it's more than that."

    na "All my life, something has been calling out to me."

    na "Calling me towards the stars. Asking, begging to be found."
    play env "sfx/Warp engines.ogg" fadein 1.0
    scene cockpit_space:
        zoom 0.75
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        ease 1.0 zoom 0.85
    #ART We see our ship from a distance, moving slowly from the right to the center of the screen, as if the camera is catching up to the fast moving ship.
    #SFX Sound of the warp drive comes louder to accompany the ship coming into focus.

    na "And when this ship is ready, there will be nothing out of my reach."

    na "No star in the sky I can't touch."

    na "So…"

    voice "voice/1-scene1-1.ogg" #Raine (Nat)
    mc sad "So why won't you finish these damn calibrations already so we can do some exploring?"

    voice "voice/1-scene1-2.ogg" #Raine (Nat)
    mc "Finish!"

    #SFX she kicks something.
    play sound2 "sfx/clunk.ogg"
    pause 1.0
    play sound "sfx/power down 1.ogg"

    #ART With a flash of light the ship comes out of light speed. Particles stop moving. An asteroid belt pops into view. Our camera zooms in on the cockpit area of the ship and we transition to an interior shot.
    #ART Increase the size of the ship sprite to simulate zooming in on the cockpit window. Fade the screen as we do to make a smooth transition.

    #SFX Decelerating from lightspeed travel.
    pause 1.0
    stop env fadeout 2.0
    play sound3 "sfx/engines.ogg" fadein 1.0

    #Scene spaceship normal

    show ju snarky a1 at ju_side

    voice "voice/1-scene1-3.ogg" #Juneau (Lily)
    ju "Hey! Don't kick the control panel!"

    voice "voice/1-scene1-4.ogg" #Raine (Nat)
    mc "Oh, Juneau. I was wondering when you were going to show up."

    #ART Juneau pouting

    voice "voice/1-scene1-5.ogg" #Juneau (Lily)
    ju @ a2 "I've been hard at work, I'll have you know. I'm just… having a little trouble with the procedure is all."

    voice "voice/1-scene1-6.ogg" #Juneau (Lily)
    ju @ concerned "The results keep coming back... wrong."

    voice "voice/1-scene1-7.ogg" #Raine (Nat)
    mc "Hmm. Your programming must be messed up."

    show ju snarky

    voice "voice/1-scene1-8.ogg" #Juneau (Lily)
    ju "Big talk coming from someone with a haywire personality routine."

    voice "voice/1-scene1-9.ogg" #Juneau (Lily)
    ju sarcastic a1 e1 b4 "Oh I'm Raine! I'm so impatient! The universe didn't love me enough as a baby so I’ll just take out all my frustrations on my poor, defenseless starship!"

    voice "voice/1-scene1-10.ogg" #Raine (Nat)
    mc "I do {b}not{/b} sound like that."

    voice "voice/1-scene1-11.ogg" #Juneau (Lily)
    ju snarky "You do too!"

    voice "voice/1-scene1-12.ogg" #Raine (Nat)
    mc "*sigh* I need coffee. Take over for a bit, will ya?"
    play sound "sfx/power up.ogg"
    hide ju with easeoutleft
    #ART In a flash of light she disappears from the console and appears in hologram form in the passenger seat beside us. She's a full body human-like AI.
    show ju snarky a2 onlayer master:
        stage_right
        hologram
    na "The hologram projectors spin up, Juneau taking a seat at the controls. I spin around and turn on the food synthesizer at the back of the ship."

    na "I set it to coffee, with French vanilla and sugar."

    voice "voice/1-scene1-13.ogg" #Juneau (Lily)
    ju concerned a2"The sensor's picking up some strange gravimetric readings around these asteroids."

    voice "voice/1-scene1-14.ogg" #Juneau (Lily)
    ju speaking eclosed"We'd better scan the area just to be safe. If we get stranded out here, I'll be stuck with you 'til you're dead and my batteries run out."

    voice "voice/1-scene1-15.ogg" #Raine (Nat)
    mc "Oh, don't be a worrywart. Besides, it wouldn't be that bad!"

    voice "voice/1-scene1-16.ogg" #Raine (Nat)
    mc "I'd just rewrite your program to make the perfect AI girlfriend for myself."

    show ju annoyed a1 with vpunch

    voice "voice/1-scene1-17.ogg" #Juneau (Lily)
    ju "I'll eject you." (what_size=50)

    voice "voice/1-scene1-18.ogg" #Raine (Nat)
    mc "Don't worry, I'm only kidding. I like you just the way you are — annoyingly useful."

    #VA: Make a pout sound. Have fun with it! Whatever "pouting" sounds like LOL

    voice "voice/1-scene1-19.ogg" #Juneau (Lily)
    ju annoyed a2 "I've set the computer to run a full scan of the belt. I estimate it'll take four hours to complete."

    voice "voice/1-scene1-20.ogg" #Raine (Nat)
    mc "*sigh* fine."

    na "I grab my coffee and bring it back to my seat."

    na "A cup of holographic tea materializes into Juneau's hand. She sips it gingerly."
    hide ju with Dissolve(2)
    na "Damn. Four hours."

    na "At least I can take the scans back to the cartographer's guild on Lumin."

    na "I don't consider myself much of an explorer, but the extra money certainly helps."

    na "Maybe I’ll buy some new drink recipes for the synthesizer. Or a new outfit for Juneau."

    na "I wonder how she'd react if I installed a maid costume on her software kit."

    voice "voice/1-scene1-21.ogg" #Raine (Nat)
    mc "Hahaha."

    voice "voice/1-scene1-22.ogg" #Juneau (Lily)
    ju "What?"

    voice "voice/1-scene1-23.ogg" #Raine (Nat)
    mc "Nothing. Just thinking about some of the things we could buy when we get back to port."

    na "Juneau flys us through the belt with the grace that only a navigator could. Her movements are effortless and graceful as she maneuvers us through the asteroids."

    na "As much of a brat as she can be sometimes, you really have to appreciate her developer's attention to the little things."

    voice "voice/1-scene1-24.ogg" #Raine (Nat)
    mc "Hey Juneau. When we get back to Lumi-"

    #SFX whoosh
    play sound "sfx/wormhole.ogg"
    #ART Wormhole appears outside the cockpit. Screen shake."
    pause 1.0
    play env "sfx/SSL1.ogg" fadein 2.0
    play music "Music/wormhole.ogg" fadein 3.0

    voice "voice/1-scene1-25.ogg" #Juneau (Lily)
    ju "Woah!" with vpunch

    voice "voice/1-scene1-26.ogg" #Raine (Nat)
    mc "Juneau, report!"

    show ju red concerned a1:
        ju_side
        hologram

    voice "voice/1-scene1-27.ogg" #Juneau (Lily)
    ju "We ran right into some kind of gravity well. Gravimetric readings are off the charts."

    voice "voice/1-scene1-28.ogg" #Raine (Nat)
    mc "Show me."

    na "I take my seat next to her and bring up the local sensor interface."

    na "Dammit! I should have known."

    voice "voice/1-scene1-29.ogg" #Raine (Nat)
    mc "Damnit! It's a wormhole. We got caught in its well."

    voice "voice/1-scene1-30.ogg" #Raine (Nat)
    mc "Forward full thrust. Give me manual control."


    voice "voice/1-scene1-31.ogg" #Juneau (Lily)
    ju red worried a1 "Huh? Okay! Forward thrust increased to full. What are you doing?"

    #layer 2 spaceship
    stop env fadeout 2.0
    play sound4 "sfx/SSL1V2.ogg" fadein 2.0

    voice "voice/1-scene1-32.ogg" #Raine (Nat)
    mc "We're caught in a gravity field. It'll tear the ship apart before we ever break free."

    voice "voice/1-scene1-33.ogg" #Raine (Nat)
    mc "We gotta go through."

    voice "voice/1-scene1-34.ogg" #Juneau (Lily)
    ju worried speaking "That's dangerous! Are you sure?"

    na "I instantly recognize Juneau's safety protocols kicking in. "
    na "Though her personality routines may pretend otherwise, as the ship's navigator AI, Juneau has a responsibility to protect me."(what_size=40)

    voice "voice/1-scene1-35.ogg" #Raine (Nat)
    mc "Disengage safety. It's the only way we get out of this."

    voice "voice/1-scene1-36.ogg" #Juneau (Lily)
    ju @ red sassy"*sigh* If you kill me, it'll be on your conscience."

    voice "voice/1-scene1-37.ogg" #Juneau (Lily)
    ju "Handing you full navigational control."
    #SFX acceleration
    hide ju with dissolve

    play env "sfx/engines2.ogg" fadein 2.0
    show cockpit_space:
        shake

    #laayer 2 spaceship v2
    na "Faster and faster we go as I fly the ship straight into the  well."

    play sound4 "sfx/wormhole loop.ogg" fadein 1.0

    na "The ship begins to shake as we pick up speed."

    "Juneau clings to her seat, pulling her knees up to her chest. If she weren'tan AI, I might think she was scared out of her mind."

    voice "voice/1-scene1-38.ogg" #Juneau (Lily)
    ju "How can you be so calm at a time like this? We don't even know where it goes!"

    voice "voice/1-scene1-39.ogg" #Raine (Nat)
    mc "We're about to find out."

    voice "voice/1-scene1-40.ogg" #Raine (Nat)
    mc "I built this ship to fly, so lets fly."

    voice "voice/1-scene1-41.ogg" #Juneau (Lily)
    ju "Ah!"

    #ART Wormhole travel
    #SFX bang
    #ART asteroid flies across the windshield and hits towards the top of our ship.
    #art planet
    play sound2 "sfx/astroid impact.ogg"

    voice "voice/1-scene1-42.ogg" #Raine (Nat)
    mc "..."

    voice "voice/1-scene1-43.ogg" #Juneau (Lily)
    ju "..."

    voice "voice/1-scene1-44.ogg" #Raine (Nat)
    mc "What the fuck was that?"
    #Juneau glitches out
    stop sound4 fadeout 2.0
    play sound5 "sfx/SSL2.ogg" fadein 2.0
    voice "voice/1-scene1-45.ogg" #Juneau (Lily)
    ju "Impact! Hull breach det-"

    #SFX start ramping up the sound of atmosphere around the ship. Build it up on top of their conversation until we fade out of this scene.
    #spaceshhip layer 3


    na "I turn to Juneau . She's gone."

    na "One by one, the displays power down."

    na "With the power out, I lose control of the ship's systems."

    na "With no steering, I've got no way to change course."

    na "And the current course happens to be right into a planet."

    voice "voice/1-scene1-46.ogg" #Raine (Nat)
    mc "Shit. Don't wanna go there."

    voice "voice/1-scene1-47.ogg" #Raine (Nat)
    mc "Juneau come back!"

    #SFX alarm starts going off. Cockpit is flashing red.
    play sound "sfx/entry_intro.ogg"
    pause 2.0
    play sound4 "sfx/SSL3.ogg" fadein 1.0

    na "Suddenly my console lights up. A notification from Juneau. Text only."

    #ART Juneau icon on one of the screens, animated? Indicating that you should put a helmet on.
    show cockpit_space:
        shake2

    voice "voice/1-scene1-48.ogg" #Juneau (Lily)
    ju "You might want to put your helmet on now."
    scene white with Dissolve(3)
    #SFX roaring and crash sound effect.

    #ART fade to white, show the crash however you like.

    stop sound3 fadeout 2.0
    stop sound4 fadeout 2.0
    stop env fadeout 2.0
    stop sound5 fadeout 2.0
    stop music fadeout 2.0
    play sound2 "sfx/Crash.ogg"

    jump scene_2
