# Reliable Geocoding Proxy

**Deployment**

* Install required python library: `pip install requests flask-restful`
* Add your API keys to credentials.json (see credentials_sample.json as an example)
* Run the proxy `python server.py`
* By default the API is available at `http://localhost:5000/geocode`

*Note*: The proxy was developed and tested using Python 2.7.

**Command Line Interface**
```
usage: server.py [-h] [--host HOST] [--port PORT] [--debug DEBUG]

Reliable Geocoding Proxy Server.

optional arguments:
  -h, --help     show this help message and exit
  --host HOST    the host ip address to listen on
  --port PORT    the port to listen on
  --debug DEBUG  debug mode
```

**Reliable Geocoding API**
----
  This API takes a query (e.g. an address) and tries to resolve the latitude/longitude. 
  
  Two third party geoding API are use (Here and Google) to obtain results more reliably. 
  If the primary provider reports an error or did not find a result, 
  the backup provider will be used. 
  

* **URL**

  /geocode?query=[string]

* **Method:**

  `GET`

*  **URL Params**

   **Required:**

   `query=[string]`

* **Data Params**

  None

* **Success Response:**
  
  If a location was found:
  
    **Code:** 200 <br />
    **Content:** `{"lat": 49.26039, "lng": -123.11336}`
  
  Otherwise:
  
    **Code:** 200 <br />
    **Content:** `{}`
  
* **Error Response:**

  * **Code:** 500 INTERNAL SERVER ERROR <br />    

* **Sample Call:**

   `curl -X GET http://127.0.0.1:5000/geocode?query=vancouver,bc`
   
   `{"lat": 49.26039, "lng": -123.11336}`

