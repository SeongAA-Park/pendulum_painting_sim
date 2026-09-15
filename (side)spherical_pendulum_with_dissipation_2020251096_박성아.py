#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pygame
import sys
from pygame.locals import *
from math import sin, cos, tan, pi
import numpy as np
from numpy.linalg import inv

#EOM
def G(y,t): 
	θ_d, ϕ_d, θ, ϕ = y[0], y[1], y[2], y[3]

	θ_dd = ϕ_d**2 * cos(θ) * sin(θ) - g/l * sin(θ) - b /m * θ_d
	ϕ_dd = -2.0 * θ_d * ϕ_d / tan(θ) - b /m *sin(θ)* ϕ_d

	return np.array([θ_dd, ϕ_dd, θ_d, ϕ_d])

#classic Runge–Kutta method
def RK4_step(y, t, dt):
	k1 = G(y,t)
	k2 = G(y+0.5*k1*dt, t+0.5*dt)
	k3 = G(y+0.5*k2*dt, t+0.5*dt)
	k4 = G(y+k3*dt, t+dt)

	return dt * (k1 + 2*k2 + 2*k3 + k4) /6

#xyz 좌표설정
def update(θ, ϕ):
	x = scale*l * sin(θ) * cos(ϕ) + offset[0]
	y = scale*l * cos(θ) + offset[1]
	z = scale*l * sin(θ) * sin(ϕ)

	return (int(x), int(y), int(z))

#Rendering Axis
def render(point):
	x, y, z = point[0], point[1], point[2]
	z_scale = (2 - z/(scale*l)) * 20.0

	if prev_point:
		pygame.draw.line(trace, RED, prev_point, (x, y), int(z_scale*0.1))

	screen.fill(WHITE)	
	if is_tracing:
		screen.blit(trace, (0,0))

#Draw rope
	pygame.draw.line(screen, GRAY, offset, (x,y), int(z_scale*0.1))
#Draw origin
	pygame.draw.circle(screen, BLACK, offset, 8)
#Drwa ball
	pygame.draw.circle(screen, BLACK, (x, y), int(2*m*z_scale))

	return (x, y)

#화면설정
w, h = 600, 600
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (140,140,140)
RED = (255,0,0)
BLUE = (0,0,255)
LT_BLUE = (230,230,255)
offset = (w//2, h//4)
scale = 500
is_tracing = True

screen = pygame.display.set_mode((w,h))
screen.fill(WHITE)
trace = screen.copy()
pygame.display.update()
clock = pygame.time.Clock()

# parameters
prev_point = None
t = 0.0
delta_t = 0.02
y = np.array([0.0,3.14/2 , 3.14/4, 0.0]) #[θ_d, ϕ_d, θ, ϕ]

l = 0.5
g = 9.81
initial_m = 0.05
m = initial_m

b = 0.08

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 38)

# Simulation Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_t:
                is_tracing = not(is_tracing)
            if event.key == K_c:
                trace.fill(WHITE)

    point = update(y[2], y[3])
    prev_point = render(point)

    time_string = 'Time: {} s'.format(round(t, 1))
    text = myfont.render(time_string, False, (0, 0, 0))
    screen.blit(text,(10, 10))

    t += delta_t
    y = y + RK4_step(y, t, delta_t)
    
    # 질량이 시간에 따라 일정한 기울기로 감소
    # m -= m_d * delta_t

    # 초기질량 대비 질량&진행시간에 따른 프로그램 종료
    if m <= 0.9 * initial_m or t > 30:
        break  # Exit the simulation loop
        # 만약 초기 질량의 1% 미만일 경우 시뮬레이션 종료

    clock.tick(60)
    pygame.display.update()


# In[ ]:




