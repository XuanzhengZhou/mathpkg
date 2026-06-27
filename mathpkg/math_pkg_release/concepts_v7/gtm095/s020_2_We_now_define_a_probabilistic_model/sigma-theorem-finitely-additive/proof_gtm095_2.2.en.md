---
role: proof
locale: en
of_concept: sigma-theorem-finitely-additive
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem (Equivalence of Four Conditions for Finitely Additive Set Functions)

**Theorem.** Let $P$ be a finitely additive set function defined over the algebra $\mathcal{A}$, with $P(\Omega) = 1$. The following four conditions are equivalent:

1. $P$ is $\sigma$-additive (i.e., $P$ is countably additive);
2. $P$ is continuous from below, i.e., $A_n \uparrow A$ implies $P(A_n) \uparrow P(A)$;
3. $P$ is continuous from above, i.e., $A_n \downarrow A$ implies $P(A_n) \downarrow P(A)$;
4. $P$ is continuous at $\varnothing$, i.e., $A_n \downarrow \varnothing$ implies $P(A_n) \downarrow 0$.

*Proof.* We establish the cycle of implications $(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (4) \Rightarrow (1)$.

**(1) $\Rightarrow$ (2).** Suppose $A_n \uparrow A$. Write the limit set as a disjoint union:

$$\bigcup_{n=1}^{\infty} A_n = A_1 + (A_2 \setminus A_1) + (A_3 \setminus A_2) + \cdots$$

By $\sigma$-additivity of $P$,

$$P\!\left(\bigcup_{n=1}^{\infty} A_n\right) = P(A_1) + P(A_2 \setminus A_1) + P(A_3 \setminus A_2) + \cdots$$

Since $P$ is finitely additive, $P(A_k \setminus A_{k-1}) = P(A_k) - P(A_{k-1})$ for $k \geq 2$. Hence the partial sum telescopes:

$$P(A_1) + \sum_{k=2}^{n} \bigl(P(A_k) - P(A_{k-1})\bigr) = P(A_n).$$

Therefore

$$P\!\left(\bigcup_{n=1}^{\infty} A_n\right) = \lim_{n} P(A_n).$$

Since $A = \bigcup A_n$, we obtain $P(A) = \lim P(A_n)$, proving continuity from below.

**(2) $\Rightarrow$ (3).** Suppose $A_n \downarrow A$. For any $n \geq 1$,

$$P(A_n) = P\bigl(A_1 \setminus (A_1 \setminus A_n)\bigr) = P(A_1) - P(A_1 \setminus A_n).$$

The sequence $\{A_1 \setminus A_n\}_{n \geq 1}$ is nondecreasing and

$$\bigcup_{n=1}^{\infty} (A_1 \setminus A_n) = A_1 \setminus \bigcap_{n=1}^{\infty} A_n = A_1 \setminus A.$$

Applying condition (2),

$$\lim_{n} P(A_1 \setminus A_n) = P\!\left(\bigcup_{n=1}^{\infty} (A_1 \setminus A_n)\right) = P(A_1 \setminus A).$$

Consequently,

$$\lim_{n} P(A_n) = P(A_1) - \lim_{n} P(A_1 \setminus A_n) = P(A_1) - P(A_1 \setminus A) = P(A_1) - \bigl(P(A_1) - P(A)\bigr) = P(A).$$

Thus $P(A_n) \downarrow P(A)$, proving continuity from above.

**(3) $\Rightarrow$ (4).** This is the special case $A = \varnothing$ of (3). If $A_n \downarrow \varnothing$, then by (3) we have $P(A_n) \downarrow P(\varnothing) = 0$.

**(4) $\Rightarrow$ (1).** Let $A_1, A_2, \ldots \in \mathcal{A}$ be pairwise disjoint with $A = \sum_{i=1}^{\infty} A_i \in \mathcal{A}$. Define the tail sums

$$B_n = \sum_{i=n+1}^{\infty} A_i.$$

Then $B_n \downarrow \varnothing$ as $n \to \infty$. By finite additivity,

$$P(A) = P\!\left(\sum_{i=1}^{n} A_i\right) + P(B_n) = \sum_{i=1}^{n} P(A_i) + P(B_n).$$

Letting $n \to \infty$ and using condition (4), $P(B_n) \to 0$. Hence

$$\sum_{i=1}^{\infty} P(A_i) = \lim_{n} \sum_{i=1}^{n} P(A_i) = \lim_{n} \bigl(P(A) - P(B_n)\bigr) = P(A).$$

Thus $P$ is $\sigma$-additive. $\square$
