# Valid email addresses must follow these rules:

# DONE 		It must have the username@websitename.extension format type.
# DONE 		The username can only contain letters, digits, dashes and underscores.
# DONE 		The website name can only have letters and digits.
# DONE 		The maximum length of the extension is . 
import re

def fun(s):
	# let's try regex
	return re.match('^[\w\-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$', s)