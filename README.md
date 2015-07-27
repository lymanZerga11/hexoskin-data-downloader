# Python Scripts for Hexoskin Data Download and Graphing #

Simple python scripts for getting live data graphs as wells as raw data sets directly

### What is this repository for? ###

* Direct download of Hexoskin Data (Timestamp","Heart Rate","Breathing Rate","Minute Ventilation","Cadence","Activity") by simply running the Python script [lastmodof5datatypes.py](https://bitbucket.org/jacob_sunny/hexoskin-data-downloader/src/43fcfb1b15e71fbabb6b15bf423ea12b87b4be98/lastmodof5datatypes.py?at=master) which saves the data into separate .csv files for separate record IDs. Also creates a file lastmod.p that keeps track of record IDs previously synced.

        Sample CSV File

        Timestamp,Heart Rate,Breathing Rate,Minute Ventilation,Cadence,Activity
        367106360273,70,40,4395.679999999999,0,0.01953125

* Direct download of Hexoskin ECG Data by simply running the Python script [ecgwithoutlastmod.py](https://bitbucket.org/jacob_sunny/hexoskin-data-downloader/src/25e627c7e399592e7afb23ddf4a2fa9f47f7a383/ecgwithoutlastmod.py?at=master) which saves the data into separate .csv files for separate record IDs.

        Sample CSV File

        367842875916,1307
        367842875921,1328
        367842875926,1340

* View static graphs of your choice of datatype using [staticallchoicesgraph.py](https://bitbucket.org/jacob_sunny/hexoskin-data-downloader/src/43fcfb1b15e71fbabb6b15bf423ea12b87b4be98/staticallchoicesgraph.py?at=master) (requires installation of files in the "Requirements" folder in the repository). Sample graph not based on live data but using the Python Graph library is provided at this [link](http://ibin.co/2A5XZVcRXgc5)

* View live graph of Heart Rate on an HTML file using [pubnubtograph.html](https://bitbucket.org/jacob_sunny/hexoskin-data-downloader/src/43fcfb1b15e71fbabb6b15bf423ea12b87b4be98/pubnubtograph.html?at=master) and [pytopubnub.py](https://bitbucket.org/jacob_sunny/hexoskin-data-downloader/src/43fcfb1b15e71fbabb6b15bf423ea12b87b4be98/pytopubnub.py?at=master) script (can be run on Heroku)

![Alt text](http://ibin.co/2A5Vg8elQYgx "Sample Graph")

### How do I get set up? ###

* For [staticallchoicesgraph.py](https://bitbucket.org/jacob_sunny/hexoskin-data-downloader/src/43fcfb1b15e71fbabb6b15bf423ea12b87b4be98/staticallchoicesgraph.py?at=master) installation of the files in the "Requirements" folder in the order specified.
* IMPORTANT: Current settings in all scripts are for downloading data for a specific Hexoskin. To change it to your Hexoskin, change the header variable in the beginning of every Python script to your [API keys](https://api.hexoskin.com/docs/index.html#api-keys-and-oauth-requests) or Basic Key
* Current TIMESTAMP format is adapted from the original Hexoskin [TIMESTAMP Format](https://api.hexoskin.com/docs/index.html#hexotimestamp)
* Basic Key (used in the Python Scripts) can be obtained from the header of a response obtained from a normal Hexoskin API call or can be replaced with the [API Keys](https://api.hexoskin.com/docs/index.html#api-keys-and-oauth-requests)

                headers={'Authorization':'Basic Y3Zlbm9idXJpKzJAZ21haWwuY29tOkhleG9za2lu'}
                
* Live graphing on HTML is implemented through [Pubnub Live Data Stream API](http://www.pubnub.com/). ( Requires pip install Pubnub before running Python script )

### Who do I talk to? ###

* Jacob Sunny (jacobsunny95@gmail.com)
* Other community