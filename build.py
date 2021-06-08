from fontmake import __main__
from fontTools.ttLib import TTFont, newTable
import shutil
import subprocess

__main__.main(("-g","sources/HachiMaruPop.glyphs", "-o","ttf",))

path = "master_ttf/HachiMaruPop-Regular.ttf"

def GASP_set(font:TTFont):
    if "gasp" not in font:
        font["gasp"] = newTable("gasp")
        font["gasp"].gaspRange = {}
    if font["gasp"].gaspRange != {65535: 0x000A}:
        font["gasp"].gaspRange = {65535: 0x000A}

modifiedFont = TTFont(path)
print ("Adding additional tables")
modifiedFont["DSIG"] = newTable("DSIG")     #need that stub dsig

print ("Making other changes")
modifiedFont["DSIG"].ulVersion = 1
modifiedFont["DSIG"].usFlag = 0
modifiedFont["DSIG"].usNumSigs = 0
modifiedFont["DSIG"].signatureRecords = []
modifiedFont["head"].flags |= 1 << 3        #sets flag to always round PPEM to integer

modifiedFont["name"].addMultilingualName({'ja':'はちまるポップ'}, modifiedFont, nameID = 1, windows=True, mac=False)
modifiedFont["name"].addMultilingualName({'ja':'Regular'}, modifiedFont, nameID = 2, windows=True, mac=False)

GASP_set(modifiedFont)

modifiedFont.save("fonts/ttf/HachiMaruPop-Regular.ttf")

shutil.rmtree("instance_ufo")
shutil.rmtree("master_ufo")
shutil.rmtree("master_ttf")