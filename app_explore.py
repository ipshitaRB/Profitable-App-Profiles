from csv import reader

open_apple_file = open('AppleStore.csv', encoding='utf8')
apple_content = reader(open_apple_file)
ios_app_data = list(apple_content)

# open and load google app contents in to a list
open_google_file = open('googleplaystore.csv', encoding='utf8')
android_content = reader(open_google_file)
android_app_data = list(android_content)

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        
explore_data(ios_app_data, 0, 5, True)
explore_data(android_app_data, 0, 5, True)

# locate row with error - category missing 
explore_data(android_app_data, 10473, 10474)

# delete row with error
del android_app_data[10473]

# confirm deletion
explore_data(android_app_data, 10473, 10474)

duplicate_apps = []
unique_apps = []

for app in android_app_data:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
        
print('Number of duplicate apps: ', len(duplicate_apps))

# empty dictionary of app name with highest number of reviews
reviews_max = {}

for app in android_app_data[1:]:
    name = app[0]
    n_reviews = float(app[3])
    if name in reviews_max:
        if reviews_max[name] < n_reviews:
            reviews_max[name] = n_reviews
    else:
        reviews_max[name] = n_reviews
        
print(len(reviews_max))

android_clean = []
already_added = []

for app in android_app_data[1:]:
    name = app[0]
    n_reviews = float(app[3])
    if n_reviews == reviews_max[name] and name not in already_added:
        android_clean.append(app)
        already_added.append(name)

print("Is the number of non duplicate rows 9659 : ", len(android_clean) == 9659)
    
        



