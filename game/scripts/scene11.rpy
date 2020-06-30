label scene_11:

    #ART Aster BG

    scene street_open_garage onlayer master with dissolve:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.22
            ease 1.0 xpos 0.09
        parallel:
            zoom 1.48
            ease 1.0 zoom 1.0

    $ hide_sides = ['Leona']
    show le tired at stage_right with dissolve

    na "I head outside after my talk with Juneau to see Leona idling by herself, leaning on the wall of a building across the street."

    voice "voice/11-default-1.ogg" #Raine (Nat)
    mc concernspeak "Leona! Any word on how things are going?"

    voice "voice/11-default-2.ogg" #Leona (Dot)
    le concernedspeaking "...We wait. That's about it, really."

    voice "voice/11-default-3.ogg" #Leona (Dot)
    le speakingtired "It'll take at least twenty minutes to set everything up, assuming nothing bites us in the ass over there."

    voice "voice/11-default-4.ogg" #Leona (Dot)
    le "I'm a little nervous, but it's far from the first time. We've been through rough spots before."

    voice "voice/11-default-5.ogg" #Leona (Dot)
    le concerned "...Even after everything, a lot of them still look up to me. It feels strange."

    voice "voice/11-default-6.ogg" #Raine (Nat)
    mc weary "Can't say I don't understand it. Every now and then you run into someone who you were {i}sure{/i} hated your guts, and all of a sudden they're talking it up like you're the best of pals."

    voice "voice/11-default-7.ogg" #Raine (Nat)
    mc wearyspeak "And it's hard to sit around doing nothing when there's something big going on. I can barely sit still for five minutes some of those days."

    voice "voice/11-default-8.ogg" #Leona (Dot)
    le shylook "Well, do you wanna do something for the time being, then?"

    voice "voice/11-default-9.ogg" #Leona (Dot)
    le "Or…"

    na "Leona's face looks shyly towards the ground, before she looks back up as her eyes meet mine."

    voice "voice/11-default-10.ogg" #Leona (Dot)
    le concernedspeaking "We should probably be talking about things while we still can. Since we have the time, I mean."

    na "...Oh god, here we go."

    voice "voice/11-default-11.ogg" #Raine (Nat)
    mc shyspeak "Y-You don't need to act so nervous about it, you know. Just makes me more anxious seeing you treat it like that."

    na "Leona fidgets around with her fingers a little bit…"

    voice "voice/11-default-12.ogg" #Leona (Dot)
    le speakingthink "W-well, I know this nice cafe that's a few blocks from here! I always liked going there whenever I had a bit of a break."

    voice "voice/11-default-13.ogg" #Raine (Nat)
    mc weary "Can we head back to your place, actually?"

    voice "voice/11-default-14.ogg" #Raine (Nat)
    mc yawn2 "All this chaos out here is giving me a headache. I need someplace quiet."

    voice "voice/11-default-15.ogg" #Leona (Dot)
    le shylook "W-Well, it's a little bit messy…"

    voice "voice/11-default-16.ogg" #Raine (Nat)
    mc stern "Don't care."

    voice "voice/11-default-17.ogg" #Leona (Dot)
    le speakingtired "You sure?"

    voice "voice/11-default-18.ogg" #Raine (Nat)
    mc annoyed "Absolutely. I've been in my fair share of messes before. I'd prefer that mess over this one."

    voice "voice/11-default-19.ogg" #Leona (Dot)
    le concernedspeaking "...Well, if you say so."

    na "Leona eyes cast toward the ground as she turns to lead us back to her home."

    show le concernedspeaking onlayer master:
        subpixel True xpos 0.75 xanchor 0.5 yanchor 1 zoom 1.21 rotate None
        parallel:
            xpos 0.75
            ease 0.5 xpos 0.7
            ease 1.0 xpos 2.0
        parallel:
            ypos 0
            ease 0.5 ypos 0
    pause(0.8)
    scene black with wiperight
    pause(0.8)
    na "She walks ahead of me, slowly and methodically. Taking her time."
    na "When we reach the front door, she slips inside without a word."
    na "Once I step inside, it'll be too late to back out."
    na "Take a deep, deep breath."
    na "Whatever happens, happens. That's how the world works."
    na "I reach out my hand, and creak open the door."
    na "Here goes nothing."
    stop env fadeout 2.0
    play sound3 "amb/Leonas House.ogg" fadein 2.0
    #ART Leona's home BG
    scene white with Dissolve(1.5)
    pause(0.5)
    scene house with Dissolve(4.5)
    pause(0.5)
    na "By the time I walk through the door, Leona is already sitting herself down on the couch."
    show le crying with Dissolve(1.5):
        subpixel True xpos 0.55 ypos 0 xanchor 0.5 yanchor 0.0 zoom 1.5 rotate None
    na "She crunches up her body, huddling her knees to her chest and wrapping them in her arms."
    $all_moves(camera_check_points={u'z': [(0, 0, None), (350, 30.0, 'ease')]})
    na "Careful not to disturb the quiet peace of this place, I slowly close the door behind me and walk over to her.."
    na "Several seconds pass, both of us unsure what to say to the other."
    na "But as always, she's the first to talk."

    voice "voice/11-default-20.ogg" #Leona (Dot)
    le cryingtalk "I'm sorry, Raine."

    na "Leona looks down to her feet, turning her eyes away from me."

    voice "voice/11-default-21.ogg" #Leona (Dot)
    le tired  "I was selfish. I tried to make you stay. That was wrong of me to do."

    voice "voice/11-default-22.ogg" #Leona (Dot)
    le crying "I let myself get scared and believe things I shouldn't have. I let myself think it was right because it was easier than saying goodbye."

    voice "voice/11-default-23.ogg" #Leona (Dot)
    le concernedspeaking "I thought if you never found a way to power your ship, you wouldn't bother trying to repair it anymore. That you'd give up and stay with me."

    voice "voice/11-default-24.ogg" #Raine (Nat)
    mc thankful "...I understand, and I-"

    voice "voice/11-default-25.ogg" #Leona (Dot)
    le "There's more."

    voice "voice/11-default-26.ogg" #Raine (Nat)
    mc "What else could there be? Weren't you just trying to protect me?"

    voice "voice/11-default-27.ogg" #Leona (Dot)
    le tired "...I had another selfish reason..."

    voice "voice/11-default-28.ogg" #Raine (Nat)
    mc "Okay."

    voice "voice/11-default-29.ogg" #Raine (Nat)
    mc shyspeak "What was it?"

    voice "voice/11-default-30.ogg" #Leona (Dot)
    le concernedspeaking "When I first realized how much more advanced you are compared to us, I had a bad thought."

    voice "voice/11-default-31.ogg" #Leona (Dot)
    le cryingtalk "I thought that if we became friends, maybe you'd give us some of your technology."

    voice "voice/11-default-32.ogg" #Raine (Nat)
    mc gentlehandtalk "...That's-"

    ##Some sort of impact to go along with Leona's next line - Camera zooms back out to normal while Leona gets closer at the same time.
    ##Flash of white as well as some sound effect of Leona hitting the couch
    ##Angry Shouting Sprite


    $camera_move(0, 0, 0, 0, duration=0.5)

    show le frustrated a1

    voice "voice/11-default-33.ogg" #Leona (Dot)
    le "I'm not done!" with hpunch

    voice "voice/11-default-34.ogg" #Leona (Dot)
    le "...I was in awe of you, ever since you arrived. It was amazing to actually have someone like you arrive."

    voice "voice/11-default-35.ogg" #Leona (Dot)
    le "And that first night, when you dove into bed and fell asleep, I couldn't help but keep glancing back at you out of the corner of my eye."

    voice "voice/11-default-36.ogg" #Leona (Dot)
    le "And I watched you for a good, long while."

    voice "voice/11-default-37.ogg" #Leona (Dot)
    le "All I could think of was how, by some miracle, you were actually here."

    voice "voice/11-default-38.ogg" #Leona (Dot)
    le "A real, living alien being."

    voice "voice/11-default-39.ogg" #Leona (Dot)
    le "And you looked so much like us."

    voice "voice/11-default-40.ogg" #Leona (Dot)
    le "And then like anyone else, you fell into bed like an explorer who'd had a bit too much of the world for the night."

    voice "voice/11-default-41.ogg" #Leona (Dot)
    le "I didn't just want to be your friend anymore, Raine."

    voice "voice/11-default-42.ogg" #Leona (Dot)
    le "I felt the need to help you. To keep you safe."

    voice "voice/11-default-43.ogg" #Leona (Dot)
    le frustratedshout "I thought... I thought that I should be the one responsible for you."

    voice "voice/11-default-44.ogg" #Leona (Dot)
    le "That, in a world like ours, it'd be easier if you just left everything to someone like me... So you wouldn't have to worry."

    voice "voice/11-default-45.ogg" #Leona (Dot)
    le frustrated a1 "That I could be someone you trusted-if I could be that for you. That I could be someone important to you, if I could be there for you."

    voice "voice/11-default-46.ogg" #Leona (Dot)
    le "That was my first mistake, thinking you needed my protection. And because of that, I hurt you."

    voice "voice/11-default-47.ogg" #Leona (Dot)
    le "And I'm sorry for that."

    voice "voice/11-default-48.ogg" #Leona (Dot)
    le "You have no idea how sorry I am."

    voice "voice/11-default-49.ogg" #Raine (Nat)
    mc surprised "...Are you done?"

    voice "voice/11-default-50.ogg" #Leona (Dot)
    le cryingtalk "...Y-Yeah."

    voice "voice/11-default-51.ogg" #Raine (Nat)
    mc "That's a lot to digest."

    voice "voice/11-default-52.ogg" #Leona (Dot)
    le "Sorry..."

    voice "voice/11-default-53.ogg" #Raine (Nat)
    mc shyspeak "I forgive you, Leona."

    voice "voice/11-default-54.ogg" #Leona (Dot)
    le crying2 "You... do...?"
    play music "music/Friends and Family.ogg" fadein 3.0
    voice "voice/11-default-55.ogg" #Raine (Nat)
    mc "Yeah. For all of it."

    voice "voice/11-default-56.ogg" #Raine (Nat)
    mc concernedspeak "Even for reading my journal, which you neglected to mention."

    voice "voice/11-default-57.ogg" #Leona (Dot)
    le "...But?"

    voice "voice/11-default-58.ogg" #Raine (Nat)
    mc gentlehandtalk "But nothin'. You understand that?"

    na "I sigh and lightly pat her shoulder."

    voice "voice/11-default-59.ogg" #Raine (Nat)
    mc "It's my life, Leona. And it's my choice to make."

    na "Leona looks shocked for a bit, glancing in my direction before turning back to the floor."

    voice "voice/11-default-60.ogg" #Leona (Dot)
    le crying "But it hurt you. Didn't it?"

    na "Several seconds pass as I try to pull the words out of my head."

    voice "voice/11-default-61.ogg" #Raine (Nat)
    mc "...Of course it did. It was one of the most painful things I've felt."

    voice "voice/11-default-62.ogg" #Raine (Nat)
    mc speaking "But it wasn't because I was stranded here. It wasn't because I couldn't go home."

    voice "voice/11-default-63.ogg" #Raine (Nat)
    mc shyspeak "I've had too many people try and tell me what they thought was best for me."

    voice "voice/11-default-64.ogg" #Raine (Nat)
    mc "People who thought they could make my decisions for me and walk all over me without a care in the world."

    voice "voice/11-default-65.ogg" #Raine (Nat)
    mc "Who made me think I wasn't worth anything if I didn't live up to what they thought I should be."

    voice "voice/11-default-66.ogg" #Raine (Nat)
    mc weary "And I wanted to think you were different than that. You were better than them!"

    voice "voice/11-default-67.ogg" #Raine (Nat)
    mc "You did so much for a girl you'd just met. I don't even know how I could repay someone like you."

    voice "voice/11-default-68.ogg" #Raine (Nat)
    mc "I wanted to trust you so badly. I did everything I could to push those feelings out of my heart."

    voice "voice/11-default-69.ogg" #Raine (Nat)
    mc weary "But…"

    voice "voice/11-default-70.ogg" #Raine (Nat)
    mc "When you confessed to me that you lied…"

    voice "voice/11-default-71.ogg" #Raine (Nat)
    mc "I let myself believe you were just the same as everyone else."

    voice "voice/11-default-72.ogg" #Raine (Nat)
    mc wearyspeak "It hurt because all I could see was the things I'd been fighting all my life."

    voice "voice/11-default-73.ogg" #Raine (Nat)
    mc "It hurt because I've been lied to so much, it makes me sick just thinking about it."

    voice "voice/11-default-74.ogg" #Raine (Nat)
    mc "And for the first time since I met you, I was afraid I couldn't trust you."

    voice "voice/11-default-75.ogg" #Raine (Nat)
    mc "And I let that fear break me and make everything worse."

    voice "voice/11-default-76.ogg" #Raine (Nat)
    mc sighing "All those times when I should have been scared, I wasn't because I was with you."

    voice "voice/11-default-77.ogg" #Raine (Nat)
    mc "I had a feeling I could trust you. I wanted it to be different this time."

    voice "voice/11-default-78.ogg" #Raine (Nat)
    mc "Being stuck in a tree, hanging by my ankles didn't scare me. I'd rather have died alone than been betrayed for the thousandth time."

    voice "voice/11-default-79.ogg" #Raine (Nat)
    mc "I'd prefer being eaten by a lion than getting shouted at about being a failure again."

    voice "voice/11-default-80.ogg" #Raine (Nat)
    mc "Even something like an explosion, I'd accepted as possible when I took off to space."

    voice "voice/11-default-81.ogg" #Raine (Nat)
    mc wearyspeak "It was when you weren't there that got me."

    voice "voice/11-default-82.ogg" #Raine (Nat)
    mc "I was this close to crying when I lost you in that cave."

    voice "voice/11-default-83.ogg" #Raine (Nat)
    mc "What would I do if I didn't have you around?"

    voice "voice/11-default-84.ogg" #Raine (Nat)
    mc "Even if I survived, I'd be alone and totally lost."

    voice "voice/11-default-85.ogg" #Raine (Nat)
    mc upset "...And when you lied to me, I let myself believe I was all alone to begin with."

    voice "voice/11-default-86.ogg" #Raine (Nat)
    mc wearyspeak "And I let myself get ruined by that fear."

    voice "voice/11-default-87.ogg" #Raine (Nat)
    mc "And I let myself do stupid, shitty things like hurt the people important to me."

    voice "voice/11-default-88.ogg" #Raine (Nat)
    mc "Up until I met you, Juneau was the only person I could trust."

    voice "voice/11-default-89.ogg" #Raine (Nat)
    mc "Even if she curses me out and makes me feel like the universe's biggest bitch, I know it's because she's hardwired to care."

    voice "voice/11-default-90.ogg" #Raine (Nat)
    mc upset "She's like the Mom I never had."

    voice "voice/11-default-91.ogg" #Raine (Nat)
    mc "And I felt, for awhile, that we're the same."

    voice "voice/11-default-92.ogg" #Raine (Nat)
    mc gentlehandtalk "People are different, though."

    voice "voice/11-default-93.ogg" #Raine (Nat)
    mc speaking "I took you for granted, Leona. And I paid the consequences for that."

    voice "voice/11-default-94.ogg" #Raine (Nat)
    mc "I decided it was better to run away and hide. Instead, I should have thought about what you were feeling."

    voice "voice/11-default-95.ogg" #Raine (Nat)
    mc "I didn't appreciate you like I should have."

    voice "voice/11-default-96.ogg" #Raine (Nat)
    mc "It's my life to live, and my choices to make. How I treat you is my responsibility, but I failed to be the person I wanted to be."

    voice "voice/11-default-97.ogg" #Raine (Nat)
    mc "And for that... I'm sorry."

    voice "voice/11-default-98.ogg" #Raine (Nat)
    mc upset "I'm sorry I wasn't a better friend."

    voice "voice/11-default-99.ogg" #Leona (Dot)
    le concerned "Raine?"

    show le:
        subpixel True xpos 0.55 ypos 0 xanchor 0.5 yanchor 0.0 zoom 1.5 rotate None
        ease 2.5 zoom 3.0
    pause 2.0
    scene cgKiss1 with Dissolve(0.5):
        zoom 0.75

    #ART KissCG1 - Getting Closer

    voice "voice/11-default-100.ogg" #Raine (Nat)
    mc "Uhhh, yeah?"

    voice "voice/11-default-101.ogg" #Leona (Dot)
    le "I told you, didn't I? I didn't just want to be a friend."

    voice "voice/11-default-102.ogg" #Leona (Dot)
    le "I want you to be my family. You're at least that important to me."

    voice "voice/11-default-103.ogg" #Leona (Dot)
    le "And family doesn't just mean looking out for those you care about."

    voice "voice/11-default-104.ogg" #Leona (Dot)
    le "It's about not giving up. About being able to brush yourself off and try again when things get tough."

    voice "voice/11-default-105.ogg" #Leona (Dot)
    le "And I'd like to try again, Raine, if you'd let me."

    #ART KissCG2
    scene cgKiss2 with dissolve:
        zoom 0.75

    na "Leona leans in closer."
    na "As she does, my heart just about leaps out of my mouth."

    voice "voice/11-default-106.ogg" #Raine (Nat)
    mc "Do... Do you have something in mind?"

    voice "voice/11-default-107.ogg" #Leona (Dot)
    le "I want to help you build another ship"

    voice "voice/11-default-108.ogg" #Raine (Nat)
    mc "How? I can't use anything here."

    voice "voice/11-default-109.ogg" #Leona (Dot)
    le "So let's explore the rest of the planet."

    voice "voice/11-default-110.ogg" #Raine (Nat)
    mc "Is that why you're packing?"

    voice "voice/11-default-111.ogg" #Leona (Dot)
    le "There has to be something out there, right?"

    voice "voice/11-default-112.ogg" #Raine (Nat)
    mc "Do you really think you'll find anything?"

    voice "voice/11-default-113.ogg" #Leona (Dot)
    le "No idea. Does it matter?"

    voice "voice/11-default-114.ogg" #Raine (Nat)
    mc "It does."

    voice "voice/11-default-115.ogg" #Leona (Dot)
    le "Why?"

    voice "voice/11-default-116.ogg" #Raine (Nat)
    mc "Because..."

    voice "voice/11-default-117.ogg" #Raine (Nat)
    mc "If you can..."

    voice "voice/11-default-118.ogg" #Raine (Nat)
    mc "I'll be able to pay you back."

    voice "voice/11-default-119.ogg" #Leona (Dot)
    le "You mean it?"

    voice "voice/11-default-120.ogg" #Raine (Nat)
    mc "I do."

    voice "voice/11-default-121.ogg" #Leona (Dot)
    le "What if I don't want to be paid back?"

    voice "voice/11-default-122.ogg" #Raine (Nat)
    mc "Does it matter?"

    voice "voice/11-default-123.ogg" #Leona (Dot)
    le "It does."

    voice "voice/11-default-124.ogg" #Raine (Nat)
    mc "...It would be selfish then."

    voice "voice/11-default-125.ogg" #Leona (Dot)
    le "I'm okay with that."

    voice "voice/11-default-126.ogg" #Raine (Nat)
    mc "In that case... do you wanna..."

    voice "voice/11-default-127.ogg" #Raine (Nat)
    mc "Live... With me? On the new ship?"

    voice "voice/11-default-128.ogg" #Leona (Dot)
    le "Will it be small?"

    voice "voice/11-default-129.ogg" #Raine (Nat)
    mc "Probably."

    voice "voice/11-default-130.ogg" #Leona (Dot)
    le "And cozy?"

    voice "voice/11-default-131.ogg" #Raine (Nat)
    mc "Sure."

    voice "voice/11-default-132.ogg" #Leona (Dot)
    le "And until that happens?"

    voice "voice/11-default-133.ogg" #Raine (Nat)
    mc "We can get to know each other."

    voice "voice/11-default-134.ogg" #Leona (Dot)
    le "You want me to tell you more stories?"

    voice "voice/11-default-135.ogg" #Raine (Nat)
    mc "Only if they're about you."

    voice "voice/11-default-136.ogg" #Leona (Dot)
    le "And what about you?"

    voice "voice/11-default-137.ogg" #Raine (Nat)
    mc "I can tell you about the stars."

    voice "voice/11-default-138.ogg" #Leona (Dot)
    le "And you?"

    voice "voice/11-default-139.ogg" #Raine (Nat)
    mc "And me."

    voice "voice/11-default-140.ogg" #Leona (Dot)
    le "Promise?"

    voice "voice/11-default-141.ogg" #Raine (Nat)
    mc "Promise."

    voice "voice/11-default-142.ogg" #Leona (Dot)
    le "Anything else you want to get off your chest?"

    voice "voice/11-default-143.ogg" #Raine (Nat)
    mc "...Maybe."

    voice "voice/11-default-144.ogg" #Leona (Dot)
    le "Tell me."

    voice "voice/11-default-145.ogg" #Raine (Nat)
    mc "Well."

    voice "voice/11-default-146.ogg" #Raine (Nat)
    mc "I might..."

    voice "voice/11-default-147.ogg" #Leona (Dot)
    le "Juuuust?"

    voice "voice/11-default-148.ogg" #Raine (Nat)
    mc "have a bit of a thing."

    voice "voice/11-default-149.ogg" #Raine (Nat)
    mc "For... You."

    #ART KissCG3, followed by KissCG4
    scene cgKiss3 with Dissolve(1.5):
        zoom 0.75
    scene cgKiss4 with Dissolve(0.5):
        zoom 0.75
    voice "voice/11-default-150.ogg" #Leona (Dot)
    le "I know."

    voice "voice/11-default-151.ogg" #Raine (Nat)
    mc "Oh, to hell with it!"
    scene cgKiss3 with Dissolve(0.5):
        zoom 0.75 anchor (0.5, 0.5) align (0.5, 0.5)
    pause 0.5
    scene black with Dissolve(1.5)
    pause 4
    #ART KissCG3, followed by a fade to black
    #ART Black BG, sticks around for 5-8 seconds
    #SFX Ringing/Beeping from radio
    #ART Leona's room BG

    scene house with Dissolve(2.0)
    stop music fadeout 1.0

    $ hide_sides = []
    voice "voice/11-default-152.ogg" #Leona (Dot)
    le surprised "Oh my god, I almost forgot!"

    voice "voice/11-default-153.ogg" #Raine (Nat)
    mc shocked m2 "L-Leona!?"

    voice "voice/11-default-154.ogg" #Leona (Dot)
    le speakingsurprised a1 "Focus! Ship, radiation, explosion!"

    voice "voice/11-default-155.ogg" #Raine (Nat)
    mc "Oh crap, what's happening out there?"

    na "Leona scrambles off the couch, and me, and books it to the radio on the table."

    voice "voice/11-default-156.ogg" #Leona (Dot)
    le catching "This is Leona! {i}Please{/i} tell me something good!"

    na "Putting myself back together, I make note of how furious Leona's tail is wagging."
    na "I never really paid attention to it before, but it's pretty cute."
    na "Shoulda taken the opportunity to take a handful of that fur and just-"


    voice "voice/11-default-157.ogg" #Leona (Dot)
    le "Raine! We're in the clear!"

    voice "voice/11-default-158.ogg" #Raine (Nat)
    mc surprised "Hmm, what? It worked? How do you know if we haven't talked to Juneau?"

    voice "voice/11-default-159.ogg" #Leona (Dot)
    le "That was her! She said the radiation is subsiding!"

    voice "voice/11-default-160.ogg" #Raine (Nat)
    mc shocked m2 "Really? She must have tied herself into communications through the Ark..."

    voice "voice/11-default-161.ogg" #Leona (Dot)
    le happy a2 "Who cares?! We're saved!"

    voice "voice/11-default-162.ogg" #Leona (Dot)
    le "Get up, we gotta go celebrate!"

    voice "voice/11-default-163.ogg" #Leona (Dot)
    le "I can go buy a bunch of meat and eggs and we can grill it and Lua can get us some of her special veggie brew and we'll-"
    stop env fadeout 3.0
    #ART Black BG
    scene black with Dissolve(2.0)
    na "She goes on and on, completely over the moon."
    na "After awhile she drags me out of the house, still psyched out and rambling about a party."
    na "It takes no small amount of effort to convince her to go see Juneau with me first, but she eventually yields."
    play env "amb/Workshop.ogg"fadein 2.0
    #ART Garage BG

    $ hide_sides = ['Juneau', 'Leona']
    scene street onlayer master with dissolve:
        subpixel True xpos 0.09 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None zoom 1.0
    show le happy a1 at stage_right with dissolve

    voice "voice/11-default-164.ogg" #Leona (Dot)
    le "Juneau! We did it!"
    play music "music/A Future Together.ogg" fadein 4.0
    show ju snarky a1 at stage_center with dissolve

    voice "voice/11-default-165.ogg" #Juneau (Lily)
    ju "Didn't I {b}just{/b} tell you that?"

    voice "voice/11-default-166.ogg" #Raine (Nat)
    mc happy "Give her a minute, she's a little high on life."

    voice "voice/11-default-167.ogg" #Leona (Dot)
    le happy speaking a2 "Hey, you should be just as happy!"

    voice "voice/11-default-168.ogg" #Leona (Dot)
    le happy speaking a3 "Afterall, we got big days ahead of us, don't we, Rainey?"

    voice "voice/11-default-169.ogg" #Raine (Nat)
    mc surprised "Excuse me?"

    voice "voice/11-default-170.ogg" #Juneau (Lily)
    ju "Rainey?"

    voice "voice/11-default-171.ogg" #Juneau (Lily)
    ju snarky a2 "Girl, I don't know what you did, but keep it up."

    voice "voice/11-default-172.ogg" #Juneau (Lily)
    ju "You might not die alone at this rate."

    voice "voice/11-default-173.ogg" #Raine (Nat)
    mc upset "You, shut face!"

    voice "voice/11-default-174.ogg" #Leona (Dot)
    le happy speaking a2 "Tehehe, you're not embarrassed now, are you?"

    voice "voice/11-default-175.ogg" #Raine (Nat)
    mc shocked armraised "What? No. No!"

    voice "voice/11-default-176.ogg" #Leona (Dot)
    le happy speaking a3 "Oh ho? You should tell her then."

    voice "voice/11-default-177.ogg" #Raine (Nat)
    mc surprised "Yeah, yeah."

    voice "voice/11-default-178.ogg" #Juneau (Lily)
    ju snarky a1 "This oughta be good."

    voice "voice/11-default-179.ogg" #Raine (Nat)
    mc "Well, for starters. We made up."

    voice "voice/11-default-180.ogg" #Leona (Dot)
    le happy2 a1 "You mean 'out'."

    voice "voice/11-default-181.ogg" #Raine (Nat)
    mc upset "Shhh!"

    voice "voice/11-default-182.ogg" #Juneau (Lily)
    ju concerned a1 "Raine, you didn't actually {i}share{/i} your {i}feelings{/i} did you?!"

    voice "voice/11-default-183.ogg" #Raine (Nat)
    mc upset "I hate you. So much."

    voice "voice/11-default-184.ogg" #Juneau (Lily)
    ju "This {b}is{/b} cause to celebrate...!"

    voice "voice/11-default-185.ogg" #Leona (Dot)
    le happy speaking a2"That's what I said!"

    #VFX Fade to black
    stop env fadeout 3.0

    scene sky with dissolve:
        zoom 0.75

    na "Leona and Juneau continue making a fuss. Shortly thereafter, the crew shows up, looking pleased now that the whole ordeal was behind the City."
    na "Eventually, Leona brings up her plans to feast and the mood further improves."
    na "It's not long before we break the news of the journey we'll be setting out on."
    na "Juneau is less than thrilled she won't be coming with us, but Leona brought up a good reason to stay behind in Aster anyway."
    na "With an AI's help, the city's efficiency should go through the roof. Not to mention, all the new tech she could give info on."
    na "With Juneau's database, plans to build a better Ark ship could be expedited."
    na "Given time, they'll be able to return to Dawne and gather the rest of their people."
    na "It'll still be awhile before it can happen, but there will be more than enough time to make backups of Juneau's database."
    na "Even if it takes a few years for Leona and I to scour the planet in search of alien technology, chances are we three will be able to leave Fireside long before the influx of Dawnese immigrants."
    na "And with Juneau now connected to the communications network, I doubt we'll ever be out of touch for too long."

    scene space with dissolve:
        zoom 0.75

    na "With all this in mind, we cut loose and celebrate together long into the night."
    na "By the time everyone had tuckered out, half the crew had gotten so drunk they passed out on the garage floor."
    na "They're not much for words, but it's nice to know that no matter what species you are, there's a party animal in all of us."
    na "As Leona and I decided to go back to her house for the night, Juneau began conjuring up hard light blankets for the strung out crewmen."
    na "We waved goodnight and left, our spirits raised and optimistic for what may lay before us tomorrow."

    scene black with Dissolve(1.5)

    jump epilogue
