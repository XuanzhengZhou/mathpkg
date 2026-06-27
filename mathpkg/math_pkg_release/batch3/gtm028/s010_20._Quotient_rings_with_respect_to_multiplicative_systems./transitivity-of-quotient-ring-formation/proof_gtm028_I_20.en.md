---
role: proof
locale: en
of_concept: transitivity-of-quotient-ring-formation
source_book: gtm028
source_chapter: "I"
source_section: "20. Quotient rings with respect to multiplicative systems"
---

Let $\bar{R} = R_M$ and let $\bar{M}$ be a multiplicative system in $\bar{R}$ containing the image of $M$. Define
$$
M_1 = \{a \in R \mid \exists\, b_1 \in M \text{ such that } a/b_1 \in \bar{M}\}.
$$

We first verify that $M_1$ is a multiplicative system in $R$: if $a_1, a_2 \in M_1$ with $a_1/b_1, a_2/b_2 \in \bar{M}$ for some $b_1, b_2 \in M$, then $(a_1a_2)/(b_1b_2) \in \bar{M}$ since $\bar{M}$ is multiplicatively closed, and $b_1b_2 \in M$, so $a_1a_2 \in M_1$. Also, $0 \notin M_1$ since $0 \notin \bar{M}$, and elements of $M_1$ are regular.

Now take an arbitrary element $\alpha \in \bar{R}_{\bar{M}}$, written as
$$
\alpha = \frac{a/b}{\bar{m}} \quad \text{with } a \in R,\; b \in M,\; \bar{m} \in \bar{M}.
$$
Write $\bar{m} = a_1/b_1$ with $a_1 \in M_1$ (by definition of $M_1$) and $b_1 \in M$. Then
$$
\alpha = \frac{a/b}{a_1/b_1} = \frac{ab_1}{a_1b}.
$$
Since $a_1 \in M_1$ and $b \in M \subset M_1$, the denominator $a_1b \in M_1$, while the numerator $ab_1 \in R$. Hence $\alpha \in R_{M_1}$.

Conversely, if $\beta = a/m_1 \in R_{M_1}$ with $a \in R$, $m_1 \in M_1$, then there exists $b_1 \in M$ such that $m_1/b_1 \in \bar{M}$. Then
$$
\beta = \frac{a}{m_1} = \frac{a/1}{m_1/1} = \frac{a/1}{m_1/b_1 \cdot b_1/1}
$$
which is an element of $\bar{R}_{\bar{M}}$ since $a/1, b_1/1 \in \bar{R}$ and $m_1/b_1 \in \bar{M}$.

Thus $R_{M_1}$ and $\bar{R}_{\bar{M}}$ contain each other, so $R_{M_1} = \bar{R}_{\bar{M}}$.
