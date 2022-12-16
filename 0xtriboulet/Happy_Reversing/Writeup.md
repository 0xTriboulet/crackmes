Opening the program in a console windows presents us with the challenge.

![image](https://user-images.githubusercontent.com/22229087/208201948-ad50907a-d380-4cfb-ac12-f859eda02743.png)


If we try to guess the password with common passwords we get an error message :c

![image](https://user-images.githubusercontent.com/22229087/208202055-79c62aba-a3b7-4b64-af5d-b567a83d5d8b.png)


Let's try to dump the strings! We know that most CTF flags use XXX{YYY} format, so lets narrow our search by looking for strings that include "{"

![image](https://user-images.githubusercontent.com/22229087/208202216-199d0dc2-6d39-41f1-ad88-4c58bf6928a4.png)


We see that the secret we found works!
![image](https://user-images.githubusercontent.com/22229087/208202327-ed657e71-36f2-41df-a4e8-408bdee259be.png)
