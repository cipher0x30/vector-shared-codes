# vector-shared-codes
Here lies Anki Vector's shared codes.


## Hourly Alarm Installation

Navigate through the directory, then type in the terminal
`chmod +x hourly-alarm.py`

Once done, type the commands below.
```
crontab -e
```
This will set to execute the python script every hour
```
0 * * * * /usr/bin/python3 /root/vector_project/vector-shared-codes/hourly-alarm/hourly-alarm.py
```
