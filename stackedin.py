import urllib
import urllib2

def Main():
	username = raw_input('Github name: ')
	token = raw_input('Access Token: ')
	url = 'https://api.github.com/user/repos?access_token=' + token
	values = {"name":"newnewnew"}
	data = urllib.urlencode(values)
	req = urllib2.Request(url,data)
	response = urllib2.urlopen(req)
	the_page = response.read();
	print the_page
	
if __name__ == "__main__":
	Main()
	
	
	

	