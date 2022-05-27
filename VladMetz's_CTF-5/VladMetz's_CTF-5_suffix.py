#!/usr/bin/env python3

__author__ = "triboulet"

q = []
w = []
e = []
r = []
t = []

def generate_q(a):
    for i in range(85,126):
        a.append(i)

def generate(a):
    for i in range(33,126):
        a.append(i)
print("generating lists")

generate_q(q)
generate(w)
generate(e)
generate(r)
generate(t)

print("generated...")
print("q=", q, end="\n\n")
print("w=", w, end="\n\n")
print("e=", e, end="\n\n")
print("r=", r, end="\n\n")
print("t=", t, end="\n\n")

print("\n\nFiring the ion cannons...\n\n")

old_i = 0
flag = 0
for i in range(0,len(q)-1):
    for j in range(0,len(w)-1):
        for k in range(0,len(e)-1):
            for l in range(0,len(r)-1):
                for m in range(0,len(t)-1):
                    final = e[k]*q[i] + r[l]*w[j] + e[k]*t[m]
                    #if(i > old_i): ## arbitrary if statement, validates program continuing to run
                        #print(final)
                        #old_i += 1
                    if final == 39666:
                        if (flag == 0):
                            print("VALID CASE:\n")
                            flag = 1
                        key = ""
                        key += chr(q[i])
                        key += chr(w[j])
                        key += chr(e[k])
                        key += chr(r[l])
                        key += chr(t[m])
                        print(key, end="\n")
