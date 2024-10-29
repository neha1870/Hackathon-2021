print("hey , i am your personal  chatbot")
a = input("how can i help you today?? \n")
b = "What are the libraries that were imported"
c = "What were the use of those libraries"
d = "What are the models that this code consists of ?"
e = "Which one is the best model in order to predict the sales ?"
f= "Does this code predict the weekly sales  ?"
g = "What does the graph states ?"
if a == b:
    print("*numb py \n *panda \n*sk learn \n*matplotlib\n*cborl\n")
elif a == c:
    print("*panda - data analysis (tabular data \n *panda - for plotting graphs \n *numb py -advance mathmatics\n ")
elif a == d:
    print(
        "multi linear , ridge , lasso , elastic and polynomial"
    )
elif a == e:
    print( "elastic , cause it had the highest traning ratio")
elif a == f:
    print( "yes it does \n ")
elif a == g :
    print( "here is a link for detailed explanation \n ")

else:
    print(" INVALID .... hey , i am the chatbot ,how can i help you today??")
