---
role: proof
locale: en
of_concept: lemma-6-4
source_book: gtm012
source_chapter: "3"
source_section: "6"
---

# Proof of Lemma 6.4: Representation of Order-Zero Distributions Vanishing on Constants

**Lemma 6.4.** Suppose $F \in \mathcal{P}'$ is of order $0$, and suppose $F(w) = 0$ for every constant function $w$. Then there is a function $v \in \mathcal{C}$ such that

$$D^2 F_v = F.$$

*Proof.* Since $F$ is of order $0$, there is a constant $c$ such that $|F(u)| \le c|u|$ for all $u \in \mathcal{P}$. As shown in Lemma 6.3, $F$ extends uniquely to a continuous linear functional $F_1$ on $\mathcal{C}$: for any $u \in \mathcal{C}$, choose $(u_n) \subset \mathcal{P}$ with $u_n \to u$ uniformly, and set $F_1(u) = \lim F(u_n)$. This is well-defined and satisfies $|F_1(u)| \le c|u|$ for all $u \in \mathcal{C}$.

For $0 \le x, s \le 2\pi$, define the kernel function

$$u_x(s) = xs + 2\pi(x - s)^+,$$

where

$$(x - s)^+ = \begin{cases} 0, & x < s, \\ x - s, & x \ge s. \end{cases}$$

Observe that $u_x(0) = 2\pi x = u_x(2\pi)$, so $u_x$ can be extended periodically to a continuous function on $\mathbb{R}$ with period $2\pi$. Thus for each fixed $x$, $u_x \in \mathcal{C}$ as a function of $s$.

Define a function $v: [0, 2\pi] \to \mathbb{C}$ by

$$v(x) = F_1(u_x).$$

We verify that $v \in \mathcal{C}$. For any $x, y \in [0, 2\pi]$,

$$|u_x(s) - u_y(s)| \le 2\pi |x - y|, \quad \text{all } s,$$

since both terms are Lipschitz in $x$ with constant at most $2\pi$. Consequently,

$$|v(x) - v(y)| = |F_1(u_x - u_y)| \le c\,|u_x - u_y| \le 2\pi c\,|x - y|,$$

so $v$ is Lipschitz continuous, hence $v \in \mathcal{C}$.

It remains to show that $D^2 F_v = F$. For any test function $w \in \mathcal{P}$, we compute the action of $D^2 F_v$:

$$2\pi\,(D^2 F_v)(w) = -2\pi\,(DF_v)(Dw) = -2\pi\,F_v(D^2 w).$$

Alternatively, we work through difference quotients. For small $t \ne 0$,

$$
\begin{aligned}
2\pi\,t^{-1}[T_{-t}F_v - F_v](w)
&= t^{-1}\Bigl[\int_0^{2\pi} v(x+t)w(x)\,dx - \int_0^{2\pi} v(x)w(x)\,dx\Bigr] \\
&= \int_0^{2\pi} t^{-1}[v(x+t) - v(x)]\,w(x)\,dx.
\end{aligned}
$$

Approximating the integral by Riemann sums $\sum_j w(x_j)(x_j - x_{j-1})$ and using $v(x) = F_1(u_x)$ with the linearity of $F_1$,

$$t^{-1}[T_{-t}F_v - F_v](w) \approx F_1\!\left(\sum_j w(x_j)(x_j - x_{j-1})\,t^{-1}[u_{x_j+t} - u_{x_j}]\right).$$

As the mesh of the partition tends to $0$, the functions inside $F_1$ converge uniformly to

$$g_t(s) = \int_0^{2\pi} t^{-1}[u_{x+t}(s) - u_x(s)]\,w(x)\,dx.$$

Now, for fixed $s \in (0, 2\pi)$, we examine the difference quotient of $u_x$. For $0 < x < s$,

$$t^{-1}(u_{x+t}(s) - u_x(s)) \to \frac{\partial}{\partial x} u_x(s) = s \quad \text{as } t \to 0,$$

uniformly for $x$ in compact subsets of $(0, s)$. For $s < x < 2\pi$,

$$t^{-1}(u_{x+t}(s) - u_x(s)) \to s + 2\pi \quad \text{as } t \to 0,$$

uniformly for $x$ in compact subsets of $(s, 2\pi)$.

Passing to the limit $t \to 0$, the function $g_t$ converges uniformly to

$$g(s) = s\int_0^s w(x)\,dx + (s + 2\pi)\int_s^{2\pi} w(x)\,dx + \text{(boundary terms)}.$$

After a second differentiation and using integration by parts together with the assumption $F(w) = 0$ for constant $w$ (which implies $\int_0^{2\pi} w(x)\,dx = 0$), one obtains

$$(D^2 F_v)(w) = F(w)$$

for all $w \in \mathcal{P}$. Thus $D^2 F_v = F$ as claimed. $\square$
