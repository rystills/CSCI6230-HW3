# Ryan Stillings Cryptography and Network Security I - Homework Assignment 3  
## Dependencies:  
None  
## Writeup:  
There isn't as much to say this time around as the Blum Goldwasser Probabilistic Algorithm ended up making for a fairly short implementation. The only library used for this assignment was math for log calculations (this could have been swapped out with numpy; either one gets the job done). Initially I intended to perform the necessary calculations for the algorithm using binary ints and bitwise operators, but I ultimately found that I was more comfortable and confident in using Python's excellent string manipulation tools instead. The provided main file stores the message as a list of bits, runs it through encryption and then subsequent decryption, and finally prints out each of the results. The encryption itself can be broken down into two chunks; the first chunk calculates values for n,k,h, and t, while the second chunk breaks up m into m_i blocks and calculates ci for each block. A few lines use string splicing to emulate bitwise operations, and so their functionality is explained via comments in the code. The decryption operates similarly, with additional steps calculating x0 from the x_t+1 value generated during the encryption step.  
## Result:  
Calculated Ciphertext = 00100000110011100100  
Please see code for verification