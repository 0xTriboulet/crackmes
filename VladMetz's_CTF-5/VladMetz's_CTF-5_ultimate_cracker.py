#!/usr/bin/env python3

__author__ = "triboulet"

valid_suffix = ["Uyv||","U|vy|","Vyv|{","V|vy{","Wvzv|","Wyv|z","W|vyz","Xvzv{","Xyv|y","X|vyy","Yrzx|","Yvzvz","Yxzr|","Yyv|x","Y|vyx","Zrzx{","Zvzvy","Zxzr{","Zyv|w","Z|vyw","[q{u|","[rzxz","[u{q|","[vzvx","[xzrz","[yv|v","[|vyv"]

max_num = 0
flag = 0
for zero in range(126,33,-1):
    for one in range(126,33,-1):
        for two in range(126,33,-1):
            for three in range(126,33,-1):
                for four in range(126,33,-1):
                    for five in range(126,33,-1):
                        xmm0 = zero
                        xmm1 = five
                        xmm2 = (five * one)-((four>>1)**2)
                        xmm3 = four >> 1
                        xmm4 = three >> 1
                        xmm5 = two / 2
                        xmm1 = xmm1 * xmm5
                        xmm2 = xmm2 * xmm0
                        xmm0 = xmm3
                        xmm0 = xmm0 * xmm4
                        xmm3 = xmm3 * xmm5
                        xmm1 = xmm1 - xmm0
                        xmm0 = one
                        xmm1 = xmm1 * xmm5
                        xmm0 = xmm0 * xmm4
                        xmm2 = xmm2 - xmm1
                        xmm3 = xmm3 - xmm0

                        xmm3 = xmm3 * xmm4
                        xmm2 = xmm2 + xmm3
                        xmm0 = xmm2


                        if (xmm2 == 733898.75): ## this is the weirdness types caused by python and C++ managing allocations differently
                            if(flag == 0):
                                print()
                                print("*POSSIBLE* Valid cases found:")
                                flag = 1
                            key = ''
                            key += chr(zero)
                            key += chr(one)
                            key += chr(two)
                            key += chr(three)
                            key += chr(four)
                            key += chr(five)                            
                            for i in valid_suffix:
                                print(key+i)
