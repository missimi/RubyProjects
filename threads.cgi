#!/usr/local/bin/ruby
# Name: Lena Zheng
# File: threads.cgi
# Date: 2014-10-30
# URL:  http://hills.ccsf.edu/~lzheng22/cs132a/threads.cgi

#practice the use of threads togenerate 10 different strings, all of which are outputting characters from
#a-Z, each thread in its own color, and having its thread number in the subscript of the character
print "Content-type: text/html","\n\n";



puts "<html><body><h1>"


colors = %w{ 'red' 'orange' 'yellow' 'green' 'blue' 'purple' 'pink' 'brown' 'black' 'grey'}
index = 0
alpha = ("a".."z").to_a + ("A".."Z").to_a
threads = []
letters = ''

10.times do
thread = Thread.new do 
	alpha.each do |i|

	if Thread.current[:num].nil? 
	Thread.current[:num] = index
	index = index.next
	end 
	print "<font color= #{colors[Thread.current[:num]]}>#{i}<sub>#{Thread.current[:num]}</sub></font> "
	$stdout.flush
	sleep (1/24)
end

end
threads << thread
end
threads.each {|t| t.join }

puts "</h1></body></html>"