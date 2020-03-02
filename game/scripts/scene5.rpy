label scene_5:

 # ART GARAGE BG (with added boxes of junk)


    scene street_open with dissolve:
        subpixel True xpos -0.94 ypos -0.33 xanchor -0.04 yanchor None rotate None

    show le happy speaking a2 at stage_left with dissolve:
        xflip
    le "Tada!"


    mc side "Oooh! Someone did some cleanup."


    le  explaining "The crew salvaged everything from the crash site while we were in here yesterday."


    le "And last night we sorted things out into those boxes."


    le smirk a2 "Being careful not to break anything, of course."


    le happy speaking a2 "Anyway, the big boxes have scrap metal and the little ones have all the gadgets we found."


    mc "What have I done to deserve you, Leona?"


    mc "Give my thanks to your crew too."


    le  happy2 a1 "Hehe!"


    le "So, what's on the agenda today?"


    mc "...I think it's time we found the other survivor."


    le questioning a3 "Other survivor?"


    le a2 "Do you mean your AI friend?"


    le speakingsurprised a1 "The one that's like a sister?"


    mc "That's the one. I'll introduce you once we get her back online."


    le "How do we do that?"


    mc "Not sure. Yesterday I touched up the hull and engine, but there's no power to release the hatch."


    mc "I guess that should be the first thing on the list."


    mc "Did you find any of my tools earlier?"


    le curious "Hmm? Well, we did find a bunch of things that might have been tools. We put them in one of the boxes."


    mc "Can you grab that for me? We're going to force the door."


    le questioning p2 "Force it? Isn't it magnetically sealed?"


    mc "You could tell?"


    le questioning a3 "Well, yeah, we used the same thing for the ark ship."


    mc "Then you should know the electromagnetic lock is fail secure."


    mc "That way, even if all power is drained, the hatch doesn't pop open in the vacuum of space."
    hide le with dissolve
    na "With a screwdriver fitted with a rubber tip, I jam the tool under the panel, thus revealing an electric port."

    mc "I'm a bit lazy when it comes to design, so the access panel is in the hatch itself. Watch."

    show le suspicious a2 at stage_left with dissolve:
        xflip

    na "Plugging the door into the hangar's power, the lock lights up."

    mc "Open Sesame!"

    na "Powered up and ready to go, I turn a safety lever. The hatch hisses and slowly swings open."

    show le surprised with Dissolve(.25)

    mc "Hold your applause, please!"


    le happy2 a1 "Encore!"


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


    mc "Leona, hook the battery to the transformer you found, and that to your hanger's power source. We should be set once you're done."

    na "These past few days without Juneau have been agonizing. Even if her hardware appears to be good to go, I won't know until I boot her up."
    na " And while I've examined the ship pretty thoroughly, I haven't looked into the availability of the parts needed to get this bird off the ground again."
    na "I have a list all drawn up, but priorities are priorities."
    na "Juneau comes first, always."


    mc "How're we doing, Leona?"

    "Almost got it!"

    na "She's surprisingly adept at the mechanical side of things, despite her clumsy nature."
    na "To be fair to her, she's been trying very hard to learn as much as she can. She wants to help me, bless her heart."
    na "While I could do all of this on my own, it feels good to have someone who isn't a collection of ones and zeros on my side for once."


    le "Ready!"

    na "Giving the relays one final checkup, I give Leona the word."
    na "She flips the breaker."
    na "A little bit of my anxiety fades as the power begins to flow. Step one is a success."
    na "At first, nothing happens. After I give it a few light taps, something jostles into place, and a status light blinks on."
    na "Yellow. That's better than nothing. Juneau is accepting power at least, but it needs some more time to warm up."
    na "I hook the computer into the hologram projector that they salvaged from the crash site."
    na "Just another part sucked out the ejection hatch with me, I guess."
    na "She won't be able to form hard light just yet, but at least she'll be on display."
    na "The light blinks slowly, then quickly, eventually becoming a solid green."
    show ju concerned a1 at hologram:
        stage_right
    ju "...Huh?"

    na "Juneau materializes."

    ju concerned a2 "I-Is t-that you? Raine? You’re okay?!"

    mc "Yeah, yeah! Leona here pulled my butt out of a tree and helped get you back online."
    show le happy a1 at stage_left with dissolve:
        xflip
    le "Hellooo~"

    ju snarky a1 "Hi! Thanks a bundle for the save. Those horns real?"

    le questioning a1 "Uuh, yes?"


    ju "Interesting. To think we'd find a planet with unknown aliens..."


    ju snarky a2 "I can't believe you've been out here having all the fun while I was offline!"
    show le speakingsurprised a1
    show ju annoyed a1
    with dissolve

    ju annoyed a1 "My clock says I was out for an entire day, Raine! You left me alone, you jerk!"

    mc "I-wait. You were the one that ejected me! {i}I'm{/i} the one that fell a couple thousand meters in nothing but a chair and fabric."


    ju sarcastic a1 e1 b4 "Oh boohoo, I'm Raine and I came out unscathed from my crash, oh woe is me!"


    ju annoyed a2 "{i}Your{/i} body wasn't torn to bits!"


    mc "Bah, you drama queen."

    na "This is good. This is {i}really{/i} good."
    na "She's acting just like herself. It appears things went right for once."
    na "Like old times, I ignore Juneau, looking over to my pride and joy."


    ju snarky a1 "Pay attention to me, dammit!"


    le happy a2 "Oh, I'll do it! I've never talked to a computer before."


    mc "Juneau, if you start spilling personal details to her I will downgrade you to a food processor."


    ju "Spoil sport. Leona, let's chat~"
    hide ju
    hide le
    with moveoutright
    na "As the two get to know each other I scour what's left of my ship."
    na "Leona's team was nice enough to bring my ship back to the city, pieces and all, but my original assessment was right - this'll be one hell of a task."
    na "Honestly, I don't know if I'll be able to get this thing flying again. So many parts are ripped up, dented, melted or downright missing."
    na "Sighing, I stretch out my arms, ready for a very, very long day."

    show ju sarcastic a1 e2 at stage_right with dissolve
    ju "Hey, you're not allowed to slack now that you have me back, lazy ass."


    mc "Is that you volunteering for something?"


    ju annoyed a2 "I can multitask, unlike you fleshlings."

    ju "The bin of parts is to your right if you want to start fixing me up. It's about time too, since you've been off playing house with your special friend here-"

    mc "Pffffft-"

    na "As always, Juneau caught me off guard."


    ju speaking eclosed "-for so long I started forgetting what you looked like."

    show le concerned at stage_left with dissolve:
        xflip
    le "Special friend? What's that supposed to mean?"


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
    ju "Z-Zhtop that!"
    play sound "sfx/Kicking panel.ogg"
    show ju red sassy at stage_right:
        zoom .85
        ease .1 yanchor +10
        ease .1 yanchor -10
    ju "This is abuse! Help! Bad touch! Stranger danger!"

    hide ju with dissolve

    na "I think Juneau got the message, though Leona is looking a little lost."

    mc "Settle down already, we got shit to do."

    ju "You can start by fixing my hard light converters!"


    mc "Chill out, we're getting to it."

    scene sky with dissolve

    mc "Leona, can you grab that other box of parts? I can't find the bit I need in this one."


    le "Here ya go!"


    mc "Hmm?"


    mc "Are you sure this is the right box? I don't recognize any of this."


    le "It's got all the stuff we found at the crash site..."


    mc "This... this isn't from my ship."


    mc "Look, it's all rusty and caked in dirt too."


    le "So it's not human? I don't get it."


    mc "No, not a chance. It's not yours either."

    na "It’s like… some old drone equipment, and what looks like lifepod parts. A bunch of mini thrusters and some eye modules here and there, busted and grimy circuitry shattered in a dozen pieces."
    na "This looks absolutely ancient, but it's easily more advanced than whatever the locals have."
    na "I think I can use some of this!"
    na "Rifling through it, there's plenty that'll help me get basic functions online, like life support and carbon dioxide scrubbing."


    mc "It might even be better than what I've got myself. You say you found it at the crash site?"


    le "According to my top lieutenant, yeah. Everything here came from that area."

    na "Hell, there's stuff here I can probably use to streamline my ship. Maybe the poor thing won't get torn apart next time I happen upon a wormhole."


    mc "Oh, that'll be a bit of a problem, Juneau. Engine's gone."


    ju "Whaddya mean 'gone?'"


    mc "I mean it's trashed. Nothing salvageable."

    na "With only the stuff on hand, I won't be able to get the ship to hover in atmosphere, let alone leave it."


    mc "Let's put a pin in this for now. I'll figure out how to fabricate a new one later."


    mc "Juneau, can you make a list for me?"


    ju "Sure, what do you need?"


    mc "For starters, two plasma injectors and three I.O.S.C chips. All destroyed on impact and needing replacements."


    mc "Two hyproxy manifolds are completely missing. They must have broken off when you came through the trees."

    na "I comb through what remains of my broken spaceship."
    na "Feels like someone put a blender through an even bigger blender."
    na "What a stinkin' mess."


    ju "Do you have any idea what it feels like seeing you poke through my carcass like a vulture?"


    mc "I could just plug you in now and letcha sort out the internals for me."


    ju "You would condemn a ghost to it's rotting corpse?!"


    mc "Only if it keeps complaining."


    ju "I should have just formatted myself the moment you tried to upload me into this junker back on Lumin..."


    mc "Just be thankful I decided to revive your sorry butt."


    mc "But if you'd rather return to the void until I get some parts in here, I might be accomodating."


    ju "Not a bad idea, honestly. The reactor here’s some of the worst nuclear engineering I’ve seen. I don’t know how I’m not blinking out of existence."


    le "I'm not surprised. To be honest, I didn't think it'd be enough juice for something so high tech."


    le "We're trying to switch over to solar right now since we can't find much radioactive material to fuel the reactor."


    mc "Sorry Juneau, looks like you're going back to sleep for a bit."


    ju "Well, before I go you should know the ship sensors are partially online and I'm detecting a large power source about 10 kilometers southwest."


    le "That doesn't sound right... There's nothing out there but mountains and some old cave systems."


    ju "Apparently not. Seeing the data, I'd say it's about three hundred meters under the surface. Maybe one of those caves leads down to something?"


    mc "Do you have the coordinates?"


    ju "I'll leave them up on the display. Wake me up if anything happens, alright?"


    mc "Will do. Thanks Juneau, you've been a huge help."


    ju "Entering Hibernation Mode. Night night."

# SFX POWERING DOWN
    play sound "sfx/power down.ogg"
# ART JUNEAU SPRITE VANISHES


    mc "Maybe I'll buy her a present when we get home to make up for all this."


    le "By 'home' you mean Lumin?" #Changed "home" to 'home' to avoid issues


    mc "Yeah."


    le "Is that your species homeworld?"


    mc "Nah, Lumin is one planet in the empire."


    mc "Like your people come from Dawne, my people came from a single planet too, and we made a lot of colonies. That was a really long time ago."


    le "What was it called?"


    mc "There are a few words for it. Terra, Earth, Gaea and so on."


    le "I wonder what it was like..."


    mc "I heard it was beautiful once. Humans don't have much reason to go there anymore."


    le "I think I'd still want to go see Dawne someday, even if it takes a while to get there."


    le "I'm happy I was born here on Fireside though. Something about all the nature feels, I dunno, right?"


    mc "Hmm, you've lost me. I prefer being up there, in space."


    mc "It's cozy living on such a small ship, and freeing to be able to just go anywhere in the galaxy."


    mc "Don't have to worry about the weather either."


    mc "Well, asteroids and wormholes aside."


    le "Wish I could go."


    le "Who knows what other civilizations are out there?"


    le "I wanna meet them and the human ones too."


    mc "Maybe you will. I mean, your people have managed to travel lightyears just to get here."


    mc "Regular space travel can't be too far behind."


    mc "Plus, since you've been such a lifesaver so far, I wouldn't be opposed to leaving behind some blueprints to make the technological jump that much easier."


    le "But it'll still be awhile, won't it?"


    mc "Rome wasn't built in a day, sadly."


    le "So what can we do right now? Maybe go check out those caves Juneau told us about?"


    mc "Worth a shot, I guess. Unless you have any better ideas?"


    le "Nope!"


    mc "Looks like we're going exploring then."


    le "Hell yeah!"


    mc "...Hell?"


    le "Oh, do you not know that expression?"


    mc "No, I do. I'm just surprised you know it."


    le "Interesting. Does that mean we have similar concepts about religion?"


    mc "Maybe. We can talk about that on the trip."


    le "Ooh, good idea. We can swap stories."

#VFX JOURNAL ENTRY ADDED 2

jump scene_6
