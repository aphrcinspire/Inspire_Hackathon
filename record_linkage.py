# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 16:23:58 2024

@author: LMumelo
"""
import pandas as pd
from recordlinkage.preprocessing import clean

#Load dataset from your directory
facility_df=pd.read_csv("C:\\Users\\lmumelo\\OneDrive - Kemri Wellcome Trust\\Projects\\Inspire_Hackathon\\datasets\\synthetic_facility_v3.csv")
hdss_df=pd.read_csv("C:\\Users\\lmumelo\\OneDrive - Kemri Wellcome Trust\\Projects\\Inspire_Hackathon\\datasets\\synthetic_hdss_v3.csv")

range(len(facility_df))
range(len(hdss_df))

# Assuming you've loaded facility_df and hdss_df
for df in [facility_df, hdss_df]:
    df['firstname_clean'] = clean(df['firstname'], lowercase=True, strip_accents='ascii', remove_brackets=True)
    df['lastname_clean'] = clean(df['lastname'], lowercase=True, strip_accents='ascii', remove_brackets=True)
    df['dob_clean'] = pd.to_datetime(df['dob'], errors='coerce').dt.date

from recordlinkage import Index

indexer = Index()
indexer.block('sex')
candidates = indexer.index(facility_df, hdss_df)


from recordlinkage import Compare

compare = Compare()
compare.string('firstname_clean', 'firstname_clean', method='jarowinkler', threshold=0.85, label='firstname_similarity')
compare.string('lastname_clean', 'lastname_clean', method='jarowinkler', threshold=0.85, label='lastname_similarity')
compare.exact('dob_clean', 'dob_clean', label='dob_match')
compare.exact('nationalid', 'nationalid', label='nationalid_match')


features = compare.compute(candidates, facility_df, hdss_df)
potential_matches = features[(features['firstname_similarity'] > 0.85) & (features['lastname_similarity'] > 0.85) & ((features['dob_match'] == 1) | (features['nationalid_match'] == 1))]


# Assume 'potential_matches' contains the matched indices as a MultiIndex
# Convert the index to a DataFrame if it's not already
matches_df = potential_matches.reset_index()

# Rename columns for clarity
matches_df.rename(columns={'level_0': 'facility_index', 'level_1': 'hdss_index'}, inplace=True)

# Merge the matched records from the facility dataset
matched_records_facility = pd.merge(matches_df, facility_df.reset_index(), left_on='facility_index', right_on='index', how='left')

# Merge the matched records from the HDSS dataset
matched_records_hdss = pd.merge(matches_df, hdss_df.reset_index(), left_on='hdss_index', right_on='index', how='left')

# Select columns to display from both datasets (adjust column names as needed)
columns_to_display = ['firstname', 'lastname', 'dob', 'sex', 'nationalid']
matched_records_display = pd.concat([
    matched_records_facility[columns_to_display + ['visitdate']], # From facility dataset
    matched_records_hdss[columns_to_display + ['hdssid', 'hdsshhid']] # From HDSS dataset
], axis=1)

# Display the matched records
print(matched_records_display.head())
