---
role: proof
locale: en
of_concept: prop-one-dimensional-aperiodic-recurrent-random-walk
source_book: gtm034
source_chapter: "7"
source_section: "016"
---

Proof: Suppose first that $a(x) = \alpha x$ for $x \geq 0$, where $\alpha > 0$. Then $\sigma^2 = \alpha^{-1}$ by T29.1. Now let $A$ be the set $A = \{-1, 0\}$. One calculates easily that

$$H_A(x, -1) = \mu_A(-1) + [a(x) - a(x + 1)]\Pi_A(0, -1), \quad x \in R.$$

Setting $x = 0$ gives

$$\mu_A(-1) = a(1)\Pi_A(0, -1) = \alpha\Pi_A(0, -1).$$

Hence

$$H_A(x, -1) = [\alpha + \alpha x - \alpha(x + 1)]\Pi_A(0, -1) = 0$$

for every $x \geq 1$. Thus, starting at a point $x_0 = x \geq 1$, the random walk can hit the set $A$ only at the point 0. There is no need to formalize the obvious argument by which one can now conclude that the random walk must be left continuous.

Conversely, suppose that we are given a left-continuous random walk with finite variance $\sigma^2$. By the same argument as before, one gets

$$H_A(x, -1) = [a(1) + a(x) - a(x + 1)]\Pi_A(0, -1), \quad x \geq 1.$$

But now we know that $H_A(x, -1) = 0$ when $

VI, the same observation was made for transient random walk, which is determined by its Green function $G(x,y)$.

The remainder of this section will be devoted to some interesting but completely straightforward consequences of P1 and P2. First we shall show how one can calculate $H_B(x,y)$ for left-continuous random walk with $\sigma^2 = \infty$. Given a set $B$ with $|B| = n$, we order its elements

$$b_1 < b_2 < \cdots < b_n.$$

Then

$$H_B(x,b_k) = \mu_B(b_k) + \sum_{j=1}^{n} a(x - b_j)[\Pi_B(b_j,b_k) - \delta(j,k)]$$

for $x \in R$, $k = 1, 2, \ldots, n$. When $|B| = 1$, there is no problem. When $|B| = n > 1$, set $x = b_i$. Then

$$\delta(i,k) = H_B(b_i,b_k) = \mu_B(b_k) + \sum_{j=i+1}^{n} a(b_i - b_j)[\Pi_B(b_j,b_k) - \delta(j,k)]$$

for $1 \leq i, k \leq n$. Setting $i = k = n$ gives

$$\mu_B(b_n) = 1.$$

But from the definition of $\mu_B(y)$ as

$$\mu_B(y) = \lim_{n \to \infty} \sum_{t \in R} P_{n+1}(x,t)H_B(t,y)$$

it is clear that

$$\sum_{y \in B} \mu_B(y) = 1, \quad \mu_B(b_k) = 0 \text{ for } k < |B| = n.$$

Now it is very easy to use

$$\delta(i,k) = \delta(n,k) + \sum_{j=i+1}^{n} a(b_i - b_j)[\Pi_B(b_j,b_k) - \delta(j,k)], \quad 1 \leq i,k \leq n,$$

to determine the matrix $\Pi_B$ in terms of the values of $a(x)$ when $x$ is a difference of points in $B$. And, of

proof applies here too, as it depended only on the fact that $a(x) > 0$ for $x \neq 0$. As in D11.3 we call this inverse $K_B(x,y)$ and denote

$$K_B(x \cdot) = \sum_{y \in B} K_B(x,y), \quad K_B(\cdot y) = \sum_{x \in B} K_B(x,y)$$

$$K_B(\cdot \cdot) = \sum_{x \in B} K_B(x \cdot), \quad x,y \in B.$$

With this notation we can imitate T11.1 and T14.2 to obtain
