import urllib
import urllib2
import json
import httplib
import base64
from urlparse import urlparse

username = None
repo = None

def Main():
	create_url = create_repo()
	encoding = gen_html()
	if create_file(create_url, encoding):
		print 'Your Stackoverflow flair for Linkedin is: ' + '\033[1m' + 'http://' + username + '.github.io' + '\033[0m'
	else:
		print 'Failed creating, deleting repository.....'
		if delete_repo():
			print 'Repository deleted'
		else:
			print 'Failed deleting ' + repo + ', please delete it manually'
		
def create_repo():
	res_code = 400
	create_url = None
	while res_code != 201:
		global username
		username = raw_input('Github username: ')
		token = raw_input('Access Token: ')
		url = 'https://api.github.com/user/repos?access_token=' + token
		global repo
		repo = username + ".github.io"
		values = {"name":repo}
		data = json.dumps(values)
		req = urllib2.Request(url,data)
		response = None
		print 'Creating repository.....'
		try: response = urllib2.urlopen(req)
		except urllib2.URLError as e:
			if e.reason == 'Unauthorized':
				print 'Invalid token, try again'
			if e.reason == 'Unprocessable Entity':
				print 'Invalid Github username, try again'
			continue
		res_code = response.getcode()
		if res_code == 201:
			print 'Repository ' + repo + ' created'
			create_url = 'https://api.github.com/repos/' + username + '/' + repo + '/contents/index.html?access_token=' + token
	return create_url	
    
def gen_html():
	valid_url = False
	flair = None
	profile = None
	while not valid_url:		
		stack_id = raw_input('Stackoverflow id: ')
		flair = 'http://stackoverflow.com/users/flair/' + stack_id + '.png'
		profile = 'http://stackoverflow.com/users/' + stack_id
		print 'Validating Stackoverflow ID.....'
		if checkUrl(flair) and checkUrl(profile):
			valid_url = True
	html = ('<!DOCTYPE html>'
	'<html>'
	'<head><meta content="0; ' + profile + '" http-equiv="refresh" />'
	'</head>'
	'<body><p><a href=' + profile + '>'
	'<img alt="Nothing" border="0" src="' + flair + '" ></a></p>'
	'</body>'
	'</html>')
	return base64.b64encode(html)
			
def checkUrl(url):
	p = urlparse(url)
	conn = httplib.HTTPConnection(p.netloc)
	conn.request('HEAD', p.path)
	resp = conn.getresponse()
	return resp.status < 400
    
def create_file(create_url, encoding):	
	values = {"message":"Stackoverflow & Linkedin","content":encoding}
	data = json.dumps(values)		
	req = urllib2.Request(create_url,data)
	req.get_method = lambda: 'PUT'
	response = None
	print 'Committing HTML file.....'
	try: response = urllib2.urlopen(req)
	except urllib2.URLError as e:
		print e
		return False
	res_code = response.getcode()
	if res_code == 201:
		return True
	return False
	
def delete_repo():
	delete_url = 'https://api.github.com/repos/' + username + '/' + repo
	req = urllib2.Request(delete_url)
	req.get_method = lambda: 'DELETE'
	response = None
	try: response = urllib2.urlopen(req)
	except urllib2.URLError as e:
		return False
	res_code = response.getcode()
	if res_code == 204:
		return True
	return False
				
if __name__ == "__main__":
	Main()
	
	
	

	
