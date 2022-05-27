#!/usr/bin/env python3

__author__ = "triboulet"

array_1 = [123,456,789,987,654,321]
array_2 = [92,29,380,2,497,296]
count = 2147483647

while(True):
    if(count % array_1[0] == array_2[0]):
        ## print("worked on 0th value")
        if(count % array_1[1] == array_2[1]):
            #print("worked on 1st value", count)
            if(count % array_1[2] == array_2[2]):
                #print("worked on 2nd value", count)
                if(count % array_1[3] == array_2[3]):
                    #print("worked on 3rd value", count)
                    if(count % array_1[4] == array_2[4]):
                        #print("worked on 4th value", count)
                        if(count % array_1[5] == array_2[5]):
                            print("SOLVED:")
                            print(count)
                            #quit()

    count += 1
