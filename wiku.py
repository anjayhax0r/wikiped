#~!~#
#python 3.7.X
#jika baru pertama kali menjalankan program ini ketikan perintah dibawah ini
#python -m pip install gtts playsound wikipedia

from gtts import gTTS
import os,wikipedia,argparse

class Run:
	def lang(self,lg):
		if lg == None:
			self.langue='en'
		else:
			self.langue=lg

	def wiki(self,query):
		wikipedia.set_lang(self.langue)
		if type(query) == list:
			kalimat=wikipedia.summary(" ".join(str(x) for x in query))
		else:
			kalimat=wikipedia.summary(query)
		print(kalimat)

def _help():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument('-l',dest='lang', help='Untuk mengubah bahasa wikipedia (default:english)')
	parser.add_argument('-q',dest='query', help='Kata kunci untuk mencari sesuatu di wikipedia', required=True, nargs='*')
	args = vars(parser.parse_args())
#	print(args)

os.system('clear')
print("""
 _ _ _ _ _ ___ _ ___ _ 
| | | | | / | | / | | | #Author  : anjayani
| | | | |  \| |  \| ' |	#Github  : github.com/anjayhax0r
|__/_/|_|_\_|_|_\_`___' #Contact : t.me/kang_nuubi
                       """)
_help()
try:
	wik=Run()
	wik.lang(args['lang'])
	wik.wiki(args['query'])
except Exception as Err:
	print("ERR: %s"%(Err))
