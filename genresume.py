#!/usr/bin/env python

class_names = [];

text = open('resume.txt', 'r').read()
lines = text.split("\n");

html = '<style>%s</style>' % open('style.css', 'r').read()

html += '<div id="wrapper"><table>'

def handleLine(line):
	global html, class_names
	
	if line.startswith('!'):
		class_names = [s.strip() for s in line[1:].split('\\')]
		return
	
	html += '<tr>'
	
	html += ''.join(['<td class="%s">%s</td>' % (class_names[i], processText(s)) for i, s in enumerate(line.split('\\'))])
	
	html += '</tr>'

def processText(text):
	if text.startswith('#'):
		return '<h1>%s</h1>' % text[1:]
	if text.startswith('> '):
		return '<blockquote>%s</blockquote>' % text[2:]
	return text

for line in lines: handleLine(line)

html += '</table></div>'

print(html)

open('index.html', 'w').write(html)

print('done')