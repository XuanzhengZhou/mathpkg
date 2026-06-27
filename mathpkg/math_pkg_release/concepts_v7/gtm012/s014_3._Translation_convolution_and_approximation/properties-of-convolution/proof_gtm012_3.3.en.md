---
role: proof
locale: en
of_concept: properties-of-convolution
source_book: gtm012
source_chapter: "3"
source_section: "3. Translation, convolution, and approximation"
---

# Proof of Proposition 3.1: Algebraic Properties of Convolution on the Circle

Recall that for $u, v \in \mathcal{C}$, the convolution $u * v$ is defined by

$$(u * v)(x) = \frac{1}{2\pi} \int_0^{2\pi} u(x - y) v(y) \, dy.$$

From this definition we have the basic estimate

$$|u * v| \leq |u| \, \frac{1}{2\pi} \int_0^{2\pi} |v(x)| \, dx \leq |u| \, |v|,$$

where $|\cdot|$ denotes the supremum norm on $\mathcal{C}$.

**Proof.** We begin with part of (10). For any $t \in \mathbb{R}$,

$$
\begin{aligned}
T_t(u * v)(x) &= (u * v)(x - t) \\
&= \frac{1}{2\pi} \int_0^{2\pi} u(x - t - y) v(y) \, dy \\
&= \frac{1}{2\pi} \int_0^{2\pi} T_t u(x - y) v(y) \, dy \\
&= (T_t u) * v(x).
\end{aligned}
$$

Therefore,

$$|T_t(u * v) - u * v| = |(T_t u) * v - u * v| = |(T_t u - u) * v| \leq |T_t u - u| \, |v|.$$

Since $u$ is uniformly continuous on the circle, $|T_t u - u| \to 0$ as $t \to 0$. Hence $|T_t(u * v) - u * v| \to 0$ as $t \to 0$, which proves that $u * v \in \mathcal{C}$ (i.e., $u * v$ is continuous).

The remaining properties are established as follows:

**(6) Commutativity:** $u * v = v * u$.
$$
(u * v)(x) = \frac{1}{2\pi} \int_0^{2\pi} u(x - y) v(y) \, dy.
$$
Substitute $z = x - y$, so $dz = -dy$. As $y$ runs from $0$ to $2\pi$, $z$ runs from $x$ to $x - 2\pi$. By periodicity of the functions on the circle, this is the same as integrating over any interval of length $2\pi$, so
$$
(u * v)(x) = \frac{1}{2\pi} \int_0^{2\pi} u(z) v(x - z) \, dz = (v * u)(x).
$$

**(7) Homogeneity:** $(a u) * v = a (u * v)$ for $a \in \mathbb{C}$.
$$
((a u) * v)(x) = \frac{1}{2\pi} \int_0^{2\pi} a u(x - y) v(y) \, dy = a \cdot \frac{1}{2\pi} \int_0^{2\pi} u(x - y) v(y) \, dy = a (u * v)(x).
$$

**(8) Additivity:** $(u + v) * w = u * w + v * w$.
$$
\begin{aligned}
((u + v) * w)(x) &= \frac{1}{2\pi} \int_0^{2\pi} [u(x - y) + v(x - y)] w(y) \, dy \\
&= \frac{1}{2\pi} \int_0^{2\pi} u(x - y) w(y) \, dy + \frac{1}{2\pi} \int_0^{2\pi} v(x - y) w(y) \, dy \\
&= (u * w)(x) + (v * w)(x).
\end{aligned}
$$

**(9) Associativity:** $(u * v) * w = u * (v * w)$.
$$
\begin{aligned}
((u * v) * w)(x) &= \frac{1}{2\pi} \int_0^{2\pi} (u * v)(x - y) w(y) \, dy \\
&= \frac{1}{2\pi} \int_0^{2\pi} \left[ \frac{1}{2\pi} \int_0^{2\pi} u(x - y - z) v(z) \, dz \right] w(y) \, dy.
\end{aligned}
$$
By Fubini's theorem we interchange the order of integration, and then substitute $t = y + z$:
$$
\begin{aligned}
((u * v) * w)(x) &= \frac{1}{2\pi} \int_0^{2\pi} u(x - t) \left[ \frac{1}{2\pi} \int_0^{2\pi} v(t - y) w(y) \, dy \right] dt \\
&= (u * (v * w))(x).
\end{aligned}
$$

**(10) Translation:** $T_t(u * v) = (T_t u) * v = u * (T_t v)$. The first equality was proved above. The second follows by commutativity:
$$
T_t(u * v) = T_t(v * u) = (T_t v) * u = u * (T_t v).
$$

Alternatively, one may verify directly:
$$
T_t(u * v)(x) = \frac{1}{2\pi} \int_0^{2\pi} u(x - t - y) v(y) \, dy = \frac{1}{2\pi} \int_0^{2\pi} u(x - y) v(y - t) \, dy = (u * (T_t v))(x),
$$
using the change of variable $y' = y + t$ and periodicity. $\square$
