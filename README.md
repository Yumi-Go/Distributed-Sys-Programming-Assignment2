# Overview
This project involves developing a small-scale distributed system. Using Python and gRPC, develop a text-based word game that is like the popular hang-man game or the Wheel of Fortune TV game show.

# Main Functionality using gRPC
I developed a server component that accepts gRPC connections from a client component. The server component should load a list of phrases from the file “phrases.txt” and for each new game randomly select a phrase. It will then return a string to the client with underscores where the letters would be.

# Extra Feature
I added a feature to the game that improves it, e.g. scores, limit on the number of guesses, the ability to guess the full phrase.
