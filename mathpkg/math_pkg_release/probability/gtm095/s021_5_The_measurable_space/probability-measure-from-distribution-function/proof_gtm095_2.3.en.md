---
role: proof
locale: en
of_concept: probability-measure-from-distribution-function
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Existence and Uniqueness of a Probability Measure from a Distribution Function

**Theorem 1.** Let $F = F(x)$ be a distribution function on the real line $R$. There exists a unique probability measure $P$ on $(R, \mathcal{B}(R))$ such that

$$P(a, b] = F(b) - F(a)$$

for all $a, b$ with $-\infty \leq a < b < \infty$.

*Proof.* Let $\mathcal{A}$ be the algebra of subsets $A$ of $R$ that are finite sums of disjoint intervals of the form $(a, b]$:

$$A = \sum_{k=1}^{n} (a_k, b_k].$$

On these sets we define a set function $P_0$ by

$$P_0(A) = \sum_{k=1}^{n} [F(b_k) - F(a_k)], \quad A \in \mathcal{A}.$$

This definition is consistent: if an element $A \in \mathcal{A}$ admits two different representations as sums of disjoint intervals $(a, b]$, the corresponding values $P_0(A)$ coincide. It is clear that $P_0$ is a finitely additive set function on $\mathcal{A}$ normalized to $P_0(R) = 1$.

Carathéodory's Theorem guarantees that once $P_0$ is shown to be countably additive (hence a probability measure) on $\mathcal{A}$, there exists a unique extension to a measure $P$ on $\sigma(\mathcal{A}) = \mathcal{B}(R)$.

We now show that $P_0$ is countably additive on $\mathcal{A}$. By the theorem from Sect. 1, it suffices to show that $P_0$ is continuous at $\varnothing$, i.e., to verify that

$$P_0(A_n) \downarrow 0, \quad \text{whenever} \quad A_n \downarrow \varnothing, \quad A_n \in \mathcal{A}.$$

Let $A_1, A_2, \ldots$ be a sequence of sets from $\mathcal{A}$ with the property $A_n \downarrow \varnothing$.

**Step 1.** Suppose first that all $A_n$ are contained in a closed interval $[-N, N]$, $N < \infty$. Since each $A_n$ is the sum of finitely many intervals of the form $(a, b]$ and since

$$P_0(a', b] = F(b) - F(a') \to F(b) - F(a) = P_0(a, b]$$

as $a' \downarrow a$ (because $F(x)$ is continuous on the right), we can find, for every $A_n$, a set $B_n \in \mathcal{A}$ such that its closure $[B_n] \subseteq A_n$ and

$$P_0(A_n) - P_0(B_n) \leq \varepsilon \cdot 2^{-n},$$

where $\varepsilon > 0$ is a preassigned positive number.

By hypothesis, $\bigcap A_n = \varnothing$, so $\bigcap [B_n] = \varnothing$ as well (since $[B_n] \subseteq A_n$). Because the sets $[B_k]$ are closed and bounded (hence compact) and their intersection is empty, there exists a finite $n_0$ such that $\bigcap_{k=1}^{n_0} [B_k] = \varnothing$, and therefore $\bigcap_{k=1}^{n_0} B_k = \varnothing$.

Using the inclusion $A_{n_0} \subseteq A_{n_0-1} \subseteq \cdots \subseteq A_1$, we obtain

$$
\begin{aligned}
P_0(A_{n_0}) &= P_0\!\left(A_{n_0} \setminus \bigcap_{k=1}^{n_0} B_k\right) + P_0\!\left(\bigcap_{k=1}^{n_0} B_k\right) \\
&= P_0\!\left(A_{n_0} \setminus \bigcap_{k=1}^{n_0} B_k\right) \\
&\leq P_0\!\left(\bigcup_{k=1}^{n_0} (A_k \setminus B_k)\right) \\
&\leq \sum_{k=1}^{n_0} P_0(A_k \setminus B_k) \leq \sum_{k=1}^{n_0} \varepsilon \cdot 2^{-k} \leq \varepsilon.
\end{aligned}
$$

Therefore $P_0(A_n) \downarrow 0$ as $n \to \infty$.

**Step 2.** We now drop the assumption that all $A_n \subseteq [-N, N]$ for some $N$. Take $\varepsilon > 0$ and choose $N$ so large that

$$P_0[-N, N] = F(N) - F(-N) > 1 - \varepsilon/2,$$

which is possible since $F(+\infty) = 1$ and $F(-\infty) = 0$. Then

$$A_n = (A_n \cap [-N, N]) \cup (A_n \cap \overline{[-N, N]}),$$

where $\overline{[-N, N]} = R \setminus [-N, N]$. It follows that

$$
\begin{aligned}
P_0(A_n) &= P_0(A_n \cap [-N, N]) + P_0(A_n \cap \overline{[-N, N]}) \\
&\leq P_0(A_n \cap [-N, N]) + P_0(\overline{[-N, N]}) \\
&\leq P_0(A_n \cap [-N, N]) + \varepsilon/2.
\end{aligned}
$$

Applying the reasoning of Step 1 to the sequence $A_n \cap [-N, N]$ (which also decreases to $\varnothing$), we find that $P_0(A_n \cap [-N, N]) \leq \varepsilon/2$ for sufficiently large $n$. Hence $P_0(A_n) \leq \varepsilon$ for sufficiently large $n$, and once again $P_0(A_n) \downarrow 0$ as $n \to \infty$.

Thus $P_0$ is countably additive on $\mathcal{A}$. By Carathéodory's Theorem, $P_0$ extends uniquely to a probability measure $P$ on $\sigma(\mathcal{A}) = \mathcal{B}(R)$. The measure $P$ satisfies (2) by construction.

Uniqueness follows from the fact that two probability measures agreeing on the $\pi$-system of intervals $(a, b]$ must coincide on the generated $\sigma$-algebra $\mathcal{B}(R)$. $\square$
