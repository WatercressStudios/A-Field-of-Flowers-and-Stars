# Voice Parser 2.0
#
# List out all voiced characters in init.rpy. Example:
#
# voices = {}
# voices['che'] = '#Cheshire (shiena)'
# voices['min'] = '#Ji-min ()'
# voices['bos'] = '#Boss ()'
# voices['mom'] = '#Mom ()'
# voices['dad'] = '#Dad ()'
# voices['caf'] = '#Cafe Owner ()'
# voices['vm'] =  '#Friend ()'
#
# To generate these:
# 1. Run the game in Ren'Py
# 2. Call the console with 'shift+o'
# 3. Type 'ParseVoices()' or 'ParseVoices(comment_out_if_missing=True)' and hit enter
#
# Use the 'comment_out_if_missing=True' version if you want the script to comment out
# the line automatically if the VA file doesn't exist
#
#
# VA filename conventions can be changed with voice_template in init.rpy. Example:
#
# voicefile_template = 'voice/{filenumber}-{labelname}-{scenelinenumber}.ogg'
#
# {filename} the script file name
# {filenum} the number in the script file name
# {labelname} the name of the current label
# {charname} the character short name
# {filelinenum} the line number in the file
# {labellinenum} the line number in the label
# {charlinenum} the line number for the character in the file
# {charlabellinenum} the line number for the character in the label
#

init python:
    import os, re

    def ParseVoices(comment_out_if_missing=False):
        filelist = []
        for root, dirs, files in os.walk(gamedir):
            for file in files:
                if file.endswith('.rpy'):
                    filelist.append((root, file))

        numFiles = 0
        for root, file in filelist:
            inputFilePath = os.path.join(root, file)
            outputFilePath = os.path.join(root, file)
            nums = re.findall(r'\d+', file)
            fileTag = '00'
            if len(nums) > 0:
                fileTag = nums[0]

            with open(inputFilePath, 'r') as infile:
                lineCount = 1
                lineLabelCount = 1
                lineCharCount = {}
                lineLabelCharCount = {}
                labelTag = 'default'

                found = False
                outstr = ""
                for line in infile:
                    trimmedLine = line.strip()
                    if trimmedLine.startswith('label '):
                        labelTag = trimmedLine.split()[1].strip(':')
                        lineLabelCount = 1
                        lineLabelCharCount = {}

                    if trimmedLine.startswith('voice ') or trimmedLine.startswith('#voice '):
                        continue
                    else:
                        for cha in voices.keys():
                            if trimmedLine.startswith(cha + ' '):
                                found = True
                                leadingWhitespace = line.split(cha)[0]
                                parsedline = voicefile_template.format(
                                    filename = os.path.splitext(os.path.basename(file))[0],
                                    filenum = fileTag,
                                    labelname = labelTag,
                                    charname = cha,
                                    filelinenum = lineCount,
                                    labellinenum = lineLabelCount,
                                    charlinenum = lineCharCount.get(cha, 1),
                                    charlabellinenum = lineLabelCharCount.get(cha, 1),
                                )
                                if comment_out_if_missing and not os.path.isfile(os.path.join(gamedir, parsedline)):
                                    outstr += leadingWhitespace + '#voice "'+ parsedline + '" ' + voices[cha] + '\n'
                                else:
                                    outstr += leadingWhitespace + 'voice "'+ parsedline + '" ' + voices[cha] + '\n'
                                lineCount += 1
                                lineLabelCount += 1
                                if not cha in lineCharCount:
                                    lineCharCount[cha] = 1
                                if not cha in lineLabelCharCount:
                                    lineLabelCharCount[cha] = 1
                                lineCharCount[cha] += 1
                                lineLabelCharCount[cha] += 1
                    outstr += line

                if found:
                    with open(outputFilePath, 'w') as outfile:
                        outfile.write(outstr)
                        numFiles += 1

                        print '  ' + outputFilePath
        res = 'Number of files edited: ' + str(numFiles)
        return res
