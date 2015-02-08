import urllib
import urllib2
import json
import httplib
from urlparse import urlparse
from xml.etree.ElementTree import ElementTree

def Main():
	create_repo()
	gen_html()
	
	
	
def create_repo():
	res_code = 400
	while res_code != 201:
		username = raw_input('Github username: ')
		token = raw_input('Access Token: ')
		url = 'https://api.github.com/user/repos?access_token=' + token
		repo = username + ".github.io"
		values = {"name":repo}
		data = json.dumps(values)
		req = urllib2.Request(url,data)
		response = None
		try: response = urllib2.urlopen(req)
		except urllib2.URLError as e:
			if e.reason == 'Unauthorized':
				print 'Invalid token'
			if e.reason == 'Unprocessable Entity':
				print 'Invalid Github username'
			continue
		res_code = response.getcode()
		if res_code == 201:
			print 'Repository ' + repo + ' created'	
    
def gen_html():
	valid_url = False
	flair = None
	profile = None
	while not valid_url:		
		stack_id = raw_input('Stackoverflow id: ')
		flair = 'http://stackoverflow.com/users/flair/' + stack_id + '.png'
		profile = 'http://stackoverflow.com/users/' + stack_id
		if checkUrl(flair) and checkUrl(profile):
			valid_url = True
	tree = ElementTree()
	tree.parse('index.html')
	head = tree.find('head')
	metas = list(head.iter('meta'))
	for i in metas:
		i.attrib['content'] = profile
	p = tree.find('body')
	imgs = list(p.iter('img'))
	for i in imgs:
		i.attrib['src'] = flair
	tree.write('index.html')
			
def checkUrl(url):
    p = urlparse(url)
    conn = httplib.HTTPConnection(p.netloc)
    conn.request('HEAD', p.path)
    resp = conn.getresponse()
    return resp.status < 400
    
def create_file():
	
			
			
if __name__ == "__main__":
	Main()
	
	
	

	
