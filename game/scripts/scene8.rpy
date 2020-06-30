label scene_8:

    #ART Leona's House
    #Color swap for UI????
    play env "amb/Leonas House.ogg" fadein 2.0
    scene house with Dissolve(2.0):
        anchor (0.5, 0.5) align (0.5, 0.5) zoom 0.75

    voice "voice/8-default-1.ogg" #Leona (Dot)
    le cryingtalk "I am so-!"

    voice "voice/8-default-2.ogg" #Leona (Dot)
    le frustratedshout "STUPID!" with hpunch

    play music "music/Consequence.ogg" fadein 2.0

    #VFX POMF

    na "Why did I do that?"
    na "All this time I knew she wanted to leave!"
    na "I wanted to help! I was helping her!"
    na "How could I do that to her? She trusted me!"

    voice "voice/8-default-3.ogg" #Leona (Dot)
    le "Stupid!" with hpunch

    na "If I had just told her the truth. If only I weren't so damn afraid!"
    na "Maybe she would have the ship fixed by now."
    na "Maybe she would have stopped the explosion too."
    na "She can do anything!"
    na "I'm just some stupid little kid living on a stupid little rock drifting through space."
    na "All I do is get in the way and cry about how much of a failure I am."
    na "This isn't what family is supposed to do."
    na "You're supposed to look out for each other, you're supposed to support them in whatever they choose."
    na "But, then, she's not family."
    na "She's not even one of us."

    voice "voice/8-default-4.ogg" #Leona (Dot)
    le crying "So why does it hurt so much?"
    play sound "voice/cryingL.ogg"
    na "Nobody said it would be like this."
    na "You're supposed to find someone really great."
    na "And if they felt the same way, you'd want to spend the rest of your lives with them."
    na "We'd paint the walls and tell each other stories."
    na "And be a family."
    na "Nobody ever told me they'd be an alien."
    na "Nobody ever told me she'd rather fly back to space than to be with me."
    na "Am I even that important to her?"
    na "Does... did she even like me? At all?"
    na "Was I just getting ahead of myself?"
    na "...What does it matter now?"
    na "I already ruined it."
    voice "voice/8-default-5.ogg" #Leona (Dot)
    le "Come on, Leona, pick yourself up by the horns."
    na "There are more important things to do right now."
    na "{i}I just blew up a mountain.{/i} I need to be out there running damage control, not laying here feeling sorry for myself."
    na "Get up!"
    na "You made a mistake, so clean it the heck up!"
    na "Whether Raine likes me or not doesn't matter anymore! People could be hurt."
    na "And once the situation is contained..."
    na "I'll have to make the disaster report to the city council."
    na "If I hadn't gone out to the caves with Raine, we all wouldn't be in this mess."
    na "That's on me. 100%%"

    voice "voice/8-default-6.ogg" #Leona (Dot)
    le concerned "...I'm gonna lose my job, aren't I?"

    voice "voice/8-default-7.ogg" #Leona (Dot)
    le tired "...Idiot. That isn't important at all right now."

    na "Stop moping around!"
    stop music fadeout 4.0


    voice "voice/8-default-8.ogg" #Leona (Dot)
    le concerned "{b}Get.{/b}"

    voice "voice/8-default-9.ogg" #Leona (Dot)
    le frustratedshout "{b}Up!{/b}" with hpunch
    stop env fadeout 2.0


    #VFX Journal Backups Loaded

    jump scene_9
