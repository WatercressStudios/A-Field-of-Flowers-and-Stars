label epilogue:

    #ART Sky BG
    $ hide_sides = []
    voice "voice/12-default-1.ogg" #Leona (Dot)
    le happy a2 "Hurry up! Daylight's burnin'!"

    voice "voice/12-default-2.ogg" #Raine (Nat)
    mc blech "Uugh, can't you just let me sleep for once?"

    voice "voice/12-default-3.ogg" #Raine (Nat)
    mc concernspeak "{i}Especially{/i} after last night."

    voice "voice/12-default-4.ogg" #Leona (Dot)
    le "Oh, don't be like that."

    voice "voice/12-default-5.ogg" #Leona (Dot)
    le smug a2 "Besides, weren't you the one that begged me to keep you up?"

    voice "voice/12-default-6.ogg" #Raine (Nat)
    mc stern "You know that's not what I meant!"

    voice "voice/12-default-7.ogg" #Leona (Dot)
    le smug a3 "Don't care. You reap what you sow."

    voice "voice/12-default-8.ogg" #Leona (Dot)
    le crazy "Now, up! Up!" with hpunch

    voice "voice/12-default-9.ogg" #Leona (Dot)
    le "We've got a lot of ground to cover today!" with hpunch

    voice "voice/12-default-10.ogg" #Leona (Dot)
    le "Just think! We're this close to the end!" with hpunch

    voice "voice/12-default-11.ogg" #Raine (Nat)
    mc  "Yeah, right! What about the trip back? We've been out here for months!"

    voice "voice/12-default-12.ogg" #Leona (Dot)
    le kind a2 "Blame Juneau. She's the one that keeps sending us new maps."

    voice "voice/12-default-13.ogg" #Raine (Nat)
    mc questioning2 "So much for a slow roll. She's really been making progress back in Aster."

    voice "voice/12-default-14.ogg" #Raine (Nat)
    mc happy "I mean, actually launching satellites this quickly?"

    voice "voice/12-default-15.ogg" #Raine (Nat)
    mc "I'm starting to think we should have stayed in Aster. We could have a new ship by now if I were there."

    voice "voice/12-default-16.ogg" #Leona (Dot)
    le shylook  "That's true, but then I wouldn't have you all to myself, now would I?"

    voice "voice/12-default-17.ogg" #Raine (Nat)
    mc "Just be careful. With Juneau's eye in the sky, she could be watching our every move..."

    voice "voice/12-default-18.ogg" #Leona (Dot)
    le smirk a2  "Didn't stop you last night."

    voice "voice/12-default-19.ogg" #Raine (Nat)
    mc annoyed  "S-Shut up!" with hpunch

    scene sky_shootingstar with dissolve:
        zoom 0.75

    na "Even with Leona's constant flirting..."
    na "It's not been a bad life out here."
    na "Sure, we've seen more than our fair share of trouble, but together it feels like we can take on the world."
    na "It's nice to know that no matter what happens, we'll always have each other."
    na "At the end of the day, we'll still make camp in the fields."
    na "We'll still share stories, together at fire's side."
    na "And when we're tired, we'll sleep beneath the stars."
    na "And when we wake, we'll look forward to doing it all again."
    na "I'm thankful for it."
    na "And I'd do it all again if given the chance."

    #ART Sky BG 2

    voice "voice/12-default-20.ogg" #Leona (Dot)
    le curious "Raine, you see that? In the sky?"

    voice "voice/12-default-21.ogg" #Raine (Nat)
    mc surprised "Huh. Looks like a shooting star."

    voice "voice/12-default-22.ogg" #Leona (Dot)
    le "It seems... familiar."

    voice "voice/12-default-23.ogg" #Raine (Nat)
    mc "It's not burning up."

    voice "voice/12-default-24.ogg" #Raine (Nat)
    mc shocked armraised "I think it's crashing."

    voice "voice/12-default-25.ogg" #Leona (Dot)
    le happy a2 "Let's go check it out!"

    voice "voice/12-default-26.ogg" #Raine (Nat)
    mc happy "Right behind ya!"

    #VFX Fade to black
    #THE END
    scene black with dissolve

    hide screen flower_menu_button
    $ renpy.music.play(config.main_menu_music)
    call screen tobecontinued_announce
    call screen credits with dissolve
    pause 2.0
    $ persistent.ending = "Complete"
