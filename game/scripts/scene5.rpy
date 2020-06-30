﻿label scene_5:

 # ART GARAGE BG (with added boxes of junk)

    play env "amb/Workshop.ogg" fadein 2.0
    scene street_open with dissolve:
        subpixel True xpos -0.94 ypos -0.33 xanchor -0.04 yanchor None rotate None

    voice "voice/5-default-1.ogg" #Leona (Dot)
    le happyspeaking a2 "Tada!"


    voice "voice/5-default-2.ogg" #Raine (Nat)
    mc side "Oooh! Someone did some cleanup."


    voice "voice/5-default-3.ogg" #Leona (Dot)
    le  explaining "The crew salvaged everything from the crash site while we were in here yesterday."


    voice "voice/5-default-4.ogg" #Leona (Dot)
    le "And last night we sorted things out into those boxes."


    voice "voice/5-default-5.ogg" #Leona (Dot)
    le smirk a2 "Being careful not to break anything, of course."


    voice "voice/5-default-6.ogg" #Leona (Dot)
    le happy speaking a2 "Anyway, the big boxes have scrap metal and the little ones have all the gadgets we found."


    voice "voice/5-default-7.ogg" #Raine (Nat)
    mc "What have I done to deserve you, Leona?"


    voice "voice/5-default-8.ogg" #Raine (Nat)
    mc "Give my thanks to your crew too."


    voice "voice/5-default-9.ogg" #Leona (Dot)
    le  happy2 a1 "Hehe!"


    voice "voice/5-default-10.ogg" #Leona (Dot)
    le "So, what's on the agenda today?"


    voice "voice/5-default-11.ogg" #Raine (Nat)
    mc "...I think it's time we found the other survivor."


    voice "voice/5-default-12.ogg" #Leona (Dot)
    le questioning a3 "Other survivor?"


    voice "voice/5-default-13.ogg" #Leona (Dot)
    le a2 "Do you mean your AI friend?"


    voice "voice/5-default-14.ogg" #Leona (Dot)
    le speakingsurprised a1 "The one that's like a sister?"


    voice "voice/5-default-15.ogg" #Raine (Nat)
    mc "That's the one. I'll introduce you once we get her back online."


    voice "voice/5-default-16.ogg" #Leona (Dot)
    le "How do we do that?"


    voice "voice/5-default-17.ogg" #Raine (Nat)
    mc "Not sure. Yesterday I touched up the hull and engine, but there's no power to release the hatch."


    voice "voice/5-default-18.ogg" #Raine (Nat)
    mc "I guess that should be the first thing on the list."


    voice "voice/5-default-19.ogg" #Raine (Nat)
    mc "Did you find any of my tools earlier?"


    voice "voice/5-default-20.ogg" #Leona (Dot)
    le curious "Hmm? Well, we did find a bunch of things that might have been tools. We put them in one of the boxes."


    voice "voice/5-default-21.ogg" #Raine (Nat)
    mc "Can you grab that for me? We're going to force the door."


    voice "voice/5-default-22.ogg" #Leona (Dot)
    le questioning p2 "Force it? Isn't it magnetically sealed?"


    voice "voice/5-default-23.ogg" #Raine (Nat)
    mc "You could tell?"


    voice "voice/5-default-24.ogg" #Leona (Dot)
    le questioning a3 "Well, yeah, we used the same thing for the ark ship."


    voice "voice/5-default-25.ogg" #Raine (Nat)
    mc "Then you should know the electromagnetic lock is fail secure."


    voice "voice/5-default-26.ogg" #Raine (Nat)
    mc "That way, even if all power is drained, the hatch doesn't pop open in the vacuum of space."
    hide le with dissolve
    na "With a screwdriver fitted with a rubber tip, I jam the tool under the panel, thus revealing an electric port."

    voice "voice/5-default-27.ogg" #Raine (Nat)
    mc "I'm a bit lazy when it comes to design, so the access panel is in the hatch itself. Watch."

    show le suspicious a2 at stage_left with dissolve:
        xflip

    na "Plugging the door into the hangar's power, the lock lights up."

    voice "voice/5-default-28.ogg" #Raine (Nat)
    mc "Open Sesame!"
    play sound "sfx/ship door.ogg"

    na "Powered up and ready to go, I turn a safety lever. The hatch hisses and slowly swings open."

    show le surprised with Dissolve(.25)

    voice "voice/5-default-29.ogg" #Raine (Nat)
    mc "Hold your applause, please!"


    voice "voice/5-default-30.ogg" #Leona (Dot)
    le happy2 a1 "Encore!"


    voice "voice/5-default-31.ogg" #Raine (Nat)
    mc "Now, let's bring the tool box inside and get to work on the central power."
    hide le with dissolve
# ART SHIP FOREGROUND, GARAGE BACKGROUND

    show street_open onlayer master:
        subpixel True
        parallel:
            ease 1.0 zoom 1.66
        parallel:
            ease 1.0 xanchor .37
        parallel:
            ease 1.0 yanchor .35
    na "After a bit of sleuthing and head scratching, Leona and I have a plan to restore power to the computer."
    na "Restoring power to the entire ship will be a lot more complicated, and for that we need Juneau anyway."
    na "Too strong a source, I fry her. Too weak, and nothing happens."


    voice "voice/5-default-32.ogg" #Raine (Nat)
    mc "Leona, hook the battery to the transformer you found, and that to your hanger's power source. We should be set once you're done."

    na "These past few days without Juneau have been agonizing. Even if her hardware appears to be good to go, I won't know until I boot her up."
    na " And while I've examined the ship pretty thoroughly, I haven't looked into the availability of the parts needed to get this bird off the ground again."
    na "I have a list all drawn up, but priorities are priorities."
    na "Juneau comes first, always."


    voice "voice/5-default-33.ogg" #Raine (Nat)
    mc "How're we doing, Leona?"
    voice "voice/5-default-34.ogg" #Leona (Dot)
    le "Almost got it!"

    na "She's surprisingly adept at the mechanical side of things, despite her clumsy nature."
    na "To be fair to her, she's been trying very hard to learn as much as she can. She wants to help me, bless her heart."
    na "While I could do all of this on my own, it feels good to have someone who isn't a collection of ones and zeros on my side for once."


    voice "voice/5-default-35.ogg" #Leona (Dot)
    le "Ready!"

    na "Giving the relays one final checkup, I give Leona the word."
    play sound "sfx/breaker.ogg"
    play sound3 "sfx/electric.ogg" fadein 3.0
    na "She flips the breaker."


    na "A little bit of my anxiety fades as the power begins to flow. Step one is a success."
    na "At first, nothing happens. After I give it a few light taps, something jostles into place, and a status light blinks on."
    na "Yellow. That's better than nothing. Juneau is accepting power at least, but it needs some more time to warm up."
    na "I hook the computer into the hologram projector that they salvaged from the crash site."
    na "Just another part sucked out the ejection hatch with me, I guess."
    na "She won't be able to form hard light just yet, but at least she'll be on display."
    na "The light blinks slowly, then quickly, eventually becoming a solid green."
    stop sound3 fadeout 1.0

    play sound "sfx/power up.ogg"
    show ju concerned a1 at hologram:
        stage_right
    voice "voice/5-default-36.ogg" #Juneau (Lily)
    ju "...Huh?"
    play music "Music/Raine and Juneau.ogg" fadein 3.0

    na "Juneau materializes."


    voice "voice/5-default-37.ogg" #Juneau (Lily)
    ju concerned a2 "I-Is t-that you? Raine? You’re okay?!"

    voice "voice/5-default-38.ogg" #Raine (Nat)
    mc "Yeah, yeah! Leona here pulled my butt out of a tree and helped get you back online."
    show le happy a1 at stage_left with dissolve:
        xflip
    voice "voice/5-default-39.ogg" #Leona (Dot)
    le "Hellooo~"

    voice "voice/5-default-40.ogg" #Juneau (Lily)
    ju snarky a1 "Hi! Thanks a bundle for the save. Those horns real?"

    voice "voice/5-default-41.ogg" #Leona (Dot)
    le questioning a1 "Uuh, yes?"


    voice "voice/5-default-42.ogg" #Juneau (Lily)
    ju "Interesting. To think we'd find a planet with unknown aliens..."


    voice "voice/5-default-43.ogg" #Juneau (Lily)
    ju snarky a2 "I can't believe you've been out here having all the fun while I was offline!"
    show le speakingsurprised a1
    show ju annoyed a1
    with dissolve

    voice "voice/5-default-44.ogg" #Juneau (Lily)
    ju annoyed a1 "My clock says I was out for an entire day, Raine! You left me alone, you jerk!"

    voice "voice/5-default-45.ogg" #Raine (Nat)
    mc "I-wait. You were the one that ejected me! {i}I'm{/i} the one that fell a couple thousand meters in nothing but a chair and fabric."


    voice "voice/5-default-46.ogg" #Juneau (Lily)
    ju sarcastic a1 e1 b4 "Oh boohoo, I'm Raine and I came out unscathed from my crash, oh woe is me!"


    voice "voice/5-default-47.ogg" #Juneau (Lily)
    ju annoyed a2 "{i}Your{/i} body wasn't torn to bits!"


    voice "voice/5-default-48.ogg" #Raine (Nat)
    mc "Bah, you drama queen."

    na "This is good. This is {i}really{/i} good."
    na "She's acting just like herself. It appears things went right for once."
    na "Like old times, I ignore Juneau, looking over to my pride and joy."


    voice "voice/5-default-49.ogg" #Juneau (Lily)
    ju snarky a1 "Pay attention to me, dammit!"


    voice "voice/5-default-50.ogg" #Leona (Dot)
    le happy a2 "Oh, I'll do it! I've never talked to a computer before."


    voice "voice/5-default-51.ogg" #Raine (Nat)
    mc "Juneau, if you start spilling personal details to her I will downgrade you to a food processor."


    voice "voice/5-default-52.ogg" #Juneau (Lily)
    ju "Spoil sport. Leona, let's chat~"
    hide ju
    hide le
    with moveoutright
    na "As the two get to know each other I scour what's left of my ship."
    na "Leona's team was nice enough to bring my ship back to the city, pieces and all, but my original assessment was right - this'll be one hell of a task."
    na "Honestly, I don't know if I'll be able to get this thing flying again. So many parts are ripped up, dented, melted or downright missing."
    na "Sighing, I stretch out my arms, ready for a very, very long day."

    show ju sarcastic a1 e2 at stage_right with dissolve
    voice "voice/5-default-53.ogg" #Juneau (Lily)
    ju "Hey, you're not allowed to slack now that you have me back, lazy ass."


    voice "voice/5-default-54.ogg" #Raine (Nat)
    mc "Is that you volunteering for something?"


    voice "voice/5-default-55.ogg" #Juneau (Lily)
    ju annoyed a2 "I can multitask, unlike you fleshlings."

    voice "voice/5-default-56.ogg" #Juneau (Lily)
    ju "The bin of parts is to your right if you want to start fixing me up. It's about time too, since you've been off playing house with your special friend here-"

    voice "voice/5-default-57.ogg" #Raine (Nat)
    mc "Pffffft-"

    na "As always, Juneau caught me off guard."


    voice "voice/5-default-58.ogg" #Juneau (Lily)
    ju speaking eclosed "-for so long I started forgetting what you looked like."

    show le concerned at stage_left with dissolve:
        xflip
    voice "voice/5-default-59.ogg" #Leona (Dot)
    le "Special friend? What's that supposed to mean?"


    voice "voice/5-default-60.ogg" #Raine (Nat)
    mc "It means there are some bugs to work out."
    show le suspicious a2 with dissolve
    pause (.3)
    hide le with moveoutleft
    pause (.5)
# SFX kICKING METAL
    play sound "sfx/Kicking panel.ogg"
# VFX JUNEAU SPRITE GLITCHING A bit
    show ju red worried a1 at stage_right with vpunch:
        zoom .85
        additive 0
        easein .1 additive 7
        easein .2 additive 0
    voice "voice/5-default-61.ogg" #Juneau (Lily)
    ju "Z-Zhtop that!"
    play sound "sfx/Kicking panel.ogg"
    show ju red sassy at stage_right:
        zoom .85
        ease .1 yanchor +10
        ease .1 yanchor -10
    voice "voice/5-default-62.ogg" #Juneau (Lily)
    ju "This is abuse! Help! Bad touch! Stranger danger!"

    hide ju with dissolve

    na "I think Juneau got the message, though Leona is looking a little lost."

    voice "voice/5-default-63.ogg" #Raine (Nat)
    mc "Settle down already, we got shit to do."

    voice "voice/5-default-64.ogg" #Juneau (Lily)
    ju "You can start by fixing my hard light converters!"


    voice "voice/5-default-65.ogg" #Raine (Nat)
    mc "Chill out, we're getting to it."

    scene sky with dissolve

    voice "voice/5-default-66.ogg" #Raine (Nat)
    mc "Leona, can you grab that other box of parts? I can't find the bit I need in this one."


    voice "voice/5-default-67.ogg" #Leona (Dot)
    le "Here ya go!"


    voice "voice/5-default-68.ogg" #Raine (Nat)
    mc "Hmm?"


    voice "voice/5-default-69.ogg" #Raine (Nat)
    mc "Are you sure this is the right box? I don't recognize any of this."


    voice "voice/5-default-70.ogg" #Leona (Dot)
    le "It's got all the stuff we found at the crash site..."


    voice "voice/5-default-71.ogg" #Raine (Nat)
    mc "This... this isn't from my ship."


    voice "voice/5-default-72.ogg" #Raine (Nat)
    mc "Look, it's all rusty and caked in dirt too."


    voice "voice/5-default-73.ogg" #Leona (Dot)
    le "So it's not human? I don't get it."


    voice "voice/5-default-74.ogg" #Raine (Nat)
    mc "No, not a chance. It's not yours either."

    na "It’s like… some old drone equipment, and what looks like lifepod parts. A bunch of mini thrusters and some eye modules here and there, busted and grimy circuitry shattered in a dozen pieces."
    na "This looks absolutely ancient, but it's easily more advanced than whatever the locals have."
    na "I think I can use some of this!"
    na "Rifling through it, there's plenty that'll help me get basic functions online, like life support and carbon dioxide scrubbing."


    voice "voice/5-default-75.ogg" #Raine (Nat)
    mc "It might even be better than what I've got myself. You say you found it at the crash site?"


    voice "voice/5-default-76.ogg" #Leona (Dot)
    le "According to my top lieutenant, yeah. Everything here came from that area."

    na "Hell, there's stuff here I can probably use to streamline my ship. Maybe the poor thing won't get torn apart next time I happen upon a wormhole."


    voice "voice/5-default-77.ogg" #Raine (Nat)
    mc "Oh, that'll be a bit of a problem, Juneau. Engine's gone."


    voice "voice/5-default-78.ogg" #Juneau (Lily)
    ju "Whaddya mean 'gone?'"


    voice "voice/5-default-79.ogg" #Raine (Nat)
    mc "I mean it's trashed. Nothing salvageable."

    na "With only the stuff on hand, I won't be able to get the ship to hover in atmosphere, let alone leave it."


    voice "voice/5-default-80.ogg" #Raine (Nat)
    mc "Let's put a pin in this for now. I'll figure out how to fabricate a new one later."


    voice "voice/5-default-81.ogg" #Raine (Nat)
    mc "Juneau, can you make a list for me?"


    voice "voice/5-default-82.ogg" #Juneau (Lily)
    ju "Sure, what do you need?"


    voice "voice/5-default-83.ogg" #Raine (Nat)
    mc "For starters, two plasma injectors and three I.O.S.C chips. All destroyed on impact and needing replacements."


    voice "voice/5-default-84.ogg" #Raine (Nat)
    mc "Two hyproxy manifolds are completely missing. They must have broken off when you came through the trees."

    na "I comb through what remains of my broken spaceship."
    na "Feels like someone put a blender through an even bigger blender."
    na "What a stinkin' mess."


    voice "voice/5-default-85.ogg" #Juneau (Lily)
    ju "Do you have any idea what it feels like seeing you poke through my carcass like a vulture?"


    voice "voice/5-default-86.ogg" #Raine (Nat)
    mc "I could just plug you in now and letcha sort out the internals for me."


    voice "voice/5-default-87.ogg" #Juneau (Lily)
    ju "You would condemn a ghost to it's rotting corpse?!"


    voice "voice/5-default-88.ogg" #Raine (Nat)
    mc "Only if it keeps complaining."


    voice "voice/5-default-89.ogg" #Juneau (Lily)
    ju "I should have just formatted myself the moment you tried to upload me into this junker back on Lumin..."


    voice "voice/5-default-90.ogg" #Raine (Nat)
    mc "Just be thankful I decided to revive your sorry butt."


    voice "voice/5-default-91.ogg" #Raine (Nat)
    mc "But if you'd rather return to the void until I get some parts in here, I might be accomodating."


    voice "voice/5-default-92.ogg" #Juneau (Lily)
    ju "Not a bad idea, honestly. The reactor here’s some of the worst nuclear engineering I’ve seen. I don’t know how I’m not blinking out of existence."


    voice "voice/5-default-93.ogg" #Leona (Dot)
    le "I'm not surprised. To be honest, I didn't think it'd be enough juice for something so high tech."


    voice "voice/5-default-94.ogg" #Leona (Dot)
    le "We're trying to switch over to solar right now since we can't find much radioactive material to fuel the reactor."


    voice "voice/5-default-95.ogg" #Raine (Nat)
    mc "Sorry Juneau, looks like you're going back to sleep for a bit."


    voice "voice/5-default-96.ogg" #Juneau (Lily)
    ju "Well, before I go you should know the ship sensors are partially online and I'm detecting a large power source about 10 kilometers southwest."


    voice "voice/5-default-97.ogg" #Leona (Dot)
    le "That doesn't sound right... There's nothing out there but mountains and some old cave systems."


    voice "voice/5-default-98.ogg" #Juneau (Lily)
    ju "Apparently not. Seeing the data, I'd say it's about three hundred meters under the surface. Maybe one of those caves leads down to something?"


    voice "voice/5-default-99.ogg" #Raine (Nat)
    mc "Do you have the coordinates?"


    voice "voice/5-default-100.ogg" #Juneau (Lily)
    ju "I'll leave them up on the display. Wake me up if anything happens, alright?"


    voice "voice/5-default-101.ogg" #Raine (Nat)
    mc "Will do. Thanks Juneau, you've been a huge help."


    voice "voice/5-default-102.ogg" #Juneau (Lily)
    ju "Entering Hibernation Mode. Night night."

# SFX POWERING DOWN
    play sound "sfx/power down.ogg"
# ART JUNEAU SPRITE VANISHES
    stop music fadeout 3.0

    voice "voice/5-default-103.ogg" #Raine (Nat)
    mc "Maybe I'll buy her a present when we get home to make up for all this."


    voice "voice/5-default-104.ogg" #Leona (Dot)
    le "By 'home' you mean Lumin?" #Changed "home" to 'home' to avoid issues


    voice "voice/5-default-105.ogg" #Raine (Nat)
    mc "Yeah."


    voice "voice/5-default-106.ogg" #Leona (Dot)
    le "Is that your species homeworld?"


    voice "voice/5-default-107.ogg" #Raine (Nat)
    mc "Nah, Lumin is one planet in the empire."


    voice "voice/5-default-108.ogg" #Raine (Nat)
    mc "Like your people come from Dawne, my people came from a single planet too, and we made a lot of colonies. That was a really long time ago."


    voice "voice/5-default-109.ogg" #Leona (Dot)
    le "What was it called?"


    voice "voice/5-default-110.ogg" #Raine (Nat)
    mc "There are a few words for it. Terra, Earth, Gaea and so on."


    voice "voice/5-default-111.ogg" #Leona (Dot)
    le "I wonder what it was like..."


    voice "voice/5-default-112.ogg" #Raine (Nat)
    mc "I heard it was beautiful once. Humans don't have much reason to go there anymore."


    voice "voice/5-default-113.ogg" #Leona (Dot)
    le "I think I'd still want to go see Dawne someday, even if it takes a while to get there."


    voice "voice/5-default-114.ogg" #Leona (Dot)
    le "I'm happy I was born here on Fireside though. Something about all the nature feels, I dunno, right?"


    voice "voice/5-default-115.ogg" #Raine (Nat)
    mc "Hmm, you've lost me. I prefer being up there, in space."


    voice "voice/5-default-116.ogg" #Raine (Nat)
    mc "It's cozy living on such a small ship, and freeing to be able to just go anywhere in the galaxy."


    voice "voice/5-default-117.ogg" #Raine (Nat)
    mc "Don't have to worry about the weather either."


    voice "voice/5-default-118.ogg" #Raine (Nat)
    mc "Well, asteroids and wormholes aside."


    voice "voice/5-default-119.ogg" #Leona (Dot)
    le "Wish I could go."


    voice "voice/5-default-120.ogg" #Leona (Dot)
    le "Who knows what other civilizations are out there?"


    voice "voice/5-default-121.ogg" #Leona (Dot)
    le "I wanna meet them and the human ones too."


    voice "voice/5-default-122.ogg" #Raine (Nat)
    mc "Maybe you will. I mean, your people have managed to travel lightyears just to get here."


    voice "voice/5-default-123.ogg" #Raine (Nat)
    mc "Regular space travel can't be too far behind."


    voice "voice/5-default-124.ogg" #Raine (Nat)
    mc "Plus, since you've been such a lifesaver so far, I wouldn't be opposed to leaving behind some blueprints to make the technological jump that much easier."


    voice "voice/5-default-125.ogg" #Leona (Dot)
    le "But it'll still be awhile, won't it?"


    voice "voice/5-default-126.ogg" #Raine (Nat)
    mc "Rome wasn't built in a day, sadly."


    voice "voice/5-default-127.ogg" #Leona (Dot)
    le "So what can we do right now? Maybe go check out those caves Juneau told us about?"


    voice "voice/5-default-128.ogg" #Raine (Nat)
    mc "Worth a shot, I guess. Unless you have any better ideas?"


    voice "voice/5-default-129.ogg" #Leona (Dot)
    le "Nope!"


    voice "voice/5-default-130.ogg" #Raine (Nat)
    mc "Looks like we're going exploring then."


    voice "voice/5-default-131.ogg" #Leona (Dot)
    le "Hell yeah!"


    voice "voice/5-default-132.ogg" #Raine (Nat)
    mc "...Hell?"


    voice "voice/5-default-133.ogg" #Leona (Dot)
    le "Oh, do you not know that expression?"


    voice "voice/5-default-134.ogg" #Raine (Nat)
    mc "No, I do. I'm just surprised you know it."


    voice "voice/5-default-135.ogg" #Leona (Dot)
    le "Interesting. Does that mean we have similar concepts about religion?"


    voice "voice/5-default-136.ogg" #Raine (Nat)
    mc "Maybe. We can talk about that on the trip."


    voice "voice/5-default-137.ogg" #Leona (Dot)
    le "Ooh, good idea. We can swap stories."

#VFX JOURNAL ENTRY ADDED 2

jump scene_6
