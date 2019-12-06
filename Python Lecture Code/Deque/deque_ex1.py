from collections import deque

channel=deque()

def send_item(item):
    channel.append(item)

def receive_item():
    a=channel.pop()
    print(a)


send_item(1)
send_item(2)
send_item(3)

receive_item()
receive_item()
receive_item()
# receive_item()

if __name__=='__main__':
    try:
        receive_item()
        print('seb')
    except IndexError:
        print('data structure empty')
    except:
        print('there is a problem with my code')