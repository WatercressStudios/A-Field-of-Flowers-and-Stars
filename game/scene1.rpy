label scene1:
    show screen flower_menu_button with easeinright
    #This is the start of the game.
    show cockpitoverlay:
        zoom 1.35
    show stars behind cockpitoverlay:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor .5 rotate None
        parallel:
            xpos 0.75
            ease 30 xpos .25
            ease 3 xpos .27
        parallel:
            ypos .5
            ease 5.0 ypos .53
            ease 5.0 ypos .47
            ease 5.0 ypos .52
            ease 5.0 ypos .49
            ease 5.0 ypos .5
        parallel:
            ease 20 rotate 10

    #ART We begin in space. Nothing else is on the screen. "Warp drive particles" move slowly from left to right to imply motion. The stars in the background are still.

    #Start text box overlay. Raine is narrating aloud.

    show le n normal with dissolve
    na "All my life I've been looking for something."

    show le sp lookaway with dissolve
    na "No, it's more than that."

    scene starfield with dissolve
    na "All my life, something has been calling out to me."

    show ju b normal with dissolve:
        xalign 0.3
    na "Calling me towards the stars. Asking, begging to be found."

    #ART We see our ship from a distance, moving slowly from the right to the center of the screen, as if the camera is catching up to the fast moving ship.
    #SFX Sound of the warp drive comes louder to accompany the ship coming into focus.

    show le h armraised with dissolve:
        xalign 0.7
    na "And when this ship is ready, there will be nothing out of my reach."

    show le h normal with dissolve
    na "No star in the sky I can't touch."

    hide le with dissolve
    hide ju with dissolve
    na "So…"

    mc "So why won't you finish these damn calibrations already so we can do some exploring?"

    mc "Finish!"

    #SFX she kicks something.

    #ART With a flash of light the ship comes out of light speed. Particles stop moving. An asteroid belt pops into view. Our camera zooms in on the cockpit area of the ship and we transition to an interior shot.
    #ART Increase the size of the ship sprite to simulate zooming in on the cockpit window. Fade the screen as we do to make a smooth transition.

    #SFX Decelerating from lightspeed travel.

    #Scene spaceship normal


    #ART If we want to show Juneau on a console inside the ship, we can do that here. Else, we'll just have her as a voice off screen for when she's not in hologram form.

    ju "Hey! Don't kick the control panel!"

    mc "Oh, Juneau. I was wondering when you were going to show up."

    #ART Juneau pouting
    ju "I've been hard at work, I'll have you know. I'm just… having a little trouble with the procedure is all."

    ju "The results keep coming back... wrong."


    mc "Hmm. Your programming must be messed up."

    ju "Big talk coming from someone with a haywire personality routine."

    ju "Oh I'm Raine! I'm so impatient. The universe didn't love me enough as a baby so I’ll just take out all my frustrations on my poor, defenseless starship."

    mc "I do {b}not{/b} sound like that."

    ju "You do too!"

    mc "*sigh* I need coffee. Take over for a bit, will ya?"

    #ART In a flash of light she disappears from the console and appears in hologram form in the passenger seat beside us. She's a full body human-like AI.

    na "The hologram projectors spin up, Juneau taking a seat at the controls. I spin around and turn on the food synthesizer at the back of the ship."

    na "I set it to coffee, with French vanilla and sugar."

    ju "The sensor's picking up some strange gravimetric readings around these asteroids."

    ju "We'd better scan the area just to be safe. If we get stranded out here, I'll be stuck with you 'til you're dead and my batteries run out."

    mc "Oh, don't be a worrywart. Besides, it wouldn't be that bad!"

    mc "I'd just rewrite your program to make the perfect AI girlfriend for myself."

    ju "I'll eject you."

    mc "Don't worry, I'm only kidding. I like you just the way you are — annoyingly useful."

    #VA: Make a pout sound. Have fun with it! Whatever "pouting" sounds like LOL

    ju "I've set the computer to run a full scan of the belt. I estimate it'll take four hours to complete."

    mc "*sigh* fine."

    na "I grab my coffee and bring it back to my seat."

    na "A cup of holographic tea materializes into Juneau's hand. She sips it gingerly."

    na "Damn. Four hours."

    na "At least I can take the scans back to the cartographer's guild on Lumin."

    na "I don't consider myself much of an explorer, but the extra money certainly helps."

    na "Maybe I’ll buy some new drink recipes for the synthesizer. Or a new outfit for Juneau."


    na "I wonder how she'd react if I installed a maid costume on her software kit."

    mc "Hahaha."

    ju "What?"

    mc "Nothing. Just thinking about some of the things we could buy when we get back to port."

    na "Juneau flys us through the belt with the grace that only a navigator could. Her movements are effortless and graceful as she maneuvers us through the asteroids."

    na "As much of a brat as she can be sometimes, you really have to appreciate her developer's attention to the little things."

    mc "Hey Juneau. When we get back to Lumi-"

    #SFX whoosh
    #ART Wormhole appears outside the cockpit. Screen shake."

    ju "Woah!"


    mc "Juneau, report!"

    ju "We ran right into some kind of gravity well. Gravimetric readings are off the charts."

    mc "Show me."

    na "I take my seat next to her and bring up the local sensor interface."

    na "Dammit! I should have known."

    mc "It's a wormhole. We got caught in its well."

    mc "Forward full thrust. Give me manual control."

    ju "Huh? Okay! Forward thrust increased to full. What are you doing?"

    mc "We're caught in a gravity field. It'll tear the ship apart before we ever break free."

    mc "We gotta go through."

    ju "That's dangerous! Are you sure?"

    na "I instantly recognize Juneau's safety protocolskicking in. Though her personality routines may pretend otherwise, as the ship's navigator AI, Juneau has a responsibility to protect me."

    mc "Disengage safety. It's the only way we get out of this."

    ju "*sigh* If you kill me, it'll be on your conscience."

    ju "Handing you full navigational control."
    #SFX acceleration

    na "Faster and faster we go as I fly the ship straight into the  well."

    na "The ship begins to shake as we pick up speed."

    "Juneau clings to her seat, pulling her knees up to her chest. If she weren'tan AI, I might think she was scared out of her mind."


    ju "How can you be so calm at a time like this? We don't even know where it goes!"

    mc "We're about to find out."

    mc "I built this ship to fly, so lets fly."

    ju "Ah!"

    #ART Wormhole travel
    #SFX bang
    #ART asteroid flies across the windshield and hits towards the top of our ship.
    #art planet

    mc "..."
    ju "..."

    mc "What the fuck was that?"
    #Juneau glitches out

    ju "Impact! Hull breach det-"

    #SFX start ramping up the sound of atmosphere around the ship. Build it up on top of their conversation until we fade out of this scene.

    na "I turn to Juneau . She's gone."

    na "One by one, the displays power down."

    na "With the power out, I lose control of the ship's systems."

    na "With no steering, I've got no way to change course."

    na "And the current course happens to be right into a planet."

    mc "Shit. Don't wanna go there."

    mc "Juneau come back!"

    #SFX alarm starts going off. Cockpit is flashing red.

    na "Suddenly my console lights up. A notification from Juneau. Text only."

    #ART Juneau icon on one of the screens, animated? Indicating that you should put a helmet on.

    ju "You might want to put your helmet on now."

    #SFX roaring and crash sound effect.
    #ART fade to white, show the crash however you like.

    jump scene_2
