---
role: proof
locale: en
of_concept: hensels-lemma
source_book: gtm058
source_chapter: "I"
source_section: "5"
---

We construct a sequence , a_2, \ldots$ of rational integers such that for all  \geq 1$:
(1) (a_n) \equiv 0 \pmod{p^{n+1}}$
(2)  \equiv a_{n-1} \pmod{p^n}$
(3) /tmp/write_gtm058.sh \leq a_n < p^{n+1}$

Induction: for =1$, write  = a_0 + b_1 p$. By Taylor expansion,
3115985F(a_1) = F(a_0 + b_1 p) \equiv F(a_0) + F'(a_0)b_1 p \pmod{p^2}.3115985
Since (a_0) = \alpha p$ and '(a_0) \not\equiv 0 \pmod{p}$, solve  \equiv -\alpha/F'(a_0) \pmod{p}$.

For general $, write  = a_{n-1} + b_n p^n$. Then
3115985F(a_n) \equiv F(a_{n-1}) + F'(a_{n-1})b_n p^n \pmod{p^{n+1}}.3115985
Since (a_{n-1}) = \alpha' p^n$ and '(a_{n-1}) \equiv F'(a_0) \not\equiv 0 \pmod{p}$, solve for $.

The limit  = \lim a_n$ is the unique solution with  \equiv a_0 \pmod{p}$.
