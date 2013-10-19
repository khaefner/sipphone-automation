import robot
import urllib
import urllib2

BEGIN_REQUEST = "<PolycomIPPhone><Data priority=\"Critical\">"
END_REQUEST = "</Data></PolycomIPPhone>"

from robot.libraries.BuiltIn import BuiltIn

class PhoneKeywords(object):
	ROBOT_LIBRARY_SCOPE = 'Global'

	def __init__(self):
		self.phones = {}
		self.builtin = BuiltIn()

	def setup_phone(self, extension, ipaddr, username, password):
		self.phones[extension] = (ipaddr, username, password)
		self.builtin.log("Added Phone")

	def call_number(self, extenson, number):
		URL = BEGIN_REQUEST + "tel:\\" + number + END_REQUEST
		_sendRequest_(self.phones[extension][0], URL)		

	def _sendRequest_(ipaddr, request):
		headers = { 'Content-Type' : 'application/x-com-polycom-spipx' }
			
