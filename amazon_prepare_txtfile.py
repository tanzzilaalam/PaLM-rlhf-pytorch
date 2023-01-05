import csv
import math

# prepare amazon review csv data and write as txt:

# 1. https://www.kaggle.com/datasets/yasserh/amazon-product-reviews-dataset

with open("try/amazon-product-reviews-dataset/archive/7817_1.csv", "r") as infile, open(
    "try/merged_data/merge.txt", "w"
) as outfile:
    reader = csv.DictReader(infile, delimiter=",")

    [
        outfile.write(
            "\n\n"
            + row.get("name")
            + "\n"
            + row.get("reviews.title")
            + "\n"
            + row.get("reviews.text")
        )
        for row in reader
        if (row.get("name") and row.get("reviews.title") and row.get("reviews.text"))
    ]

print("preprocessing of amazon-product-reviews-dataset is done.")
# 2. https://www.kaggle.com/datasets/kritanjalijain/amazon-reviews

# importing python package

import os
import glob
import pandas as pd

path = "try/amazon_reviews/archive/"
extension = 'csv'

oldpwd = os.getcwd()
os.chdir(path)
csv_filesList = glob.glob(f'*.{extension}')
os.chdir(oldpwd)


    
for csvfile in csv_filesList:

    # read contents of csv file
    file = pd.read_csv(path + csvfile)

    # adding header\
    headerList = ['id', 'reviews.title', 'reviews.text']

    # converting data frame to csv
    file.to_csv(path + "edited_" + csvfile, header=headerList, index=False)


    with open(path + "edited_" + csvfile, "r") as infile, open(
        "try/merged_data/merge.txt", "a"
    ) as outfile:
        reader = csv.DictReader(infile, delimiter=",")

        [
            outfile.write(
                "\n\n"
                + row.get("reviews.title")
                + "\n"
                + row.get("reviews.text")
            )
            for row in reader
            if (row.get("reviews.title") and row.get("reviews.text"))
        ]

print("preprocessing of amazon-reviews is done.")

# 3. https://www.kaggle.com/datasets/grikomsn/amazon-cell-phones-reviews

with open("try/amazon_cell_phone reviews/archive/20191226-reviews.csv", "r") as infile, open(
    "try/merged_data/merge.txt", "a"
) as outfile:
    reader = csv.DictReader(infile, delimiter=",")

    [
        outfile.write(
            "\n\n"
            + row.get("title")
            + "\n"
            + row.get("body")
        )
        for row in reader
        if (row.get("title") and row.get("body"))
    ]

print("preprocessing of amazon-cell-phones-reviews is done.")

# 4. https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products

import os
import glob

path = "try/consumer_reviews_of_amazon_products/archive/"
extension = 'csv'

oldpwd = os.getcwd()
os.chdir(path)
csv_filesList = glob.glob(f'*.{extension}')
os.chdir(oldpwd)


for csvfile in csv_filesList:

    with open(path + csvfile, "r") as infile, open(
        "try/merged_data/merge.txt", "a"
    ) as outfile:
        reader = csv.DictReader(infile, delimiter=",")

        [
            outfile.write(
                "\n\n"
                + row.get("name")
                + "\n"
                + row.get("reviews.title")
                + ". "
                + row.get("reviews.text")
            )
            for row in reader
            if (row.get("name") and row.get("reviews.title") and row.get("reviews.text"))
        ]

print("preprocessing of consumer-reviews-of-amazon-products is done.")