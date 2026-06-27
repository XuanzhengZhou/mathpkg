---
role: proof
locale: en
of_concept: characterization-of-continuous-linear-functionals
source_book: gtm012
source_chapter: "3"
source_section: "The space L'"
---

# Proof of Theorem 3.3: Characterization of Continuous Linear Functionals on $\mathcal{L}$

**Theorem.** Suppose $F: \mathcal{L} \to \mathbb{C}$ is linear. Then $F$ is continuous if and only if there exist an integer $k \geq 0$ and constants $a, M, K \in \mathbb{R}$ such that

$$|F(u)| \leq K |u|_{k,a,M}, \quad \text{for all } u \in \mathcal{L}. \tag{13}$$

**Proof.** ($\Leftarrow$) Suppose the estimate (13) holds. If $u_n \to 0$ in $\mathcal{L}$, then by definition of convergence in $\mathcal{L}$, we have $|u_n|_{k,a,M} \to 0$ for any fixed $k, a, M$. From (13) it follows that $|F(u_n)| \leq K |u_n|_{k,a,M} \to 0$, so $F(u_n) \to 0 = F(0)$. By linearity, $F(u_n) \to F(u)$ whenever $u_n \to u$, hence $F$ is continuous.

($\Rightarrow$) Conversely, suppose $F$ is continuous but no such estimate exists. Then for each positive integer $n$, taking $k = n$, $a = -n$, $M = -n$, and $K = n$, the estimate (13) must fail. Thus there exists $u_n \in \mathcal{L}$ such that

$$|F(u_n)| > n |u_n|_{n, -n, -n}.$$

Define
$$v_n = \frac{u_n}{n |u_n|_{n, -n, -n}}.$$
Then
$$|F(v_n)| = \frac{|F(u_n)|}{n |u_n|_{n, -n, -n}} > 1.$$
On the other hand,
$$|v_n|_{n, -n, -n} = \frac{|u_n|_{n, -n, -n}}{n |u_n|_{n, -n, -n}} = \frac{1}{n} \to 0.$$

By definition of the seminorms, this implies $v_n \to 0$ in $\mathcal{L}$. (More precisely, one verifies using Corollary 2.5 that convergence to zero with respect to the family of seminorms $|\cdot|_{k,a,M}$ is equivalent to convergence in $\mathcal{L}$.) Since $F$ is assumed continuous, we must have $F(v_n) \to F(0) = 0$. But $|F(v_n)| > 1$ for all $n$, a contradiction. Hence the estimate (13) must hold for some $k, a, M, K$. $\square$

**Remark.** This theorem is fundamental: it shows that continuity of a linear functional on $\mathcal{L}$ is equivalent to a uniform estimate by a single seminorm. In particular, every $F \in \mathcal{L}'$ satisfies an estimate of the form (13) for suitable parameters. This fact is used repeatedly; for example, it immediately yields Corollary 3.4 on the half-line support of distributions.
