---
role: proof
locale: en
of_concept: thm-for-aperiodic-recurrent-two-dimensional-random
source_book: gtm034
source_chapter: "3"
source_section: "007"
---

Proof: First we check that the formula in T2 gives $g_B(x,y) = 0$ when either $x$ or $y$ or both are in $B$. Supposing that $x$ is in $B$,

$$\sum_{t \in B} A(x,t)[\Pi_B(t,s) - \delta(t,s)] = H_B(x,s) - \mu_B(s).$$

The right-hand side in T2 therefore becomes

$$-A(x,y) - \frac{1}{K_B(\cdot)} + \sum_{s \in B} \mu(s)A(s,y) + \sum_{t \in B} A(x,t)\mu^*(t)$$
$$+ \sum_{s \in B} H_B(x,s)A(s,y) - \sum_{s \in B} \mu(s)A(s,y)$$
$$= -A(x,y) - \frac{1}{K_B(\cdot)} + \sum_{t \in B} A(x,t)\mu^*(t) + \sum_{s \in B} \delta(x,s)A(s,y)$$
$$= -\frac{1}{K_B(\cdot)} + \sum_{t \in B} A(x,t)\mu^*(t) = 0.$$

When $y$ is in $B$ the verification is

For the rest of the proof we may assume that neither $x$ nor $y$ is in $B$. We shall use a method which is often useful in classical potential theory, i.e., we find a "partial differential equation" satisfied by $g_B(x,y)$ and solve it. The theory of the Poisson equation in P13.3 will turn out to provide the appropriate existence theorem.

The equation we start with is

(1) $H_B(x,y) - \delta(x,y) = \sum_{t \in R} g_B(x,t)P(t,y) - g_B(x,y),$

for all $x,y$ in $R$. This is an obvious extension of part (c) of P10.1, to the full product space of all pairs $(x,y)$ in $R \times R$. Here, and in the rest of the proof, we define $H_B(x,y) = 0$ for $x \in R, y \in R - B$.

Now we fix a value of $x$ in $R - B$ and let

(2) $u(t) = g_B(x,t) + A(x,t), \quad t \in R.$

Substitution into equation (1), using P13.3, gives

(3) $\sum_{t \in R} u(t)P(t,y) - u(y) = H_B(x,y), \quad y \in R.$

The next step consists in solving (3) and we shall show that every solution of (3) is of the form

(4) $u(y) = \text{constant} + \sum_{t \in B} H_B(x,t)A(t,y), \quad y \in R,$

where of course the constant may depend on $x$.

First of all we rewrite equation (3) in the form

(5) $\sum_{t \in R} P^*(y,t)u(t) - u(y) = 0$ for $y \in R - B$
$= \rho(y) \geq 0$ for $y \in B,$

where $\rho(y) = H_B(x,y)$. Thus $u(t)$ is a solution of Poisson's equation discussed in D13.2, and by P13.3 equation (4) indeed is a solution of (3). But since

Introducing the reversed random walk, we have

$$M(x) = \sup_{t \in R} g_B^*(t,x) = \sup_{t \in R} H_{B \cup \{z\}}^*(t,x) g_B^*(x,x)$$

$$\leq g_B^*(x,x) = g_B(x,x) < \infty.$$

Thus the function $u(t)$ has the property that $u(t) - A(x,t)$ is bounded, and, in view of P12.2, this is the same as saying that $u(t) - a(-t)$ is a bounded function on $R$.

Now let

$$w(y) = \sum_{t \in B} H_B(x,t) A(t,y).$$

Then

$$h(y) = u(y) - w(y) = u(y) - a(-y) + \sum_{t \in B} H_B(x,t)[A(0,y) - A(t,y)]$$

is a bounded function of $y$ (since $A(0,y) - A(t,y)$ is bounded for each $t$ according to P12.2). Furthermore $u(y)$ satisfies (5), so that

$$\sum_{s \in R} P^*(y,s)h(s) = h(y) \text{ for } y \in R.$$

By P13.1, $h(y) = c(x)$, a constant depending on $x$ of course—and therefore we have proved that $u(y) = c(x) + w(y)$ is given by equation (4).

The rest is easy. We now have

$$g_B(x,y) = -A(x,y) + c(x) + \sum_{t \in B} H_B(x,t) A(t,y)$$

$$= -A(x,y) + c(x) + \sum_{s \in B} \mu(s) A(s,y)$$

$$+ \sum_{s \in B} \sum_{t \in B} A(x,s)[\Pi_B(s,t) - \delta(s,t)] A(t,y).$$

To complete the proof of T2, we now have only to show that

$$c(x) = -\frac{1}{K_B(\cdot \cdot)} + \sum_{t

The result of T2 can be used to develop further the theory along the lines of classical logarithmic potential theory. There are no great surprises in store as the entire development exactly parallels the classical theory. We shall outline the principal facts—delegating the proofs to the problem section at the end of the chapter.

We fix a set $B$, with cardinality $1 \leq |B| < \infty$ and omit the subscript $B$ in $H_B, \mu_B, K_B, \Pi_B, g_B$, as this will cause no confusion at all. Remember that a charge on $B$ is a non-negative function vanishing off the set $B$. And let us define the potential due to the charge $\psi$ on $B$ as

$$A\psi(x) = \sum_{t \in B} A(x,t)\psi(t), \quad x \in R.$$

It may be shown that potentials satisfy the minimum principle; i.e., every potential $A\psi(x)$ assumes its minimum on the set $B$, or rather on the subset of $B$ where the charge $\psi$ is positive (for a proof see T31.2).

The minimum principle can be shown to imply that among all charges $\psi$ on $B$ with total charge $\sum_{x \in B} \psi(x) = 1$, there is exactly one with the property that its potential is constant on $B$. This particular unit charge is called the equilibrium charge $\mu^*(x)$ of the set $B$. It is easily shown that

$$\mu^*(x) = 1 \text{ if } |B| = 1$$

$$\mu^*(x) = \frac{K(x)}{K(\cdot)} \text{ when } |B| \geq 2,$$

and of course,

$$A\mu^*(x) = \frac{1}{K(\cdot)} \text{ when } x \in B$$

$$\geq \frac{1}{K(\cdot)} \text{ when } x \in R - B.$$

To make the last and subsequent statements meaningful when $|B| = 1$, we define

$$K(\cdot) = \infty, \quad \frac{1}{K(\cdot)} = 0 \text{ when } |B|

There are two other equivalent definitions of capacity. It is easily shown that there is one and only one constant $C$ such that for every unit charge $\psi$ on $B$

(6) $$\min_{z \in B} A\psi(x) \leq C \leq \max_{z \in B} A\psi(x).$$

This constant $C$ is defined to be the capacity of $B$, and it is true that $C = C(B)$.

Another useful definition of capacity is in terms of the Green function $g(x,y)$ of the set $B$. It is

(7) $$C' = \sum_{t \in B} A(x,t)\mu^*(t) - \lim_{|y| \to \infty} g(x,y).$$

It will presently be shown in T3 below that

$$\lim_{|y| \to \infty} g(x,y) = g(x,\infty)$$

exists for all $x$ in $R$, that $C'$ is indeed independent of $x$, and finally that $C' = [K(\cdot)]^{-1}$. This then is a third definition of capacity. Of all the three definitions it is the most useful one in uncovering the properties of $C(B)$ as a set function on the finite subsets of $R$. The two most important laws governing $C(B)$ are:

(8) If $B_1 \subset B_2 \subset R$, then $C(B_1) \leq C(B_2)$.

(9) If $B_1$ and $B_2$ have a nonempty intersection, then

$$C(B_1 \cup B_2) + C(B_1 \cap B_2) \leq C(B_1) + C(B_2).$$

The reader who investigates the analogy with classical logarithmic theory in [79] will find the name of capacity for $C(B)$ to be a misnomer. $C(B)$ is really the discrete analogue of the so-called Robin's constant, which is the logarithm of the logarithmic capacity.

Because of its importance in the study of time dependent phenomena in section 16, we single out the asymptotic behavior of $g_B(x,y)$ for further study.
