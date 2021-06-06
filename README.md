# Instragram-auto-follow

If you are one of those who hopes from one accout to other constently, this script might help you alot.

As the name suggests you provide list of account names to the script and it will follow them automatically.

## How to use

If you don't have any knowledge of pyhton, don't worry. You will be fine.

- You will need a chromeDriver and chrome browser installed first.

    - For Chrome

        https://www.google.com/chrome/

    - For chromeDriver

        https://chromedriver.chromium.org/downloads

        Download the version same to that of your browser and paste the downloaded exe file in Windows folder inside C drive.


- Clone this project and run

    ``` pip install -r requirements.txt ```

    Ofcourse you will need pip and python installed

- Create a ```.env``` file same as in ``` .env.example ``` and fill your account details

- Open the ``` main.py``` file and fill all the names in the name list:

    ```py
        names = [
            "Charli Brown",
            "Joe Kenway"
        ]

    ```

- Run

    ``` python main.py ```

    and let things happen...



