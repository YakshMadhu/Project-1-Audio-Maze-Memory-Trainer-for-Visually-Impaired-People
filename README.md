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
- Implement the main menu system with the following options:
     - Start --> entry point for Human mode / AI mode selection
     - Continue --> displays a list of incomplete saved maze sessions
     - Guide --> provides instructions and all available voice commands
     - Shop (planned) --> placeholder for reward-based system
     - Information (planned) --> placeholder for user performance analysis
- Develop a duration-based keypress detection system to navigate the menu
- Integrate audio-guide system (TTS):
     - example, "Welcome", "press any key for x seconds to select this."
- The overall goal is to establish a navigation flow and interaction model

Day 2 - Audio Interaction System

- Integrate core audio libraries:
     - PyAudio --> captures the audio
     - SpeechRecognition --> speech-to-text (STT)
     - pyttsx3 --> text-to-speech (TTS)
- Implement an audio feedback system for instructions and responses
- Develop voice command recognition:
     - Up, Down, Left, Right, Exit
- The overall goal is to establish a gameplay driven by audio interaction       
  

Day 3 - Maze / Path Generation Engine

- Design a maze as a directional sequence abstraction (list-based path)
- Implement a random path generation algorithm using Python's random module
- Ensure paths generated are valid and solvable
- Introduce scaling of paths based on difficulty via variable sequence lengths

Day 4 - Path Structuring & Logic:

- Convert the maze system into a shortest path model for efficient evaluation
- Implement sequence validation algorithm (O(n)) to compare:
     - optimal path vs user input
- Ensure structural integrity for internal data representation for:
     - generated paths
     - user responses 
- Develop the program's accuracy checking mechanism 

Day 5 - Gameplay Interaction & Rhythm:

- Implement AI Mode:
     - system generates and speaks path (TTS)
- Implement Human Mode:
     - user defines a custom path before the execution 
- Develop time-based rhythm engine:
     - randomized delays (1-10 seconds) between two steps
     - beep signals represent time intervals
- Handling step-by-step input processing 

Day 6 (**Levels of difficulty and scoring mechanisms**):

Day 7 (**Final changes**): 
