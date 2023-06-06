# Zoom Attendance 

This repository solution to the problem of taking attendance in Zoom. It is a simple Python script that uses the Zoom API to get the list of participants in a meeting and then writes the list to a Google Sheet.

# How to use it

1. Clone this repository
```bash
> git clone https://github.com/jaywyawhare/Zoom-Attendance.git
```

2. Install the requirements
```bash
> pip3 install -r requirements.txt
```

3. Add environment variables 

    a. Create a file called `.env` in the root directory of the project

    b. Get your google service account credentials and add them to the root directory of the project. Name the file `credentials.json`

    c. Add the following environment variables t the file
    ```txt
    ZOOM_API_KEY=YOUR_ZOOM_API_KEY
    ZOOM_API_SECRET=YOUR_ZOOM_API_SECRET
    ```
        


4. Run the script
   
    a. First run the script in gsheet folder
    ```bash
    > python3 gsheet/main.py
    ```
    b. Then run the main.py script 
    ```bash
    > python3 main.py
    ```

