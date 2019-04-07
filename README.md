# Grofers-Assignment
This repository provides the backend and frontend of the sample app to store and modify and view keyvalue pair and subscribe to realtime changes.<br/>
To deploy this code easily use docker. If not already installed then get it installed from snap using the following command<br/>
```
sudo snap install docker
```
After installing clone this repository and navigate to backend foler at /Backend using command<br/>
```
cd Grofers-Assignment/Backend
```
Create and enable docker container using the following command<br/>
```
sudo docker build -t grofers .
sudo docker run --name grofers-api -p 8000:8000 -d grofers
```
This will enable the API at the port 8000 of the host.<br/>
Install the python from [Python.org](https://python.org)<br/>
Navigate to frontend Repository and install dependency using the following command
```
cd ..
cd Frontend-CLI
pip install -r requirements.txt
```
Use the command as per the following instruction:<br/>
1. To get the value of a key use
```
python store.py get <key>
```
2. To add or update the value of a key use
```
python store.py put <key> <value>

```
3. To monitor realtime changes to the key values start the following in separate console
```
python store.py watch
```
Any queries must be asked at admin@nikhilkumar.cf
