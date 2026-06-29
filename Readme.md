# CrisisMap

## Description
CrisisMap is a platform where users can fill a for to report an emergency, then the departments such as fire brigade, rescue organizations can see the report. OpenAI will score the emergency out of 5, based on the location in the form, coordinates will be extracted, at that coordinates, based on the score, an specific colour pin will be dropped. This is a project for  #horizons.

## Here are some screenshots of my project:

<img width="536" height="401" alt="picture 1 of CrisisMap" src="https://github.com/user-attachments/assets/19cb1d55-7d4e-4289-96b5-87b284fff983" />

<img width="935" height="398" alt="picture 2 of CrisisMap" src="https://github.com/user-attachments/assets/30e90712-d5da-4522-ae40-f34df5f9165d" />

<img width="937" height="292" alt="picture 3 of CrisisMap" src="https://github.com/user-attachments/assets/7a416997-ba28-4486-b8db-32efd2d23e23" />

<img width="959" height="410" alt="picture 4 of CrisisMap" src="https://github.com/user-attachments/assets/a633d85d-02b4-430c-a0ff-ab17c5fb50ee" />

## Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: Python (Flask)
OpenAI Api for Seveirty Score
Nominatim for coordinates



## Motivation
The motivation i got to create this project is from incidents in my city Karachi. Karachi is a vey big city, with population in millions, many incidents happen daily, one incident which i even remember today was the Gul Plaza tragedy in Feb 2026. A shopping centre, hundreds of shops, suddenly captured fire, people called fire department, they came too late. In the inquiry, people get to know that the fire department didnt respond immediately, they simply didnt care. People got jobless, businesses destroyed, main thing, many lives got lost. I thought maybe there were many people stuck inside who have data, no balance, or many inside and outside, who have called, but no reply, why not a platform, managing by the top officials of the city, if they get to know that a fire has been erupted in a flat, they would take action, but fire department, the officers over there don't care. The main motivation was this, Gul Plaza is one tragedy, there are hundreds of other in karachi, some day  fire began, some day xx got stuck under marble. This is why i thought, why not create something which is effective, now the app i created took me 20-21 hours tracked coding, ofcourse it is not as stronger and proffessional to be used in government departments, but this is a concept for an idea, maybe it could save desturction, save the people of my city. Well that is the motivation!

## how it works
Okay so it works and the start is when a user fills a form, now he fills his name, location of the emergency, emergency message. 
Once it is all fullfilled,OpenAI model gives the emergency score out of 5, this is based on the message by the reporter, then the data goes to a route which name is report, that report route is rendered with report.html. 
Now it is not required to see the report by manually opening the report.html, instead dashboard.html is a concept serve for departments, there is a report button which leads to report.html.
There is a chatbot in dashboard, only has frontend, no backend, so no AI, so no reply.
Once the report data comes to report.html, then map.html automatically fetches the coordinates and a score. it drops an specific colour pin to the coordinates. Map will drop red pins at score 5, yellow at score 3 and 4, green at score 1. 
If same location, then new pin will replaced old one.
One thing is necessary to explain, that i have added navigation of map and dahsboard in afterform, also map in dashboard,reports are accessible through report button in dashboard, the concept is that dashboard, report and map are the things which should be not accessible by a normal user, they are for departments, but as I dont have authentication and login, so i have given all the navigation.

## AI vs Non AI
The frontend: HTML/CSS/JS 
the form,
the map rendering,
report display was written by me.
For the backend, I used AI assistance to help implement two specific pieces:
The OpenAI scoring function score() in main.py and the geocoding fallback logic.
I went through several rounds of debugging these including a bug where the AI model was never actually receiving the user's submitted message.
Fixing each one by inquiring about actual output, not just accepting code that looked right. 
The problems_and_debugging file documents that process in detail.

## How to use it
Its very simple to use it, first headover to this link: https://crisismap.umer-pc.hackclub.app/, this is the form. After submitting the form, the user will be leaded to Afterform.html, where user can navigate to dashboard.html, where user can access reports by clicking the report button. Map is accessible by navigating from Afterform.html or dashboard.html.
If anyone wants to visit direct links, then here are these:
https://crisismap.umer-pc.hackclub.app/report.html (reports(If it dosent show reports immediately, make sure to refresh the page)
https://crisismap.umer-pc.hackclub.app/map.html (map)
https://crisismap.umer-pc.hackclub.app/index.html (form)
https://crisismap.umer-pc.hackclub.app/Afterform.html (Afterform)
https://crisismap.umer-pc.hackclub.app/dashboard.html (dashboard)






