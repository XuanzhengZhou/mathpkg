---
role: proof
locale: en
of_concept: law-of-conservation-of-energy-1d
source_book: gtm060
source_chapter: "2"
source_section: "4"
---
Let $x(t)$ be a solution of $\ddot{x} = f(x)$. Then

$$\frac{d}{dt}E(x(t), \dot{x}(t)) = \frac{d}{dt}\left(\frac{1}{2}\dot{x}^2 + U(x)\right) = \dot{x}\ddot{x} + \frac{dU}{dx}\dot{x}.$$

Since $U(x) = -\int_{x_0}^x f(\xi)d\xi$, we have $dU/dx = -f(x)$. Substituting:

$$\frac{dE}{dt} = \dot{x}\ddot{x} - f(x)\dot{x} = \dot{x}(\ddot{x} - f(x)).$$

By the equation of motion $\ddot{x} = f(x)$, the right-hand side vanishes identically. Hence $E(x(t), \dot{x}(t))$ is constant in $t$.
