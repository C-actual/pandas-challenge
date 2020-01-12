# Notes for Pandas HW since Jupyter Notebook was having issues auto saving---
#For Heroes of Pymoli section: 

#ln[1]
# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)
purchase_data.head()

#ln[27]
#player_list = purchase_data["SN"]
#player_list.value_counts()

#solve for player count
player_count = len(purchase_data["SN"].unique())
player_count

#Make it look like solution
headers = ["Player Count"]
player_count_output_df = pd.DataFrame(columns=headers)
new_row = [{"Player Count":player_count}]
player_count_output_df = player_count_output_df.append(new_row, ignore_index=True, sort=False)
player_count_output_df






#ln[37]
#solve for required items
Num_unique_items = len(purchase_data["Item ID"].unique())
Num_unique_items

total_revenue = sum(purchase_data["Price"])
total_revenue

total_transactions = len(purchase_data["Price"])
total_transactions

average_price = total_revenue / total_transactions
average_price

price_of_avg_transaction = purchase_data["Price"].mean()
price_of_avg_transaction #same thing

# This put in to an array with a new row for each item
#stats_dict = [{"Number of Unique Items" : Num_unique_items},
#             {"Average Price" : average_price},
#             {"Number of Purchases" : total_transactions},
#              {"Total Revenue" : total_revenue}]
#stats_dict_df = pd.DataFrame(stats_dict)
#stats_dict_df


#put into single line array to match solution output
headers = ["Number of Unique Items","Average Price","Number of Transactions","Total Revenue"]
stats_df = pd.DataFrame(columns=headers)

new_row = [{"Number of Unique Items": Num_unique_items,"Average Price":average_price,"Number of Transactions": total_transactions,"Total Revenue":total_revenue}]
stats_df = stats_df.append(new_row, ignore_index=True, sort=False)
stats_df



#ln[64]
#Count calc:
count_dict = purchase_data["Gender"].value_counts()
count_df = pd.DataFrame(count_dict)
count_df = count_df.rename(columns = {"Gender": "Count"})


count_df

pct_dict = purchase_data["Gender"].value_counts("percent") # "Percent" is just a filler word-- I think anything not found in the col. will display as a percentage
pct_df = pd.DataFrame(pct_dict)
pct_df = pct_df.rename(columns = {"Gender": "Percent"})
pct_df

output_df = count_df.join(pct_df)
output_df = output_df.rename(columns={"Gender":"Percent"})
output_df = output_df.rename(columns={"Gender":"Percent"})
output_df





# Purchasing Analysis:
#purchase_data.head()

#Female Calcs
f_df = purchase_data.loc[purchase_data["Gender"] == "Female"]
f_df
# Purchase Count
f_purchase_count = len(f_df["Purchase ID"].unique())
f_purchase_count
# Avg. Purhcase Price = 
f_avg_purchase = f_df["Price"].mean()
f_avg_purchase
#Total purchase price
f_tot_purchase = f_df["Price"].sum()
f_tot_purchase
#Avg Total Purchase per Person
f_names = len(f_df["SN"].unique())
f_per_person = f_tot_purchase / f_names
f_per_person

female_dict = [{"Purchase Count": f_purchase_count},
             {"Average Purchase Price": f_avg_purchase},
             {"Total Purchase Value": f_tot_purchase},
             {"Avg Total per Person": f_per_person}]




#Male Calcs
m_df = purchase_data.loc[purchase_data["Gender"] == "Male"]
m_df
# Purchase Count
m_purchase_count = len(m_df["Purchase ID"].unique())
m_purchase_count
# Avg. Purhcase Price = 
m_avg_purchase = m_df["Price"].mean()
m_avg_purchase
#Total purchase price
m_tot_purchase = m_df["Price"].sum()
m_tot_purchase
#Avg Total Purchase per Person
m_names = len(m_df["SN"].unique())
m_per_person = m_tot_purchase / m_names
m_per_person

male_dict = [{"Purchase Count": m_purchase_count},
             {"Average Purchase Price": m_avg_purchase},
             {"Total Purchase Value": m_tot_purchase},
             {"Avg Total per Person": m_per_person}]





#Other Calcs
o_df = purchase_data.loc[purchase_data["Gender"] == "Other / Non-Disclosed"]
# Purchase Count
o_purchase_count = len(o_df["Purchase ID"].unique())
# Avg. Purhcase Price = 
o_avg_purchase = o_df["Price"].mean()
#Total purchase price
o_tot_purchase = o_df["Price"].sum()

#Avg Total Purchase per Person
o_names = len(o_df["SN"].unique())
o_per_person = o_tot_purchase / o_names


other_dict = [{"Purchase Count": o_purchase_count},
             {"Average Purchase Price": o_avg_purchase},
             {"Total Purchase Value": o_tot_purchase},
             {"Avg Total per Person": o_per_person}]








#Create empty datatable
headers = ["Purchase Count","Average Purchase Price","Total Purchase Value", "Avg Total per Person" ]
pa_df = pd.DataFrame(columns=headers)
#Bring in data
pa_df = pa_df.append(male_dict, ignore_index=True, sort=False)
pa_df = pa_df.append(female_dict, ignore_index=True, sort=False)
pa_df = pa_df.append(other_dict, ignore_index=True, sort=False)
pa_df




