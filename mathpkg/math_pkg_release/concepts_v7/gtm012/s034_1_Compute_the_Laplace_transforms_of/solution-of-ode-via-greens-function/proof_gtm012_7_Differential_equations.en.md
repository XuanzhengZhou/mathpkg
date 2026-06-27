---
role: proof
locale: en
of_concept: solution-of-ode-via-greens-function
source_book: gtm012
source_chapter: "7"
source_section: "Differential equations"
---

# Proof of Solution of Linear ODEs via Green's Function Convolution

**Theorem 7.4.** Suppose $p$ is a polynomial of degree $n > 0$, and suppose $f: [0, \infty) \to \mathbb{C}$ is a continuous function. Then there is a unique solution $u: [0, \infty) \to \mathbb{C}$ to the problem

$$p(D)u(t) = f(t), \qquad t > 0,$$
$$D^j u(0+) = 0, \qquad 0 \leq j \leq n-1.$$

This solution is given by

$$u(t) = \int_0^t G(t-s) f(s) \, ds,$$

where $G$ is the Green's function for the operator $p(D)$.

**Proof.** We use properties (1)–(5) of $G$ established in Theorem 7.3. Recall in particular that

$$G(0+) = DG(0+) = \cdots = D^{n-2}G(0+) = 0, \qquad D^{n-1}G(0+) = a_n^{-1}.$$

Define $u$ by the convolution integral

$$u(t) = \int_0^t G(t-s) f(s) \, ds, \qquad t \geq 0.$$

Differentiating successively and applying the Leibniz rule for differentiating under the integral sign:

$$Du(t) = G(0+) f(t) + \int_0^t DG(t-s) f(s) \, ds = \int_0^t DG(t-s) f(s) \, ds,$$

since $G(0+) = 0$. Similarly, for $1 \leq k \leq n-2$,

$$D^k u(t) = \int_0^t D^k G(t-s) f(s) \, ds.$$

For the $(n-1)$-st derivative,

$$D^{n-1} u(t) = D^{n-2} G(0+) f(t) + \int_0^t D^{n-1} G(t-s) f(s) \, ds = \int_0^t D^{n-1} G(t-s) f(s) \, ds,$$

since $D^{n-2} G(0+) = 0$. Finally, for the $n$-th derivative,

$$D^n u(t) = D^{n-1} G(0+) f(t) + \int_0^t D^n G(t-s) f(s) \, ds = a_n^{-1} f(t) + \int_0^t D^n G(t-s) f(s) \, ds.$$

Now apply the differential operator $p(D) = \sum_{k=0}^{n} a_k D^k$. Using the expressions above,

$$\begin{aligned}
p(D)u(t) &= \sum_{k=0}^{n} a_k D^k u(t) \\
&= \sum_{k=0}^{n-1} a_k \int_0^t D^k G(t-s) f(s) \, ds + a_n \left( a_n^{-1} f(t) + \int_0^t D^n G(t-s) f(s) \, ds \right) \\
&= f(t) + \int_0^t \left( \sum_{k=0}^{n} a_k D^k G(t-s) \right) f(s) \, ds \\
&= f(t) + \int_0^t p(D) G(t-s) f(s) \, ds.
\end{aligned}$$

But $p(D)G(t-s) = 0$ for $t - s > 0$ by property (1) of $G$, so the integral vanishes. Hence

$$p(D)u(t) = f(t), \qquad t > 0.$$

Moreover, from the expressions for $D^k u(t)$ above we immediately obtain

$$D^k u(0+) = 0, \qquad 0 \leq k \leq n-1.$$

Thus $u$ is indeed a solution.

*Uniqueness.* The uniqueness of $u$ follows from Theorem 7.1. Define a distribution $F_u \in \mathcal{L}'$ by extending $u$ to be $0$ for $t < 0$ (which is valid because $u$ has at most exponential growth). Then $p(D)F_u$ and the distribution determined by $f$ (also extended by $0$ for $t < 0$) agree for $t > 0$. By Theorem 7.1, there is a unique distribution solution to $p(D)F = H$ in $\mathcal{L}'$; therefore $F_u$ is uniquely determined, and hence so is $u$ as a function on $(0, \infty)$.

$\square$

The more general problem

$$p(D)u(t) = f(t), \quad t > 0,$$
$$D^k u(0+) = b_k, \quad 0 \leq k < n$$

may be reduced to the case above. For example, one may choose a polynomial $u_0$ satisfying the initial conditions, and then solve for $v = u - u_0$ with zero initial data and modified right-hand side $f - p(D)u_0$, as shown in the exercises.
