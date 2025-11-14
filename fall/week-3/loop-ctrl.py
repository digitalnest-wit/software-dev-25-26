msg = 'Hello, there'

for i in range(len(msg)):
    if i % 2 == 0:
        print(msg[i])
    elif msg[i] == 'h':
        print('found an h. skipping..')
        continue

    print('next')