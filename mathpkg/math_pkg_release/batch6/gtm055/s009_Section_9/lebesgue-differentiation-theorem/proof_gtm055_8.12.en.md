---
role: proof
locale: en
of_concept: lebesgue-differentiation-theorem
source_book: gtm055
source_chapter: "8"
source_section: "9"
---

Assume $f$ is increasing (without loss). Let $m < M$ be positive numbers and consider $E_{m,M} = \{t \in (a,b) : d_-(t) < m < M < D_+(t)\}$. Since $f$ is increasing, all derivates are nonnegative, so it suffices to use positive $m, M$. By Lemma 8.11 with $U = (a,b)$, there exists an open set $W_1$ with $E_{m,M} \subset W_1$ and $\mu_1(W_1) \leq (m/M)(b-a)$. Applying Lemma 8.11 again with $U = W_1$ yields $W_2$ with $E_{m,M} \subset W_2 \subset W_1$ and $\mu_1(W_2) \leq (m/M)^2(b-a)$. By induction, we obtain a nested sequence $W_1 \supset W_2 \supset \cdots \supset E_{m,M}$ with $\mu_1(W_n) \downarrow 0$. Hence $\mu_1(E_{m,M}) = 0$. The set where any two derivates differ is a countable union of such $E_{m,M}$ with rational $m, M$, hence has measure zero. At remaining points, all four derivates agree, so $f'$ exists.
