We open the program in a console and we’re presented with the challenge:
 
![image](https://user-images.githubusercontent.com/22229087/208213055-f9782c37-3942-4bb8-8d2b-dfbc2dffbe84.png)


And if we enter the wrong key we get an error!
 
![image](https://user-images.githubusercontent.com/22229087/208213056-1a27f31d-26a2-4d1a-be95-699de450315c.png)


Lets open the program in a debugger and see if we learn anything. I’m going to use x64dbg.

We can probably expect to find the key sometime after the “Enter the secret key:” string is referenced, so it might be a good idea to search for that.
 
 ![image](https://user-images.githubusercontent.com/22229087/208213064-e15995ce-c4da-4e10-aac0-dfee056ab700.png)
 ![image](https://user-images.githubusercontent.com/22229087/208213069-78334ff4-8678-496e-933a-87da8c8b39e4.png)



And if we look around memory we see that the string we want is nearby!
“You key was correct!”
 
 ![image](https://user-images.githubusercontent.com/22229087/208213076-be003828-cfa3-402d-8009-9503874afa56.png)


Looking at the strings around this we see an interesting set of strings here:
 
![image](https://user-images.githubusercontent.com/22229087/208213078-816ddec3-3b74-4133-82da-0b1c4ce330c9.png)


Lets set some break points and see if we find anything interesting. After some careful stepping we find an interesting string…
 
 ![image](https://user-images.githubusercontent.com/22229087/208213084-5781e97a-9883-4122-a906-b7c3e2d3ea26.png)


We test that string on our binary and find that it works!

![image](https://user-images.githubusercontent.com/22229087/208213088-a8c07cb8-5899-46e6-8ec1-de20279b1daa.png)

 