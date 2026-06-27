---
role: proof
locale: en
of_concept: probability-measure-from-n-dimensional-distribution-function
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Existence and Uniqueness of a Probability Measure from an $n$-Dimensional Distribution Function

**Theorem 2.** Let $F_n = F_n(x_1, \ldots, x_n)$ be a distribution function on $R^n$. Then there exists a unique probability measure $P$ on $(R^n, \mathcal{B}(R^n))$ such that

$$P(a, b] = \Delta_{a_1 b_1} \cdots \Delta_{a_n b_n} F_n(x_1, \ldots, x_n)$$

for arbitrary $a = (a_1, \ldots, a_n)$, $b = (b_1, \ldots, b_n)$ with $a_i \leq b_i$. Here

$$\Delta_{a_i b_i} F_n(x_1, \ldots, x_n) = F_n(x_1, \ldots, x_{i-1}, b_i, x_{i+1}, \ldots, x_n) - F_n(x_1, \ldots, x_{i-1}, a_i, x_{i+1}, \ldots, x_n)$$

is the first difference operator acting on the $i$-th coordinate, and $\Delta_{a_1 b_1} \cdots \Delta_{a_n b_n}$ denotes their composition.

*Proof.* The proof follows by the same reasoning as Theorem 1, adapted to $R^n$.

**Construction of the algebra.** Let $\mathcal{A}_n$ be the algebra of subsets of $R^n$ that are finite sums of disjoint $n$-dimensional intervals of the form

$$(a, b] = (a_1, b_1] \times (a_2, b_2] \times \cdots \times (a_n, b_n].$$

**Definition of the set function.** Define $P_0$ on $\mathcal{A}_n$ by

$$P_0\!\left(\sum_{k=1}^{m} (a^{(k)}, b^{(k)}]\right) = \sum_{k=1}^{m} \Delta_{a_1^{(k)} b_1^{(k)}} \cdots \Delta_{a_n^{(k)} b_n^{(k)}} F_n(x_1, \ldots, x_n).$$

The properties $F_n(+\infty, \ldots, +\infty) = 1$ and $\lim_{x \downarrow y} F_n(x_1, \ldots, x_n) = 0$ when at least one coordinate of $y$ equals $-\infty$ guarantee that $P_0(R^n) = 1$.

**Verification of countable additivity.** As in Theorem 1, it suffices to show that $P_0$ is continuous at $\varnothing$. Let $A_m \in \mathcal{A}_n$ with $A_m \downarrow \varnothing$.

First suppose all $A_m$ are contained in a bounded hypercube $[-N, N]^n$. For each $A_m$, which is a finite union of $n$-dimensional intervals $(a, b]$, we use the right continuity of $F_n$ with respect to the variables collectively to find a set $B_m \in \mathcal{A}_n$ with $[B_m] \subseteq A_m$ and

$$P_0(A_m) - P_0(B_m) \leq \varepsilon \cdot 2^{-m}.$$

The closure $[B_m]$ is compact in $R^n$. Since $\bigcap A_m = \varnothing$ implies $\bigcap [B_m] = \varnothing$, there exists $m_0$ such that $\bigcap_{k=1}^{m_0} B_k = \varnothing$. Then, by the same estimate as in Theorem 1,

$$P_0(A_{m_0}) \leq \sum_{k=1}^{m_0} P_0(A_k \setminus B_k) \leq \varepsilon.$$

Therefore $P_0(A_m) \downarrow 0$.

Now drop the boundedness assumption. Choose $N$ large enough so that

$$P_0([-N, N]^n) = \Delta_{-N, N} \cdots \Delta_{-N, N} F_n > 1 - \varepsilon/2,$$

and decompose $A_m = (A_m \cap [-N, N]^n) \cup (A_m \cap \overline{[-N, N]^n})$. The same argument as in Theorem 1 then yields $P_0(A_m) \downarrow 0$.

Thus $P_0$ is countably additive on $\mathcal{A}_n$.

**Extension.** By Carathéodory's Theorem, $P_0$ extends uniquely to a probability measure $P$ on $\sigma(\mathcal{A}_n) = \mathcal{B}(R^n)$. By construction, $P$ satisfies (12).

**Uniqueness.** Two probability measures on $\mathcal{B}(R^n)$ that agree on the $\pi$-system of $n$-dimensional intervals $(a, b]$ must coincide on the generated $\sigma$-algebra $\mathcal{B}(R^n)$, completing the proof. $\square$

**Remark.** When $F_n(x_1, \ldots, x_n) = F^1(x_1) \cdots F^n(x_n)$ is a product of one-dimensional distribution functions, the resulting probability measure $P$ is the product measure $P = P^1 \times \cdots \times P^n$ on $(R^n, \mathcal{B}(R^n))$, where each $P^i$ is the probability measure on $(R, \mathcal{B}(R))$ corresponding to $F^i$.
