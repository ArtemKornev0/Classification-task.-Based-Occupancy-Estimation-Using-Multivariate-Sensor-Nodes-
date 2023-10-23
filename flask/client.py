import requests


if __name__ == '__main__':

    quest = 'A'

    while quest != 'Q':

        print('Enter the data as a string of 16 numbers with a separator ", ":')
        data = input()

        r = requests.post('http://localhost:5000/predict', json=data)

        if r.status_code == 200:

           print(f'Prediction is: {int(r.json())}')

        else:

           print('Something"s wrong !!!!!')
           print(r.text)
           break

        quest = input('If you want to exit, press "Q", if you want to continue - any other symbol:   ')
