import math
import pygame
#import matplotlib.pyplot as plt


def sqr(number):
    return number*number


def diag(dot1, dot2):
    dx = dot2.pos[0]-dot1.pos[0]
    dy = dot2.pos[1]-dot1.pos[1]
    return math.sqrt(sqr(dx)+sqr(dy))


class eulerdot:
    bounces = 0

    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.pos, 10)


class verletdot:
    bounces = 0

    def __init__(self, pos):
        self.pos = pos
        self.prevPos = pos

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 255), self.pos, 10)


def Euler(dot, t, a):
    # x0 + v0*t + 1/2*a*sqr(t)
    dispx = dot.pos[0] + dot.vel[0]*t + (1/2)*a[0]*sqr(t)
    dispy = dot.pos[1] + dot.vel[1]*t + (1/2)*a[1]*sqr(t)
    dot.pos = (dispx, dispy)
    # v0 + at
    vx = dot.vel[0]+a[0]*t
    vy = dot.vel[1]+a[1]*t
    dot.vel = (vx, vy)

    if dot.pos[1] > 500-10:
        dot.pos = (dot.pos[0], 490)
        dot.vel = (dot.vel[0], dot.vel[1]*-1)
        dot.bounces += 1
        print(dot.bounces)


def SemiEuler(dot, t, a):
    # v0 + at
    vx = dot.vel[0]+a[0]*t
    vy = dot.vel[1]+a[1]*t
    dot.vel = (vx, vy)
    # x0 + v0*t + 1/2*a*sqr(t)
    dispx = dot.pos[0] + dot.vel[0]*t + (1/2)*a[0]*sqr(t)
    dispy = dot.pos[1] + dot.vel[1]*t + (1/2)*a[1]*sqr(t)
    dot.pos = (dispx, dispy)

    if dot.pos[1] > 500-10:
        dot.pos = (dot.pos[0], 490)
        dot.vel = (dot.vel[0], dot.vel[1]*-1)


def Verlet(dot, t, a):
    # x0 + (dx)*t + 1/2*a*sqr(t)
    vx = (dot.pos[0]-dot.prevPos[0])
    vy = (dot.pos[1]-dot.prevPos[1])
    dispx = dot.pos[0] + vx + a[0]*sqr(t)
    dispy = dot.pos[1] + vy + a[1]*sqr(t)
    dot.prevPos = dot.pos
    dot.pos = (dispx, dispy)

    if dot.pos[1] > 500-10:
        dot.prevPos = (dot.prevPos[0], (dot.pos[1] -
                       dot.prevPos[1])*2+dot.prevPos[1])


def MidPoint(dot, timestep):
    pass


def RungeKutta(dot, timestep):
    pass


a = (0, 9.82)
timestep = 0.001
doteuler = eulerdot((100, 200), (0, 0))
dotsemieuler = eulerdot((200, 200), (0, 0))
dotverlet = verletdot((300, 200))

pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False

    # Fill the background with white
    screen.fill((150, 150, 150))
    pygame.draw.line(screen, (200, 0, 0), (0, 200), (500, 200))

    doteuler.draw(screen)
    dotsemieuler.draw(screen)
    dotverlet.draw(screen)

    Euler(doteuler, timestep, a)
    SemiEuler(dotsemieuler, timestep, a)
    Verlet(dotverlet, timestep, a)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
