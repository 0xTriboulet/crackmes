Opening the program in a console windows presents us with the challenge.

![image](https://user-images.githubusercontent.com/22229087/208202557-2f7aa8aa-6ee9-4269-8937-1d3d78c2be73.png)


If we try to guess the password with common passwords we get an error message :c
 
 ![image](https://user-images.githubusercontent.com/22229087/208202580-18e60755-2e95-4be5-8cde-f5ad7b885472.png)

 
Let's try to dump the strings! We know that most CTF flags use XXX{YYY} format, so lets narrow our search by looking for strings that include "{"
 
 ![image](https://user-images.githubusercontent.com/22229087/208202609-82cd5212-54d5-414f-a269-bae9b42247c0.png)
 
 
We see that the secret we found works!  

![image](https://user-images.githubusercontent.com/22229087/208202635-98ad026b-dbe9-45cf-8e36-bac59ad3f80e.png)
