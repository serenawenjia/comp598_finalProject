# Data Collection for COMP598 Final Project

## Table of Contents
- [row_1_70.json](https://github.com/serenawenjia/comp598_finalProject/blob/main/data_collection/row_1_70.json): samples for deciding categories for Sophearah
- [row_351_420.json](https://github.com/serenawenjia/comp598_finalProject/blob/main/data_collection/row_351_420.json): samples for deciding categories for Ran
- [row_701_760.json](https://github.com/serenawenjia/comp598_finalProject/blob/main/data_collection/row_701_760.json): samples for deciding categories for Wenjia
- [extra_sample1.json](https://github.com/serenawenjia/comp598_finalProject/blob/main/data_collection/extra_sample1.json): extra samples in case some samples are NOT about COVID or NOT English for Sophearah
- [extra_sample2.json](https://github.com/serenawenjia/comp598_finalProject/blob/main/data_collection/extra_sample2.json): extra samples in case some samples are NOT about COVID or NOT English for Ran
- [extra_sample3.json](https://github.com/serenawenjia/comp598_finalProject/blob/main/data_collection/extra_sample3.json): extra samples in case some samples are NOT about COVID or NOT English for Wenjia


## Setup

1. Copy `.env.example` to `.env` and fill in Twitter app credentials. You can find them by clicking on the key icon in the [Twitter Developer Portal](https://developer.twitter.com/en/portal/projects-and-apps).
1. Create environment: `python3 -m venv env`
1. Activate environment: `source env/bin/activate`
1. Install dependencies: `pip3 install -r requirements.txt`

## How to Run

1. Activate environment: `source env/bin/activate`
1. To collect data: `python3 search_tweet_<suffix>.py` where `<suffix>` is the version or endpoint used to fetch Twitter data
1. To process data: `python3 processing.py input_json_path [start_row end_row]`