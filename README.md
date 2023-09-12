# Devpost link for more info:
https://devpost.com/software/ecosorter-4yqt9b

# HackDuke2023
A device for the Environmental Track in the Hackathon at Duke. Our device uses a trained ML model to classify the category of garbage as either recycling, compost, or e-waste. It flips the servo motor to dispose of the waste as appropriate.

# Inspiration
In a world growing increasingly conscious about its environmental footprint, we were driven to conceive a solution that embodies innovation and sustainability at its core. Drawing inspiration from the urgent need to streamline waste management and recycling procedures, our concept for a smart garbage bin germinated. We were inspired by the potential of integrating technology into daily life, not just to add convenience but to cultivate a positive impact on the environment by fostering responsible waste disposal habits.

# What it does
Our project, now known as "EcoSorter", is a smart garbage bin that revolutionizes the concept of waste disposal and recycling. It harnesses the power of a webcam to identify and segregate waste items accurately. Once an item is deposited into the bin, the webcam identifies the nature of the waste — be it recyclable, compostable, or batteries. If a battery is detected, the lid would not open in any direction, as batteries are prohibited in the bin. Leveraging a Python script running on a Raspberry Pi, it then automatically tilts the lid to guide the waste into the appropriate compartment, ensuring an efficient sorting process that helps in recycling and reducing waste contamination. Moreover, it contributes to a cleaner and more sustainable environment by encouraging people to dispose of waste responsibly.

# How we built it
The heart of EcoSorter lies in the integration of hardware and software components working in harmony. The primary hardware components include a webcam and a servo motor, both connected to a Raspberry Pi. The webcam serves as the eye of the system, capturing images of the waste items. The Raspberry Pi processes these images using a Python script that incorporates machine learning algorithms for object recognition.

We developed a Python script to control the servo motor, which in turn manipulates the lid of the bin to tilt towards the appropriate compartment based on the identified waste type. This script is executed in real-time on the Raspberry Pi, making the process seamless and efficient. Additionally, we incorporated features to log the type and quantity of waste being sorted, fostering a data-driven approach to waste management.

# Challenges we ran into
Throughout the development phase, we encountered several challenges. The first hurdle was achieving accurate recognition of various types of waste materials through the webcam, which required us to train our system extensively with diverse datasets. Balancing the servo motor's precision and speed to ensure a smooth yet quick operation of the tilting lid was another technical challenge we navigated. Additionally, we faced hurdles in integrating the various hardware components and ensuring they worked cohesively to deliver a seamless user experience.

# Accomplishments that we're proud of
We are immensely proud of developing a solution that not only incorporates cutting-edge technology but also contributes to a more sustainable future. Successfully training our Python script to identify and segregate waste with high accuracy marks a significant milestone in our journey. Moreover, we managed to engineer a mechanism where the servo motor efficiently and reliably operates the bin lid, thereby bringing our vision of an automated sorting garbage bin to life.

Creating a prototype that is not only functional but also potentially scalable to a commercial level stands as a testimony to our team's synergy and the relentless effort put into this project.

# What we learned
Throughout this project, we gained valuable insights into the intersection of technology and sustainability. We learned the intricacies of combining hardware components like Raspberry Pi and servo motors with software elements to create a cohesive system. The experience also honed our skills in Python programming and machine learning, enabling us to develop an intelligent waste sorting system. Beyond the technical aspects, we understood the critical role of innovation in driving environmental conservation, thereby making a positive difference in the world.

# What's next for EcoSorter
The journey for EcoSorter doesn't end here. Looking forward, we plan to enhance its capabilities by incorporating more sophisticated machine learning algorithms for improved accuracy and efficiency in waste sorting. We envision developing a companion app that can provide users with insights into their waste disposal habits, encouraging a more conscious and sustainable lifestyle. Furthermore, we aim to collaborate with local governments and organizations to potentially integrate EcoSorter into communities, playing a vital role in fostering a cleaner and greener environment.
