AI-Assisted Smart Eye Drop Guidance and Dispensing System
# Smarteye_dispenser

An AI-powered automated eye drop dispensing system that detects the user's eye, aligns the eye-drop bottle automatically, and dispenses a controlled dosage with minimal user intervention.


## Overview

The Smart Eye Drop Dispenser is designed to improve the accuracy, safety, and convenience of administering eye drops. The system uses computer vision to detect the user's eye, estimate its position, and guide the dispensing mechanism to the correct location before releasing the prescribed number of drops.

This project combines Artificial Intelligence, Computer Vision, Embedded Systems, and Automation to create a hands-free eye drop delivery solution.


## Problem Statement

Millions of patients experience difficulty administering eye drops correctly due to:

- Poor hand-eye coordination
- Incorrect bottle positioning
- Multiple drops being dispensed unintentionally
- Risk of bottle tip contamination
- Inaccurate dosage
- Medication wastage

The proposed system addresses these issues by automating the alignment and dispensing process.


## Objectives

- Detect the user's eye using computer vision.
- Calculate the eye position in real time.
- Automatically align the eye-drop bottle.
- Detect eye openness before dispensing.
- Dispense the required number of eye drops.
- Improve dosing accuracy and user convenience.


## Features

- Real-time eye detection
- Eye landmark estimation
- Eye center localization
- Blink/Open-eye detection
- Automatic alignment logic
- Controlled eye drop dispensing
- Modular software architecture
- Ready for Raspberry Pi integration


## System Workflow


Start
   │
   ▼
Camera Initialization
   │
   ▼
Eye Detection
   │
   ▼
Eye Center Calculation
   │
   ▼
Eye Open Verification
   │
   ▼
Bottle Presence Check
   │
   ▼
Alignment Calculation
   │
   ▼
Servo Motor Positioning
   │
   ▼
Bottle Tilt
   │
   ▼
Drop Dispensing
   │
   ▼
Return to Home Position


## Technologies Used

Programming Language
- Python

 Computer Vision
- OpenCV
- MediaPipe

AI
- Pretrained MediaPipe Face Mesh

 Hardware
- Raspberry Pi
- Servo Motors
- Camera Module
- Bottle Holder Mechanism
- IR Sensor / Limit Switch (Bottle Detection)
- TOF sensor

