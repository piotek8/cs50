word = 'hello'
request = input('Greeting: ').strip()

if request.lower().startswith(word) :
    print('$0')
elif request[0].lower() == 'h':
    print('$20')
else:
    print('$100')
