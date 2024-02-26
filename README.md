# save-retrieve-Program

-Clear instructions for how to programmatically REQUEST data from the microservice you implemented. Include an example call.

Ok so to request data from the microservice, all you have to do is give it a very long string separated by commas. Specifically you need to have a long string separated by commas twice to have three pieces of information. num1 = "retrieve/TifaandCloud.png,TifaandCloud.png,retrieve" This is an example of what you need to send. It will then be split into three pieces of information at specified commas. The retrieve/ file name is the relative path to store the already saved file in the mongodb database to the retrieve folder located in the same place as the microservice program. The name of the file in the second split is also necessary in order to query the mongodb database to find the correct file metadata and the chunks associated with it. It will then allow you to write the file to the retrieve folder. The last split is the retrieve which is also necessary in order to activate the if else statement. If it is retrieve, then you are retrieving file, if it is something else ie save, then you are saving it. 

"save,ff7_rebirth_party.jpg,save"
to save you use that example string. The save in the first split and the save in the third split will allow the program to know that you want to save the name of the file. 

Lastly, you just need to connect to the correct host name and port number. host = socket.gethostname()
port = 7245 use that to connect. Then lastly, once you have the correct string in your function to make the call, just call the name of the function and it will do the work for you. 

So in example, retrievefunction():
insert string of what you want to do with correct commas.
then use retrievefunction() to call it and the microservice will do the work for you! That's it you got it!


-Clear instructions for how to programmatically RECEIVE data from the microservice you implemented.

You don't have to receive any data from the microservice. All you got to do is send the request data to the microservice and you got something working! The microservice will do the work for you! All you have to do is call the correct function and make sure the correct function has the right string as mentioned above! 

-UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your partner (and your grader) will understand

The UML diagram is saved in the github as uml diagram(1).png!
