import requests,json

def get_lab_data(lab_id):
    url = f"https://www.marham.pk/api/lab/tests-optimized?lab_id={lab_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        try:
            data = response.json()
            return data
        except ValueError:
            print(f"Error: Received invalid JSON for lab ID {lab_id}")
            return None
    else:
        print(f"Error: Unable to fetch data for lab ID {lab_id}")
        return None

def get_top_labs(lab_ids):
    top_labs = []
    for lab_id in lab_ids:
        print(f"Fetching data for Lab ID: {lab_id}")
        data = get_lab_data(lab_id)
        if data:
            top_labs.append({"lab_id": lab_id, "data": data})
        if len(top_labs) >= 10:
            break
    return top_labs

lab_ids_to_try = range(1, 21)

top_10_labs = get_top_labs(lab_ids_to_try)

with open('data_more','w')as f:
    json.dump(top_10_labs,f,ensure_ascii=False,indent=4)