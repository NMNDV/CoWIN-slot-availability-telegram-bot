import time
import requests
import datetime

def show_states(debug: bool = False):
    
    url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/90.0.4430.212 Safari/537.36"
    }
    state_id_dict = None
    tot_cnts = 20
    while True:
        try:
            lr = requests.get(url, headers=headers)
            finite = lr.json()
            state_id_dict = {}
            for state in finite["states"]:
                if debug:
                    print(state["state_name"] + ": " + str(state["state_id"]))
                state_id_dict[state["state_name"]] = state["state_id"]
            break
        except:
            if debug:
                print("server error trying again")
        tot_cnts -= 1
        if not tot_cnts:
            return None
    return state_id_dict


def show_districts_by_ID(id: int, debug: bool = False):
    if not (1 <= id <= 36 and isinstance(id, int)):
        raise ValueError("Invalid ID")
 
    url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/" + str(id)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/90.0.4430.212 Safari/537.36"
    }

    tot_cnts = 20
    district_id_dict = None
    
    while True:
        try:
            lr = requests.get(url, headers=headers)
            finite = lr.json()
            district_id_dict = {}
            for state in finite["districts"]:
                if debug:
                    print(state["district_name"] + ": " + str(state["district_id"]))
                district_id_dict[state["district_name"]] = state["district_id"]
            break
        except:
            if debug:
                print("server error trying again")
        tot_cnts -= 1
        if not tot_cnts:
            return None
    return district_id_dict


def show_districts_by_state_name(name: str, debug: bool = False):
    
    id = -1
    states_dict = show_states()
    if name.capitalize() in states_dict:
        id = states_dict[name.capitalize()]
    else:
        raise ValueError("Invalid Name")
    
    if not (1 <= id <= 36 and isinstance(id, int)):
        raise ValueError("Invalid ID")
 
    url = "https://cdn-api.co-vin.in/api/v2/"
    url += "admin/location/districts/" + str(id)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/90.0.4430.212 Safari/537.36"
    }

    tot_cnts = 20
    district_id_dict = None
    
    while True:
        try:
            lr = requests.get(url, headers=headers)
            finite = lr.json()
            district_id_dict = {}
            for state in finite["districts"]:
                if debug:
                    print(state["district_name"] + ": " + str(
                        state["district_id"]
                        ))
                district_id_dict[state["district_name"]] = state["district_id"]
            break
        except:
            if debug:
                print("Error message trying again")
            tot_cnts -= 1
            if not tot_cnts:
                return None
    return district_id_dict


if __name__ == "__main__":
    #show_states(debug=True)
    #show_districts_by_ID(11, debug=True)
    show_districts_by_state_name("Gujarat", debug=True)