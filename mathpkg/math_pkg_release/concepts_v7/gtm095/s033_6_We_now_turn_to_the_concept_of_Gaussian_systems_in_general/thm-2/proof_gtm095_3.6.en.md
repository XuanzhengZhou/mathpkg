---
role: proof
locale: en
of_concept: thm-2
source_book: gtm095
source_chapter: "3"
source_section: "6"
---

# Proof of Theorem 2 (Weak Convergence on the Real Line)

**Theorem 2.** Let $P, P_n$ ($n \geq 1$) be probability measures on the real line $(R, \mathcal{B}(R))$ and let $F, F_n$ be the corresponding distribution functions. The following conditions are equivalent:

(1) $P_n \xrightarrow{w} P$ (weak convergence of measures),

(2) $P_n \Rightarrow P$ (convergence in general of measures),

(3) $F_n \xrightarrow{w} F$ (weak convergence of distribution functions: $\int_R g \, dF_n \to \int_R g \, dF$ for every bounded continuous $g$),

(4) $F_n \Rightarrow F$ (convergence in general of distribution functions: $F_n(x) \to F(x)$ for all $x \in \mathbb{C}(F)$, the continuity points of $F$).

*Proof.* The equivalence (1) $\Leftrightarrow$ (2) is precisely Theorem 1 applied to the metric space $(R, |\cdot|)$. The equivalence (3) $\Leftrightarrow$ (4) is the same statement expressed in terms of distribution functions rather than measures, since $\int g \, dF_n = \int g \, dP_n$ and $F_n(x) = P_n((-\infty, x])$.

It remains to connect the measure statements with the distribution function statements.

---

### (4) $\Rightarrow$ (2)

Assume $F_n(x) \to F(x)$ at every continuity point $x$ of $F$. We must show $P_n(A) \to P(A)$ for every Borel set $A$ with $P(\partial A) = 0$.

First, consider a half-open interval $I = (a, b]$ with $a, b \in \mathbb{C}(F)$. Then

$$P_n(I) = F_n(b) - F_n(a) \to F(b) - F(a) = P(I).$$

Now let $A \subseteq R$ be an arbitrary open set. Every open set in $R$ can be written as a countable disjoint union of open intervals: $A = \bigcup_{k=1}^{\infty} (a_k, b_k)$. For each $k$, choose $a_k', b_k' \in \mathbb{C}(F)$ such that $a_k < a_k' < b_k' < b_k$ and

$$P((a_k, b_k) \setminus (a_k', b_k']) < \varepsilon \cdot 2^{-k}.$$

This is possible because the continuity points of a monotone function are dense. Set $I_k' = (a_k', b_k']$. Then $\bigcup_{k=1}^{m} I_k' \subseteq A$ for any finite $m$, and

$$\liminf_n P_n(A) \geq \liminf_n P_n\!\left(\bigcup_{k=1}^{m} I_k'\right) = \liminf_n \sum_{k=1}^{m} P_n(I_k') = \sum_{k=1}^{m} P(I_k'),$$

where the convergence holds because each $I_k'$ has endpoints in $\mathbb{C}(F)$. Letting $m \to \infty$, we obtain

$$\liminf_n P_n(A) \geq \sum_{k=1}^{\infty} P(I_k') \geq \sum_{k=1}^{\infty} \big(P((a_k, b_k)) - \varepsilon \cdot 2^{-k}\big) = P(A) - \varepsilon.$$

Since $\varepsilon > 0$ is arbitrary, $\liminf_n P_n(A) \geq P(A)$ for every open $A$. This establishes condition (III) of Theorem 1. By Theorem 1, (III) $\Rightarrow$ (I) $\Rightarrow$ (II) $\Rightarrow$ (IV), and in particular (III) $\Rightarrow$ (2), which is $P_n \Rightarrow P$.

---

### (2) $\Rightarrow$ (4)

Conversely, assume $P_n \Rightarrow P$, i.e., $P_n(A) \to P(A)$ for all $A$ with $P(\partial A) = 0$. For any $x \in \mathbb{C}(F)$, the boundary of $(-\infty, x]$ is $\{x\}$, and $P(\{x\}) = F(x) - F(x-) = 0$ (since $x$ is a continuity point of $F$). Therefore

$$F_n(x) = P_n((-\infty, x]) \to P((-\infty, x]) = F(x).$$

Thus $F_n \Rightarrow F$.

---

Combining all implications, we have the chain:

$$(1) \;\Longleftrightarrow\; (2) \;\Longleftrightarrow\; (3) \;\Longleftrightarrow\; (4),$$

where $(1) \Leftrightarrow (2)$ and $(3) \Leftrightarrow (4)$ are instances of Theorem 1, and the argument above establishes $(4) \Rightarrow (2)$ and $(2) \Rightarrow (4)$. $\square$

---

**Remark.** The essence of the proof is that on the real line, the class of half-open intervals with endpoints in $\mathbb{C}(F)$ is a convergence-determining class. A more general version of this theorem holds for $R^n$ (see Problem 1), where the "elementary" sets $(-\infty, x_1] \times \cdots \times (-\infty, x_n]$ serve as a convergence-determining class.
