label scene_12:
    play env "amb/workshop.ogg" fadein 2.0
    na "Well, it took a few days, but I think I have everything working now."
    na "The drive's in place, albeit with a few... extra modifications to work with my custom chassis."
    na "The rest of the parts Leona and I found were more than enough to get the rest of the ship up and running."
    #voice "voice/12-scene_12-1.ogg" #Raine (VA Name)
    mc "I think... we're ready."

    #show leona

    #voice "voice/12-scene_12-2.ogg" #Leona (VA Name)
    le "Ready for what?"
    #voice "voice/12-scene_12-3.ogg" #Raine (VA Name)
    mc "Ah, hey there."
    #voice "voice/12-scene_12-4.ogg" #Leona (VA Name)
    le "Hey."
    na "Just hearing her #voice is uplifting."
    #voice "voice/12-scene_12-5.ogg" #Raine (VA Name)
    mc "I was thinking... remember last night?"
    #voice "voice/12-scene_12-6.ogg" #Leona (VA Name)
    le "About the test flight?"
    #voice "voice/12-scene_12-7.ogg" #Raine (VA Name)
    mc "Yeah. I think we have things ready to go for one today. Interested?"
    #voice "voice/12-scene_12-8.ogg" #Leona (VA Name)
    le "Do you even have to ask? Of course I am!"
    #voice "voice/12-scene_12-9.ogg" #Raine (VA Name)
    mc "Well, step aboard."

    #show BG_new_ship

    na "The ship's interior is mostly how I remember it, but we had to make room for some of the older drive tech."
    na "Kind of reminds me of the old holovids I used to watch as a kid."
    na "Humans apparently thought you could get to the moon in just a tiny, cramped capsule launched out of a cannon."
    na "Now, several ages later, it looks like I'm doing much of the same."
    na "Minus the cannon part, that is."
    #voice "voice/12-scene_12-10.ogg" #Juneau (VA Name)
    ju "Welcome aboard, Raine. Are we flying today?"
    #voice "voice/12-scene_12-11.ogg" #Juneau (VA Name)
    ju "We can take the new girl up too. This 'new' drive you installed is pretty old, but it's twice as powerful as the one you made yourself."
    #voice "voice/12-scene_12-12.ogg" #Raine (VA Name)
    mc "Hey!"
    #voice "voice/12-scene_12-13.ogg" #Juneau (VA Name)
    ju "Just stating the facts."
    na "I'm... a little insulted, but also surprised that the drive really is that powerful."
    #voice "voice/12-scene_12-14.ogg" #Raine (VA Name)
    mc "How's everything else looking, Juneau?"
    #voice "voice/12-scene_12-15.ogg" #Juneau (VA Name)
    ju "Your hodgepodge assemblage of parts is looking good!"
    #voice "voice/12-scene_12-16.ogg" #Raine (VA Name)
    mc "Really? That's what you called the ship the {b}first{/b} time I tested it on Lumin."
    #voice "voice/12-scene_12-17.ogg" #Juneau (VA Name)
    ju "Hah! Wait, you actually believed me? No, I mean it this time. Despite the crash, you've done a good job getting this thing back into shape."
    #voice "voice/12-scene_12-18.ogg" #Juneau (VA Name)
    ju "Good job."
    #voice "voice/12-scene_12-19.ogg" #Raine (VA Name)
    mc "Heh, thanks. But it wasn't just me."
    na "Leona finally stops moving around the cabin in time for me to indirectly mention her."
    #voice "voice/12-scene_12-20.ogg" #Leona (VA Name)
    le "Oh, I helped!"
    na "Leona here found the parts we needed to get back in business."
    #voice "voice/12-scene_12-21.ogg" #Juneau (VA Name)
    ju "So I've heard. Good morning, Leona."
    #voice "voice/12-scene_12-22.ogg" #Leona (VA Name)
    le "Heya!"
    #voice "voice/12-scene_12-23.ogg" #Leona (VA Name)
    le "So, anything else we need to do?"
    #voice "voice/12-scene_12-24.ogg" #Juneau (VA Name)
    ju "Nope, you can just take a seat and strap in."
    #voice "voice/12-scene_12-25.ogg" #Leona (VA Name)
    le "Awesome!"
    na "Leona eagerly sits down at the nearest chair and bounces happily, waiting for me to sit down as well."
    #voice "voice/12-scene_12-26.ogg" #Raine (VA Name)
    mc "Okay, okay, easy girl."
    na "I take a seat and get the ship ready for launch."
    stop env fadeout 1.0

    #plane engine SFX
    play sound "sfx/engines up.ogg"
    pause 2.0
    play env "sfx/engines3.ogg" fadein 1.0

    #voice "voice/12-scene_12-27.ogg" #Leona (VA Name)
    le "So how do we get to—"

    play sound3 "sfx/engines2.ogg" fadein 1.0
    #faster engine SFX

    #voice "voice/12-scene_12-28.ogg" #Leona (VA Name)
    le "—spaaaaaaaace!?"

    na "The new drive whirs to life and rapidly accelerates us to escape velocity."
    play sound "sfx/power down 2.ogg"
    stop env fadeout 1.0
    stop sound3 fadeout 1.0
    na "In about a minute, we're at the edge of the atmosphere, successfully in orbit around Fireside."

    #voice "voice/12-scene_12-29.ogg" #Juneau (VA Name)
    ju "Okay, we're stable. You guys want to try zero gravity?"

    play music "music/floating.ogg" fadein 2.0

    #voice "voice/12-scene_12-30.ogg" #Leona (VA Name)
    le "Huh?"
    #voice "voice/12-scene_12-31.ogg" #Raine (VA Name)
    mc "C'mon, let me show you!"
    na "In one smooth motion, I unbuckle myself and Leona from our seats, and we start lifting out of our chairs."
    #voice "voice/12-scene_12-32.ogg" #Leona (VA Name)
    le "Ah! I'm floating!"
    #voice "voice/12-scene_12-33.ogg" #Raine (VA Name)
    mc "That's what zero gravity does, silly."
    na "I guide her around the cabin, showing her how to move around."
    #voice "voice/12-scene_12-34.ogg" #Leona (VA Name)
    le "Wheeee!"
    #voice "voice/12-scene_12-35.ogg" #Raine (VA Name)
    mc "Hey, now you're getting it!"
    na "Her eagerness is infectious. I don't know why, but when I see her grinning like that, I'm doing the exact same thing."
    na "Why haven't I been doing that?"
    na "How long has it been since I've really enjoyed myself?"
    na "And Juneau always said that I needed a vacation. Somehow, I don't think this is what she had in mind..."

    stop music fadeout 2.0

    #timeskip
    play env "amb/Leonas house.ogg" fadein 2.0
    na "Sometime later, we finish up our test flight and land back on Fireside."
    #voice "voice/12-scene_12-36.ogg" #Leona (VA Name)
    le "Raine, that was amazing!"
    #voice "voice/12-scene_12-37.ogg" #Raine (VA Name)
    mc "Was that your first time flying?"
    #voice "voice/12-scene_12-38.ogg" #Leona (VA Name)
    le "Not like that. My hoverbike is the most I've ever been off the ground."
    #voice "voice/12-scene_12-39.ogg" #Raine (VA Name)
    mc "You're missing out."
    #voice "voice/12-scene_12-40.ogg" #Leona (VA Name)
    le "On Dawne, they have bigger aircraft that can take lots of people and cargo, but we don't have anything like that on Fireside."
    #voice "voice/12-scene_12-41.ogg" #Raine (VA Name)
    mc "Why?"
    #voice "voice/12-scene_12-42.ogg" #Leona (VA Name)
    le "We don't have a need for it at the moment. We've spent most of our time and resources focused on building out Aster."
    #voice "voice/12-scene_12-43.ogg" #Raine (VA Name)
    mc "Ah, makes sense."
    na "Living here on this planet is like traveling through time. All the primitive tech, the lack of familiar amenities, and the open space here is nothing like I anticipated."
    na "It's equal parts exhilarating and exhausting."
    na "I'm so far from home, and yet I'm so excited to be here."
    na "I want to head out into space, but I can't help but wonder..."
    na "Would I be happier staying here with Leona?"
    #voice "voice/12-scene_12-44.ogg" #Leona (VA Name)
    le "Raine?"
    #voice "voice/12-scene_12-45.ogg" #Raine (VA Name)
    mc "Hm?"
    #voice "voice/12-scene_12-46.ogg" #Leona (VA Name)
    le "You looked like you were spacing out again. You okay?"
    #voice "voice/12-scene_12-47.ogg" #Raine (VA Name)
    mc "Yeah, sorry. Just a bit tired."
    #voice "voice/12-scene_12-48.ogg" #Leona (VA Name)
    le "Well, it's getting late anyway. Let's head home! I'll cook for you."
    #voice "voice/12-scene_12-49.ogg" #Raine (VA Name)
    mc "I'd like that."
    na "With the ship repaired, it's a simple matter to land within a few minutes of Leona's house."
    na "Leona points at the controls, asking about all of their functions while I fly us home."
    na "She's seriously cute when she does that."
    #voice "voice/12-scene_12-50.ogg" #Raine (VA Name)
    mc "Okay, we're here!"
    #voice "voice/12-scene_12-51.ogg" #Leona (VA Name)
    le "All right! That was incredible, Raine. I'll get dinner started!"
    na "Leona wastes no time in jumping out of the ship and setting up dinner."
    na "As she leaves, Juneau materialises next to me."
    #voice "voice/12-scene_12-52.ogg" #Juneau (VA Name)
    ju "You know, you need to make a decision soon."
    #voice "voice/12-scene_12-53.ogg" #Raine (VA Name)
    mc "Yea, yeah."
    #voice "voice/12-scene_12-54.ogg" #Raine (VA Name)
    mc "How was the analysis?"
    na "While Leona may have been the primary focus of our journey, Juneau and I had one other... secondary mission."
    #voice "voice/12-scene_12-55.ogg" #Juneau (VA Name)
    ju "It's still there, but not for long. We have a little over a day."
    #voice "voice/12-scene_12-56.ogg" #Raine (VA Name)
    mc "Until the wormhole's gone forever."
    #voice "voice/12-scene_12-57.ogg" #Juneau (VA Name)
    ju "Until the wormhole is gone forever."
    na "I nod to Juneau, understanding the gravity of the sitation. No pun intended, this time. I take my leave for the night."
    na "This very well may be the last chance I get. After today, I won't be able to see Leona's house... or her. I'll enjoy it while it lasts."
    na "As Leona continues her cooking, I can't help but think about our conversation the other night."
    na "Would Leona really be okay with me taking her with me?"
    na "She's got so much here: her people, her culture, and I'm sure she's got a lot of close friends and family she'd miss, too."
    na "And yet..."
    na "It'd be so easy to say 'yes' and take her with me."
    na "She'd be overjoyed. But is she doing this because she's in love with—"
    na "Oh my God."
    #voice "voice/12-scene_12-58.ogg" #Leona (VA Name)
    le "Raine? You there?"
    na "That's why she wants to come with."
    na "I'm such an idiot."
    #voice "voice/12-scene_12-59.ogg" #Raine (VA Name)
    mc "Ah, sorry. I'm more tired than I thought."
    #voice "voice/12-scene_12-60.ogg" #Leona (VA Name)
    le "Maybe some food will help! Come on, eat with me."
    #voice "voice/12-scene_12-61.ogg" #Raine (VA Name)
    mc "Can't say no to that. Thanks, Leona!"
    na "The food is delicious. As always, Leona's got an amazing sense for cooking."
    na "We enjoy a wonderful night in, staying close and enjoying each other's company."
    #voice "voice/12-scene_12-62.ogg" #Leona (VA Name)
    le "Hey, Raine..."
    #voice "voice/12-scene_12-63.ogg" #Raine (VA Name)
    mc "Yeah?"
    #voice "voice/12-scene_12-64.ogg" #Leona (VA Name)
    le "Tell me about Lumin."
    #voice "voice/12-scene_12-65.ogg" #Raine (VA Name)
    mc "Why?"
    #voice "voice/12-scene_12-66.ogg" #Leona (VA Name)
    le "I just want to know what your home is like."
    #voice "voice/12-scene_12-67.ogg" #Raine (VA Name)
    mc "Well, it's mostly urban. The whole planet is one big city, save for a few aforementioned places."
    #voice "voice/12-scene_12-68.ogg" #Raine (VA Name)
    mc "The entire city is this one big hub of information, electricity, and people."
    #voice "voice/12-scene_12-69.ogg" #Raine (VA Name)
    mc "For a while, it was home."
    #voice "voice/12-scene_12-70.ogg" #Raine (VA Name)
    mc "I managed to make a living as an engineer and for a while, it was fun."
    #voice "voice/12-scene_12-71.ogg" #Leona (VA Name)
    le "For a while?"
    #voice "voice/12-scene_12-72.ogg" #Raine (VA Name)
    mc "Yeah."
    #voice "voice/12-scene_12-73.ogg" #Raine (VA Name)
    mc "Something in me just got... sad, I guess. I wanted to see what was out there."
    #voice "voice/12-scene_12-74.ogg" #Raine (VA Name)
    mc "I kept thinking to myself, 'Is this it for me? Could I be doing more with my life?'"
    #voice "voice/12-scene_12-75.ogg" #Raine (VA Name)
    mc "So I decided I'd get out there and explore. I built a ship and took off."
    #voice "voice/12-scene_12-76.ogg" #Leona (VA Name)
    le "And that's how you ended up here?"
    #voice "voice/12-scene_12-77.ogg" #Raine (VA Name)
    mc "Eventually, yeah."
    #voice "voice/12-scene_12-78.ogg" #Leona (VA Name)
    le "I think I understand. You really wanted to explore, like me."
    #voice "voice/12-scene_12-79.ogg" #Raine (VA Name)
    mc "Yeah."
    #voice "voice/12-scene_12-80.ogg" #Leona (VA Name)
    le "That's so cool! I don't know if I would have been able to do all of that on my own."
    #voice "voice/12-scene_12-81.ogg" #Leona (VA Name)
    le "You're really brave."
    #voice "voice/12-scene_12-82.ogg" #Raine (VA Name)
    mc "Heh, thanks."
    #voice "voice/12-scene_12-83.ogg" #Raine (VA Name)
    mc "It was pretty scary, actually."
    #voice "voice/12-scene_12-84.ogg" #Raine (VA Name)
    mc "I just... up and left without much fanfare. Heck, my apartment is still there with a few of my things."
    #voice "voice/12-scene_12-85.ogg" #Raine (VA Name)
    mc "It was kind of impulsive."
    #voice "voice/12-scene_12-86.ogg" #Leona (VA Name)
    le "I'll say!"
    #voice "voice/12-scene_12-87.ogg" #Raine (VA Name)
    mc "But, you know..."
    na "I reach out and hold her hand."
    #voice "voice/12-scene_12-88.ogg" #Raine (VA Name)
    mc "I'd do it all over again if it meant I could meet you every time."
    #voice "voice/12-scene_12-89.ogg" #Leona (VA Name)
    le "Raine, I... wow."
    na "Her cheeks are so red they're practically glowing."
    #voice "voice/12-scene_12-90.ogg" #Leona (VA Name)
    le "That's um..."
    #voice "voice/12-scene_12-91.ogg" #Leona (VA Name)
    le "Um..."
    #voice "voice/12-scene_12-92.ogg" #Leona (VA Name)
    le "..."
    stop env fadeout 2.0
    #show kiss_CG1
    #pause (3)
    na "The kiss lingers in the air, fading out all of the sounds of the city outside."
    na "The two of us say nothing for a while as Leona holds me close to her."
    #pause (3)
    #voice "voice/12-scene_12-93.ogg" #Leona (VA Name)
    le "Raine... I like you. I {i}really{/i} like you. Like, {i}like{/i} like you."
    #voice "voice/12-scene_12-94.ogg" #Leona (VA Name)
    le "I just... don't want you to go, Raine!"
    #voice "voice/12-scene_12-95.ogg" #Leona (VA Name)
    le "I don't want to be alone."
    #show kiss_CG2
    play music "music/they cry.ogg" fadein 2.0
    play sound3 "amb/leonas house.ogg" fadein 2.0
    na "Her #voice breaks as she starts crying."
    na "I'm stunned. All I can do is hug her tighter in response."
    na "There's so much I want to say."
    na "But I can't."
    na "Leona's been there for me, ever since I fell out of the sky."
    na "She's given me a home, showed me the beautiful planet, and even given me a reason to stay in one place for longer than a few days."
    na "But I still feel that yearning for more adventure."
    na "I know that I can't stay here."
    na "I know that I'll always want to travel amongst the stars."
    na "But still..."
    na "But still."
    #voice "voice/12-scene_12-96.ogg" #Raine (VA Name)
    mc "Leona."
    #show kiss_CG3
    na "I love you too."
    na "My body is screaming at me to say it."
    na "But I can't do it."
    #voice "voice/12-scene_12-97.ogg" #Raine (VA Name)
    mc "Forgive me... but I have to leave Fireside."
    #voice "voice/12-scene_12-98.ogg" #Raine (VA Name)
    mc "The wormhole is going to close in a few days."
    #voice "voice/12-scene_12-99.ogg" #Raine (VA Name)
    mc "I have to go now, or I'll never make it home."
    #end CG
    #voice "voice/12-scene_12-100.ogg" #Raine (VA Name)
    mc "You know it's a one-way trip."
    #voice "voice/12-scene_12-101.ogg" #Raine (VA Name)
    mc "If I — or both — of us go through there, we might not come back here for a while."
    #voice "voice/12-scene_12-102.ogg" #Raine (VA Name)
    mc "I hate to admit it, but you were right. We might not come back here ever again."
    #voice "voice/12-scene_12-103.ogg" #Raine (VA Name)
    mc "Do you think you can really leave your people here, just like that?"
    #voice "voice/12-scene_12-104.ogg" #Leona (VA Name)
    le "Didn't you?"
    #voice "voice/12-scene_12-105.ogg" #Raine (VA Name)
    mc "..."
    #voice "voice/12-scene_12-106.ogg" #Leona (VA Name)
    le "You don't think I can make those kinds of sacrifices, too? That I should just stay here and forget all about you?"
    #voice "voice/12-scene_12-107.ogg" #Leona (VA Name)
    le "No. I can't ever forget about you, Raine!"
    #voice "voice/12-scene_12-108.ogg" #Leona (VA Name)
    le "If you think you have to do this all by yourself, that's fine."
    #voice "voice/12-scene_12-109.ogg" #Leona (VA Name)
    le "But it's not fair to me."
    na "Leona continues to cry, I can no longer hold back my tears either."
    na "I know."
    #voice "voice/12-scene_12-110.ogg" #Raine (VA Name)
    mc "I need some fresh air."
    na "I run outside towards the ship."
    #show outdoors_night
    stop sound3 fadeout 2.0
    play env "amb/city night.ogg" fadein 2.0
    na "The night air is cool and crisp, like a slap to the face."
    na "I have to do this now, or I'll miss my chance."
    na "If I leave the way I am now, I can do it with no regrets."
    na "Finally, the ship comes into view."
    na "God, I'm such a coward."
    na "I made up my mind. I told myself that I'd take her with me. But I'm not really good with commitment, am I?"
    na "This is it. It's time to leave Fireside behind for good."
    #voice "voice/12-scene_12-111.ogg" #Raine (VA Name)
    mc "Open up, Juneau!"
    #voice "voice/12-scene_12-112.ogg" #Raine (VA Name)
    mc "We're heading out."
    na "The ship's bay doors open, and I hop inside."
    #voice "voice/12-scene_12-113.ogg" #Juneau (VA Name)
    ju "It's so late, though... can't it wait until morning?"
    #show inside_ship
    #voice "voice/12-scene_12-114.ogg" #Raine (VA Name)
    mc "No, we should leave early before the wormhole closes."
    #voice "voice/12-scene_12-115.ogg" #Juneau (VA Name)
    ju "And your girlfriend? Is she coming, too?"
    #voice "voice/12-scene_12-116.ogg" #Raine (VA Name)
    mc "I..."
    #voice "voice/12-scene_12-117.ogg" #Juneau (VA Name)
    ju "I saw the way you looked at her earlier. You're in love with her, right?"
    #voice "voice/12-scene_12-118.ogg" #Raine (VA Name)
    mc "What makes you say that?"
    #voice "voice/12-scene_12-119.ogg" #Juneau (VA Name)
    ju "The Raine I know doesn't smile like that at just anyone."
    #voice "voice/12-scene_12-120.ogg" #Juneau (VA Name)
    ju "Not even me."
    #voice "voice/12-scene_12-121.ogg" #Juneau (VA Name)
    ju "And frankly, I'm insulted."
    #voice "voice/12-scene_12-122.ogg" #Raine (VA Name)
    mc "About... what, exactly?"
    #voice "voice/12-scene_12-123.ogg" #Juneau (VA Name)
    ju "That you fall head over heels for an alien, yet you still insist on putting your boots up on my console every time, despite all we've been through."
    #voice "voice/12-scene_12-124.ogg" #Juneau (VA Name)
    ju "Honestly, you humans are so weird about love. It's like you're hard-wired to do the most ridiculous stuff when your hormones go off."
    #voice "voice/12-scene_12-125.ogg" #Juneau (VA Name)
    ju "You do a lot of stupid shit, you know. I need someone else to check you, it's obvious that I can't do the job alone anymore."
    #voice "voice/12-scene_12-126.ogg" #Raine (VA Name)
    mc "I'm not... stupid."
    #voice "voice/12-scene_12-127.ogg" #Juneau (VA Name)
    ju "Bullshit."
    #pause (5)
    #voice "voice/12-scene_12-128.ogg" #Raine (VA Name)
    mc "...Shit."
    na "I've never seen Juneau get so real with me."
    na "I needed that reality check, huh?"
    na "She's right, I do love Leona, and I can't just run away whenver I'm scared."
    na "For an adventurer, I'm really bad at handling the unexpected."
    #voice "voice/12-scene_12-129.ogg" #Raine (VA Name)
    mc "Juneau... thank you."
    #voice "voice/12-scene_12-130.ogg" #Juneau (VA Name)
    ju "That's what I'm here for. Now go, before you make things worse."

    stop env fadeout 2.0
    play sound3 "amb/leonas house.ogg" fadein 2.0

    #show leona_house
    na "I run back to a still-sobbing Leona, who's curled up in her piles of cushions in a vain attempt to sleep."
    na "She instantly embraces me."
    #voice "voice/12-scene_12-131.ogg" #Leona (VA Name)
    le "Raine!"
    #voice "voice/12-scene_12-132.ogg" #Raine (VA Name)
    mc "I'm sorry. I was being selfish."
    #voice "voice/12-scene_12-133.ogg" #Raine (VA Name)
    mc "I was so focused on getting home I didn't stop to think what would happen if I..."
    #voice "voice/12-scene_12-134.ogg" #Raine (VA Name)
    mc "If I fell in love with you."
    #voice "voice/12-scene_12-135.ogg" #Leona (VA Name)
    le "Raine..."
    #voice "voice/12-scene_12-136.ogg" #Raine (VA Name)
    mc "But now I know what I should do. I always knew. I'm just really, really dense."
    #voice "voice/12-scene_12-137.ogg" #Raine (VA Name)
    mc "I'm taking you with me, Leona, because we need each other in this beautiful universe."
    #voice "voice/12-scene_12-138.ogg" #Leona (VA Name)
    le "You really scared me, Raine. This entire time, I was afraid that you'd just up and leave me."
    #voice "voice/12-scene_12-139.ogg" #Leona (VA Name)
    le "You almost did, too!"
    #voice "voice/12-scene_12-140.ogg" #Leona (VA Name)
    le "But... I'll go with you. Wherever you want to go."
    #voice "voice/12-scene_12-141.ogg" #Leona (VA Name)
    le "And that's because I know that no matter what, we'll have fun."
    #voice "voice/12-scene_12-142.ogg" #Raine (VA Name)
    mc "I'm really sorry. I know that doesn't really mean much now. I mean it, though."
    #voice "voice/12-scene_12-143.ogg" #Leona (VA Name)
    le "I'll forgive you, Raine, on one condition."
    #voice "voice/12-scene_12-144.ogg" #Leona (VA Name)
    le "Don't you ever, ever do that to me {b}ever{/b} again."
    #voice "voice/12-scene_12-145.ogg" #Raine (VA Name)
    mc "Y-Yeah. You're absolutely right."
    #show kiss_CG4
    na "We kiss again, but this time it's different."
    na "We're not pulling away from each other, we're getting closer and closer."
    na "I'm falling into Leona, and all the heat and pressure that comes with it feels so relieving."
    na "And I know she's feeling the same way."
    stop music fadeout 2.0
    #voice "voice/12-scene_12-146.ogg" #Raine (VA Name)
    mc "I love you, Leona."
    #voice "voice/12-scene_12-147.ogg" #Leona (VA Name)
    le "I love you too."
    na "We stay in each other's arms for a long, long time after that, until we both fall asleep."

    #timeskip

    na "The next day, I help Leona pack her belongings and get the ship ready for travel."
    na "The hardware I installed makes things a bit cramped, but I think it'll work out."
    na "The first thing we're doing is upgrading this ship to be more roomy, for sure."
    #voice "voice/12-scene_12-148.ogg" #Juneau (VA Name)
    ju "You sure have a lot of stuff, Leona."
    #voice "voice/12-scene_12-149.ogg" #Leona (VA Name)
    le "Can't leave home without all of these!"
    na "She motions to her bedding, her outfits, and a variety of other knick knacks she's collected."
    #voice "voice/12-scene_12-150.ogg" #Juneau (VA Name)
    ju "I sure hope we can get into orbit with all of this."
    #voice "voice/12-scene_12-151.ogg" #Raine (VA Name)
    mc "Oh hush, it's fine. You know that the new engine is definitely powerful enough for that."
    #voice "voice/12-scene_12-152.ogg" #Raine (VA Name)
    mc "Besides. Think of the upgrades we can make to this baby once we hit Danhamye or any of the other colonies."
    #voice "voice/12-scene_12-153.ogg" #Raine (VA Name)
    mc "The extra I.S.O.C chips are old, but collectors will salivate for anything that ancient."
    #voice "voice/12-scene_12-154.ogg" #Raine (VA Name)
    mc "Something about 'vintage firmware' that they can use will sell well on pretty much any market."
    #voice "voice/12-scene_12-155.ogg" #Juneau (VA Name)
    ju "I demand a new console, for starters."
    #voice "voice/12-scene_12-156.ogg" #Raine (VA Name)
    mc "Deal."
    na "The ship looks more and more like Leona's house than it does mine."
    na "Pretty much all of my belongings were destroyed during re-entry, so all I have left is the stuff currently on my person."
    na "Still, Leona's house had its comforts, and we thankfully were able to fit the things that mattered, plus a few extras."
    na "She's dying to show me more of her cooking sometime, so she's brought some of her cookware."
    na "I didn't have the heart to tell her that there's no stove on board, just the synthesizer."
    na "It wouldn't be that hard to install one later, though."
    na "Leona: the GOAT homemaker."
    play music "music/leaving fireside.ogg" fadein 2.0
    #voice "voice/12-scene_12-157.ogg" #Raine (VA Name)
    mc "Well, I think that's everything."
    #voice "voice/12-scene_12-158.ogg" #Leona (VA Name)
    le "Got anything else you want to grab before we say goodbye?"
    #voice "voice/12-scene_12-159.ogg" #Raine (VA Name)
    mc "You packed extra o'eke'ke, right?"
    #voice "voice/12-scene_12-160.ogg" #Leona (VA Name)
    le "Yup!"
    #voice "voice/12-scene_12-161.ogg" #Raine (VA Name)
    mc "Then we're fine."
    #voice "voice/12-scene_12-162.ogg" #Leona (VA Name)
    le "Yay!"
    #voice "voice/12-scene_12-163.ogg" #Raine (VA Name)
    mc "Are {b}you{/b} ready, Leona? It's going to be a long time before we see Fireside again."
    #voice "voice/12-scene_12-164.ogg" #Leona (VA Name)
    le "I wouldn't have packed all of my life into your ship if I wasn't ready, Raine."
    na "She sits down and straps herself in."
    #voice "voice/12-scene_12-165.ogg" #Leona (VA Name)
    le "Let's go!"
    #voice "voice/12-scene_12-166.ogg" #Raine (VA Name)
    mc "All right then!"
    #voice "voice/12-scene_12-167.ogg" #Raine (VA Name)
    mc "Juneau, you know what to do."
    #voice "voice/12-scene_12-168.ogg" #Juneau (VA Name)
    ju "Roger that. Starting up the engines."
    #engine startup
    na "I turn to Leona as I take the ship up."
    na "She gives me her trademark grin as she observes the scenery outside."
    na "Fireside quietly falls away as we reach orbit, the exosphere, and finally, open space."
    #voice "voice/12-scene_12-169.ogg" #Leona (VA Name)
    le "Is it going to be okay, the wormhole?"
    #voice "voice/12-scene_12-170.ogg" #Raine (VA Name)
    mc "I'm ready this time. I know where it is, and where it'll spit us out."
    #voice "voice/12-scene_12-171.ogg" #Raine (VA Name)
    mc "Juneau, you have the coordinates, right?"
    #voice "voice/12-scene_12-172.ogg" #Juneau (VA Name)
    ju "Right here."
    na "The wormhole's location pops up on a nearby monitor. Not too far away."
    #voice "voice/12-scene_12-173.ogg" #Juneau (VA Name)
    ju "It's definitely going to close soon. Probably within the next 24 hours."
    #voice "voice/12-scene_12-174.ogg" #Juneau (VA Name)
    ju "Either you go now, or never again."
    #voice "voice/12-scene_12-175.ogg" #Juneau (VA Name)
    ju "You sure you want to go?"
    na "I look to Leona."
    na "She nods, determined."
    #voice "voice/12-scene_12-176.ogg" #Raine (VA Name)
    mc "We're sure. Let's go."
    #voice "voice/12-scene_12-177.ogg" #Juneau (VA Name)
    ju "All right, then. Setting engines to maximum!"
    #engine SFX
    #voice "voice/12-scene_12-178.ogg" #Raine (VA Name)
    mc "The engines accelerate us closer and closer to the wormhole's event horizon."
    #voice "voice/12-scene_12-179.ogg" #Juneau (VA Name)
    ju "600 kilometers until breach."
    #voice "voice/12-scene_12-180.ogg" #Raine (VA Name)
    mc "Well, here we go, Leona."
    #voice "voice/12-scene_12-181.ogg" #Raine (VA Name)
    mc "It'll be quite a trip, don't you think? There's a lot out here."
    #voice "voice/12-scene_12-182.ogg" #Leona (VA Name)
    le "Yeah. But I'm excited to see it all with you."
    na "She leans in for a kiss."
    #voice "voice/12-scene_12-183.ogg" #Raine (VA Name)
    mc "Thanks, Leona. For everything."
    #voice "voice/12-scene_12-184.ogg" #Juneau (VA Name)
    ju "300 kilometers."
    #voice "voice/12-scene_12-185.ogg" #Raine (VA Name)
    mc "You're really something out of this world, you know?"
    #voice "voice/12-scene_12-186.ogg" #Leona (VA Name)
    le "I'd say the same to you, Raine."
    na "Juneau rolls her eyes at our cliche."
    #voice "voice/12-scene_12-187.ogg" #Juneau (VA Name)
    ju "Disgusting."
    na "We laugh as the ship gets closer and closer to our destination."
    #voice "voice/12-scene_12-188.ogg" #Juneau (VA Name)
    ju "Fifty kilometers."
    na "This is it. I'm finally starting on my great adventure..."
    na "No."
    na "That adventure ended when I met Leona."
    #voice "voice/12-scene_12-189.ogg" #Juneau (VA Name)
    ju "Ten."
    na "When I fell in love with her."
    #voice "voice/12-scene_12-190.ogg" #Juneau (VA Name)
    ju "Five."
    na "And now..."
    #wormhole SFX
    #voice "voice/12-scene_12-191.ogg" #Juneau (VA Name)
    ju "Entering event horizon. We're in the wormhole!"
    #voice "voice/12-scene_12-192.ogg" #Leona (VA Name)
    le "It's so pretty!"
    na "I'm starting another great adventure with Leona, one that's going to be ten times the adventure the last one was."
    na "One that I can enjoy with her to the fullest."
    #voice "voice/12-scene_12-193.ogg" #Raine (VA Name)
    mc "Hang on to your belt, the trip is a little bumpy."
    #wormhole intensifies
    na "The intensity of the wormhole momentarily spikes."
    #voice "voice/12-scene_12-194.ogg" #Juneau (VA Name)
    ju "Gravity is getting stronger here. Watch out!"
    #voice "voice/12-scene_12-195.ogg" #Raine (VA Name)
    mc "Got it!"
    #switch SFX
    na "I make some on-the-fly adjustments as the ship careens into oblivion."
    na "Leona's fascinated by it all, enraptured by the lights and colors around her."
    na "God, she's cute."
    na "Soon, the gravity settles down, and Juneau senses that we're near the end."
    #voice "voice/12-scene_12-196.ogg" #Juneau (VA Name)
    ju "Getting ready to decelerate. Don't want to collide with {b}another{/b} asteroid as soon as we leave."
    #voice "voice/12-scene_12-197.ogg" #Raine (VA Name)
    mc "Good call."
    #voice "voice/12-scene_12-198.ogg" #Raine (VA Name)
    mc "Almost there. And...."
    na "The ship finally exits the wormhole."
    #voice "voice/12-scene_12-199.ogg" #Raine (VA Name)
    mc "We're out!"
    #voice "voice/12-scene_12-200.ogg" #Juneau (VA Name)
    ju "Decelerating."
    na "The ship slows down until we get to a more reasonable speed."
    #voice "voice/12-scene_12-201.ogg" #Juneau (VA Name)
    ju "Exit confirmed. We're about a lightyear from the nearest planet, according to our maps."
    na "Now back in familiar territory, I finally sigh in relief."
    #voice "voice/12-scene_12-202.ogg" #Raine (VA Name)
    mc "Well Leona, we're here!"
    #voice "voice/12-scene_12-203.ogg" #Leona (VA Name)
    le "That was awesome! Where should we go first?"
    #voice "voice/12-scene_12-204.ogg" #Raine (VA Name)
    mc "I think we should try this place out."
    #voice "voice/12-scene_12-205.ogg" #Raine (VA Name)
    mc "I scroll my map to one place I've been thinking about for a while."
    #voice "voice/12-scene_12-206.ogg" #Leona (VA Name)
    le "What's that planet?"
    #voice "voice/12-scene_12-207.ogg" #Raine (VA Name)
    mc "Lumin."
    #voice "voice/12-scene_12-208.ogg" #Raine (VA Name)
    mc "Home."
    #voice "voice/12-scene_12-209.ogg" #Raine (VA Name)
    mc "You've shown me your home, so how about I show you mine?"
    #voice "voice/12-scene_12-210.ogg" #Leona (VA Name)
    le "I'd love that."
    #voice "voice/12-scene_12-211.ogg" #Raine (VA Name)
    mc "Juneau, take us home."
    #voice "voice/12-scene_12-212.ogg" #Juneau (VA Name)
    ju "Sounds good to me."
    #voice "voice/12-scene_12-213.ogg" #Raine (VA Name)
    mc "I'm going to be honest, I wasn't entirely sure we'd make the trip back."
    #voice "voice/12-scene_12-214.ogg" #Leona (VA Name)
    le "I never doubted you. I'm glad you got us here safe and sound."
    #voice "voice/12-scene_12-215.ogg" #Raine (VA Name)
    mc "Yeah, me too,"
    #voice "voice/12-scene_12-216.ogg" #Leona (VA Name)
    le "Well, I'm ready to see your home planet."
    #voice "voice/12-scene_12-217.ogg" #Leona (VA Name)
    le "Maybe after we stay there for a while, you can show me more planets!"
    #voice "voice/12-scene_12-218.ogg" #Raine (VA Name)
    mc "Of course. I'd love to take you."
    na "We kiss, Juneau tells us to get a room, and we spend the rest of the trip back planning out where we want to go next."
    na "There's so much I want to show her, and I'm sure she's excited to see it all."
    na "And I'm excited too. Scared, but excited."
    na "We'll get you back home one day, Leona. I promise."
    #fade to black
    stop music

return
