---
role: proof
locale: en
of_concept: lebesgue-stieltjes-measure-correspondence
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of the Correspondence between Lebesgue–Stieltjes Measures and Generalized Distribution Functions

**Theorem (Generalized Theorem 1).** The formula

$$\mu(a, b] = G(b) - G(a)$$

establishes a one-to-one correspondence between Lebesgue–Stieltjes measures $\mu$ on $(R, \mathcal{B}(R))$ and generalized distribution functions $G$ on $R$.

Recall that a Lebesgue–Stieltjes measure on $(R, \mathcal{B}(R))$ is a countably additive measure $\mu$ such that the measure $\mu(I)$ of every bounded interval $I$ is finite. A generalized distribution function $G = G(x)$ is a nondecreasing function with values in $(-\infty, \infty)$ that is continuous on the right.

*Proof.* The proof follows the same structure as Theorem 1, with the normalization condition $F(+\infty) = 1$, $F(-\infty) = 0$ replaced by the condition that $G$ takes finite values.

**From $G$ to $\mu$ (existence).** Let $G$ be a generalized distribution function. Let $\mathcal{A}$ be the algebra of finite unions of disjoint intervals $(a, b]$. Define a set function $\mu_0$ on $\mathcal{A}$ by

$$\mu_0\!\left(\sum_{k=1}^{n} (a_k, b_k]\right) = \sum_{k=1}^{n} [G(b_k) - G(a_k)].$$

We must show that $\mu_0$ is a countably additive, $\sigma$-finite measure on $\mathcal{A}$. Finite additivity is clear from the definition. For countable additivity, we verify continuity at $\varnothing$.

Let $A_n \in \mathcal{A}$ with $A_n \downarrow \varnothing$. By $\sigma$-finiteness, we may first consider the case where all $A_n$ are contained in a bounded interval $[-N, N]$ on which $G$ is finite. The same compactness argument as in Theorem 1 applies: for each $n$, choose $B_n \in \mathcal{A}$ with $[B_n] \subseteq A_n$ and $\mu_0(A_n \setminus B_n) \leq \varepsilon \cdot 2^{-n}$. Since $\bigcap A_n = \varnothing$ implies $\bigcap [B_n] = \varnothing$, compactness yields $\bigcap_{k=1}^{n_0} B_k = \varnothing$ for some finite $n_0$, and

$$\mu_0(A_{n_0}) \leq \sum_{k=1}^{n_0} \mu_0(A_k \setminus B_k) \leq \varepsilon.$$

For the general case, write $\mu_0$ as the sum of measures on $[-N, N]$ and its complement, and let $N \to \infty$. The countable additivity follows.

Thus $\mu_0$ is a $\sigma$-finite, countably additive measure on $\mathcal{A}$. By Carathéodory's theorem (which remains valid for $\sigma$-finite measures), $\mu_0$ extends uniquely to a measure $\mu$ on $\sigma(\mathcal{A}) = \mathcal{B}(R)$. This $\mu$ is a Lebesgue–Stieltjes measure: for any bounded interval $I = (a, b]$, $\mu(I) = G(b) - G(a) < \infty$, and for any bounded interval $I$ we can approximate it by half-open intervals.

**From $\mu$ to $G$ (converse).** Let $\mu$ be a Lebesgue–Stieltjes measure. Fix an arbitrary point $x_0 \in R$ and define

$$
G(x) = \begin{cases}
\mu(x_0, x] & \text{if } x > x_0, \\
0 & \text{if } x = x_0, \\
-\mu(x, x_0] & \text{if } x < x_0.
\end{cases}
$$

Then $G$ is nondecreasing (by monotonicity of $\mu$), takes finite values on bounded intervals (since $\mu(I) < \infty$ for bounded $I$), and is right-continuous (by continuity of $\mu$ along decreasing sequences). Hence $G$ is a generalized distribution function. Moreover, for any $a < b$,

$$\mu(a, b] = G(b) - G(a),$$

which can be verified by considering the relative positions of $a, b$ and $x_0$.

**One-to-one correspondence.** The two constructions are inverses of each other. If we start with $G$, construct $\mu_G$, and then recover $\tilde{G}$ from $\mu_G$, we obtain $\tilde{G} = G$ up to an additive constant. Normalizing by $G(x_0) = 0$ fixes the constant, establishing the bijection.

**Lebesgue measure.** The case $G(x) = x$ yields the Lebesgue measure $\lambda$ on $(R, \mathcal{B}(R))$:

$$\lambda(a, b] = b - a.$$

This measure can be completed to the system $\overline{\mathcal{B}}(R)$ of Lebesgue-measurable sets as described in the text. $\square$
