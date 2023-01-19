
note : after 500 stars i will login using phone number support in this repo (open source)
       i.e mutlipul users can use one instance of the bot without invite link 


srb is a https://github.com/vasusen-code/SaveRestrictedContentBot fork





with 

bug fixes 

working batch upto 1000

reanme support while saving from pvt chats

save from forword restricted bot


pyrogram 2.0

/stats

/speedtest for admins

quee supoort 

for more details check the code


    API_ID
    API_HASH
    SESSION   - pv2  from https://replit.com/@SpEcHiDe/GenerateStringSession
    BOT_TOKEN
    AUTH - Owner user id
    FORCESUB - Public channel username without '@'. Don't forget to add bot in channel as administrator.




deply using docker (heroku , railway , render , etc)



Deploy on `VPS`

Easy Method:

- Intall docker-compose
- Fill in the variables in docker-compose.yml file using your favorite text editor or nano 
- Start the container 

```
sudo apt install docker-compose -y
nano docker-compose.yml
sudo docker-compose up --build
```

The hard Way:

- Fill vars in your fork in [this](https://github.com/vasusen-code/SaveRestrictedContentBot/blob/master/main/__init__.py) file as shown in this [picture](https://t.me/MaheshChauhan/36)
- enter all the below commands

```
sudo apt update
sudo apt install ffmpeg git python3-pip
git clone your_repo_link
cd saverestrictedcontentbot 
pip3 install -r requirements.txt
python3 -m main
```

- if you want bot to be running in background then enter `screen -S srcb` before `python3 -m main` 
- after `python3 -m main`, click ctrl+A, ctrl+D
- if you want to stop bot, then enter `screen -r srcb` and click ctrl+A then press K and enter Y.


