---
role: exercise
locale: en
chapter: "5"
section: "24"
exercise_number: 2
---

Calculate the matrix of the transformation $A$ after period $T = 2\pi$ in the basis $(x, \dot{x})$ for the system

$$\ddot{x} = -\omega^2(1 + \varepsilon a(t))x$$

with $\varepsilon = 0$.

**Solution.** The general solution is $x = c_1 \cos \omega t + c_2 \sin \omega t$.

The solution with initial conditions $x = 1$, $\dot{x} = 0$ is $x = \cos \omega t$, $\dot{x} = -\omega \sin \omega t$.

The solution with initial conditions $x = 0$, $\dot{x} = 1$ is $x = \frac{1}{\omega} \sin \omega t$, $\dot{x} = \cos \omega t$.

Therefore

$$A = \begin{bmatrix}
\cos 2\pi\omega & \frac{1}{\omega} \sin 2\pi\omega \\
-\omega \sin 2\pi\omega & \cos 2\pi\omega
\end{bmatrix}.$$

Hence $|\operatorname{tr} A| = |2 \cos 2\pi\omega| < 2$ if $\omega \neq k/2$, $k = 0, 1, \ldots$.
