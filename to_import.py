import usercomments as text

#to get the list of user comments(strings), you need to do as follow:
text_to_analyze = text.get_comments("skin", "@CallofDuty")
#and text_to_analyze will be a list of strings/user comments
#text.get_comments takes 2 parameters, keyword and the account you are tracking.
#if you leave the two parameters empty when calling text.get_comments, the program will ask you to input a keyword and an account.

#the following tests the items in text_to_analyze
for i in text_to_analyze:
    print (i+"\n")

