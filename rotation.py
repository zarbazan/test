#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

teta_cmd = 30.0      # целевое положение
teta_0 = 0.0   # начальное положение
teta1_0 = 0.0  # начальная скорость
teta2_0 = 0.0  # начальное ускорение

# e_teta      ошибка по положению
# teta_1_cmd  целевая скорость
# teta_2_cmd целевое ускорение

teta = teta_0    # текущее положеие
teta1 = teta1_0  # текущая скорость

Iy = 7.16914e-05   # момент инерции
kb = 3.9865e-08    # коэфф тяги
l = 0.17           # длина базы

dt = 0.01          # шаг интегрирования
Tend = 10         # время моделирования
t0 = 0             # начало моделирования
t = t0             # время
Tcmd = 10           # целевая тяга
Lim1 = 100000        # ограничение по скорости
Lim2 = 100000        # ограничение по ускорению

kP = 2
kI = 1
kD = 0.5

kP1 = 2
kI1 = 1
kD1 = 0.5

e_teta_past = teta
e_teta_1_past = teta1


def integral(param):
    param +=param * dt
    return param

# расчет ошибки
def error(input1, input2):
    return input1 - input2


# PID вычислитель
def PID(error, Kp, Ki, Kd, error_past, Lim):

    P = Kp * error
    I = Ki * integral(error)
    D = Kd * ((error - error_past)/dt)
    PID = P + I+ D

    if (PID > Lim):
        PID = Lim
    elif (PID < -Lim):
        PID = -Lim

    #print("P", P, "I", I, "D", D)

    return PID

# модель
def model(teta_2_cmd, Tcmd, kb, l, Iy):
    omega1 = -teta_2_cmd + Tcmd  #угловая скорость 1 мотора   1  ^  2
    omega2 = -teta_2_cmd + Tcmd  #угловая скорость 2 мотора     \ /
    omega3 = teta_2_cmd + Tcmd  #угловая скорость 3 мотора      / \
    omega4 = teta_2_cmd + Tcmd  #угловая скорость 4 мотора    4     3
    My = kb * l * ((omega4**2 + omega3**2) - (omega1**2 + omega2**2))
    teta2 = My / Iy
    print(My)
    return teta2




while t <= 2*dt: #Tend:


    e_teta = error(teta_cmd, teta)               # расчет ошибки по положению
    e_teta_past = e_teta
    teta_1_cmd = PID(e_teta, kP, kI, kD, e_teta_past, Lim1)  # расчет  целевой скорости
    print(e_teta, e_teta_past, teta_1_cmd)

    e_teta_1 = error(teta_1_cmd, teta1)   # расчет ошибки по скорости
    e_teta_1_past = e_teta_1
    teta_2_cmd = PID(e_teta_1, kP1, kI1, kD1, e_teta_1_past, Lim2)   # расчет  целевого ускорения
    print(e_teta_1, e_teta_1_past, teta_2_cmd)

    teta2 = model(teta_2_cmd, Tcmd, kb, l, Iy)
    teta1 = integral(teta2)
    teta = integral(teta1)



    print(teta2, teta1, teta)
    print("___________")
    t += dt



