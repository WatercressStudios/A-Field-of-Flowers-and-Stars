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

    basedict = {}
    pathlist = {}
    spritedict = {}
    def DefineImages(imageFolder, composite=False, prepend=None, overrideCharname=None, overrideLayerOrder=None, allcombinations=False):
        if composite:
            imglist = []

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
                    pathlist[path_list] = path

        if composite:
            baselist = []
            for path_list in imglist:
                # get the list of sprite pose folders, which are detected if they contain:
                # 1. a base ('/base.')
                # 2. default eye ('/e default.' or '/ec default.')
                # 3. default mouth ('/m default.' or '/mc default.')
                basepath = path_list[:-1]
                if basepath in baselist:
                    continue
                if u'base' in path_list[-1]:
                    has_eyes = False
                    if basepath + (u'e', u'default') in pathlist:
                        has_eyes = True
                    if basepath + (u'ec', u'default') in pathlist:
                        has_eyes = True

                    has_mouth = False
                    if basepath + (u'm', u'default') in pathlist:
                        has_mouth = True
                    if basepath + (u'mc', u'default') in pathlist:
                        has_mouth = True

                    if has_eyes and has_mouth:
                        baselist.append(basepath)

            for basepath in baselist:
                charname = overrideCharname
                if charname is None:
                    charname = basepath[0]
                #devlog.info('==== ' + charname)

                # build the lists
                basedict[basepath] = {}
                basedict[basepath]['bases'] = []
                basedict[basepath]['parts'] = []
                basedict[basepath]['emotes'] = []
                basedict[basepath]['list'] = []
                basedict[basepath]['extraparts'] = {}
                basedict[basepath]['optionals'] = []
                baselen = len(basepath)
                for path_list in imglist:
                    if path_list[:baselen] == basepath:
                        if len(path_list) - baselen == 1:
                            basedict[basepath]['bases'].append(path_list[-1])
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

                # special case for 'e' and 'ec': build blinking eyes into 'ed'
                # fill in the missing files as "default"
                if 'e' in basedict[basepath]['parts'] or 'ec' in basedict[basepath]['parts']:
                    for emote in basedict[basepath]['emotes']:
                        eyesopen = basepath + (u'e', emote)
                        eyesclose = basepath + (u'ec', emote)
                        if not eyesopen in basedict[basepath]['list']:
                            renpy.image(('_'.join(eyesopen), ), '_'.join(basepath+(u'e', u'default')))
                        if not basepath+(u'e', u'default') in basedict[basepath]['list']:
                            renpy.image(('_'.join(basepath+(u'e', u'default')), ), '_'.join(basepath+(u'ec', u'default')))
                        if not eyesclose in basedict[basepath]['list']:
                            renpy.image(('_'.join(eyesclose), ), '_'.join(basepath+(u'ec', u'default')))
                        if not basepath+(u'ec', u'default') in basedict[basepath]['list']:
                            renpy.image(('_'.join(basepath+(u'ec', u'default')), ), '_'.join(basepath+(u'e', u'default')))
                        renpy.image(('_'.join(basepath + (u'ed', emote)), ), blinkeyes('_'.join(eyesopen), '_'.join(eyesclose)))
                        basedict[basepath]['list'].append(basepath + (u'ed', emote))
                    basedict[basepath]['parts'].append('ed')

                # special case for 'm' and 'mc': build flapping mouth into 'md'
                # fill in the missing files as "default"
                if 'm' in basedict[basepath]['parts'] or 'mc' in basedict[basepath]['parts']:
                    for emote in basedict[basepath]['emotes']:
                        mouthopen = basepath + (u'm', emote)
                        mouthclose = basepath + (u'mc', emote)
                        if not mouthopen in basedict[basepath]['list']:
                            renpy.image(('_'.join(mouthopen), ), '_'.join(basepath+(u'm', u'default')))
                        if not basepath+(u'm', u'default') in basedict[basepath]['list']:
                            renpy.image(('_'.join(basepath+(u'm', u'default')), ), '_'.join(basepath+(u'mc', u'default')))
                        if not mouthclose in basedict[basepath]['list']:
                            renpy.image(('_'.join(mouthclose), ), '_'.join(basepath+(u'mc', u'default')))
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
                            layers.append(Attribute('base', base, '_'.join(basepath+(base,)), base == 'base'))
                    elif layer == 'eyes':
                        for emote in basedict[basepath]['emotes']:
                            eyes = basepath+(u'ed', emote)
                            layers.append(Attribute('ed', emote, '_'.join(eyes), emote == 'default'))
                    elif layer == 'mouth':
                        for emote in basedict[basepath]['emotes']:
                            mouth = basepath+(u'md', emote)
                            layers.append(Attribute('md', emote, '_'.join(mouth), emote == 'default'))
                    elif layer in basedict[basepath]['optionals']:
                        layers.append(Attribute(layer, layer, '_'.join(basepath + (u'optional', layer))))
                    else:
                        for ex in sorted(basedict[basepath]['extraparts'].keys()):
                            if layer == ex:
                                for emote in basedict[basepath]['emotes']:
                                    layers.append(Attribute(ex, emote, '_'.join(basepath + (ex, emote)), emote == 'default'))
                layered = LayeredImage(layers)
                spritedict[basepath] = layered
                renpy.image(basepath, layered)

            #pretty(basedict)

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

        if eyes == None:
            eyes = ('ed', 'default')
        if mouth == None:
            mouth = ('md', 'default')
        for ek in extraparts.keys():
            if extraparts[ek] == None:
                extraparts[ek] = (ek, 'default')

        if charpath in spritedict.keys():
            layered = spritedict[charpath]
        else:
            layered = spritedict[basepath]
        found = False
        layers = []
        # print "Attributes: ", len(layered.attributes)
        for a in layered.attributes:
            #print "Group: ", a.group, "Attribute: ", a.attribute, "Image: ", a.image, "Default: ", a.default
            if bases == a.attribute and a.group == 'base':
                layers.append(Attribute(a.group, a.attribute, a.image, a.default))
                layers.append(Attribute(a.group, newemote, '_'.join(basepath+(bases,))))
            elif newemote == a.attribute:
                found = True
                if eyes != None and a.group == 'ed':
                    layers.append(Attribute(a.group, a.attribute, '_'.join(basepath+eyes), a.default))
                elif mouth != None and a.group == 'md':
                    layers.append(Attribute(a.group, a.attribute, '_'.join(basepath+mouth), a.default))
                elif a.group in extraparts.keys() and extraparts[a.group] != None:
                    layers.append(Attribute(a.group, a.attribute, '_'.join(basepath+extraparts[a.group]), a.default))
                else:
                    layers.append(Attribute(a.group, a.attribute, a.image, a.default))
            elif optionals != None and a.group in optionals:
                layers.append(Attribute(a.group, a.attribute, a.image, a.default))
                layers.append(Attribute('___'.join((a.group,newemote)), newemote, '_'.join(basepath + (u'optional', a.group))))
            else:
                layers.append(Attribute(a.group, a.attribute, a.image, a.default))

        if not found:
            oldlayers = layers
            layers = []
            for a in oldlayers:
                layers.append(a)
                if eyes != None and a.group == 'ed':
                    layers.append(Attribute('ed', newemote, '_'.join(basepath+eyes)))
                    eyes = None
                elif mouth != None and a.group == 'md':
                    layers.append(Attribute('md', newemote, '_'.join(basepath+mouth)))
                    mouth = None
                elif a.group in extraparts.keys() and extraparts[a.group] != None:
                    layers.append(Attribute(a.group, newemote, '_'.join(basepath+extraparts[a.group])))
                    extraparts[a.group] = None

        layered = LayeredImage(layers)
        spritedict[charpath] = layered
        renpy.image(charpath, layered)

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

    def CSprite(base, size, *layers):
        if size is None or layers is None or len(layers) == 0:
            return base
        argslayers = []
        for l in layers:
            argslayers.append((0, 0))
            argslayers.append(l)
        return LiveComposite(
                size,
                *argslayers
            )

    class BaseCSprite:
        def __init__(self, basesprite, size):
            self.basesprite = basesprite
            self.size = size

        def __call__(self, layers=[]):
            return CSprite(self.basesprite, self.size, *layers)
