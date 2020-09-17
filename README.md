# vector-shared-codes
Here lies Anki Vector's shared codes.


## Hourly Alarm Installation

Navigate through the directory, then type in the terminal
`chmod +x hourly-alarm.py`

Once done, do the next steps and save.
```
crontab -e
```
This will set to execute the python script every hour
```
0 * * * * cd vector_project/vector-shared-codes/hourly-alarm/ && /usr/bin/python3 hourly-alarm.py >> /var/tmp/hourly.log
```
