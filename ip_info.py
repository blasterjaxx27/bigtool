from Config.Util import *
from Config.Config import *
try:
    from json import *
    import requests
except Exception as e:
   ErrorModule(e)

Title("Ip Info")

def ip_info():
    ip = input(f"{color.RED}\n{INPUT} IP Address -> {color.RESET}")
    print(f"{color.RED}{WAIT} Information Recovery..{reset}")
    response = requests.get(f"http://ip-api.com/json/{ip}")
    data = response.json()
    status = data.get("status", "Invalid")
    if status == "fail":
        status = "Invalid"
        ip_adress, country, country_code, region, region_code, city, zip_postal, latitude, longitude, timezone, isp, org, as_number, url_position = "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None", "None"
    else:
        status = "Valid"
        ip_adress = data.get("query", "None")
        country = data.get("country", "None")
        country_code = data.get("countryCode", "None")
        region = data.get("regionName", "None")
        region_code = data.get("region", "None")
        city = data.get("city", "None")
        zip_postal = data.get("zip", "None")
        latitude = data.get("lat", "None")
        longitude = data.get("lon", "None")
        timezone = data.get("timezone", "None")
        isp = data.get("isp", "None")
        org = data.get("org", "None")
        as_number = data.get("as", "None")
        url_position = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

    print(f"""
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} IP Address : {color.WHITE}{ip_adress}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Status     : {color.WHITE}{status}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Country    : {color.WHITE}{country} ({country_code}){color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Region     : {color.WHITE}{region} ({region_code}){color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Zip        : {color.WHITE}{zip_postal}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} City       : {color.WHITE}{city}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Latitude   : {color.WHITE}{latitude}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Longitude  : {color.WHITE}{longitude}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Timezone   : {color.WHITE}{timezone}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} ISP        : {color.WHITE}{isp}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} Org        : {color.WHITE}{org}{color.RED}
{color.WHITE}[{color.RED}+{color.WHITE}]{color.RED} AS         : {color.WHITE}{as_number}{color.RED}
{color.RESET}""")
    try:
        BrowserPrivate(site=url_position, title=f"Ip Localisation ({latitude}, {longitude})", search_bar=False)
    except:
        pass
    Continue()
    Reset()

def main():
    while True:
        Title("Ip Info")
        ip_info()
        print("\nPress Enter to return to menu")
        input()
        os.system("python bigtool.py")

if __name__ == "__main__":
    main()
