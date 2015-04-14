#!/usr/bin/env python
### OPOINTRO 
##### VERSION: 1.3.5 BETA
##### RELEASE DATE: APRIL 14, 2015
##### AUTHOR: vvn
##### DESCRIPTION: simple library to port ADB and FASTBOOT functions to PYTHON
#####
##### USER LICENSE AGREEMENT & DISCLAIMER
##### copyright, copyleft (C) 2014-15  vvn <vvn@notworth.it>
##### 
##### This program is FREE software: you can use it, redistribute it and/or modify
##### it as you wish. Copying and distribution of this file, with or without modification,
##### are permitted in any medium without royalty provided the copyright
##### notice and this notice are preserved. This program is offered AS-IS,
##### WITHOUT ANY WARRANTY; without even the implied warranty of
##### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##### GNU General Public License for more details.
##### 
##### For more information, please refer to the "LICENSE AND NOTICE" file that should
##### accompany all official download releases of this program. 
##### 
##### getting credited for my work is nice. so are donations.
##### but to really show your appreciation, you should buy my EP instead!
##### you can stream and purchase it at: dreamcorp.bandcamp.com
##### (you might even enjoy listening to it)
##### questions, comments, feedback, bugs, complaints, death threats, marriage proposals?
##### contact me at:
##### vvn (at) notworth (dot) it

import time


#################################
#################################
######### COLOR LIBRARY #########
#################################
#################################

class acolors:
   CLEAR = '\033[0m'
   BOLD = '\033[1m'
   GREY = '\033[2m'
   UNDERLINE = '\033[4m'
   BLINK = '\033[5m'
   INVERSE = '\033[7m'
   BLACK = '\033[30m'
   ORANGE = '\033[31m'
   GREEN = '\033[32m'
   YELLOW = '\033[33m'
   BLUE = '\033[34m'
   MAGENTA = '\033[35m'
   AQUA = '\033[36m'
   BEIGE = '\033[37m'
   BLACKBG = '\033[40m'
   REDBG = '\033[41m'
   GREENBG = '\033[42m'
   YELLOWBG = '\033[43m'
   BLUEBG = '\033[44m'
   MAGENTABG = '\033[45m'
   AQUABG = '\033[46m'
   BEIGEBG = '\033[47m'
   OKGREY = '\033[90m'
   OKORANGE = '\033[91m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   OKBLUE = '\033[94m'
   OKMAGENTA = '\033[95m'
   OKAQUA = '\033[96m'
   OKBEIGE = '\033[97m'


#################################
#################################
######## SCROLLING INTRO ########
#################################
#################################

class opointro(object):

##### CLEAN #####

   def cleanlogo(self):
      print ("##################################################################################")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~ HALF-ASSED ONEPLUS ONE TOOLKIT ~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ v1.3.5 BETA ~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~                            77~~~~~~                   7~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~         7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~         7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~               7~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~               7~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~ SUPPORT MY WORK - BUY MY EP! ~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~ http://dreamcorp.bandcamp.com ~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~                                               7~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ AUTHOR: VVN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~ RELEASE DATE: APRIL 14, 2015 ~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ COPYLEFT (C) 2014-2015 VVN ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#")
      time.sleep(0.1)
      print ("##################################################################################")
      time.sleep(4.5)
      print ("\n\n")

##### COLOR #####

   def colorlogo(self):
   
      print ("\033[41m\033[37;1m#################################################################\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~~~~~~~~~~~~~~~ \033[40m\033[33;1mTHE HALF-ASSED\033[41m\033[37;1m ~~~~~~~~~~~~~~~~~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~~~~~~~~~~~~~ \033[40m\033[33mONEPLUS ONE TOOLKIT\033[41m\033[37m ~~~~~~~~I\033[41m\033[37;1m   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~~~~~~~~~~~~~~~~~ \033[41m\033[40;1mv1.3.4 BETA\033[41m\033[37;1m ~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I                           77~~~~~I               7~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~I         7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\033[0m")
      time.sleep(0.2)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~I   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\033[0m")
      time.sleep(0.2)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~I   7~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.2)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~I   7~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.2)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~I   7~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~I   7~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~I   7~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~I   7~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~I               7~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~ SUPPORT MY WORK - BUY MY EP! ~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~ http://dreamcorp.bandcamp.com ~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I   7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~I   7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~I                                            7~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~~~~~~~~~~~~~~~~~~ \033[40m\033[35;1mAUTHOR: VVN \033[41m\033[37;1m~~~~~~~~~~~~~~~~~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~~~~~~~~~ \033[40m\033[36;1mRELEASE DATE: APRIL 14, 2015 \033[41m\033[37;1m~~~~~~~~~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\033[0m")
      time.sleep(0.1)
      print ("\033[41m\033[37;1m#################################################################\033[0m")
      time.sleep(4.5)
      print("\n\n")

#####################
#####################
##### MAIN MENU #####
#####################
#####################

##### CLEAN #####
      
   cleanmenu = '''
*********************************************************** 
************ THE HALF-ASSED ONEPLUS ONE TOOLKIT ***********
**************** VERSION: 1.3.5 BETA * by vvn *************
***********************************************************
*** this is a FREE program, released AS-IS: NO WARRANTY ***
****************** USE AT YOUR OWN RISK! ******************
*********************************************************** 
*************** support my work: buy my EP! ***************
************** http://dreamcorp.bandcamp.com **************
***********************************************************
DEVICE MUST BE CONNECTED VIA USB WITH ANDROID DEBUGGING ENABLED. 
MAIN MENU:
-[1] reboot into android, bootloader, or recovery
-[2] flash partitions or wipe device
-[3] boot once into custom recovery without flashing - need unlocked bootloader
-[4] install or uninstall APK
-[5] copy files between computer and device, or sync
-[6] backup or restore device
-[7] root device and/or install ZIP in fastboot
-[8] flash stock or custom ROM image
-[9] unlock bootloader or flash custom recovery
-[10] run shell command on device
-[11] get bug report from device
-[12] find/list apps, pull APK from device
-[13] list services
-[14] list features
-[15] list permissions
-[16] view logcat from device
-[0] quit
'''

##### COLOR #####   

   colormenu = '''
\033[40m\033[34m***********************************************************\033[0m 
\033[40m\033[34m************ \033[36mTHE HALF-ASSED ONEPLUS ONE TOOLKIT \033[34m***********\033[0m
\033[40m\033[34m**************** \033[37mVERSION: 1.3.5 BETA \033[34m* \033[35mby vvn \033[34m*************\033[0m
\033[40m\033[34m***********************************************************\033[0m
\033[40m\033[34m*** \033[33mthis is a FREE program, released AS-IS: NO WARRANTY \033[34m***\033[0m
\033[40m\033[34m****************** \033[32mUSE AT YOUR OWN RISK! \033[34m******************\033[0m
\033[40m\033[34m***********************************************************\033[0m 
\033[40m\033[34m*************** \033[37msupport my work: buy my EP! \033[34m***************\033[0m
\033[40m\033[34m************** \033[37mhttp://dreamcorp.bandcamp.com \033[34m**************\033[0m
\033[40m\033[34m***********************************************************\033[0m \n
\033[33mDEVICE MUST BE CONNECTED VIA USB WITH ANDROID DEBUGGING ENABLED. \033[0m \n
\033[32mMAIN MENU:\033[0m
-\033[31m[1]\033[37m reboot into android, bootloader, or recovery\033[0m
-\033[31m[2]\033[37m flash partitions or wipe device\033[0m
-\033[31m[3]\033[37m boot once into custom recovery without flashing - need unlocked bootloader\033[0m
-\033[31m[4]\033[37m install or uninstall APK\033[0m
-\033[31m[5]\033[37m copy files between computer and device, or sync\033[0m
-\033[31m[6]\033[37m backup or restore device\033[0m
-\033[31m[7]\033[37m root device and/or install ZIP in fastboot\033[0m
-\033[31m[8]\033[37m flash stock or custom ROM image\033[0m
-\033[31m[9]\033[37m unlock bootloader or flash custom recovery\033[0m
-\033[31m[10]\033[37m run shell command on device\033[0m
-\033[31m[11]\033[37m get bug report from device\033[0m
-\033[31m[12]\033[37m find/list apps, pull APK from device\033[0m
-\033[31m[13]\033[37m list services\033[0m
-\033[31m[14]\033[37m list features\033[0m
-\033[31m[15]\033[37m list permissions\033[0m
-\033[31m[16]\033[37m view logcat from device\033[0m
-\033[31m[0]\033[37m quit \033[0m\n'''

######################
######################
##### WIPE  MENU #####
######################
######################

##### CLEAN #####

cleanwipemenu = '''
***WIPING SOME PARTITIONS WILL ERASE YOUR DATA.***
please make sure to back up any important data before proceeding!\n\n
CHOOSE AN OPTION 1-8:
-[1] perform a full system wipe [system, data, and cache partitions]
-[2] wipe only the system partition
-[3] wipe only the data partition
-[4] wipe only the cache partition
-[5] wipe only the boot partition
-[6] wipe only the recovery partition
-[7] flash device to factory images [flash system, boot, and recovery]
-[8] return to main menu
'''

##### COLOR #####

colorwipemenu = '''
\033[35m***WIPING SOME PARTITIONS WILL ERASE YOUR DATA.***
please make sure to back up any important data before proceeding!\n\n
\033[36mCHOOSE AN OPTION 1-8:\033[32m
-[1]\033[37m perform a full system wipe [system, data, and cache partitions]\033[32m
-[2]\033[37m wipe only the system partition\033[32m
-[3]\033[37m wipe only the data partition\033[32m
-[4]\033[37m wipe only the cache partition\033[32m
-[5]\033[37m wipe only the boot partition\033[32m
-[6]\033[37m wipe only the recovery partition\033[32m
-[7]\033[37m flash device to factory images [flash system, boot, and recovery]\033[32m
-[8]\033[37m return to main menu\n\033[0m
'''

######################
######################
##### FLASH MENU #####
######################
######################

##### CLEAN #####

cleanversionmenu = '''
CHOOSE A RELEASE VERSION - must be your current version or earlier to restore, or ONE version higher to upgrade. [1-7]
-[1] XNPH25R
-[2] XNPH30O
-[3] XNPH33R
-[4] XNPH38R
-[5] XNPH44S
-[6] XNPH05Q
-[7] return to main menu
'''

##### COLOR #####

colorversionmenu = '''
CHOOSE A RELEASE VERSION - must be your current version or earlier to restore, or ONE version higher to upgrade. [1-6]
-\033[36m[1]\033[37m XNPH25R \033[0m
-\033[36m[2]\033[37m XNPH30O \033[0m
-\033[36m[3]\033[37m XNPH33R \033[0m
-\033[36m[4]\033[37m XNPH38R \033[0m
-\033[36m[5]\033[37m XNPH44S \033[0m
-\033[36m[6]\033[37m XNPH05Q \033[0m
-\033[36m[7]\033[37m return to main menu \033[0m
'''

######################
######################
##### FLASH MENU #####
######################
######################

##### CLEAN #####

cleanflashmenu = '''
STOCK IMAGES AVAILABLE TO FLASH - THIS WILL REPLACE YOUR CURRENT PARTITION!
FLASH IN SEQUENTIAL ORDER IF POSSIBLE - BOOT.IMG SHOULD GO FIRST
-[1] stock BOOT.IMG
-[2] stock USERDATA.IMG -or- USERDATA_64.IMG [WIPES USER DATA!]
-[3] stock SYSTEM.IMG
-[4] stock RECOVERY.IMG
-[5] stock CACHE.IMG
-[6] stock NON-HLOS.BIN, modem, aboot, & more [flash-radio.sh]
-[7] stock radio, modem, sbl1, aboot [flash-extras.sh]
-[8] FLASH ENTIRE STOCK OR CUSTOM ROM IMAGE
-[9] return to main menu
CHECK THAT DEVICE IS UNLOCKED AND COMPUTER IS AUTHORIZED FOR ADB ACCESS.
'''

##### COLOR #####

colorflashmenu = '''
\n\033[36mSTOCK IMAGES AVAILABLE TO FLASH - THIS WILL REPLACE YOUR CURRENT PARTITION!
\033[37mFLASH IN SEQUENTIAL ORDER IF POSSIBLE - BOOT.IMG SHOULD GO FIRST
-\033[31m[1]\033[37m stock BOOT.IMG \033[0m
-\033[31m[2]\033[37m stock USERDATA.IMG -or- USERDATA_64.IMG \033[35m[WIPES USER DATA!]\033[0m
-\033[31m[3]\033[37m stock SYSTEM.IMG \033[0m
-\033[31m[4]\033[37m stock RECOVERY.IMG \033[0m
-\033[31m[5]\033[37m stock CACHE.IMG \033[0m
-\033[31m[6]\033[37m stock NON-HLOS.BIN, modem, aboot & more [flash-radio.sh]\033[0m
-\033[31m[7]\033[37m stock radio, modem, sbl1, aboot \033[34m[flash-extras.sh]\033[0m
-\033[31m[8]\033[37m flash complete stock or ROM image \033[0m
-\033[31m[9]\033[37m return to main menu\033[0m\n
\033[35mCHECK THAT DEVICE IS UNLOCKED AND COMPUTER IS AUTHORIZED FOR ADB ACCESS.\n\033[0m'''
