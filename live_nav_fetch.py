import requests
import pandas as pd

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        try:
            data = response.json()

            df = pd.DataFrame(data["data"])

            df.to_csv(
                f"data/raw/{name}.csv",
                index=False
            )

            print(f"{name} saved successfully")

        except Exception as e:
            print(f"Error in {name}: {e}")

    else:
        print(f"Failed for {name}. Status Code: {response.status_code}")