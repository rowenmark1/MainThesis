import requests

api_address="https://newsapi.org/v2/everything?q=Apple&from=2021-09-09&sortBy=popularity&apiKey=e957f48d45654f47a20f807f1033c1ed"
json_data = requests.get(api_address).json()

ar=[]
def news():
    for i in range(3):
        ar.append("Number "+ str(i+1)+" ," + json_data["articles"][i]["title"]+".")

    return ar



