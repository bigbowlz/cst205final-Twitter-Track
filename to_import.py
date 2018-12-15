import usercomments as text

#to get the list of user comments(strings), you need to do as follow:
text_to_analyze = text.get_comments("skin", "roe_tencent", "2018-10-00")
#and text_to_analyze will be a list of strings/user comments
#text.get_comments takes 3 parameters: 1. keyword 2. the account you are tracking 3. the start date you wanna track from.
#if you input the wrong type of parameters when calling text.get_comments, the program will ask you to manually imput answers.

#the following tests the items in text_to_analyze
for i in text_to_analyze:
    print (i+"\n")

