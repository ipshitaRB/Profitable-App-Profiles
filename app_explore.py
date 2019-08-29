from csv import reader

open_apple_file = open('AppleStore.csv')
apple_content = reader(open_apple_file)
ios_app_data = list(apple_content)

