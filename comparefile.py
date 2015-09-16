import string
import os


Path = 'D:/work/diff/'
Filenames = os.listdir(Path)
DictOrig = {}
DictTest = {}

if(len(Filenames)>0):
	for fn in Filenames:
		if "TEST_" in fn:
			DictTest["%s" %fn] = ''
		else:
			DictOrig["%s" %fn] = ''

			
			
for origfn in DictOrig:
	index = origfn.find('_', 0) +1
	TEST_origfn = origfn[0:index] + "TEST_" + origfn[index:]
	if TEST_origfn in DictTest:
		result = os.system('diff %s %s' %(Path+origfn, Path+TEST_origfn));
		DictOrig["%s" %origfn] = result
	else:
		DictOrig["%s" %origfn] = "error"
			
			

for origfn in DictOrig:
	print (origfn + ":" + DictOrig["%s" %origfn])
