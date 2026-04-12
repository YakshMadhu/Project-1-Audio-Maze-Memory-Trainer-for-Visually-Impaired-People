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

**Timeline Draft for the pr(Maximum: 7 day):**

Day 1 - GUI & Main Menu 

- Built the initial GUI window based on Tkinter (1920 x 1080)
- Implement the main menu system with the follow options:
     - Start --> entry point for Human mode / AI mode selection
     - Continue --> displays list of incompleted saved maze sessions
     - Guide --> provides instructions and all available voice commands
     - Shop (planned) --> placeholder for reward-based system
     - Information (planned) --> placeholder for user performance analysis
- Develop duration-based keypress detection system to navigate the menu
- Integrate audio-guide system (TTS):
     - example, "Welcome", "press any key for x seconds to select this"
- Overall goal is to establish a navigation flow and interaction model

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
