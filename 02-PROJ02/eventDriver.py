import asyncio
import time

def reminder():
    print('Wake up!')
    print('Calling the Pizza Company \n')
    loop.call_later(1,reminder)

def doorBell():
    print('Ding Dong!')
    print('I opened the door..."Thanks for the PIZZA"\n')
    loop.call_later(4,doorBell)

def phoneRings():
    print('Trin Trin..')
    print('I answered the phone... "Hello, who is this?" \n')
    loop.call_later(5,phoneRings)
#    loop.stop()

loop = asyncio.get_event_loop()
loop.call_later(1,reminder)
loop.call_later(4,doorBell)
loop.call_later(5,phoneRings)

print('Startnig the event loop...\n')
loop.run_forever()

print('The event loop stopped; Closing it down')
loop.close()