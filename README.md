# WRO README FILE 

In the beggining , we would love to introduce ourselves , we ARE the LEGION , the LEGION contains three members , AYHAM , TAHA and MOHAMMED .

These three humble students , directed by their teacher "NOOR GHANNAM" , were able to go through every single obstacle they faced in their way .

# The members 

Each member of THE LEGION have participated in several missions including building the code , collecting the ***** , building and designing the
robot and many other messions ...
1. Taha :
  As he has participated in the previous version of the compitition , he had some important information to share with the other members ,
  he discribed them the instructions of the compition , rules , and what are the things they needed to complete the chalenge .
2. Ayham :
  Armed with the knowledge of robots and their work , and the experience he optained from other compititions , he had special abilities in
  programming and engineering 
3. Mohammed :
   Even that it was his first time in a compitition like this , he had some innovative ideas to share , and he participated in programming
   and designing the robot very much , and he optained some experience .
finally , the director 'teacher Noor Ghannam' , managed to supervise the work of the students and get them the material they need .

# Journey , Problems and Solutions
First we've been told about the competition 1 month before it !! , so we had to start as quick as possible .

We started the work by collecting the material we need to build the robot , we looked for the material and got them ready , and we started 
discussing about rules and the work , but in the second week , each member had it's own curcumstances to deal with and we got delayed for a week , 
but we managed to make up for lost time .

A week later , we started programming each part of the robot to make sure that everything was fine , all the parts were working great , except for 
the color sensor which was an absolute nightmare , it took us three days and evantually it burned so we stoped using it and replaced it with the 
ultrasonics . 

Then some other events came in the way , like 'Eid al-adha' so we got delayed once again .

Thankfully , our team was strong and we easelly made up for lost time .

After we finished programming ,  the only thing left was to design the robot itself , we started thinking about building it from scratch , but we had 
no time , so we bought an RC car module and started placing the material .

The diagram was simple every thing was moving perfectly , until one of the motors burned , we had to check that nothing else was damaged ,
but thankfully , nothing was damaged , and we spent the rist of the day fixing it ...

Some other problems we had in the way is , how are we gonna power up the raspberry pi ? , well we found that we need a power bank with 5v and 
3A minimum to start the raspberry pi , it was a very hard task to find one , but we found it .

overall , despite the hard times we've been through , our team had fun and enjoyed every single moment together .

# Material 

1. 3 Ultrasonics :
   one for the front side
   two for the sides 'left and right'
2. A motor driver l298n :
   used to control the DC motors 'back and forward , left and right'
3. A Raspberry pi camera :
   It's only powered in the second round of the compitition
5. Raspberry pi 4b:
   This is our micro controller , the mind of our robot
6. Breadboard :
   Used for expanding the Raspberry PINS
7. GPIO expander :
   expand the Raspberry PINS into the bread board

# Algorithem 

First , we started by choosing the programming language , we choosed python because all of the LEGION members have worked with it before , and we saw 
that the abilities this language gives us is very wide and easy .

We started by assembling the material codes , motors , ultrasonics , camera , each material had it's own coode , and after we checked every 
part , we began the journey of assembling the code .

The idea was simple , define every part's programm as a function and then we use in the code .

1. avoiding opstacles :
   We use a Raspberry pi camera to recognize the colors red and green , and to give us information about the position of the obstacle so we can avoid it
   easily .
2. Ultrasonics :
   Three ultrasonics is all we need , we put one in the head of the robot to detict the distance in the front to avoid crashing into any thing in the
   field , the two other ultrasonics were put on the both sides left and right , to give us the distances of each side , it's very important because
   we had to use it to know where to go if we passed the middle field and went into a corner , then we know that we have to turn to the side that has the
   bigger distance 
3. Motor driver :
   This part is one of the most important parts , it controls our two DC motors , the back motor and the front motor , the back motor is atached
   to the wheels in the back and it works as an actuator motor and we can easely control it's speed , the front motor is atached with a steering
   system that controls the front wheels .

# An Unexpected Problem

While workin on the project , we bought an RC car , but while working on it , it broke , so we needed to change it , that took us a lot of time and 
money , we managed to search for a better RC body , evantually , we found one , it had an even better steering system and a stronger dc motor , 
but as usual , some problems were found , like the idea of having a small servo that needs to be changed , and many other problems .

# Ending 

At the end , despite the problems and opstacles we faced , our LEGION had fun , and enjoyed every moment of the work procedure , and the most important part is that everyone optained some important experience from this compition ...

# Written by 'THE LEGION'  
