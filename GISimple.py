#!/usr/bin/env python
# coding: utf-8

# In[15]:


import random
import colorama
from colorama import Fore

def golem_next_position(current_position,golem_min_speed,golem_max_speed):
    next_position=current_position+random.randrange(golem_min_speed,golem_max_speed+1)
    return next_position

def imp_next_position(current_position,imp_min_speed,imp_max_speed):
    next_position=current_position+random.randrange(imp_min_speed,imp_max_speed+1)
    return next_position

def game_status(golem_position,imp_position,road_length): 
    status=''
    if imp_position>=road_length:
        status='Scaped'
    elif golem_position>=imp_position:
        status='Back'
    else:
        status='Continue'  
    return status


def GISimple(impSpd=[1,9],golemSpd=[3,5],headStart=5,exitPosition=50):
    golem_min_speed=golemSpd[0]
    golem_max_speed=golemSpd[1]
    imp_min_speed=impSpd[0]
    imp_max_speed=impSpd[1]
    g_position=0
    i_position=headStart
    road_len=exitPosition
    
    while game_status(g_position,i_position,road_len)=='Continue':
        g_position=golem_next_position(g_position,golem_min_speed,golem_max_speed)
        i_position=imp_next_position(i_position,imp_min_speed,imp_max_speed)

    s=game_status(g_position,i_position,road_len)
    if s=='Scaped':
        return True
    else:
        return(False)


# In[ ]:





# In[ ]:




