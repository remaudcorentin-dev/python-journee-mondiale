# python-journee-mondiale
##### v0.1

Very useful Python API to get the World Day(s)  
(French version)

### Installation :
`pip install python-journee-mondiale`  

### Requirements :
`python >= 3.4`  
`beautifulsoup4 >= 4.6`  

### Usage / Example :

```python
from journeemondiale import JourneeMondiale

JourneeMondiale.get()  # Will use the current date
# ["Journée Mondiale de ..."]

JourneeMondiale.get("26-04")  # Or use a date format 'dd-mm'
# ["Journée Mondiale de ...", "Journée Mondiale du ..."]
```  

Life is fun :)  

Refs: https://www.journee-mondiale.com/  

###### Support / Contact : remaudcorentin.dev@gmail.com

