import webbrowser

print("Hello! My name is Julia. In what category you want get help: popular music, news, weather(in Kyiv)?")
category = input('(to stop write off)').lower()
while category != "off":
    if category == 'music':
        print("Today`s top hits")
        webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M")
    elif category == 'news':
        print("Today`s hottest news: https://edition.cnn.com")
    elif category == 'weather':
        print("The weather for today: https://ua.sinoptik.ua/погода-київ")
    else:
        print("Wrong category. You always can buy our merch: merch.com")
    category = input('(to stop write off)').lower()
print("We hope Julia had helped you. Please, leave the feedback at feedback.com")
