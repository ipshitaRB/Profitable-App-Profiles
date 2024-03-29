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

def is_english(input):
    """ check whether a string is in English or not """
    out_of_range_num = 0
    for char in input:
        if ord(char) > 127:
            
            out_of_range_num += 1
    if out_of_range_num > 3:
                return False        
    return True

# Test is_english function
def test_is_english(input):
    statement = " Is '{}' English?"
    outcome = is_english(input)
    print(statement.format(input), outcome)
    
test_is_english("Instagram")
test_is_english('爱奇艺PPS -《欢乐颂2》电视剧热播')
test_is_english('Docs To Go™ Free Office Suite')

ios_english = []
android_english = []

for app in ios_app_data[1:]:
    name = app[2]
    if is_english(name):
        ios_english.append(app)
        
for app in android_clean:
    name = app[0]
    if is_english(name):
        android_english.append(app)
        
explore_data(android_english, 0, 3, True)
print('\n')
explore_data(ios_english, 0, 3, True)

android_price_index = 7
ios_price_index = 5

android_free = []
ios_free = []

for app in android_english:
    price = app[android_price_index]
    if price == '0':
        android_free.append(app)

for app in ios_english:
    price = app[ios_price_index]
    if price == '0.0' or price == '0':
        ios_free.append(app)


print('Number of free Android apps : ', len(android_free))
print('Number of free ios apps : ', len(ios_free))

# create frequency table function

def freq_table(dataset, index):
    freq_table = {}
    total = 0
    for app in dataset:
        total += 1
        column = app[index]
        if column in freq_table:
            freq_table[column] += 1
        else:
            freq_table[column] = 1
    
    freq_percentages = {}
    for key in freq_table:
        freq_percentages[key] = (freq_table[key] * 100) / total
    return freq_percentages

def display_table(dataset, index, column_name, platform):
    percentages = freq_table(dataset, index)
    percentage_sorted = sorted(percentages.items(), key = 
             lambda kv:(kv[1], kv[0]), reverse = True)

    print("\nFrequencies of {} in {} Apps : \n".format(column_name, platform))

    for app, frequency in percentage_sorted:
        print("{} : {}".format(app, frequency))



ios_genre_index = -5
android_genre_index = 9
android_category_index = 1

display_table(ios_free, ios_genre_index,"prime genre", "iOS")
display_table(android_free, android_genre_index,"genre", "Android")
display_table(android_free, android_category_index,"category", "Android")

print("\nAverage user ratings of ios Prime Genres\n")
genres_ios = freq_table(ios_free, ios_genre_index)

for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios_free:
        genre_app = app[ios_genre_index]
        if genre_app == genre:
            num_ratings = float(app[6])
            total += num_ratings
            len_genre += 1
    average_rating = total / len_genre
    print(genre, " : ", average_rating)
    
print('\nAverage number of installs for each Android Category\n')
category_android = freq_table(android_free, android_category_index)

for category in category_android:
    total = 0
    len_category = 0
    for app in android_free:
        category_app = app[android_category_index]
        if category_app == category:
            num_installs = app[5]
            num_installs = num_installs.replace('+','')
            num_installs = num_installs.replace(',','')
            num_installs = float(num_installs)
            total += num_installs
            len_category += 1
    average_installs = total / len_category
    print(category,":",average_installs)
    