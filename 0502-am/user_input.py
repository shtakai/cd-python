# create var called greeting that holds the val of string
greeting = "Hello ninja!"
print greeting

print 'what is your name?'
name = raw_input()
print "how old are you"
age = input()
'''
check
        how old are you
        a
        Traceback (most recent call last):
          File "user_input.py", line 8, in <module>
            age = input()
          File "<string>", line 1, in <module>
        NameError: name 'a' is not defined
'''

print "your name is", name
print "you are", age, "years old"

# comment
'''
 comment osashimi tabetai naa
'''

raw_input("\n\nPress the enter key to exit")
