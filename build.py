from fontmake import __main__
from fontTools.ttLib import TTFont, newTable
import shutil
import subprocess

__main__.main(("-g","sources/HachiMaruPop.glyphs", "-o","ttf",))

path = "master_ttf/HachiMaruPop-Regular.ttf"

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

modifiedFont.save("fonts/ttf/HachiMaruPop-Regular.ttf")

shutil.rmtree("instance_ufo")
shutil.rmtree("master_ufo")
shutil.rmtree("master_ttf")

subprocess.check_call(
        [
            "ttfautohint",
            "--stem-width",
            "nsn",
            "fonts/ttf/HachiMaruPop-Regular.ttf",
            "fonts/ttf/HachiMaruPop-Regular-hinted.ttf",
        ]
    )
shutil.move("fonts/ttf/HachiMaruPop-Regular-hinted.ttf", "fonts/ttf/HachiMaruPop-Regular.ttf")