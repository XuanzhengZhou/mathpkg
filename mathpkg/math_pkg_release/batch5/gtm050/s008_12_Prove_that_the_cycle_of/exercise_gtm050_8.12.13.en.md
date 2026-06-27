---
role: exercise
locale: en
chapter: "8"
section: "12"
exercise_number: 13
---

Prove that the English method produces all solutions of Pell's equation.

[One can proceed as follows. Let $x^2 - Ay^2 = 1$. Assume without loss of generality that $x$ and $y$ are positive. Set $x = x_0$, $y = y_0$, and apply the English method to $x_0^2 - Ay_0^2 = 1$ to find $x_1^2 - Ay_1^2 = k_1$, $x_2^2 - Ay_2^2 = k_2$, $\ldots$. Then, by Exercise 6, $x_{i+1} = n_i x_i + x_{i-1}$, $y_{i+1} = n_i y_i + y_{i-1}$ where the sequence of positive integers $n_1, n_2, n_3, \ldots$ is periodic. By periodicity, $n_i$ can be defined for all integers $i$, not just positive integers. Then $x_i$, $y_i$ can be defined for all integers $i$. Prove that $x_i^2 - Ay_i^2 = k_i$ where $k_i$ is defined for negative $i$ by periodicity. Obviously if $x_i$ and $y_i$ are both positive for all $i \geqslant j$ (as they are in the case $j = 0$) then $|x_{j+2}| > |x_{j+1}|$ and $|y_{j+2}| > |y_{j+1}|$.]
