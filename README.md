# Project-1-Audio-Maze-Memory-Trainer-for-Visually-Impaired-People

**The hypothetical format in which I will write my README.md document:**

-Problem: What's the issue that I'm trying to solve?

-But why?: the impact the solution will have.

-System architecture: how different parts of the system will interact to create a functional solution to the problem I'm addressing. 

-Design decisions: the reason behind choosing certain approaches and how these choices were made during the development (the inner reflection of what was going on in my mind).

-Algorithms and programming techniques: what the system relies on.

-Programmer challenges: The technical problems encountered and how they were solved.

-Demo video: A short video demonstrating the core features of the final output.

-Manual: step-by-step instructions for setting up and running the project locally.

**Timeline (Maximum: 7 days), What to complete each day:**

Day 1 (**GUI window with interactive buttons**):

-A simple 1920x1080 size 
-At start, will display three interactive buttons: Human mode, AI mode, and Guide:
    **Human mode**: User inputs the winning path using the arrow key or via specified voice command ('Left', 'Right', 'Up', 'Down') for simplicity.
    **AI mode**: Depending on the level of difficulty chosen, it will give a random direction leading to a winning path 
    **Guide**: Just talks about instructions, what the voice commands are, etc...
-For GUI window I will use **tkniter**

Day 2 (**Voice interface**):

-This implies that since the users are mainly targeted for visually impaired people, it's better, instead of text, to use voice cues and a program that speaks 
-Another thing it implies is that the program understands the voice commands of the person using it
-To enable this to happen I'm thinking of using three things:
    **For audio capture**: pyaudio
    **for converting speech to text**: speech_recognition
    **for converting text to speech**: pyttsx3
  

Day 3 (**Random maze generator**:

-This part is simply using Python inherent builtins, after initializing **import random**

Day 4 (**Modify the maze generator**):

-

Day 5 (**Refine Maze interactions**):

Day 6 (**Levels of difficulty and scoring mechanisms**):

Day 7 (**Final changes**): 
