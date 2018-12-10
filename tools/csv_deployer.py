import csv
import requests
import json
from requests.auth import HTTPBasicAuth

NSO_HOST = 'localhost'
NSO_USERNAME = 'admin'
NSO_PASSWORD = 'admin'

AUTH = requests.auth.HTTPBasicAuth(NSO_USERNAME, NSO_PASSWORD)


def deploy_app(service_name,
               ltm_name,
               vip_ip,
               vip_port,
               node_name,
               node_ip,
               node_port,
               dns_name,
               gtm0_name,
               gtm1_name):

    payload = {
        "app-vip-deployment:app-vip-deployment": [
            {
                "name": service_name,
                "dns_name": dns_name,
                "gtm": [
                    {
                        "device": gtm0_name
                    },
                    {
                        "device": gtm1_name
                    }
                ],
                "ltm": [
                    {
                        "device": ltm_name,
                        "vip_address": vip_ip,
                        "vip_port": vip_port,
                        "nodes": [
                            {
                                "name": node_name,
                                "address": node_ip,
                                "port": node_port,
                            }
                        ]
                    }
                ]
            }
        ]
    }

    # serialize payload
    payload = json.dumps(payload)

    url = "http://{}:8080/api/running/".format(NSO_HOST)
    headers = {
        'Content-Type': "application/vnd.yang.data+json",
        'Accept': "application/vnd.yang.data+json"
    }
    print(payload)
    response = requests.request("POST",
                                url,
                                auth=AUTH,
                                data=payload,
                                headers=headers)
    return response


if __name__ == "__main__":
    with open('input.csv') as csvfile:
        vips = csv.reader(csvfile)
        # This skips the first row of the CSV file (header)
        next(vips)
        for v in vips:
            print(deploy_app(*v))
