__author__ = 'marek'
from sys import argv

script, user_name, age = argv

prompt = 'Tell me! '

print "Hi %s. So you say you're %d. I'm the %s script and I am a newborn." % \
      (user_name, int(age), script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)