# Simple_Twitch_IRC

# Running
Use a virtual environment and pip install the requirements from requirements.txt


create an oauth code on twitch and then create a config.py file in the src/ dir
the file should look like this: 

```
CONFIG = {
        "BOT_USERNAME":"<username>",
        "OAUTH_TOKEN": "oauth:<oauth code here>
}
```

dont include the '<' '>'
