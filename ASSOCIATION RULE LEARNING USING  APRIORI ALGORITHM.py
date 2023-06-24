import pandas as pd
import numpy as np
df = pd.read_csv('/content/drive/MyDrive/MLT Datasets/Shop1.csv')
df.head()
supp_thres = 8/100
N = df.shape[0]
supp_count = N * supp_thres
def create_item_sets(item_lst):
 item_set = []
 for items in item_lst:
 item_set.append(frozenset(items.split(",")))
 return item_set
df_1 = df.copy()
df_1["Item"] = create_item_sets(df_1["Item"])
df_1.head()
def generate_candidates(freq_itemsets):
 candidates = set()
 for itemset1 in freq_itemsets:
 for itemset2 in freq_itemsets:
 # Combine two frequent itemsets only if they differ in exactly
one item
 if len(itemset1.union(itemset2)) == len(itemset1) + 1:
 candidates.add(itemset1.union(itemset2))
 return candidates
# Function to calculate the support of an itemset in the dataset
def calculate_support(itemset, dataset):
 count = 0
 for transaction in dataset:
 if itemset.issubset(transaction):
 count += 1
 return count
def apriori(dataset, min_support):
 # Calculate the support of each item in the dataset
 supports = {}
 for transaction in dataset:
 for item in transaction:
 if item in supports:
 supports[item] += 1
 else:
 supports[item] = 1
 
 # Find frequent itemsets that meet the minimum support threshold
 frequent_itemsets = {}
 for itemset in supports:
 if supports[itemset] >= min_support:
 frequent_itemsets[frozenset([itemset])] = supports[itemset]
print(f"For k = {1}, the candidate set is:")
 print([list(x) for x in frequent_itemsets])
 print("################################################################
###")
 print(f"For k = {1}, the frequency set is:")
 for key, val in frequent_itemsets.items():
 print(list(key), ":", val)
 print("-----------------------------------------------------------")
 
 # Generate frequent itemsets of size k+1 until no more frequent itemset
s can be found
 k = 1
 candidate_itemsets = frequent_itemsets
 while frequent_itemsets:
 # Generate candidate itemsets of size k+1 from frequent itemsets of
size k
 candidates = generate_candidates(frequent_itemsets.keys())
 print(f"For k = {k+1}, the candidate set is:")
 print([list(x) for x in candidates])
 print("############################################################
#######") 
 
 # Calculate the support of each candidate itemset and keep only the
frequent ones
 frequent_itemsets = {}
 for itemset in candidates:
 support = 0
 for transaction in dataset:
 if itemset.issubset(transaction):
 support += 1
 if support >= min_support:
 frequent_itemsets[itemset] = support
 candidate_itemsets[itemset] = support
 
 print(f"For k = {k+1}, the frequency set is:")
 for key, val in frequent_itemsets.items():
 print(list(key), ":", val)
 print("-----------------------------------------------------------
")
 k += 1
 
 return candidate_itemsets
frequent_itemsets = apriori(df_1["Item"], supp_count)
print("Frequent itemsets:")
for itemset, support in frequent_itemsets.items():
 print("{}: {}".format(list(itemset), support))
confidence_df = pd.DataFrame(columns = ["Item1", "Item2", "Confidence"])
min_confidence = 0.5
conf_lst = [(itemset1, itemset2, frequent_itemsets.get(frozenset(itemset1.u
nion(itemset2)))/frequent_itemsets[itemset2])
 for itemset1 in frequent_itemsets.keys() for itemset2 in freque
nt_itemsets.keys()
 if len(itemset1.intersection(itemset2)) == 0 and
 frequent_itemsets.get(frozenset(itemset1.union(itemset2)))
!= None and
 frequent_itemsets.get(frozenset(itemset1.union(itemset2)))
/frequent_itemsets[itemset2] >= 0.5]
confidence_df = pd.DataFrame(conf_lst, columns = ["Item1", "Item2", "Confid
ence"])
confidence_df = pd.DataFrame(columns = ["Item1", "Item2", "Confidence"])
min_confidence = 0.5
for itemset1 in frequent_itemsets.keys():
 for itemset2 in frequent_itemsets.keys():
 if len(itemset1.intersection(itemset2)) == 0:
 combined_support = frequent_itemsets.get(frozenset(itemset1.union(ite
mset2)))
 if combined_support != None:
 curr_confidence = combined_support/frequent_itemsets[itemset2]
 if curr_confidence >= 0.5:
 confidence_df.loc[len(confidence_df)] = [itemset1, itemset2, curr
_confidence]
print(confidence_df)
