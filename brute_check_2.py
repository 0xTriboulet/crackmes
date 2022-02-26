#!/usr/bin/env python3

__author__ = "triboulet"

def check_viable(pass_list, sum_of_pass): ## manipulates the ones digit of the equation in order to try to get a valid answer
    new_list = pass_list[:]
    out_sum = 0
    sub_num = sum_of_pass - 8254
    if(not(sub_num > 93 or sub_num < 0)):
        new_list[1] -= sub_num
        for i in range(0, len(new_list)):
            out_sum += new_list[i]*i
        if(out_sum == 8254):
            key = ''
            #print("Viable...")
            #print(out_sum)
            for i in new_list:
                key += chr(i)
            #print(new_list)
            print(key, end="\n\n")

def click_down_faster(pass_list): ## just trying to iterate through possibilities faster
    if 33 in pass_list:
        ind = pass_list.index(33)
        pass_list[pass_list.index(33)-1] -= 1
        pass_list[ind] = 126
    else:
        pass_list[-1] -= 93
    return pass_list

def click_down(pass_list):
    if 33 in pass_list:
        ind = pass_list.index(33)
        pass_list[pass_list.index(33)-1] -= 1
        pass_list[ind] = 126
    else:
        pass_list[-1] -= 1
    return pass_list

def reset(pass_list):
    iter_count = len(pass_list) + 1
    pass_list = []
    for i in range(0, iter_count):
        pass_list.append(126)
    # print(len(pass_list))
    return pass_list

sum_of_pass = 0
goal_number = 8254
key = ''
count = 0
pass_chars = [126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126]

## there's definitely a better way to do this, but this is my clunky solution

while(True):
    # print(sum_of_pass)
    # print(pass_chars)
    sum_of_pass = 0
    count += 1
    for i in range(0, len(pass_chars)):
        sum_of_pass += pass_chars[i]*i
    if (sum_of_pass > 9000):
        pass_chars = click_down_faster(pass_chars)
    elif(sum_of_pass > 8254 - (len(pass_chars) * 126)):
        # print("clicking down...")
        if(sum_of_pass < 8380):
            check_viable(pass_chars, sum_of_pass)
        pass_chars = click_down(pass_chars)
    elif(sum_of_pass < 8254 - (len(pass_chars) * 126)):
        print("Resetting...")
        pass_chars = reset(pass_chars)
        print(sum_of_pass)
        print(len(pass_chars))
        print(pass_chars)
        #quit()
    elif(sum_of_pass == 8254):
        key = ''
        print(pass_chars)
        print("\n\nSolved:")
        for i in pass_chars:
            key += chr(i)
        print(key, end="\n\n")
        quit()
    if(count > 1000000):
        print(sum_of_pass)
        print(len(pass_chars))
        print(pass_chars)
        count = 0

