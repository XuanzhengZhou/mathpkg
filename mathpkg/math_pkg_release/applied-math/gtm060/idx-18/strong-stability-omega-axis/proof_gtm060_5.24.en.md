---
role: proof
locale: en
of_concept: strong-stability-omega-axis
source_book: gtm060
source_chapter: "5"
source_section: "24"
---

For $\varepsilon = 0$, Equation (4) has constant coefficients and is clearly solvable. The general solution is
$$x = c_1 \cos \omega t + c_2 \sin \omega t.$$

The solution with initial conditions $x = 1$, $\dot{x} = 0$ is $x = \cos \omega t$, $\dot{x} = -\omega \sin \omega t$. The solution with initial conditions $x = 0$, $\dot{x} = 1$ is $x = \frac{1}{\omega} \sin \omega t$, $\dot{x} = \cos \omega t$.

Therefore, the matrix of the mapping $A$ after period $T = 2\pi$ in the basis $(x, \dot{x})$ is
$$A = \begin{bmatrix}
\cos 2\pi\omega & \frac{1}{\omega} \sin 2\pi\omega \\
-\omega \sin 2\pi\omega & \cos 2\pi\omega
\end{bmatrix}.$$

Hence $|\operatorname{tr} A| = |2 \cos 2\pi\omega| < 2$ if $\omega \neq k/2$, $k = 0, 1, \ldots$, and the theorem follows from the preceding corollary on strong stability via the trace condition.
