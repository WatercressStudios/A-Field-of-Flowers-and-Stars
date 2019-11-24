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
#
# To generate these:
# 1. Run the game in Ren'Py
# 2. Call the console with 'shift+o'
# 3. Type 'ParseVoices()' and hit enter
#

init python:
    import os, re

    def ParseVoices():
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
                labelTag = 'default'

                found = False
                outstr = ""
                for line in infile:
                    trimmedLine = line.strip()
                    if trimmedLine.startswith('label '):
                        labelTag = trimmedLine.split()[1].strip(':')

                    if trimmedLine.startswith('voice '):
                        continue
                    else:
                        for cha in voices.keys():
                            if trimmedLine.startswith(cha + ' '):
                                found = True
                                leadingWhitespace = line.split(cha)[0]
                                outstr += leadingWhitespace + 'voice "voice/' + fileTag + '-' + labelTag + '-' + str(lineCount) + '.ogg" ' + voices[cha] + '\n'
                                lineCount += 1
                    outstr += line

                if found:
                    with open(outputFilePath, 'w') as outfile:
                        outfile.write(outstr)
                        numFiles += 1

                        print '  ' + outputFilePath
        res = 'Number of files edited: ' + str(numFiles)
        return res
