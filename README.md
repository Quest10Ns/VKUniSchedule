# VKUniSchedule - VK Mini App for University Timetables

VKUniSchedule is a VK Mini App that allows university students to easily access and manage their class schedules directly within the VKontakte platform. The application is built using Python for the backend and React for the frontend, providing a simple and intuitive interface for viewing daily and weekly timetables.

## Features:
- View current and upcoming classes based on your group.
- Responsive design optimized for mobile devices.
- Integration with VK Bridge for seamless user authentication and interaction.
- Backend powered by FastAPI/Flask for secure and fast data retrieval.
- Supports multiple groups and custom timetable updates.

## Technologies Used:
- **Backend**: Python (FastAPI/Flask)???
- **Frontend**: React, VK Bridge
- **Database**:  None
- **Deployment**: None

## How to Run:
1. Clone the repository:
   ```bash
    https://github.com/Vantsev/VKUniSchedule.git
    cd my-app
   
2. Start the local server:
   ```bash
    uvicorn main:app --reload --host 0.0.0.0
    npm start

3. Start the VK server:
   ```bash
   npm run tunnel