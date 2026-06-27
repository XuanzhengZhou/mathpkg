---
role: exercise
locale: en
chapter: "5"
section: "25"
exercise_number: 2
---

**Stability of an inverted pendulum with vertically oscillating point of suspension.**

Can the topmost, usually unstable, equilibrium position of a pendulum become stable if the point of suspension oscillates in the vertical direction?

Let the length of the pendulum be $l$, the amplitude of the oscillation of the point of suspension be $a \ll l$, the period of oscillation of the point of suspension be $2\tau$, and, moreover, in the course of every half-period let the acceleration of the point of suspension be constant and equal to $\pm c$ (then $c = 8a/\tau^2$). It turns out that for fast enough oscillations of the point of suspension ($\tau \ll 1$) the topmost equilibrium becomes stable.

*Solution.* The equation of motion can be written in the form $\ddot{x} = (\omega^2 \pm d^2)x$ (the sign changes after time $\tau$), where $\omega^2 = g/l$ and $d^2 = c/l$. If the oscillation of the suspension is fast enough, then $d^2 > \omega^2$ ($d^2 = 8a/l\tau^2$).

As in the previous problem, $A = A_2 A_1$, where

$$A_1 = \begin{bmatrix} \text{ch } k\tau & \frac{1}{k} \text{sh } k\tau \\ k \text{sh } k\tau & \text{ch } k\tau \end{bmatrix}, \quad A_2 = \begin{bmatrix} \cos \Omega\tau & \frac{1}{\Omega} \sin \Omega\tau \\ -\Omega \sin \Omega\tau & \cos \Omega\tau \end{bmatrix}$$

with $k^2 = d^2 + \omega^2$, $\Omega^2 = d^2 - \omega^2$. The stability condition $|\text{tr } A| < 2$ takes the form

$$\left| 2 \text{ch } k\tau \cos \Omega\tau + \left( \frac{k}{\Omega} - \frac{\Omega}{k} \right) \text{sh } k\tau \sin \Omega\tau \right| < 2.$$

Set $\varepsilon = a/(2l)$ and $\mu = \omega/d$. Then $k\tau = 2\sqrt{2}\varepsilon\sqrt{1 + \mu^2}$, $\Omega\tau = 2\sqrt{2}\varepsilon\sqrt{1 - \mu^2}$, and $(k/\Omega - \Omega/k) = 2\mu^2 + O(\mu^4)$. For small $\varepsilon$ and $\mu$, expanding gives

$$\text{ch } k\tau = 1 + 4\varepsilon^2(1 + \mu^2) + \frac{8}{3}\varepsilon^4 + \cdots, \quad \cos \Omega\tau = 1 - 4\varepsilon^2(1 - \mu^2) + \frac{8}{3}\varepsilon^4 + \cdots$$

$$\left( \frac{k}{\Omega} - \frac{\Omega}{k} \right) \text{sh } k\tau \sin \Omega\tau = 16\varepsilon^2\mu^2 + \cdots$$

so the stability condition reduces to $\frac{4}{3}16\varepsilon^4 \geq 32\mu^2\varepsilon^2$, or $\mu \leq \varepsilon\sqrt{2/3}$, or $g/c \leq 2a/3l$, which can be rewritten as

$$N \geq \sqrt{\frac{3}{64}}\,\omega\,\frac{l}{a} \approx 0.22\,\omega\,\frac{l}{a},$$

where $N = 1/(2\tau)$ is the frequency of oscillation.

Verify that this condition indeed guarantees stability of the inverted pendulum.
