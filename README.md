# StrongPasswordGenerator
Status: Production
author: markus kaleton  
email: markus.kaleton@gmail.com  

Description:
Strong password generator that uses mouse to generate a base for an RNG seed, after that it calculates values out of the base and generates
the seed.

Future development:
Calculation to further randomize the users input by throwing it in a algorithmic machine that does calculations and cuts
with bitwise and //, Won't reduce len due to bruteforce reasons :D
Add more security by modifying the seed by replacing numbers, check Counter(seed), low amounts of a number(s)
due  to obvious reasons.

Current Master:
Uses plain 1000-4000 len string as seed, mapped by users mouse input

Maybe:
Photo/facial recognition seed generation with facial structure
