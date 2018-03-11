# Secret Messages

This is the second project in Treehouse Python tech degree.

To use run league_builder.py

## Description

Take a few of the famous ciphers listed and implement 
them in Python so you can quickly encode and decode secret 
messages. 

Each cipher should be created as a Python class and 
each has to expose two methods: encrypt and decrypt. 
Each of these methods should take a single string to be 
encoded or decoded and should return the properly 
encoded or decoded version of the string according 
to the cipher.

My ciphers:
- Affine
- Atbash
- Bifid

## Extra Credit

Implement a one-time pad to secure the cipher.

A one-time pad is an additional input step 
required prior to enc or decrypt a message. As long
as both the sender and receiver use the same pad,
the message itself becomes secure. Without the pad,
the message cannot be recovered.