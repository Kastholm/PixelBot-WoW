import random
import time
from fabric import Connection

result = Connection('raspberrypi', port=22, user='pi', connect_kwargs={'password': '1234'})
#result.run('ls')
def avg_click_dur(s=0.05, e=0.3):
    sleep_duration = random.uniform(s, e)
    time.sleep(sleep_duration)

def random_sleep(s=0.25, e=0.61):
    sleep_duration = random.uniform(s, e)
    time.sleep(sleep_duration)

def release():
    result.run('sudo python3 release.py')

def w(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 w.py')
    if one_click == True:
        avg_click_dur(s, e)

def s(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 s.py')
    if one_click == True:
        avg_click_dur(s, e)

def a(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 a.py')
    if one_click == True:
        avg_click_dur(s, e)

def d(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 d.py')
    if one_click == True:
        avg_click_dur(s, e)

def q(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 q.py')
    if one_click == True:
        avg_click_dur(s, e)

def e(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 e.py')
    if one_click == True:
        avg_click_dur(s, e)

def space(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 space.py')
    if one_click == True:
        avg_click_dur(s, e)

def f(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 f.py')
    if one_click == True:
        avg_click_dur(s, e)

def z(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 z.py')
    if one_click == True:
        avg_click_dur(s, e)

def we(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 we.py')
    if one_click == True:
        avg_click_dur(s, e)

def wq(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 wq.py')
    if one_click == True:
        avg_click_dur(s, e)

def wz(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 wz.py')
    if one_click == True:
        avg_click_dur(s, e)

def wf(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 wf.py')
    if one_click == True:
        avg_click_dur(s, e)

def wspace(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 wspace.py')
    if one_click == True:
        avg_click_dur(s, e)

def wespace(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 wespace.py')
    if one_click == True:
        avg_click_dur(s, e)

def wqspace(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 wqspace.py')
    if one_click == True:
        avg_click_dur(s, e)

def waspace(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 waspace.py')
    if one_click == True:
        avg_click_dur(s, e)

def wdspace(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 wdspace.py')
    if one_click == True:
        avg_click_dur(s, e)

def wzspace(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 wzspace.py')
    if one_click == True:
        avg_click_dur(s, e)

def sspace(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 sspace.py')
    if one_click == True:
        avg_click_dur(s, e)

def release(one_click=False, s=0.05, e=0.3):
    result.run('sudo python3 release.py')
    if one_click == True:
        avg_click_dur(s, e)

def z(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 z.py')
    if one_click == True:
        avg_click_dur(s, e)

def f(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 f.py')
    if one_click == True:
        avg_click_dur(s, e)

def one(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 1.py')
    if one_click == True:
        avg_click_dur(s, e)

def two(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 2.py')
    if one_click == True:
        avg_click_dur(s, e)


def three(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 3.py')
    if one_click == True:
        avg_click_dur(s, e)

def four(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 4.py')
    if one_click == True:
        avg_click_dur(s, e)

def five(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 5.py')
    if one_click == True:
        avg_click_dur(s, e)

def six(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 6.py')
    if one_click == True:
        avg_click_dur(s, e)

def seven(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 7.py')
    if one_click == True:
        avg_click_dur(s, e)

def eight(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 8.py')
    if one_click == True:
        avg_click_dur(s, e)

def nine(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 9.py')
    if one_click == True:
        avg_click_dur(s, e)

def zero(one_click=True, s=0.05, e=0.3):
    result.run('sudo python3 0.py')
    if one_click == True:
        avg_click_dur(s, e)