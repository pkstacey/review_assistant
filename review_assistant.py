"""
Authored by Dr Patrick Stacey to ease but not replace the review process.

"""


import os

#path to file to be reviewed and generate the 'essence' file:
path = ""

# make lexicon of academic power words:
__KEYWDS__ = ["we","contribute", "contribution", "contributions", "under-researched","question","objective", "aims", "focus", "conclude","conclusion", "conclusions","findings","conceptualization", "limitation", "gap", "survey", "interview", "implications","implication","recommendations"]
__VALIDSENTENCES__ = []

#ingest pdf/document to review:
file_source = input("enter filename:")
output=path+file_source+".txt"
os.system(("pdftotext %s %s") %( path+file_source , output))

#break into sentences:
file = open(path+file_source+".txt","r")
article_text = file.read().replace("\n", " ")
file.close()
at_sents = article_text.split(".")

#quick clean
at_sents = [w.replace('i.e.', '') for w in at_sents]
at_sents = [w.replace('e.g.', '') for w in at_sents]

#analyse each sentence.
for index, row in enumerate(at_sents):
    intersection = [i for index2,i in enumerate(row.lower().split(" ")) if i in set(__KEYWDS__)]
    if len(intersection) > 0:
        __VALIDSENTENCES__.append(intersection)
        __VALIDSENTENCES__.append(row)
        if (index < len(at_sents)):
            __VALIDSENTENCES__.append(at_sents[index+1])

with open(path+file_source+'_essence.txt', 'w') as outfile:
    for line in __VALIDSENTENCES__:
        outfile.write(str(line)+"\r\n\r\n")

# save essence into sep file:
os.system(("rm %s") %(output))

