###############################
#
# INCLUDE THIS FILE FOR USEFUL & AUTOMATIC DEFINITIONS
#
###############################

init:
    transform blinkeyes(eyes1, eyes2):
        eyes1
        choice:
            3.5
        choice:
            2.5
        choice:
            1.5
        # This randomizes the time between blinking.
        eyes2
        .15
        repeat

    transform flapmouth(mouth1, mouth2):
        mouth1
        .2
        mouth2
        .2
        repeat

    transform flip:
        xzoom -1.0

    transform centerleft:
        xpos 0.25
        ypos 0.0
        xanchor 0.5
        yalign 1.0

    transform centerright:
        xpos 0.75
        ypos 0.0
        xanchor 0.5
        yalign 1.0

    transform height:
        ypos 1.05


init -100 python:
    import os
    import sys
    import logging
    import pygame.scrap

    # absolute path to the game directory, which is formatted according
    # to the conventions of the local OS
    gamedir = os.path.normpath(config.gamedir)

    # required to make the above work with with RenPy:
    config.reject_backslash = False

    # setting the window on center
    # useful if game is launched in the window mode
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    sys.setdefaultencoding('utf-8')

    # Game may bug out on saving, in such case, comment should be removed
    # config.use_cpickle = False

    # enable logging via the 'logging' module
    try:
        logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(name)-15s %(message)s')
        devlog = logging.getLogger(" ".join([config.name, config.version]))
        devlogfile = logging.FileHandler(os.path.join(gamedir, "devlog.txt"))
        devlogfile.setLevel(logging.DEBUG)
        devlog.addHandler(devlogfile)
        devlog.critical("\n--- launch game ---")
        fm = logging.Formatter('%(levelname)-8s %(name)-15s %(message)s')
        devlogfile.setFormatter(fm)
        del fm
        devlog.info("Game directory: %s" % gamedir)
    except:
        class DevlogStub:
            def debug(self, msg, *agrs, **kwargs):
                print str
            def info(self, msg, *agrs, **kwargs):
                print str
            def warning(self, msg, *agrs, **kwargs):
                print str
            def error(self, msg, *agrs, **kwargs):
                print str
            def critical(self, msg, *agrs, **kwargs):
                print str
        devlog = DevlogStub()

    def pretty(d, indent=0):
        if isinstance(d, list):
            for value in d:
                pretty(value, indent)
        elif isinstance(d, dict):
            for key, value in d.items():
                devlog.info('\t' * indent + str(key))
                pretty(value, indent+1)
        else:
            devlog.info('\t' * (indent) + str(d))


init -50 python:
    import os
    import itertools

    eyesdef = ('e', 'ec', 'ed')
    mouthdef = ('m', 'mc', 'md', 'mdo')
    eyesauto = ('ed', 'ec')
    mouthauto = ('md', )

    batchmapemotes = False
    basedict = {}
    originalsizedict = {}
    sizedict = {}
    sidelist = []
    offsetdict = {}
    pathdict = {}
    mapemotedict = {}
    spritedict = {}
    charlist = []
    posedict = {}
    haseyeslist = []
    hasmouthlist = []
    def DefineImages(imageFolder, composite=False, prepend=None, autoEmotes=False, overrideCharname=None, overrideLayerOrder=None, offsets=None, zooms=None, sides=None):
        if composite:
            imglist = []
        if sides != None and type(sides) == list:
            for s in sides:
                if not s in sidelist:
                    sidelist.append(s)

        excludeFirstXFolders = len(imageFolder.split('/'))
        if prepend is None:
            prepend = []
        if type(prepend) is unicode:
            prepend = [prepend,]

        for path in renpy.list_files():
            if path.startswith(imageFolder + "/"):
                path_list = path.split("/")
                if ' ' in path_list[-1]:
                    path_list = path_list[0:-1] + path_list[-1].split()
                path_list[-1] = os.path.splitext(path_list[-1])[0]
                path_list = tuple(prepend + path_list[excludeFirstXFolders:])
                lowerpath_list = tuple([ x.lower() for x in path_list ])

                if composite:
                    renpy.image(('_'.join(path_list),), path)
                    if lowerpath_list != path_list:
                        renpy.image(('_'.join(lowerpath_list),), path)
                else:
                    renpy.image(path_list, path)
                    if lowerpath_list != path_list:
                        renpy.image(lowerpath_list, path)

                if composite:
                    # keep ordered list of all images, and also the corresponding paths
                    imglist.append(path_list)
                    pathdict[path_list] = path

        if composite:
            baselist = []
            for path_list in imglist:
                # get the list of sprite pose folders, which are detected if they contain a base e.g. '/base.png'
                basepath = path_list[:-1]
                if basepath in baselist:
                    continue
                if u'base' in path_list[-1]:
                    has_eyes = False
                    if basepath + (u'e', u'default') in pathdict:
                        has_eyes = True
                    if basepath + (u'ec', u'default') in pathdict:
                        has_eyes = True

                    has_mouth = False
                    if basepath + (u'm', u'default') in pathdict:
                        has_mouth = True
                    if basepath + (u'mc', u'default') in pathdict:
                        has_mouth = True

                    if has_eyes:
                        haseyeslist.append(basepath)
                    if has_mouth:
                        hasmouthlist.append(basepath)
                    baselist.append(basepath)

            for basepath in baselist:
                charname = overrideCharname
                if charname is None:
                    charname = basepath[0]
                if not charname in charlist:
                    charlist.append(charname)
                if not charname in posedict:
                    posedict[charname] = []
                posedict[charname].append(basepath)
                #devlog.info('==== ' + charname)

                # build the lists
                basedict[basepath] = {}
                basedict[basepath]['bases'] = []
                basedict[basepath]['parts'] = []
                basedict[basepath]['emotes'] = []
                basedict[basepath]['list'] = []
                basedict[basepath]['eyes'] = []
                basedict[basepath]['mouth'] = []
                basedict[basepath]['extraparts'] = {}
                basedict[basepath]['optionals'] = []
                baselen = len(basepath)
                for path_list in imglist:
                    if path_list[:baselen] == basepath:
                        if len(path_list) - baselen == 1:
                            basedict[basepath]['bases'].append(path_list[-1])
                            img = Image(pathdict[path_list])
                            imgsize = renpy.image_size(img)
                            if imgsize[1] > config.screen_height:
                                sizedict[basepath] = float(config.screen_height) / imgsize[1]
                            else:
                                sizedict[basepath] = 1.0
                            originalsizedict[basepath] = sizedict[basepath]
                            if zooms != None:
                                if type(zooms) == float:
                                    sizedict[basepath] *= zooms
                                elif type(zooms) == dict:
                                    if basepath in zooms and type(zooms[basepath]) == float:
                                        sizedict[basepath] *= zooms[basepath]
                                    elif basepath[0] in zooms and type(zooms[basepath[0]]) == float:
                                        sizedict[basepath] *= zooms[basepath[0]]
                            if offsets != None:
                                if type(offsets) == tuple and len(offsets) == 2:
                                    offsetdict[basepath] = offsets
                                elif type(offsets) == dict:
                                    if basepath in offsets and type(offsets[basepath]) == tuple and len(offsets[basepath]) == 2:
                                        offsetdict[basepath] = offsets[basepath]
                                    elif basepath[0] in offsets and type(offsets[basepath[0]]) == tuple and len(offsets[basepath[0]]) == 2:
                                        offsetdict[basepath] = offsets[basepath[0]]
                            if not basepath in offsetdict:
                                offsetdict[basepath] = (0, 0)
                        if len(path_list) - baselen == 2:
                            part = path_list[-2]
                            emote = path_list[-1]
                            if part == 'optional':
                                basedict[basepath]['optionals'].append(emote)
                            elif not part in eyesdef + mouthdef:
                                default_path_list = path_list[:-1] + (u'default',)
                                if default_path_list in imglist:
                                    #devlog.info(path_list)
                                    if not part in basedict[basepath]['extraparts']:
                                        basedict[basepath]['extraparts'][part] = []
                                    basedict[basepath]['extraparts'][part].append(emote)
                                    if not emote in basedict[basepath]['emotes']:
                                        basedict[basepath]['emotes'].append(emote)
                            else:
                                if not part in basedict[basepath]['parts']:
                                    basedict[basepath]['parts'].append(part)
                                if not emote in basedict[basepath]['emotes']:
                                    basedict[basepath]['emotes'].append(emote)
                        basedict[basepath]['list'].append(path_list)

                if basepath in haseyeslist:
                    # special case for 'e' and 'ec': build blinking eyes into 'ed'
                    # fill in the missing files as "default"
                    if 'e' in basedict[basepath]['parts'] or 'ec' in basedict[basepath]['parts']:
                        for emote in basedict[basepath]['emotes']:
                            eyesopen = basepath + (u'e', emote)
                            eyesclose = basepath + (u'ec', emote)
                            if not eyesopen in basedict[basepath]['list']:
                                renpy.image(('_'.join(eyesopen), ), '_'.join(basepath+(u'e', u'default')))
                            else:
                                basedict[basepath]['eyes'].append('ed_' + emote)
                            if not basepath+(u'e', u'default') in basedict[basepath]['list']:
                                renpy.image(('_'.join(basepath+(u'e', u'default')), ), '_'.join(basepath+(u'ec', u'default')))
                            if not eyesclose in basedict[basepath]['list']:
                                renpy.image(('_'.join(eyesclose), ), '_'.join(basepath+(u'ec', u'default')))
                            else:
                                basedict[basepath]['eyes'].append('ec_' + emote)
                            if not basepath+(u'ec', u'default') in basedict[basepath]['list']:
                                renpy.image(('_'.join(basepath+(u'ec', u'default')), ), '_'.join(basepath+(u'e', u'default')))
                            renpy.image(('_'.join(basepath + (u'ed', emote)), ), blinkeyes('_'.join(eyesopen), '_'.join(eyesclose)))
                            basedict[basepath]['list'].append(basepath + (u'ed', emote))
                        basedict[basepath]['parts'].append('ed')

                if basepath in hasmouthlist:
                    # special case for 'm' and 'mc': build flapping mouth into 'md'
                    # fill in the missing files as "default"
                    if 'm' in basedict[basepath]['parts'] or 'mc' in basedict[basepath]['parts']:
                        for emote in basedict[basepath]['emotes']:
                            mouthopen = basepath + (u'm', emote)
                            mouthclose = basepath + (u'mc', emote)
                            if not mouthopen in basedict[basepath]['list']:
                                renpy.image(('_'.join(mouthopen), ), '_'.join(basepath+(u'm', u'default')))
                            else:
                                basedict[basepath]['mouth'].append('mdo_' + emote)
                            if not basepath+(u'm', u'default') in basedict[basepath]['list']:
                                renpy.image(('_'.join(basepath+(u'm', u'default')), ), '_'.join(basepath+(u'mc', u'default')))
                            if not mouthclose in basedict[basepath]['list']:
                                renpy.image(('_'.join(mouthclose), ), '_'.join(basepath+(u'mc', u'default')))
                            else:
                                basedict[basepath]['mouth'].append('md_' + emote)
                            if not basepath+(u'mc', u'default') in basedict[basepath]['list']:
                                renpy.image(('_'.join(basepath+(u'mc', u'default')), ), '_'.join(basepath+(u'm', u'default')))
                            renpy.image(('_'.join(basepath + (u'md', emote)), ), FlapMouth('_'.join(mouthclose), '_'.join(mouthopen), cha=charname))
                            renpy.image(('_'.join(basepath + (u'mdo', emote)), ), FlapMouth('_'.join(mouthopen), '_'.join(mouthclose), cha=charname))
                            basedict[basepath]['list'].append(basepath + (u'md', emote))
                            basedict[basepath]['list'].append(basepath + (u'mdo', emote))
                        basedict[basepath]['parts'].append('md')
                        basedict[basepath]['parts'].append('mdo')

                # go through the extras and fill in the missing files as "default"
                for ek in basedict[basepath]['extraparts']:
                    for emote in basedict[basepath]['emotes']:
                        ev = basepath + (ek, emote)
                        if not ev in basedict[basepath]['list']:
                            renpy.image(('_'.join(ev), ), '_'.join(basepath+(ek, u'default')))
                        basedict[basepath]['list'].append(basepath + (ek, emote))

                # determine the layer order
                layerorder = overrideLayerOrder
                if layerorder is None:
                    layerorder = ['base', 'eyes', 'mouth']
                    layerorder += sorted(basedict[basepath]['extraparts'].keys())
                    layerorder += basedict[basepath]['optionals']
                basedict[basepath]['layerorder'] = layerorder

                # build the livecomposites from bases and emotes
                layers = []
                for layer in layerorder:
                    if layer == 'base':
                        for base in basedict[basepath]['bases']:
                            layers.append(Attribute(layer, base, '_'.join(basepath+(base,)), base == 'base'))
                    elif layer == 'eyes' and basepath in haseyeslist:
                        for emote in basedict[basepath]['emotes']:
                            if not autoEmotes and emote != 'default':
                                continue
                            eyes = basepath+(u'ed', emote)
                            layers.append(Attribute(layer, emote, '_'.join(eyes), emote == 'default'))
                    elif layer == 'mouth' and basepath in hasmouthlist:
                        for emote in basedict[basepath]['emotes']:
                            if not autoEmotes and emote != 'default':
                                continue
                            mouth = basepath+(u'md', emote)
                            layers.append(Attribute(layer, emote, '_'.join(mouth), emote == 'default'))
                    elif layer in basedict[basepath]['optionals']:
                        layers.append(Attribute(layer, layer, '_'.join(basepath + (u'optional', layer))))
                    else:
                        for ex in sorted(basedict[basepath]['extraparts'].keys()):
                            if layer == ex:
                                for emote in basedict[basepath]['emotes']:
                                    if not autoEmotes and emote != 'default':
                                        continue
                                    layers.append(Attribute(layer, emote, '_'.join(basepath + (ex, emote)), emote == 'default'))

                layered = LayeredImage(layers, at=Transform(zoom=sizedict[basepath], pos=offsetdict[basepath]))
                spritedict[basepath] = layered
                renpy.image(basepath, layered)
                if basepath in sidelist:
                    renpy.image(('side',)+basepath, layered)
                elif basepath[0] in sidelist:
                    renpy.image(('side',)+basepath, layered)

            #pretty(basedict)
            DynamicSprites_VarUpdate()

    def SetBatchMapEmote(value):
        global batchmapemotes
        batchmapemotes = value

    def DoBatchMapEmote():
        for charpath in mapemotedict:
            layereddict = mapemotedict[charpath]['layereddict']
            layers = []
            for layer in layerorder:
                layers += layereddict[layer]
            layered = LayeredImage(layers, at=Transform(zoom=sizedict[charpath], pos=offsetdict[charpath]))
            spritedict[charpath] = layered
            renpy.image(charpath, layered)
            if charpath[0] in sidelist:
                renpy.image(('side',)+charpath, layered)

    def MapEmote(newname, oldname, addOptionals=True):
        newpath = tuple(newname.split())
        charname = newpath[0]
        charpath = tuple(newpath[0:len(newpath)-1])
        newemote = newpath[-1]

        oldpath = oldname.split()
        basepath = None
        for basepath2 in basedict:
            if basepath2 == tuple(oldpath[:len(basepath2)]):
                basepath = basepath2
                break
        if basepath is None:
            return None
        sizedict[charpath] = sizedict[basepath]
        offsetdict[charpath] = offsetdict[basepath]

        bases = None
        eyes = None
        mouth = None
        extraparts = {}
        for ek in basedict[basepath]['extraparts']:
            extraparts[ek] = None
        optionals = []
        i = len(basepath)
        while i < len(oldpath):
            if oldpath[i] in basedict[basepath]['bases']:
                bases = oldpath[i]
            elif oldpath[i].split('_')[0] in eyesdef:
                eyes = (oldpath[i],)
            elif oldpath[i].split('_')[0] in mouthdef:
                mouth = (oldpath[i],)
            elif oldpath[i].split('_')[0] in basedict[basepath]['extraparts']:
                extraparts[oldpath[i].split('_')[0]] = (oldpath[i],)
            elif oldpath[i] in basedict[basepath]['optionals']:
                optionals.append(oldpath[i])
            i += 1
        optionals = tuple(sorted(optionals))

        if bases == None:
            bases = ('base')
        if eyes == None and basepath in haseyeslist:
            eyes = ('ed', 'default')
        if mouth == None and basepath in hasmouthlist:
            mouth = ('md', 'default')
        for ek in extraparts.keys():
            if extraparts[ek] == None:
                extraparts[ek] = (ek, 'default')

        if not charpath in mapemotedict.keys():
            layereddict = {}
            emotesdict = {}
            for layer in layerorder:
                layereddict[layer] = []
            for p in spritedict:
                if p == charpath:
                    for a in spritedict[p].attributes:
                        layer = a.group
                        emote = a.attribute
                        layereddict[layer].append(a)
                        if not emotesdict.has_key(emote):
                            emotesdict[emote] = {}
                        emotesdict[emote][layer] = a
            mapemotedict[charpath] = {}
            mapemotedict[charpath]['layereddict'] = layereddict
            mapemotedict[charpath]['emotesdict'] = emotesdict

        layereddict = mapemotedict[charpath]['layereddict']
        emotesdict = mapemotedict[charpath]['emotesdict']

        change = False
        if emotesdict.has_key(newemote):
            emotelayers = emotesdict[newemote]
            for layer in layerorder:
                if emotelayers.has_key(layer):
                    a = emotelayers[layer]
                    if layer == 'base':
                        a.image = ImageReference(('_'.join(basepath+(bases,)),))
                    elif eyes != None and layer == 'eyes':
                        a.image = ImageReference(('_'.join(basepath+eyes),))
                    elif mouth != None and layer == 'mouth':
                        a.image = ImageReference(('_'.join(basepath+mouth),))
                    elif layer in extraparts.keys() and extraparts[layer] != None:
                        a.image = ImageReference(('_'.join(basepath+extraparts[layer]),))
                    elif layer in optionals:
                        a.image = ImageReference(('_'.join(basepath + (u'optional', layer)),))
                    else:
                        change = True
                        layereddict[layer].remove(a)
                        del emotelayers[layer]
                elif layer in optionals:
                    change = True
                    a = Attribute(layer, newemote, '_'.join(basepath + (u'optional', layer)))
                    layereddict[layer].append(a)
                    emotelayers[layer] = a
        else:
            change = True
            emotelayers = {}
            emotesdict[newemote] = emotelayers
            for layer in layerorder:
                a = None
                if layer == 'base':
                    a = Attribute(layer, newemote, '_'.join(basepath+(bases,)))
                elif eyes != None and layer == 'eyes':
                    a = Attribute(layer, newemote, '_'.join(basepath+eyes))
                elif mouth != None and layer == 'mouth':
                    a = Attribute(layer, newemote, '_'.join(basepath+mouth))
                elif layer in extraparts.keys() and extraparts[layer] != None:
                    a = Attribute(layer, newemote, '_'.join(basepath+extraparts[layer]))
                elif optionals != None and layer in optionals:
                    a = Attribute(layer, newemote, '_'.join(basepath + (u'optional', layer)))
                if not a is None:
                    layereddict[layer].append(a)
                    emotelayers[layer] = a

        if change and not batchmapemotes:
            layers = []
            for layer in layerorder:
                layers += layereddict[layer]
            layered = LayeredImage(layers, at=Transform(zoom=sizedict[charpath], pos=offsetdict[charpath]))
            spritedict[charpath] = layered
            renpy.image(charpath, layered)
            if charname in sidelist:
                renpy.image(('side',)+charpath, layered)

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None

    # This returns speaking if the character is speaking, and done if the
    # character is not.
    def while_speaking(name, speak_d, done_d, st, at):
        if (renpy.music.is_playing('voice') or not config.has_voice) and speaking == name:
            return speak_d, .1
        else:
            return done_d, None

    # Curried form of the above.
    curried_while_speaking = renpy.curry(while_speaking)

    # Displays speaking when the named character is speaking, and done otherwise.
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))

    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking

        if config.has_voice:
            speaking = name
        else:
            if event == "show":
                speaking = name
            elif event == "slow_done":
                speaking = None
            elif event == "end":
                speaking = None

    # Curried form of the same.
    speaker = renpy.curry(speaker_callback)

    def FlapMouth(mouth1, mouth2, cha=None):
        if cha is None and '_' in mouth1:
            cha = mouth1.split('_')[0]
        elif cha is None:
            cha = mouth1.split(' ')[0]
        mouth = flapmouth(mouth1, mouth2)
        return WhileSpeaking(cha, mouth, mouth1)

    def BlinkEyes(eyes1, eyes2):
        return blinkeyes(eyes1, eyes2)

    dynamicspritespreview_var_selectedchar = None
    dynamicspritespreview_var_selectedpose = None
    dynamicspritespreview_var_selectedlayers = {}
    dynamicspritespreview_text_selectedchar = None
    dynamicspritespreview_text_selectedpose = None
    dynamicspritespreview_text_selectedlayers = {}
    values = {}
    valuespath = {}
    valueszoom = 1.0
    mapemotecode = None
    mapemotecode_postscript = None
    def DynamicSprites_VarUpdate():
        global dynamicspritespreview_var_selectedchar, dynamicspritespreview_var_selectedpose, dynamicspritespreview_var_selectedlayers
        global dynamicspritespreview_text_selectedchar, dynamicspritespreview_text_selectedpose, dynamicspritespreview_text_selectedlayers
        global values, valuespath, valueszoom, mapemotecode, mapemotecode_postscript
        if len(charlist) == 0:
            dynamicspritespreview_text_selectedchar = "No character"
        else:
            if dynamicspritespreview_var_selectedchar is None:
                dynamicspritespreview_var_selectedchar = 0
            dynamicspritespreview_text_selectedchar = charlist[dynamicspritespreview_var_selectedchar]

        if len(charlist) == 0 or len(posedict) == 0:
            dynamicspritespreview_text_selectedpose = "No pose"
        else:
            if dynamicspritespreview_var_selectedpose is None:
                dynamicspritespreview_var_selectedpose = 0
            basepath = posedict[dynamicspritespreview_text_selectedchar][dynamicspritespreview_var_selectedpose]
            if len(basepath) < 2:
                dynamicspritespreview_text_selectedpose = "default pose"
            else:
                dynamicspritespreview_text_selectedpose = basepath[1]
            infodict = basedict[basepath]
            layerorder = infodict['layerorder']
            values = {}
            valuespath = {}
            values['base'] = list(infodict['bases'])
            if 'base' in values['base']:
                values['base'].remove('base')
            values['base'] = ['base'] + sorted(values['base'])
            valuespath['base'] = []
            for base in values['base']:
                valuespath['base'].append('_'.join(basepath+(base,)))
            valueszoom = originalsizedict[basepath]

            values['eyes'] = list(infodict['eyes'])
            if 'ed_default' in values['eyes']:
                values['eyes'].remove('ed_default')
            values['eyes'] = ['ed_default'] + sorted(values['eyes'])
            valuespath['eyes'] = []
            for eyes in values['eyes']:
                valuespath['eyes'].append('_'.join(basepath+(eyes,)))

            values['mouth'] = list(infodict['mouth'])
            if 'md_default' in values['mouth']:
                values['mouth'].remove('md_default')
            values['mouth'] = ['md_default'] + sorted(values['mouth'])
            valuespath['mouth'] = []
            for mouth in values['mouth']:
                valuespath['mouth'].append('_'.join(basepath+(mouth,)))

            for op in sorted(list(infodict['optionals'])):
                values[op] = ["No", "Yes"]
                valuespath[op] = [ None, '_'.join(basepath+('optional',op,)) ]

            for ex in infodict['extraparts']:
                values[ex] = list(infodict['extraparts'][ex])
                if 'default' in values[ex]:
                    values[ex].remove('default')
                values[ex] = ['default'] + sorted(values[ex])
                valuespath[ex] = []
                for e in values[ex]:
                    valuespath[ex].append('_'.join(basepath+(ex, e,)))

            dynamicspritespreview_text_selectedlayers = {}
            if len(basepath) < 2:
                mapemotecode = "MapEmote('{char} NEWEMOTE', '{char}".format(char=dynamicspritespreview_text_selectedchar)
            else:
                mapemotecode = "MapEmote('{char} NEWEMOTE', '{char} {pose}".format(char=dynamicspritespreview_text_selectedchar, pose=dynamicspritespreview_text_selectedpose)
            for layer in layerorder:
                if not layer in values:
                    continue
                if not layer in dynamicspritespreview_var_selectedlayers:
                    dynamicspritespreview_var_selectedlayers[layer] = 0
                dynamicspritespreview_text_selectedlayers[layer] = values[layer][dynamicspritespreview_var_selectedlayers[layer]]
                if layer == 'base':
                    mapemotecode += " " + dynamicspritespreview_text_selectedlayers[layer]
                elif layer == 'eyes':
                    mapemotecode += " " + dynamicspritespreview_text_selectedlayers[layer]
                elif layer == 'mouth':
                    mapemotecode += " " + dynamicspritespreview_text_selectedlayers[layer]
                elif layer in infodict['optionals']:
                    if dynamicspritespreview_text_selectedlayers[layer] == "Yes":
                        mapemotecode += " " + layer
                else:
                    mapemotecode += " " + layer + "_" + dynamicspritespreview_text_selectedlayers[layer]
            mapemotecode += "')"
            DynamicSprites_CheckClipboard()()

    class DynamicSprites_ChangeSelectedChar:
        def __init__(self, i, layer=None):
            self.i = i
        def __call__(self):
            global dynamicspritespreview_var_selectedchar, dynamicspritespreview_var_selectedpose, dynamicspritespreview_var_selectedlayers
            dynamicspritespreview_var_selectedchar = self.i
            dynamicspritespreview_var_selectedpose = 0
            dynamicspritespreview_var_selectedlayers = {}
            DynamicSprites_VarUpdate()
    class DynamicSprites_ChangeSelectedPose:
        def __init__(self, i, layer=None):
            self.i = i
        def __call__(self):
            global dynamicspritespreview_var_selectedpose, dynamicspritespreview_var_selectedlayers
            dynamicspritespreview_var_selectedpose = self.i
            dynamicspritespreview_var_selectedlayers = {}
            DynamicSprites_VarUpdate()
    class DynamicSprites_ChangeSelectedLayer:
        def __init__(self, i, layer):
            self.i = i
            self.layer = layer
        def __call__(self):
            global dynamicspritespreview_var_selectedlayers
            dynamicspritespreview_var_selectedlayers[self.layer] = self.i
            DynamicSprites_VarUpdate()
    class DynamicSprites_CopyToClipboard:
        def __call__(self):
            global mapemotecode, mapemotecode_postscript
            if type(mapemotecode) is unicode and mapemotecode != "":
                pygame.scrap.put(pygame.scrap.SCRAP_TEXT, mapemotecode.encode("utf-8"))
            DynamicSprites_CheckClipboard()()
    class DynamicSprites_CheckClipboard:
        def __call__(self):
            global mapemotecode, mapemotecode_postscript
            cb = pygame.scrap.get(pygame.scrap.SCRAP_TEXT)
            if type(mapemotecode) != unicode or mapemotecode == "":
                mapemotecode_postscript = ""
            elif cb == mapemotecode:
                mapemotecode_postscript = " <COPIED>"
            else:
                mapemotecode_postscript = " <CLICK TO COPY>"
            renpy.restart_interaction()

screen dynamicspritespreview_dropdown(currentselected, selectionlist, callback, layer=None, offset=(0,0)):
    zorder 201
    frame:
        background None
        xysize (1.0, 1.0)
        margin (0,0)
        padding (0,0)
        #action Hide("dynamicspritespreview_dropdown")
        button:
            background Solid("222e")
            align (0.94, 0.3)
            offset offset
            xysize (400, 600)
            margin (0,0)
            padding (15,15,50,15)
            action Hide("dynamicspritespreview_dropdown")
            viewport id "dynamicspritespreview_viewport_dropdown":
                draggable True
                mousewheel True
                vbox:
                    spacing 5
                    for i in range(len(selectionlist)):
                        $ t = selectionlist[i]
                        if t == currentselected:
                            $ t = '{b}'+t+'{/b}'
                        button:
                            background Solid("000e")
                            hover_background Solid("225e")
                            xysize (1.0, 60)
                            hovered [ callback(i, layer),
                                    Show('dynamicspritespreview'),
                                    Show('dynamicspritespreview_dropdown',
                                        currentselected = selectionlist[i],
                                        selectionlist = selectionlist,
                                        callback = callback,
                                        layer = layer,
                                        offset = offset) ]
                            action Hide("dynamicspritespreview_dropdown")
                            text t:
                                size 24
                                color "fff"
                                align (0.5, 0.5)
                                text_align 0.5

            vbar value YScrollValue("dynamicspritespreview_viewport_dropdown"):
                xalign 1.0
                xoffset 35

screen dynamicspritespreview:
    zorder 200
    $ mapemotecode_text = str(mapemotecode) + '{b}' + str(mapemotecode_postscript) + '{/b}'
    button:
        background Solid("fff9")
        xysize (1.0, 1.0)
        margin (0,0)
        padding (0,0)
        action [Hide("dynamicspritespreview"), Hide("dynamicspritespreview_dropdown")]
        text "DYNAMIC SPRITES PREVIEW (click here to close)":
            size 40
            color "000f"
        hbox:
            spacing 0
            button:
                background Solid("fffe")
                xysize (config.screen_width/2, 1.0)
                margin (10,50,5,10)
                padding (5,5)
                action DynamicSprites_CopyToClipboard()
                frame:
                    background None
                    margin (0,0,0,50)
                    padding (0,0)
                    align (0.5, 0.0)
                    viewport id "dynamicspritespreview_viewport_previewimage":
                        draggable True
                        mousewheel True
                        xinitial 0.5
                        yinitial 0.5
                        for layer in layerorder:
                            if layer in values:
                                $ img = valuespath[layer][dynamicspritespreview_var_selectedlayers[layer]]
                                if not img is None:
                                    add valuespath[layer][dynamicspritespreview_var_selectedlayers[layer]]:
                                        align (0.5, 0.5)
                                        zoom 0.8 * valueszoom
                frame:
                    background None
                    margin (0,0)
                    padding (0,0)
                    align (0.5, 1.0)
                    text mapemotecode_text:
                        align (0.5, 0.5)
                        text_align 0.5
                        size 18
                        color "000"

            button:
                background Solid("fffe")
                xysize (config.screen_width/4, 1.0)
                margin (5,50,5,10)
                padding (5,5)
                action Hide("dynamicspritespreview_dropdown")
                vbox:
                    spacing 10
                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        button:
                            background Solid("222")
                            hover_background Solid("225e")
                            xysize (150, 60)
                            margin (0,0)
                            padding (0,0)
                            hovered Show("dynamicspritespreview_dropdown",
                                currentselected=dynamicspritespreview_text_selectedchar,
                                selectionlist=charlist,
                                callback=DynamicSprites_ChangeSelectedChar,
                                offset=(-300,-100))
                            action Hide("dynamicspritespreview_dropdown")
                            text dynamicspritespreview_text_selectedchar:
                                size 20
                                color "fff"
                                align (0.5, 0.5)
                                text_align 0.5
                        button:
                            background Solid("222")
                            hover_background Solid("225e")
                            xysize (290, 60)
                            margin (0,0)
                            padding (0,0)
                            hovered Show("dynamicspritespreview_dropdown",
                                currentselected=dynamicspritespreview_text_selectedpose,
                                selectionlist=[x[-1] for x in posedict[dynamicspritespreview_text_selectedchar]],
                                callback=DynamicSprites_ChangeSelectedPose,
                                offset=(0,-100))
                            action Hide("dynamicspritespreview_dropdown")
                            text dynamicspritespreview_text_selectedpose:
                                size 20
                                color "fff"
                                align (0.5, 0.5)
                                text_align 0.5
                    null height 20
                    for i in range(len(layerorder)):
                        $ l = layerorder[i]
                        if l in values:
                            hbox:
                                spacing 10
                                label l:
                                    xysize (150, 60)
                                    margin (0,0)
                                    padding (0,0)
                                    text_size 24
                                    text_color "000"
                                    text_align (0.5, 0.5)
                                    text_text_align 1.0
                                button:
                                    background Solid("222")
                                    hover_background Solid("225e")
                                    xysize (290, 60)
                                    margin (0,0)
                                    padding (0,0)
                                    hovered Show("dynamicspritespreview_dropdown",
                                        currentselected=dynamicspritespreview_text_selectedlayers[l],
                                        selectionlist=values[l],
                                        callback=DynamicSprites_ChangeSelectedLayer,
                                        layer=l,
                                        offset=(0,i*60))
                                    action Hide("dynamicspritespreview_dropdown")
                                    text dynamicspritespreview_text_selectedlayers[l]:
                                        size 20
                                        color "fff"
                                        align (0.5, 0.5)
                                        text_align 0.5
            button:
                background Solid("fffe")
                xysize (config.screen_width/4, 1.0)
                margin (5,50,10,10)
                padding (5,5)
                action Hide("dynamicspritespreview_dropdown")
