label scene1:
    scene space at main_menu_bg_transform
    show screen quick_menu
    show screen flower_menu_button with easeinright
    #This is the start of the game.
    #ART We begin in space. Nothing else is on the screen. "Warp drive particles" move slowly from left to right to imply motion. The stars in the background are still.

    na "All my life I've been looking for something."

    na "No, it's more than that."

    na "All my life, something has been calling out to me."

    na "Calling me towards the stars. Asking, begging to be found."

    # scene space at main_menu_bg_restore_transform
    # pause 6.0

    # ART - OVERLAY SHIP COCKPIT BG/SPRITE OVER SPACE BG
    # SFX - FADE IN GENTLE HUM OF SHIP ENGINES
    scene space at main_menu_bg_transform:
        ease 1.0 zoom 0.95
    pause 0.5
    show cockpitoverlay2 with dissolve:
        zoom 0.85
        anchor (0.5, 0.5)
        align (0.5, 0.0)
        easein 1.0 zoom 0.75 yalign 0.5
    play env "sfx/Warp engines.ogg" fadein 1.0

    na "And when this ship is ready, there will be nothing out of my reach."

    na "No star in the sky I can't touch."

    na "So…"

    voice "voice/1-scene1-1.ogg" #Raine (Nat)
    mc grumpy "So why won't you finish these damn calibrations already?!"

    voice "voice/1-scene1-2.ogg" #Raine (Nat)
    mc grumpy "I want to get back to exploring!"

    voice "voice/1-scene1-3.ogg" #Raine (Nat)
    mc upset "Finish! Come! Ooon!"

    # SFX - ONE SOLID KICK TO SOMETHING METAL.
    # VFX - WARP DRIVE PARTICLES FADE OUT
    # VFX- ZOOM INTO SHIP'S WINDOW AND CONTROL PANELS
    show cockpitoverlay2 with hpunch
    play sound2 "sfx/clunk.ogg"
    pause .5
    play sound "sfx/power down 1.ogg"
    scene space at main_menu_bg_restore_transform:
        zoom 0.95
        ease 2.0 zoom 1.0
    show cockpitoverlay2:
        zoom 0.75
        anchor (0.5, 0.5)
        align (0.5, 0.0)
    pause 2

    # SFX - DECELERATING FROM LIGHTSPEED TRAVEL.
    # ART - JUNEAU CONSOLE SPRITE (ANGRY) APPEARS
    # TIMING - THE ABOVE FIVE EFFECTS SHOULD TAKE PLACE OVER FIVE TO SEVEN SECONDS
    pause 1.0
    stop env fadeout 2.0
    play sound3 "sfx/engines.ogg" fadein 1.0

    #Scene spaceship normal

    #show ju snarky a1 at ju_side
    $ hide_sides = ['Juneau']
    voice "voice/1-scene1-4.ogg" #Juneau (Lily)
    ju snarky a1 "Hey! Stop kicking shit!"

    voice "voice/1-scene1-5.ogg" #Raine (Nat)
    mc questioning "Oh, Juneau."

    voice "voice/1-scene1-6.ogg" #Raine (Nat)
    mc questioning2 "About time you woke up. Gonna make yourself useful now or what?"

    #ART Juneau pouting

    voice "voice/1-scene1-7.ogg" #Juneau (Lily)
    ju @ a2 "I've been hard at work, I'll have you know. I'm just… having a little trouble with the procedure is all."

    voice "voice/1-scene1-8.ogg" #Juneau (Lily)
    ju @ concerned "The results keep coming back all screwy. It's been a real head scratcher."

    voice "voice/1-scene1-9.ogg" #Raine (Nat)
    mc "You must have a fried processor or something."

    voice "voice/1-scene1-10.ogg" #Juneau (Lily)
    ju snarky "Big talk coming from someone with a haywire personality routine."

    voice "voice/1-scene1-11.ogg" #Juneau (Lily)
    ju sarcastic a1 e1 b4 "Oh I'm Raine! I'm so impatient. The universe didn't love me enough as a baby so I’ll just take out all my frustrations on my poor, defenseless starship."

    voice "voice/1-scene1-12.ogg" #Raine (Nat)
    mc blech "I do {b}not{/b} sound like that."

    voice "voice/1-scene1-13.ogg" #Juneau (Lily)
    ju snarky "You do too!"

    voice "voice/1-scene1-14.ogg" #Raine (Nat)
    mc blech "*sigh* I need a breather. Take over for a bit."
    play sound "sfx/power up.ogg"

    $ hide_sides = ['Juneau']
    #ART In a flash of light she disappears from the console and appears in hologram form in the passenger seat beside us. She's a full body human-like AI.
    show ju snarky a1 onlayer master:
        stage_right
        hologram
    na "The hologram projectors come online and Juneau appears at the controls. I spin my seat around and head for the food synthesizer at the rear of the cockpit."
    na "With a press of a button, the machine materializes a toasty warm cup of coffee, French vanilla cream and extra sugar already included."

    show ju concerned a2 with dissolve
    voice "voice/1-scene1-15.ogg" #Juneau (Lily)
    ju "The sensors are picking up some strange gravimetric readings coming from somewhere within this asteroid field."

    show ju speaking eclosed with dissolve
    voice "voice/1-scene1-16.ogg" #Juneau (Lily)
    ju "Running a comprehensive scan just to be sure. If we hit something and get stranded out here, I'll be stuck with you 'til you're dead and my batteries run out."

    voice "voice/1-scene1-17.ogg" #Raine (Nat)
    mc amused "Oh, don't be a worrywart. Your batteries will die long before the food synthesizer's will."

    show ju annoyed a1 with vpunch
    voice "voice/1-scene1-18.ogg" #Juneau (Lily)
    ju "I have full authority to eject you whenever I desire, space or no space. You realize that, right?"

    voice "voice/1-scene1-19.ogg" #Raine (Nat)
    mc happy "Yeah, but your moral circuitry won't let you. I know it should, I installed it."

    #VA: Make a pout sound. Have fun with it! Whatever "pouting" sounds like LOL
    voice "voice/1-scene1-20.ogg" #Juneau (Lily)
    ju annoyed a1 "Tch!"

    voice "voice/1-scene1-21.ogg" #Raine (Nat)
    mc "Besides, if I get lonely I can just tweak those silly little subroutines you call a personality, reroute power, and reboot you as an adorable girlfriend to comfort me as we drift eternally into open space."

    voice "voice/1-scene1-22.ogg" #Juneau (Lily)
    ju snarky a1 "And then I can wait to die while cuddling your perfectly preserved corpse."

    voice "voice/1-scene1-23.ogg" #Raine (Nat)
    mc amused "Well, when you put it like that..."

    voice "voice/1-scene1-24.ogg" #Juneau (Lily)
    ju snarky a2 "Or I lock you out of the system right now and save myself all that trouble."

    voice "voice/1-scene1-25.ogg" #Raine (Nat)
    mc happy "Don't worry, I'm only kidding. I like you just the way you are — annoyingly useful."

    voice "voice/1-scene1-26.ogg" #Juneau (Lily)
    ju speaking eclosed "...Yeah yeah, keep begging for your life. See if I care..."

    voice "voice/1-scene1-27.ogg" #Juneau (Lily)
    ju annoyed a1 "I've set the computer to run a full scan of the belt. I estimate it'll take four hours to complete."

    voice "voice/1-scene1-28.ogg" #Raine (Nat)
    mc weary "Fine."
    hide ju with dissolve
    na "I retrieve my coffee from the receptacle and turn back towards the console."

    scene asteroidfield at main_menu_bg_transform with dissolve

    na "At least I can sell the data from the scan to the cartographer's guild on Lumin."
    na "I don't consider myself much of a map maker, but I guess the extra credits wouldn't hurt."
    na "Maybe I’ll buy some new drink recipes for the synthesizer. Or a new outfit for Juneau."
    na "I wonder how she'd react if I installed a maid costume on her software kit."

    show cockpitoverlay2:
        alpha 0
        zoom 0.78
        anchor (0.5, 0.5)
        align (0.5, 0.0)
        easein 0.5 zoom 0.75 yalign 0.5 alpha 1
    #play sound "sfx/power up.ogg"
    voice "voice/1-scene1-29.ogg" #Raine (Nat)
    mc happy "Hahaha."
    show ju snarky a3 onlayer master:
        stage_right
        hologram
    voice "voice/1-scene1-30.ogg" #Juneau (Lily)
    ju "What?"

    voice "voice/1-scene1-31.ogg" #Raine (Nat)
    mc "Nothing. Just thinking about some of the things we could buy when we get back to port."

    hide ju with Dissolve(1.0)

    na "Juneau guides us through the belt with the graceful touch that only an AI navigator could..."
    na "...gingerly sipping her own holographic tea, eyes closed, having a simulated good time while the bulk of her processing power pilots the ship."
    na "What a show off."
    na "As much of a brat as she can be at times, she was literally made for this role."
    na "I'd rate her a full three-and-a-half stars."

    voice "voice/1-scene1-32.ogg" #Raine (Nat)
    mc "Hey Juneau. When we get back to Lum- {nw}"

    scene asteroidfield_red at main_menu_bg_restore_transform
    show cockpitoverlay2:
        zoom 0.75
        anchor (0.5, 0.5)
        align (0.5, 0.0)

    #SFX whoosh
    play sound "sfx/wormhole.ogg"
    voice "voice/1-scene1-33.ogg" #Juneau (Lily)
    play music "Music/wormhole.ogg" fadein 3.0
    play env "sfx/SSL1.ogg" fadein 2.0
    show cockpitoverlay2:
        parallel:
            ease 0.3 zoom 0.8
        parallel:
            block:
                ease 0.25 pos (0.502, 0.003)
                ease 0.23 pos (0.498, -0.003)
                ease 0.27 pos (0.502, -0.003)
                ease 0.22 pos (0.498, 0.003)
                repeat
    ju red concerned a1 "Woah!" with vpunch
    #ART Wormhole appears outside the cockpit. Screen shake."
    $ hide_sides = []
    show asteroidfield_red:
        linear 60.0 align (0.2, 0.43)
    voice "voice/1-scene1-34.ogg" #Raine (Nat)
    mc shocked armraised "Juneau, report!"
    voice "voice/1-scene1-35.ogg" #Juneau (Lily)
    ju red concerned a1 "We ran right into some kind of gravity well. Gravimetric readings are off the charts."

    voice "voice/1-scene1-36.ogg" #Raine (Nat)
    mc "Show me."

    na "I slide my cup back into the synthesizer before returning to the console and bringing up the local sensor interface."

    voice "voice/1-scene1-37.ogg" #Raine (Nat)
    mc "It's a wormhole! We got caught in the gravity well!"

    na "Damn. I should have known. That explains the sensor readings."

    voice "voice/1-scene1-38.ogg" #Raine (Nat)
    mc annoyed "Forward full thrust! Give me manual control!"

    voice "voice/1-scene1-39.ogg" #Juneau (Lily)
    ju red worried a1 "Huh? Okay! Forward thrust increased to full. What are you doing?"
    #layer 2 spaceship
    stop sound3 fadeout 2.0
    stop env fadeout 2.0
    play sound4 "sfx/SSL1V2.ogg" fadein 2.0

    voice "voice/1-scene1-40.ogg" #Raine (Nat)
    mc "I told you, we're caught in its gravity well. The shear will tear the ship apart before we ever break free."

    voice "voice/1-scene1-41.ogg" #Raine (Nat)
    mc upset "The only way out is straight through!"

    voice "voice/1-scene1-42.ogg" #Juneau (Lily)
    ju worried speaking "That's dangerous! Are you sure?"

    na "I recognize Juneau's safety protocols kicking in. Though her personality subroutines may pretend otherwise, as the ship's navigator AI, Juneau has a responsibility to protect me."

    voice "voice/1-scene1-43.ogg" #Raine (Nat)
    mc happy "Disengage safety. It's the only way we get out of this."

    voice "voice/1-scene1-44.ogg" #Juneau (Lily)
    ju @ red sassy "If you kill me, it'll be on your conscience."

    voice "voice/1-scene1-45.ogg" #Juneau (Lily)
    ju "Handing you full navigational control."

    #SFX acceleration
    play env "sfx/engines2.ogg" fadein 2.0
    show asteroidfield_red:
        subpixel True
        parallel:
            ease 5.0 align (0.26, 0.37)
        parallel:
            ease 0.15 offset (2, 2)
            ease 0.13 offset (-2, -2)
            ease 0.17 offset (-2, 2)
            ease 0.12 offset (2, -2)
            repeat

    #laayer 2 spaceship v2
    na "Faster and faster we go as I fly the ship straight into the  well."


    na "The ship begins to shake as we pick up speed."

    na "Juneau clings to her seat, pulling her knees up to her chest."

    voice "voice/1-scene1-46.ogg" #Juneau (Lily)
    ju "How can you be so calm at a time like this? We don't even know where it goes!"

    voice "voice/1-scene1-47.ogg" #Raine (Nat)
    mc "We're about to find out!"

    voice "voice/1-scene1-48.ogg" #Raine (Nat)
    mc annoyed "I built this ship to fly, so let's fly straight down its throat!"

    # ###
    # VFX - SCREEN SHAKING BECOMES EVER MORE VIOLENT
    # ART/VFX - INSIDE THE WORMHOLE BG (LIKE A VORTEX, DOESN'T NEED TO BE FANCY SINCE IT DOESN'T LAST LONG. MAYBE JUST DISTORT/SPIN THE WORMHOLE BG?)
    show asteroidfield_red:
        linear .2 zoom 5
        parallel:
            linear .2 xanchor .27
            linear .2 yanchor .38
    play sound2 "sfx/astroid impact.ogg"
    play sound5 "sfx/SSL2.ogg"
    scene wormhole:
        subpixel True
        parallel:
            anchor (0.5, 0.5)
            zoom 1.55
            align (0.5, 0.5)
        parallel:
            block:
                rotate 0.0
                linear 5 rotate 359.9
                repeat
    show cockpitoverlay2:
        parallel:
            zoom 0.75
            anchor (0.5, 0.5)
            align (0.5, 0.0)
            ease 0.3 zoom 0.77
        parallel:
            block:
                ease 0.15 pos (0.504, 0.006)
                ease 0.13 pos (0.496, -0.006)
                ease 0.17 pos (0.504, -0.006)
                ease 0.12 pos (0.496, 0.006)
                repeat
    show wormhole with vpunch
    voice "voice/1-scene1-49.ogg" #Juneau (Lily)
    ju "Ah!"
    play sound3 "sfx/wormhole loop.ogg"
    pause 1.0

    # SFX - BANGING (ASTEROIDS HITTING THE HULL)
    # VFX - ASTEROIDS FLY ACROSS THE SCREEN OUTSIDE THE SHIP
    # TIMING - WAIT 2 SECONDS BEFORE NEXT EFFECT
    # ART - PLANET BG REPLACEES WORMHOLE BG
    # ###

    voice "voice/1-scene1-50.ogg" #Raine (Nat)
    mc shocked armraised "SHIT!"

    #Juneau glitches out



    voice "voice/1-scene1-51.ogg" #Juneau (Lily)
    ju red worried a1 "IMPACT - HULL BREACH DET-"

    play sound2 "sfx/astroid impact.ogg"
    scene stars:
        align (0.5, 0.5)
        alpha 15
        easein_elastic .5 yzoom .9
        parallel:
            ease .5 alpha 1
    show cockpitoverlay2:
        parallel:
            zoom 0.75
            anchor (0.5, 0.5)
            align (0.5, 0.0)
            ease 0.3 zoom 0.77
        parallel:
            block:
                ease 0.15 pos (0.504, 0.006)
                ease 0.13 pos (0.496, -0.006)
                ease 0.17 pos (0.504, -0.006)
                ease 0.12 pos (0.496, 0.006)
                repeat
    show stars with hpunch

    voice "voice/1-scene1-52.ogg" #Raine (Nat)
    mc upset "WHAT THE HELL WAS THAT?!"

    ###
    # SFX - START RAMPING UP THE SOUND OF ATMOSPHERE AROUND THE SHIP. BUILD IT UP ON TOP OF THEIR CONVERSATION UNTIL WE FADE OUT OF THIS SCENE.
    ###
    play sound4 "sfx/SSL3.ogg" fadein 1.0
    na "I turn to Juneau. She's gone."
    na "One by one, the displays power down."

    show stars:
        parallel:
            linear 15 zoom 1.5 align (0.0, 0.8)
        parallel:
            ease 0.15 offset (2, 2)
            ease 0.13 offset (-2, -2)
            ease 0.17 offset (-2, 2)
            ease 0.12 offset (2, -2)
            repeat

    na "I tug at the controls but the ship doesn't respond."
    na "With no steering, I've got no way to change course."
    na "And the current course happens to be...."
    na "...pulling us straight into a planet."

    voice "voice/1-scene1-53.ogg" #Raine (Nat)
    mc shocked armraised "Shit. Don't wanna go there."

    voice "voice/1-scene1-54.ogg" #Raine (Nat)
    mc annoyed "Out of the frying pan and into the fire."

    voice "voice/1-scene1-55.ogg" #Raine (Nat)
    mc upset "Juneau, I need you! Like, right now!"

    #SFX alarm starts going off. Cockpit is flashing red.

    pause 0.5


    na "My console flickers, just for a second. A notification from Juneau. Audio only."

    $ hide_sides = ['Juneau']
    voice "voice/1-scene1-56.ogg" #Juneau (Lily)
    ju "You might want to put your helmet on now."
    scene white with Dissolve(3)
    play sound "sfx/entry_intro.ogg"

    #SFX roaring and crash sound effect.

    #ART fade to white, show the crash however you like.

    stop sound3 fadeout 2.0
    stop sound4 fadeout 2.0
    stop env fadeout 2.0
    stop sound5 fadeout 2.0
    stop music fadeout 2.0
    play sound2 "sfx/Crash.ogg"

    jump scene_2
