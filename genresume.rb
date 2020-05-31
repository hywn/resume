#!/usr/bin/env ruby

text = File.read 'resume.txt'
css  = File.read 'style.css'

lines = text.lines.map(&:strip).filter {|line| not line.empty?}

header, *rest = lines

classes = header[1..-1].split('\\')

trs = rest.map { |line|

	parts = line.split('\\').each_with_index.map { |content, i|

		content.strip!

		content = "<h1>#{$1}</h1>"                 if content.match /#(.+)/
		content = "<blockquote>#{$1}</blockquote>" if content.match /^> (.+)/

		"<td class=\"#{classes[i]}\">#{content}</td>"

	}

	parts = ['<td></td>'] if parts.empty?

	"<tr>#{parts.join ''}</tr>"

}

File.write 'index.html', "<style>#{css}</style><table>#{trs.join ''}</table>"