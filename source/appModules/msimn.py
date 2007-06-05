#appModules/msimn.py - Outlook Express appModule
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2007 NVDA Contributors <http://www.nvda-project.org/>
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import winUser
import api
import IAccessibleHandler
import appModuleHandler
import speech

envelopeNames={
	1000:_("Attachments"),
	1001:_("To:"),
	1002:_("Newsgroup:"),
	1003:_("CC:"),
	1004:_("Subject:"),
	1005:_("From:"),
	1016:_("Date:"),
	1018:_("Forward to:"),
	1019:_("Answer to:"),
	1020:_("Organisation:"),
	1021:_("Distribution:"),
	1022:_("Key words:"),
	1026:_("BCC:"),
	1037:_("From:"),
}

class appModule(appModuleHandler.appModule):

	def __init__(self,*args):
		appModuleHandler.appModule.__init__(self,*args)
		self.previousClassName=None

	def event_NVDAObject_init(self,obj):
		controlID=obj.windowControlID
		windowHandle=obj.windowHandle
		parentWindow=winUser.getAncestor(windowHandle,winUser.GA_PARENT)
		parentClassName=winUser.getClassName(parentWindow)
		if parentClassName=="OE_Envelope" and obj.IAccessibleChildID==0 and envelopeNames.has_key(controlID):
			obj.name=envelopeNames[controlID]
			self.previousClassName=parentClassName
		elif parentClassName=="Outlook Express Message List":
			if parentClassName==self.previousClassName:
				obj.name=""
			else:
				self.previousClassName=parentClassName
