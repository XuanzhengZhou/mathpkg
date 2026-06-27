---
role: proof
locale: en
of_concept: path-independence-of-integral-J
source_book: gtm023
source_chapter: "9"
source_section: "3. Pairs of symmetric bilinear functions"
---

Define the mapping $\omega: E \to \mathbb{C}$ by $\omega(x) = \Phi(x) + i\Psi(x)$. For a curve $x(t)$ in $\dot{E}$, set $\omega(t) = \omega(x(t)) = \Phi(x(t)) + i\Psi(x(t))$. The hypothesis $\Phi(x)^2 + \Psi(x)^2 \neq 0$ ensures $\omega(t) \neq 0$ for all $t$.

Writing $\omega(t) = u(t) + iv(t)$, the integrand of $J$ can be rewritten. Since $\Phi(x(t)) = u(t)$ and $\Psi(x(t)) = v(t)$, and noting that
$$\dot{u} = 2\Phi(x, \dot{x}), \quad \dot{v} = 2\Psi(x, \dot{x}),$$
we have
$$\Phi(x)\Psi(x, \dot{x}) - \Phi(x, \dot{x})\Psi(x) = \frac{1}{2}(u \dot{v} - \dot{u} v).$$
Thus
$$J = \frac{1}{2} \int_0^1 \frac{u \dot{v} - \dot{u} v}{u^2 + v^2} \, dt.$$

Let $\theta(t)$ be an angle function for the curve $\omega(t)$ in the punctured complex plane, i.e., $\omega(t) = |\omega(t)| e^{i\theta(t)}$. Then $u = |\omega|\cos\theta$, $v = |\omega|\sin\theta$. Differentiating and using
$$\sin\theta \cdot \dot{\theta} = \frac{-\dot{u}|\omega| + u\frac{d|\omega|}{dt}}{|\omega|^2}, \quad \cos\theta \cdot \dot{\theta} = \frac{\dot{v}|\omega| - v\frac{d|\omega|}{dt}}{|\omega|^2},$$
multiplying by $\sin\theta$ and $\cos\theta$ respectively and adding yields
$$\dot{\theta} = \frac{u\dot{v} - \dot{u}v}{u^2 + v^2}.$$
Integrating from $t=0$ to $t=1$ gives
$$2J = \theta(1) - \theta(0).$$

Now consider another curve $\bar{x}(t)$ with the same endpoints $x_0$ and $x$, and let $\bar{J}$ be the integral along it with angle function $\bar{\theta}$. Since $\omega(0) = \bar{\omega}(0)$ and $\omega(1) = \bar{\omega}(1)$, we have
$$\bar{\theta}(0) = \theta(0) + 2\pi k_0, \quad \bar{\theta}(1) = \theta(1) + 2\pi k_1$$
for integers $k_0, k_1$. Hence
$$\bar{J} - J = \pi(k_1 - k_0) = k\pi.$$

To show $k = 0$, we use that $n \geq 3$ implies $\dot{E} = E \setminus \{0\}$ is simply connected. There exists a differentiable homotopy $x = x(t,\tau)$ ($0 \leq t, \tau \leq 1$) in $\dot{E}$ such that $x(t,0) = x(t)$, $x(t,1) = \bar{x}(t)$, $x(0,\tau) = x_0$, $x(1,\tau) = x$. For each fixed $\tau$, form $J(\tau)$ as the integral along $x(t,\tau)$. Then $J(\tau)$ is continuous in $\tau$ and $J(\tau) - J = \pi k(\tau)$ for an integer-valued function $k(\tau)$. A continuous integer-valued function on $[0,1]$ must be constant. Since $k(0) = 0$, we have $k(\tau) = 0$ for all $\tau$, and in particular $k(1) = 0$, so $\bar{J} = J$.
