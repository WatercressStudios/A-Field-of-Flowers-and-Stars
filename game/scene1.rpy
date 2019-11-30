label scene1:
    show screen flower_menu_button with easeinright
    #This is the start of the game.
    show cockpit_space:
        zoom .85
    #ART We begin in space. Nothing else is on the screen. "Warp drive particles" move slowly from left to right to imply motion. The stars in the background are still.

    #Start text box overlay. Raine is narrating aloud.

    na "All my life I've been looking for something."

    na "No, it's more than that."

    #scene starfield with dissolve
    na "All my life, something has been calling out to me."

    na "Calling me towards the stars. Asking, begging to be found."
    play env "sfx/Warp engines.ogg" fadein 2.0

    #ART We see our ship from a distance, moving slowly from the right to the center of the screen, as if the camera is catching up to the fast moving ship.
    #SFX Sound of the warp drive comes louder to accompany the ship coming into focus.

    na "And when this ship is ready, there will be nothing out of my reach."

    na "No star in the sky I can't touch."

    na "So…"

    #voice "voice/1-scene1-1.ogg" #Raine (VA Name)
    mc sad "So why won't you finish these damn calibrations already so we can do some exploring?"

    #voice "voice/1-scene1-2.ogg" #Raine (VA Name)
    mc "Finish!"

    #SFX she kicks something.
    play sound2 "sfx/clunk.ogg"
    play sound "sfx/power down 1.ogg"

    #ART With a flash of light the ship comes out of light speed. Particles stop moving. An asteroid belt pops into view. Our camera zooms in on the cockpit area of the ship and we transition to an interior shot.
    #ART Increase the size of the ship sprite to simulate zooming in on the cockpit window. Fade the screen as we do to make a smooth transition.

    #SFX Decelerating from lightspeed travel.
    pause 2.0
    play env "sfx/engines.ogg" fadein 1.0

    #Scene spaceship normal


    #ART If we want to show Juneau on a console inside the ship, we can do that here. Else, we'll just have her as a #voice off screen for when she's not in hologram form.

    #voice "voice/1-scene1-3.ogg" #Juneau (VA Name)
    show ju snarky a1 at ju_side
    ju "Hey! Don't kick the control panel!"

    #voice "voice/1-scene1-4.ogg" #Raine (VA Name)
    mc "Oh, Juneau. I was wondering when you were going to show up."

    #ART Juneau pouting
    #voice "voice/1-scene1-5.ogg" #Juneau (VA Name)
    ju @ a2 "I've been hard at work, I'll have you know. I'm just… having a little trouble with the procedure is all."

    #voice "voice/1-scene1-6.ogg" #Juneau (VA Name)
    ju @ concerned "The results keep coming back... wrong."

    #voice "voice/1-scene1-7.ogg" #Raine (VA Name)
    mc "Hmm. Your programming must be messed up."

    #voice "voice/1-scene1-8.ogg" #Juneau (VA Name)
    show ju snarky
    ju "Big talk coming from someone with a haywire personality routine."

    #voice "voice/1-scene1-9.ogg" #Juneau (VA Name)
    ju sarcastic a1 e2 "Oh I'm Raine! I'm so impatient."

    ju sarcastic a1 e1 b4 "The universe didn't love me enough as a baby so I’ll just take out all my frustrations on my poor, defenseless starship."

    #voice "voice/1-scene1-10.ogg" #Raine (VA Name)
    mc "I do {b}not{/b} sound like that."

    #voice "voice/1-scene1-11.ogg" #Juneau (VA Name)
    ju snarky "You do too!"

    #voice "voice/1-scene1-12.ogg" #Raine (VA Name)
    mc "*sigh* I need coffee. Take over for a bit, will ya?"
    hide ju with easeoutleft
    #ART In a flash of light she disappears from the console and appears in hologram form in the passenger seat beside us. She's a full body human-like AI.

    show ju snarky a2 onlayer master:
        stage_right
        hologram
    na "The hologram projectors spin up, Juneau taking a seat at the controls. I spin around and turn on the food synthesizer at the back of the ship."

    na "I set it to coffee, with French vanilla and sugar."

    #voice "voice/1-scene1-13.ogg" #Juneau (VA Name)
    ju concerned a2"The sensor's picking up some strange gravimetric readings around these asteroids."

    #voice "voice/1-scene1-14.ogg" #Juneau (VA Name)
    ju speaking eclosed"We'd better scan the area just to be safe. If we get stranded out here, I'll be stuck with you 'til you're dead and my batteries run out."

    #voice "voice/1-scene1-15.ogg" #Raine (VA Name)
    mc "Oh, don't be a worrywart. Besides, it wouldn't be that bad!"

    #voice "voice/1-scene1-16.ogg" #Raine (VA Name)
    mc "I'd just rewrite your program to make the perfect AI girlfriend for myself."

    #voice "voice/1-scene1-17.ogg" #Juneau (VA Name)
    show ju annoyed a1 with vpunch
    ju "I'll eject you." (what_size=50)

    #voice "voice/1-scene1-18.ogg" #Raine (VA Name)
    mc "Don't worry, I'm only kidding. I like you just the way you are — annoyingly useful."

    #VA: Make a pout sound. Have fun with it! Whatever "pouting" sounds like LOL

    #voice "voice/1-scene1-19.ogg" #Juneau (VA Name)
    ju annoyed a2 "I've set the computer to run a full scan of the belt. I estimate it'll take four hours to complete."

    #voice "voice/1-scene1-20.ogg" #Raine (VA Name)
    mc "*sigh* fine."

    na "I grab my coffee and bring it back to my seat."

    na "A cup of holographic tea materializes into Juneau's hand. She sips it gingerly."
    hide ju with Dissolve(2)
    na "Damn. Four hours."

    na "At least I can take the scans back to the cartographer's guild on Lumin."

    na "I don't consider myself much of an explorer, but the extra money certainly helps."

    na "Maybe I’ll buy some new drink recipes for the synthesizer. Or a new outfit for Juneau."


    na "I wonder how she'd react if I installed a maid costume on her software kit."

    #voice "voice/1-scene1-21.ogg" #Raine (VA Name)
    mc "Hahaha."

    #voice "voice/1-scene1-22.ogg" #Juneau (VA Name)
    ju "What?"

    #voice "voice/1-scene1-23.ogg" #Raine (VA Name)
    mc "Nothing. Just thinking about some of the things we could buy when we get back to port."

    na "Juneau flys us through the belt with the grace that only a navigator could. Her movements are effortless and graceful as she maneuvers us through the asteroids."

    na "As much of a brat as she can be sometimes, you really have to appreciate her developer's attention to the little things."

    #voice "voice/1-scene1-24.ogg" #Raine (VA Name)
    mc "Hey Juneau. When we get back to Lumi-"

    #SFX whoosh
    #ART Wormhole appears outside the cockpit. Screen shake."
    play env "sfx/SSL1.ogg" fadein 1.0

    #voice "voice/1-scene1-25.ogg" #Juneau (VA Name)
    ju "Woah!" with vpunch

    #voice "voice/1-scene1-26.ogg" #Raine (VA Name)
    mc "Juneau, report!"

    #voice "voice/1-scene1-27.ogg" #Juneau (VA Name)
    show ju red concerned a1:
        ju_side
        hologram

    ju "We ran right into some kind of gravity well. Gravimetric readings are off the charts."

    #voice "voice/1-scene1-28.ogg" #Raine (VA Name)
    mc "Show me."

    na "I take my seat next to her and bring up the local sensor interface."

    na "Dammit! I should have known."

    #voice "voice/1-scene1-29.ogg" #Raine (VA Name)
    mc "It's a wormhole. We got caught in its well."

    #voice "voice/1-scene1-30.ogg" #Raine (VA Name)
    mc "Forward full thrust. Give me manual control."
    play music "Music/wormhole.ogg" fadein 3.0

    #voice "voice/1-scene1-31.ogg" #Juneau (VA Name)

    ju red worried a1 "Huh? Okay! Forward thrust increased to full. What are you doing?"

    #layer 2 spaceship
    play env "sfx/SSL1.ogg" fadein 1.0
    #voice "voice/1-scene1-32.ogg" #Raine (VA Name)
    mc "We're caught in a gravity field. It'll tear the ship apart before we ever break free."

    #voice "voice/1-scene1-33.ogg" #Raine (VA Name)
    mc "We gotta go through."

    #voice "voice/1-scene1-34.ogg" #Juneau (VA Name)

    ju worried speaking "That's dangerous! Are you sure?"

    na "I instantly recognize Juneau's safety protocols kicking in. Though her personality routines may pretend otherwise, as the ship's navigator AI, Juneau has a responsibility to protect me."(what_size=29)

    #voice "voice/1-scene1-35.ogg" #Raine (VA Name)
    mc "Disengage safety. It's the only way we get out of this."

    #voice "voice/1-scene1-36.ogg" #Juneau (VA Name)

    ju @ red sassy"*sigh* If you kill me, it'll be on your conscience."

    #voice "voice/1-scene1-37.ogg" #Juneau (VA Name)
    ju "Handing you full navigational control."
    #SFX acceleration
    hide ju with dissolve

    play sound3 "sfx/SSL1V2.ogg" fadein 1.0
    show cockpit_space:
        shake

    #laayer 2 spaceship v2
    na "Faster and faster we go as I fly the ship straight into the  well."

    na "The ship begins to shake as we pick up speed."

    "Juneau clings to her seat, pulling her knees up to her chest. If she weren'tan AI, I might think she was scared out of her mind."


    #voice "voice/1-scene1-38.ogg" #Juneau (VA Name)
    ju "How can you be so calm at a time like this? We don't even know where it goes!"

    #voice "voice/1-scene1-39.ogg" #Raine (VA Name)
    mc "We're about to find out."

    #voice "voice/1-scene1-40.ogg" #Raine (VA Name)
    mc "I built this ship to fly, so lets fly."

    #voice "voice/1-scene1-41.ogg" #Juneau (VA Name)
    ju "Ah!"

    #ART Wormhole travel
    #SFX bang
    #ART asteroid flies across the windshield and hits towards the top of our ship.
    #art planet
    play sound2 "sfx/Crash.ogg"

    #voice "voice/1-scene1-42.ogg" #Raine (VA Name)
    mc "..."
    #voice "voice/1-scene1-43.ogg" #Juneau (VA Name)
    ju "..."

    #voice "voice/1-scene1-44.ogg" #Raine (VA Name)
    mc "What the fuck was that?"
    #Juneau glitches out

    #voice "voice/1-scene1-45.ogg" #Juneau (VA Name)
    ju "Impact! Hull breach det-"

    #SFX start ramping up the sound of atmosphere around the ship. Build it up on top of their conversation until we fade out of this scene.
    #spaceshhip layer 3
    play sound4 "sfx/SSL2.ogg" fadein 1.0

    na "I turn to Juneau . She's gone."

    na "One by one, the displays power down."

    na "With the power out, I lose control of the ship's systems."

    na "With no steering, I've got no way to change course."

    na "And the current course happens to be right into a planet."

    #voice "voice/1-scene1-46.ogg" #Raine (VA Name)
    mc "Shit. Don't wanna go there."

    #voice "voice/1-scene1-47.ogg" #Raine (VA Name)
    mc "Juneau come back!"

    #SFX alarm starts going off. Cockpit is flashing red.
    play sound "sfx/entry_intro.ogg"
    pause 2.0
    play env "sfx/SSL3.ogg" fadein 2.0

    na "Suddenly my console lights up. A notification from Juneau. Text only."

    #ART Juneau icon on one of the screens, animated? Indicating that you should put a helmet on.
    show cockpit_space:
        shake2
    #voice "voice/1-scene1-48.ogg" #Juneau (VA Name)
    ju "You might want to put your helmet on now."
    scene white with Dissolve(3)
    #SFX roaring and crash sound effect.

    #ART fade to white, show the crash however you like.

    stop sound3 fadeout 2.0
    stop sound4 fadeout 2.0
    stop env fadeout 2.0
    stop music fadeout 2.0
    play sound2 "sfx/Crash.ogg"


    jump scene_2
