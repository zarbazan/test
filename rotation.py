#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

teta_0 = 5   # начальное положение
teta1_0 = 0  # начальная скорость
teta2_0 = 0  # начальное ускорение
# e_teta      ошибка по положению
# teta_1_cmd  целевая скорость

teta = teta_0    # текущее положеие
teta1 = teta1_0  # текущая скорость

Iy = 7.16914e-05   # момент инерции
kb = 3.9865e-08    # коэфф тяги
l = 0.17           # длина базы
teta_cmd = 10      # целевое положение
dt = 0.01          # шаг интегрирования
Tend = 10          # время моделирования
t0 = 0             # начало моделирования
t = t0             # время
Tcmd = 1           # целевая тяга
Lim1 = 1000        # ограничение по скорости
Lim2 = 1000        # ограничение по ускорению

kP = 10
kI = 10
kD = 0.005

kP1 = 0.10
kI1 = 0.10
kD1 = 0.005

e_teta_past = teta
e_teta_1_past = teta1
N = 0     # номер итерации

# расчет ошибки по положению
def error_teta(teta):
    return teta_cmd - teta


# PID вычислитель по скорости
def PID1(e_teta, e_teta_past, N):
    # e_teta_past = 0
    P = kP * e_teta
    I = kI * e_teta * dt * N
    D = kD * ((e_teta - e_teta_past)/dt)
    PID = P + I+ D

    if ((P+I+D) > Lim1):
        PID = Lim1
    elif ((P+I+D) < -Lim1):
        PID = -Lim1

    print("P", P, "I", I, "D", D)

    return PID


# расчет ошибки по скорости
def error_teta_1(teta_1_cmd, teta1):
    return teta_1_cmd - teta1


# PID вычислитель по ускорению
def PID2(e_teta_1, e_teta_1_past, N):
    # e_teta_past = 0
    P = kP1 * e_teta_1
    I = kI1 * e_teta_1 * dt * N
    D = kD1 * ((e_teta_1 - e_teta_1_past)/dt)
    PID2 = P + I+ D

    if ((P+I+D) > Lim2):
        PID2 = Lim2
    elif ((P+I+D) < -Lim2):
        PID2 = -Lim2

    print("P", P, "I", I, "D", D)

    return PID2


e_teta = error_teta(teta)               # расчет ошибки по положению
teta_1_cmd = PID1(e_teta, e_teta_past, N)  # расчет  целевой скорости
e_teta_past = e_teta

e_teta_1 = error_teta_1(teta_1_cmd, teta1)   # расчет ошибки по скорости
teta_2_cmd = PID2(e_teta_1, e_teta_1_past, N)   # расчет  целевого ускорения
e_teta_1_past = e_teta_1


print(teta_1_cmd, teta_2_cmd)




