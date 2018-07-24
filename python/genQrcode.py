import pyqrcode

def genQrcode(txtFile,imgFile,encoding='utf'):
	try:
		f = open(txtFile, 'r')
		str = f.read()
		img = pyqrcode.create(str,encoding=encoding)
		img.png(imgFile)	
		print "qrcode of txt file ",txtFile ," is saved in ", imgFile
	finally:
		if f:
			f.close()
		
		
genQrcode('c:/nsi.log','c:/nsi.png'	)
