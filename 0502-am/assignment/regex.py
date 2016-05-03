import re

def m(match):
    pass
    # if match:
    #     print 'found', match.group()
    # else:
    #     print 'did not found'


m(re.search(r'word:\w\w\w', 'an expample word:cat!'))
m(re.search(r'iii', 'piiig'))
m(re.search(r'igs', 'piiig'))
m(re.search(r'..g', 'piiig'))
m(re.search(r'\d\d\d', 'p123g'))
m(re.search(r'\w\w\w', '@@abcd!!'))
m(re.search(r'pi+', 'piiig'))
m(re.search(r'i+', 'piigiiii'))
m(re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx'))
m(re.search(r'\d\s*\d\s*\d', 'xx12  3xx'))
m(re.search(r'\d\s*\d\s*\d', 'xx123xx'))
m(re.search(r'^b\w+', 'foobar'))
m(re.search(r'b\w+', 'foobar'))
m(re.search(r'\w+@\w+', 'purple alice-b@google.com monkey dishwasher'))
m(re.search(r'[\w.-]+@[\w.-]+','purple alice-b@google.com monkey dishwasher'))


str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
    pass
    # print match.group()
    # print match.group(1)
    # print match.group(2)


str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
for email in emails:
    pass
    # print email

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
# print tuples
for tuple in tuples:
    pass
    # print tuple[0]
    # print tuple[1]

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
