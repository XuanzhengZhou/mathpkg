---
role: proof
locale: en
of_concept: theorem-8-12
source_book: gtm055
source_chapter: "7-8"
source_section: "Section 09_Section_9"
---

Proof. We assume, as we clearly may, that $f$ is increasing. Let $m$ and $M$ be positive numbers such that $m < M$ and consider the set $E_{m, M}$ of those points $t$ in $(a, b)$ at which $d_-(t) < m < M < D_+(t)$. (Since $f$ is increasing, all four of its derivates are nonnegative at every point, so it will suffice to use positive numbers for $m$ and $M$.) According to the preceding lemma (with $U = (a, b)$), there exists an open subset $W_1$ of $(a, b)$ such that $E_{m, M} \subset W_1$ and $\mu_1(W_1) \leq (m/M)(b - a)$. Then, applying the lemma again with $U = W_1$, we obtain a second open set $W_2$ such that $E_{m, M} \subset W_2 \subset W_1$ and such that $\mu_1(W_2) \leq (m/M)\mu_1(W_1) \leq (m/M)^2(b - a)$. Continuing in this manner, we obtain by mathematical induction a nested sequence of open sets

$$W_1 \supset W_2 \supset \cdots \supset W_n \supset \cdots \supset E_{m, M}$$

such that $\mu_1(W_n) \downarrow 0$. Hence $\mu_1(E_{m, M}) = 0$. (See Problems C and E; note that it is not asserted here that $E_{m, M}$ is a Borel set, only that it is Lebesgue measurable by virtue of having measure zero.)

Next we consider the set $E = \{
