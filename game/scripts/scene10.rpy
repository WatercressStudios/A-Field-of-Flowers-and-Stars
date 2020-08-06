label scene_10:
    play sound3 "sfx/running.ogg"
    #ART Aster BG
    show street_open_garage:
        ease 4.0 xpos 1.0

    na "I run through Aster's streets, my feet clattering against the ground."
    na "What do I even say to her?"
    na "'Hey, we're all screwed if you don't help. Oh, and I'm sorry for being an asshole.'"
    na "I don't know how I'm going to apologize and bring up the current predicament at the same time."
    na "...I should've appreciated her more. She's been trying to help me since I arrived."
    na "What have I done for her except cause trouble?"
    na "...I gotta get my head together. I have more than our relationship to worry about right now."
    na "Just... Do the right thing for once in your damn life, Raine."

    #ART Leona sprite appears, she is not amused
    stop sound3 fadeout 1.0
    show le concerned at stage_right with Dissolve(1.5)
    na "As I approach her home, Leona comes out the front door."
    na "And with that I'm out of preptime."

    voice "voice/10-default-1.ogg" #Raine (Nat)
    mc shocked armraised "H-Hey, Leona.."

    $ hide_sides = ['Leona']
    voice "voice/10-default-2.ogg" #Leona (Dot)
    le "Hey. Did you leave something behind?"

    voice "voice/10-default-3.ogg" #Raine (Nat)
    mc unimpressed "...No. That's not why I'm here."

    voice "voice/10-default-4.ogg" #Raine (Nat)
    mc thankful "I have something important to talk about. It isn't very simple but we need to do something."

    voice "voice/10-default-5.ogg" #Leona (Dot)
    le tired "I've been through enough today. I can't handle this right now."

    voice "voice/10-default-6.ogg" #Raine (Nat)
    mc stern "It's important. More important than whatever's between us right now."

    voice "voice/10-default-7.ogg" #Raine (Nat)
    mc shyspeak "...I'm sorry about the way I treated you. Whether I was upset or not, I overreacted. You deserve better than that."

    voice "voice/10-default-8.ogg" #Leona (Dot)
    le crying "Raine, I-"

    voice "voice/10-default-9.ogg" #Raine (Nat)
    mc "...I know, but we don't have time. Things suck right now, but something weird is happening to my ship and the Ark. If we don't do something, people are going to get hurt."

    voice "voice/10-default-10.ogg" #Raine (Nat)
    mc "There's some sort of a reaction that's causing radiation to build up in and around Aster."

    voice "voice/10-default-11.ogg" #Leona (Dot)
    le frustrated a1 "Radiation!? Because of the explosion?"

    voice "voice/10-default-12.ogg" #Raine (Nat)
    mc "I don't know how to explain it. Juneau detected some strange readings coming from the blast site."

    voice "voice/10-default-13.ogg" #Raine (Nat)
    mc blech "We figured out that whatever is coming from there is having an interaction with both of our ships."

    voice "voice/10-default-14.ogg" #Raine (Nat)
    mc speaking "Mine is sending out a rare form of radiation and it's causing the Ark's reactor to start to break down."

    voice "voice/10-default-15.ogg" #Raine (Nat)
    mc "And if we don't do something, everyone here could end up dead."

    voice "voice/10-default-16.ogg" #Leona (Dot)
    le "That's..."

    voice "voice/10-default-17.ogg" #Leona (Dot)
    le crying "...I can't help you, Raine. I'm just a civilian now, remember?"

    voice "voice/10-default-18.ogg" #Raine (Nat)
    mc stern "You're the only one who's willing to trust me, Leona."

    voice "voice/10-default-19.ogg" #Raine (Nat)
    mc "If I go storming the castle with prophecies of doom I doubt anybody will give me a second thought."

    voice "voice/10-default-20.ogg" #Raine (Nat)
    mc questioning2 "And I trust you. I need to trust you. If anybody can help me figure this out, it's you and only you. And I know I can't do it alone."

    voice "voice/10-default-21.ogg" #Leona (Dot)
    le "So what do you want me to do?"

    voice "voice/10-default-22.ogg" #Raine (Nat)
    mc unimpressed "We need to get back to Juneau, now. I don't think we have a lot of time before the effect begins to snowball."

    voice "voice/10-default-23.ogg" #Raine (Nat)
    mc "If that happens, there's no telling how far beyond radiation sickness will be."

    voice "voice/10-default-24.ogg" #Raine (Nat)
    mc shyspeak "Off the top of my head, the only thing I can think of is to disable the nuclear reactor inside the Ark ship. Didn't you mention that it's what powers the city?"

    voice "voice/10-default-25.ogg" #Leona (Dot)
    le tired "Not possible. Can't help you."

    voice "voice/10-default-26.ogg" #Raine (Nat)
    mc "Okay, what if we took some parts from it and used it to build a new engine for my ship?"

    voice "voice/10-default-27.ogg" #Raine (Nat)
    mc "If I take it and leave, the problem should be solved."

    voice "voice/10-default-28.ogg" #Leona (Dot)
    le crying2 "I just told you, that's not possible! Our entire city relies on that, Raine!"

    voice "voice/10-default-29.ogg" #Raine (Nat)
    mc grumpy "God! Damn it!"

    voice "voice/10-default-30.ogg" #Raine (Nat)
    mc stern "Fine! {b}Fine!{/b}"

    voice "voice/10-default-31.ogg" #Raine (Nat)
    mc "I hate that it's coming down to this!"

    voice "voice/10-default-32.ogg" #Raine (Nat)
    mc grumpy "Help me blow my ship up!"

    voice "voice/10-default-33.ogg" #Raine (Nat)
    mc "Or help me take it far away from here! Help me dump it in the ocean or blast it into space with a missile, {b}whatever{/b}!"

    voice "voice/10-default-34.ogg" #Raine (Nat)
    mc stern "Leona, people are going to die if something isn't done right {i}now{/i}!"

    voice "voice/10-default-35.ogg" #Leona (Dot)
    le frustratedshout "Stop yelling and get in the house! You're gonna freak the neighbors out!"
    stop env fadeout 2.0
    play sound3 "amb/Leonas house.ogg" fadein 2.0
    #ART Leona's House BG

    scene house with dissolve:
        zoom 0.75 anchor (0.5, 0.5) align (0.5, 0.5)
    na "Leona drags me inside by the arm and shuts the door behind her."

    show le concerned at stage_right with dissolve:
    voice "voice/10-default-36.ogg" #Leona (Dot)
    le "You'd destroy your ship to save us?"

    voice "voice/10-default-37.ogg" #Raine (Nat)
    mc blech "I may be an asshole, but I'm not a monster. There's too much at stake here for me to be some stubborn bitch."

    voice "voice/10-default-38.ogg" #Raine (Nat)
    mc shyspeak "Even if I wasn't stuck here, I can't leave you to die like that. That goes for everyone here."

    voice "voice/10-default-39.ogg" #Leona (Dot)
    le "I need to know, right now, if you truly mean that."

    voice "voice/10-default-40.ogg" #Leona (Dot)
    le "There's no going back on this. Your ship will not survive."

    voice "voice/10-default-41.ogg" #Raine (Nat)
    mc grumpy "...If that's what it takes, then that's what it takes. I already decided I couldn't sit here and do nothing."

    voice "voice/10-default-42.ogg" #Leona (Dot)
    le "And Juneau? What happens to her if your ship is gone?"

    voice "voice/10-default-43.ogg" #Raine (Nat)
    mc shocked armraised "...Oh, God, I hadn't thought of that."

    voice "voice/10-default-44.ogg" #Leona (Dot)
    le cryingtalk "We can't disable the nuclear reactor. Plenty of people could die from losing that power ."

    voice "voice/10-default-45.ogg" #Leona (Dot)
    le concernedspeaking "You can't get any parts from it either. The council would never allow it. We need everything there just to keep Aster running."

    voice "voice/10-default-46.ogg" #Raine (Nat)
    mc happy "The Ark ship! If we removed Juneau's hardware and hooked it up directly to the Ark's systems, she should be fine even if we destroy my ship."

    voice "voice/10-default-47.ogg" #Leona (Dot)
    le curious "It'd draw a lot of power, but it might work. Do we really need to remove her hardware though?"

    voice "voice/10-default-48.ogg" #Leona (Dot)
    le "Can't you like, just upload her or something?"

    voice "voice/10-default-49.ogg" #Raine (Nat)
    mc blech "Nope, interference aside, there's not enough time for an upload of that size."

    voice "voice/10-default-50.ogg" #Raine (Nat)
    mc speaking "We were looking to build a new engine with whatever we could find, so I had her try to access the central database to gather information."

    voice "voice/10-default-51.ogg" #Raine (Nat)
    mc "That's when we found out about the radiation."

    voice "voice/10-default-52.ogg" #Leona (Dot)
    le concerned "And you didn't ask me because we'd already..."

    voice "voice/10-default-53.ogg" #Raine (Nat)
    mc "None of that matters right now. We have to act, now."

    voice "voice/10-default-54.ogg" #Raine (Nat)
    mc "It's only going to get a lot worse."

    voice "voice/10-default-55.ogg" #Raine (Nat)
    mc stern "A handful of minutes could be all it takes."

    voice "voice/10-default-56.ogg" #Raine (Nat)
    mc "Juneau could be the first to go. Her systems are going to start scrambling the worse the radiation gets."

    voice "voice/10-default-57.ogg" #Leona (Dot)
    le frustrated a1 "This is a nightmare... Come on, let's go talk to her. I have an idea."

    voice "voice/10-default-58.ogg" #Raine (Nat)
    mc "Thank God, you're a lifesaver."

    na "Literally."

    voice "voice/10-default-59.ogg" #Raine (Nat)
    mc shyspeak "And Leona?"

    voice "voice/10-default-60.ogg" #Leona (Dot)
    le concerned "Hmm?"

    voice "voice/10-default-61.ogg" #Raine (Nat)
    mc "I...I really am sorry."

    voice "voice/10-default-62.ogg" #Leona (Dot)
    le "We can discuss this later. There's no time to waste."

    voice "voice/10-default-63.ogg" #Leona (Dot)
    le shylook "I promise we'll talk about it, but right now we need to go."

    hide le with dissolve

    na "Leona rushes past me, out the door."
    na "As I turn to follow, I notice the boxes around the door half filled with Leona's belongings."
    na "Is she moving out?"

    $ hide_sides = []

    voice "voice/10-default-64.ogg" #Leona (Dot)
    le frustrated a1 "Raine, hurry up! And don't forget to close the door!"

    voice "voice/10-default-65.ogg" #Raine (Nat)
    mc grumpy "Coming! On my way!"
    stop music fadeout 3.0
    show street_open_garage with dissolve:
        zoom 0.75 anchor (0.5, 0.5) align (0.0, 0.5)
        pause 0.5
        ease 1.0 xalign 0.9
    pause 1.0
    stop env fadeout 2.0
    play sound3 "amb/Workshop.ogg" fadein 2.0

    #ART Ship in Garage BG

    scene street_open_garage with dissolve:
        zoom 3.8 anchor (0.5, 0.5) align (0.86, 0.81)
    show cockpitoverlay2 with dissolve:
        zoom 0.75

    $ hide_sides = ['Juneau']
    show ju annoyed a1 at stage_right with dissolve

    voice "voice/10-default-66.ogg" #Juneau (Lily)
    ju "Could you two dilly-dally around any longer!?"

    voice "voice/10-default-67.ogg" #Juneau (Lily)
    ju annoyed a2 "A bit of an update while you were gone, I'm kinda basically {b}fucked{/b}!"
    play music "music/Critical .ogg" fadein 3.0

    voice "voice/10-default-68.ogg" #Juneau (Lily)
    ju "There's no way we can do anything to that Ark ship of yours from here, so the only viable option is to do something to this one!"

    voice "voice/10-default-69.ogg" #Juneau (Lily)
    ju annoyed a1 "To {b}me{/b}!"

    voice "voice/10-default-70.ogg" #Raine (Nat)
    mc happy "Calm down, Leona has an idea."

    voice "voice/10-default-71.ogg" #Leona (Dot)
    le happy a2 "We're gonna yank your hardware out and get rid of your ship."

    show ju annoyed a2
    voice "voice/10-default-72.ogg" #Juneau (Lily)
    ju "I reiterate; {b}fucked{/b}!" with hpunch

    voice "voice/10-default-73.ogg" #Leona (Dot)
    le "Calm down, we're going to hook you up to the Ark's systems."

    voice "voice/10-default-74.ogg" #Leona (Dot)
    le "There's an access port right outside, behind the ship."

    voice "voice/10-default-75.ogg" #Juneau (Lily)
    ju concerned a1 "Well why didn't you plug me in earlier?!"

    voice "voice/10-default-76.ogg" #Leona (Dot)
    le questioning a2 "Uh, hello? Aliens show up one day and we're supposed to give you that kind of access right away?"

    voice "voice/10-default-77.ogg" #Leona (Dot)
    le "Do you two not have security standards where you come from?"

    voice "voice/10-default-78.ogg" #Leona (Dot)
    le crazy "You're lucky I even got permission to let you jack into the power grid."

    voice "voice/10-default-79.ogg" #Juneau (Lily)
    ju snarky a2 "Does this mean I {i}shouldn't{/i} have access to the information network?"

    voice "voice/10-default-80.ogg" #Leona (Dot)
    le frustrated a1 "...No, of course not! How did you even manage that!?" with hpunch

    voice "voice/10-default-81.ogg" #Leona (Dot)
    le questioning a2 "Wait, is that why I had to reinitiate my mediapads?"

    voice "voice/10-default-82.ogg" #Raine (Nat)
    mc grumpy "Tick tock, people. Wasting time!"

    voice "voice/10-default-83.ogg" #Juneau (Lily)
    ju snarky a1 "She's right, we gotta get to work!"

    scene street_open_garage:
        zoom 3.8 anchor (0.5, 0.5) align (0.86, 0.81)
        ease 0.5 zoom 2.5 xalign 0.91
    pause 0.5
    #ART Garage BG

    na "While I set to work unhooking Juneau's systems from the ship, Leona helps to carry her out, piece by piece."
    na "Once she's off the ship, Leona opens up a panel to the Ark's network access portal."
    na "I hook Juneau up to the network, and at the same time Leona grabs her radio from her bag."

    voice "voice/10-default-84.ogg" #Leona (Dot)
    le frustrated a1 "Hey, it's Leona! Urgent need of a last-minute favor!"

    na "Within minutes, the crew spilled in and helped strip the ship inside and out for anything that looked even remotely useful."
    na "By the time I was ready to bring Juneau back online, a whirlwind had passed through the garage."
    na "When they were done unloading the ship, they had attached lines from a handful of hoverbikes and hauled the ship away."

    voice "voice/10-default-85.ogg" #Raine (Nat)
    mc happy "...Alright, that should do it."

    #VFX Juneau powers up/sprite fades in
    show ju snarky a1:
        xalign 0.5
        hologram
    pause 0.5
    stop music fadeout 3.0

    voice "voice/10-default-86.ogg" #Juneau (Lily)
    ju "Yay! Thanks for not getting me killed!"

    voice "voice/10-default-87.ogg" #Raine (Nat)
    mc "You're not out of the woods yet. Without the ship's bulkhead shielding you from the radiation, you're basically a canary in a coal mine."

    voice "voice/10-default-88.ogg" #Juneau (Lily)
    ju "Fan-fuckin'-tastic."

    voice "voice/10-default-89.ogg" #Leona (Dot)
    le "How are you feeling? Can I get a status report?"

    voice "voice/10-default-90.ogg" #Juneau (Lily)
    ju "I had to offload some processes onto the Ark computer systems, but other than that I'm fine."

    voice "voice/10-default-91.ogg" #Leona (Dot)
    le "Good. Do you have access to the Ark's sensors?"

    voice "voice/10-default-92.ogg" #Juneau (Lily)
    ju "All's good to go, but it's primitive as all hell. I have no idea how this mess handled an interplanetary trip to begin with. What's on your mind?"

    voice "voice/10-default-93.ogg" #Leona (Dot)
    le crazy "Locate your ship. We're having it moved out to the mountain range."

    voice "voice/10-default-94.ogg" #Juneau (Lily)
    ju "Aye, I see it! What's the plan?"

    voice "voice/10-default-95.ogg" #Leona (Dot)
    le catching "Scouts found a hole in the rubble of the explosion, shaped like a large shaft. Runs deep enough that we haven't even begun to reach the bottom, a dozen kilometers at bare minimum."

    voice "voice/10-default-96.ogg" #Leona (Dot)
    le "We're using it as our disposal ground, but I have a question first."

    voice "voice/10-default-97.ogg" #Leona (Dot)
    le smug a3 "Which would be more effective; burying or outright destruction?"

    voice "voice/10-default-98.ogg" #Raine (Nat)
    mc "Either of those could work, I think."

    voice "voice/10-default-99.ogg" #Juneau (Lily)
    ju "Better safe than sorry; both, if you can manage it."

    voice "voice/10-default-100.ogg" #Juneau (Lily)
    ju snarky a2 "Even with these stone-age sensors I can tell the radiation is all over the place. It's definitely getting stronger."

    voice "voice/10-default-101.ogg" #Juneau (Lily)
    ju "I've got less than 30 minutes before the rads overload me, just about. After that, there's no telling what'll happen."

    voice "voice/10-default-102.ogg" #Leona (Dot)
    le crazy "Alright. The plan is to drop the ship into the pit, and line the shaft with explosives from above."

    voice "voice/10-default-103.ogg" #Leona (Dot)
    le "Then we set it to blow and send the whole thing crashing in on itself."

    voice "voice/10-default-104.ogg" #Juneau (Lily)
    ju snarky a1 "And the rubble will act like a cork, sealing any residual radiation from the remains!"

    voice "voice/10-default-105.ogg" #Raine (Nat)
    mc onfire "My poor baby..."

    voice "voice/10-default-106.ogg" #Juneau (Lily)
    ju "Oh, get over it. You've built three already, a fourth won't hurt."

    voice "voice/10-default-107.ogg" #Leona (Dot)
    le questioning a2 "Wait, did you actually build that thing?"

    voice "voice/10-default-108.ogg" #Raine (Nat)
    mc "Uh, yeah? Did I not mention that?"

    voice "voice/10-default-109.ogg" #Leona (Dot)
    le happy a2 "No! I thought you were just a really good mechanic or something!"

    voice "voice/10-default-110.ogg" #Raine (Nat)
    mc "Oh boy, do I have some stories for you then."

    voice "voice/10-default-111.ogg" #Juneau (Lily)
    ju snarky a2 "Not the time for this!"

    voice "voice/10-default-112.ogg" #Leona (Dot)
    le frustrated a1 "I'm moving, I'm moving!"

    voice "voice/10-default-113.ogg" #Leona (Dot)
    le snarky a1 "Sending out the order now! I'll let you know as soon as I hear back!"

    voice "voice/10-default-114.ogg" #Raine (Nat)
    mc happy "If all goes as planned, we'll be able to tell from here if it worked, right Juneau?"

    voice "voice/10-default-115.ogg" #Juneau (Lily)
    ju snarky a1 "Uh... Yeah. Sure. Assuming I'm not a fine metallic soup by then."

    voice "voice/10-default-116.ogg" #Leona (Dot)
    le shylook "...I'll leave you to it then."

    pause 0.5
    show ju:
        anchor (0.5, 1.0) align (0.5, -0.3) zoom 1.0
        ease 0.5 zoom 1.5 yalign -0.1
    pause 0.5

    na "As Leona steps out to make the call, Juneau leans in close, giving me the stink eye."


    voice "voice/10-default-117.ogg" #Raine (Nat)
    mc speaking "What?"

    voice "voice/10-default-118.ogg" #Juneau (Lily)
    ju snarky a2 "The hell was that?! She just saved everyone's bacon and you just sent her on her way!"

    voice "voice/10-default-119.ogg" #Raine (Nat)
    mc shyspeak "I didn't-fine, I'll go check up on her."
    stop sound3 fadeout 2.0
    play env "amb/City Night.ogg" fadein 2.0
    jump scene_11
