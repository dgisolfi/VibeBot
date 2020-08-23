#!/usr/bin/env python3

"""Image uploader for GroupMe

Given a folder path all images will be uploaded to the groupme image service 

Author(s)
---------
Daniel Gisolfi <Daniel.Gisolfi1@marist.edu>

Usage
-----
    python3 upload.py -h
"""
import os
import argparse

import requests

api_token = os.getenv("API_TOKEN")
api_base_url = "https://image.groupme.com"


def main(path: str):
    urls = {}
    if os.path.isdir(path):
        for file in os.listdir(path):
            if file.split(".")[-1].lower() in ["jpg", "png", "gif", "jpeg"]:
                params = {"token": api_token}
                f = {
                    "file": (file, open(os.path.join(path, file), "rb")),
                    "Content-Type": "image/jpeg",
                }
                # post image to image service
                response = requests.post(
                    f"{api_base_url}/pictures", params=params, files=f
                )
                if response.status_code == 200:
                    print(f"Uploaded image: {file}")
                    urls[file] = response.json()["payload"]
                else:
                    print(
                        f"Unable to upload image: {file}. Response: {response.json()}"
                    )
        print(urls)
    else:
        raise FileNotFoundError(f"The directory: '{path}' does not exist")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image uploader for GroupMe")
    parser.add_argument(
        "path", metavar="P", type=str, help="path to a directory of imgs to be uploaded"
    )

    args = parser.parse_args()
    main(args.path)
