#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:15:28 2019

@author: max
"""
import io
import os
import re

# First, connect to google vision, upload image, and pull data from cloud
os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/semideum_zepodesgan01/PycharmProjects/RxMinder/api/PennApps 2019 RxMinder-49ae1b133ea3.json"

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


def image_processing(image):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        '../{}'.format(image))

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file

    response = client.text_detection(image=image)
    retrieved_texts = response.text_annotations
    document = response.full_text_annotation

    raw_text = document.text.lower().replace('\n', ' ')
    print(raw_text)

    # next, we must parse the data!
    data_to_send = dict()
    # parse dosage
    dosage_re = re.search(
        "take (one|once|two|twice|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9)(.*?)(every morning and evening|every day and night|every morning and night|every day and evening|day|doy|once daily|daily|morning|afternoon|evening|night|bedtime)",
        raw_text)
    if (dosage_re is not None):
        dosage_str = dosage_re.group(0)
        print('dosage string: {}'.format(dosage_str))
        dosage_split = dosage_str.split(' ')
        # dosage string contains two quantities: # of pills and # of times per day to take # of pills

        if dosage_split[1] == 'one' or dosage_split[1] == '1':
            num_pills = 1
        elif dosage_split[1] == 'two' or dosage_split[1] == '2':
            num_pills = 2
        elif dosage_split[1] == 'three' or dosage_split[1] == '3':
            num_pills = 3
        elif dosage_split[1] == 'four' or dosage_split[1] == '4':
            num_pills = 4
        elif dosage_split[1] == 'five' or dosage_split[1] == '5':
            num_pills = 5
        elif dosage_split[1] == 'six' or dosage_split[1] == '6':
            num_pills = 6
        elif dosage_split[1] == 'seven' or dosage_split[1] == '7':
            num_pills = 7
        elif dosage_split[1] == 'eight' or dosage_split[1] == '8':
            num_pills = 8
        elif dosage_split[1] == 'nine' or dosage_split[1] == '9':
            num_pills = 9
        else:
            print('num_pills not found')
            num_pills = 1

        five = ['five times', '5 times', '5x', 'five', '5 tablets', '5 capsules', '5 pills']
        four = ['four times', '4 times', '4x', 'four', 'every 6 hours', 'every six hours', '4 tablets', '4 capsules',
                '4 pills']
        three = ['three times', '3 times', '3x', 'three', 'every 8 hours', 'every eight hours', '3 tablets', '3 capsules',
                 '3 pills']
        twice = ['twice a day', 'twice daily', 'twice', 'two times', '2 times', '2 tablets', '2 capsules', '2 pills',
                 'every morning and evening', 'every day and night', 'every morning and night', 'every day and evening']
        once = ['once a day', 'once daily', 'once', 'daily', 'one time', '1 time', '1 tablet', '1 capsule', '1 pill',
                'every morning', 'every day', 'every afternoon', 'every evening', 'every night', 'every bedtime', 'midday']

        if any(x in dosage_str for x in five):
            num_times = 5;
        elif any(x in dosage_str for x in four):
            num_times = 4;
        elif any(x in dosage_str for x in three):
            num_times = 3;
        elif any(x in dosage_str for x in twice):
            num_times = 2;
        elif any(x in dosage_str for x in once):
            num_times = 1;
        else:
            print('dose num times per day not found')
            num_times = 1

        data_to_send['pills_per_dose'] = num_pills
        data_to_send['doses_per_day'] = num_times

    else:
        print('dosage data not found')
        data_to_send['pills_per_dose'] = None
        data_to_send['doses_per_day'] = None

    # parse quantity in bottle
    qty_re = re.search("(qty|quantity|oty):? \d+", raw_text)
    if (qty_re is not None):
        print('qty string: {}'.format(qty_re.group(0)))
        qty = qty_re.group(0).split(' ')[1]
        data_to_send['total_qty'] = qty
    else:
        print('qty data not found')
        data_to_send['total_qty'] = None

    # parse milligram information
    mg_re = re.search("(\d+ ?mg)", raw_text)
    print(mg_re)
    if (mg_re is not None):
        print('mg string: {}'.format(mg_re.group(0)))
        mg_dose = mg_re.group(0).split(' ')[0]
        data_to_send['num_mg'] = mg_dose
    else:
        print('mg data not found')
        data_to_send['num_mg'] = None

    # parse medication name
    with open('/Users/semideum_zepodesgan01/PycharmProjects/RxMinder/api/medication_names.txt') as f:
        med_names = f.readlines()
        med_names = [x.strip() for x in med_names]

    data_to_send['medication_name'] = None
    for m in med_names:
        if m in raw_text:
            print("medication {} found".format(m))
            data_to_send['medication_name'] = m
            break

    # finally, we have distilled all useful data into this dictionary!! Yay!!!
    print(data_to_send)
    return data_to_send

