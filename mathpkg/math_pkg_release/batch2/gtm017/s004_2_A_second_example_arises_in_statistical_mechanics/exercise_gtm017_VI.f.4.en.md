---
role: exercise
locale: en
chapter: "VI"
section: "b"
exercise_number: 4
---

Consider a telephone trunking problem with infinitely many channels. Calls end with probability $\mu h$ and new calls arrive with probability $\lambda h$ in $(t,t+h)$. The system is in state $n$ if $n$ lines are busy. Show $P(s,t)=\sum_n p_{0,n}(t)s^n$ satisfies $\partial P/\partial t = (1-s)\{-\lambda P + \mu \partial P/\partial s\}$. Solve and find limit of $p_{0,n}(t)$.
