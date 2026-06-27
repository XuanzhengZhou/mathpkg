---
role: proof
locale: en
of_concept: factorization-into-irreducibles
source_book: gtm028
source_chapter: "IV"
source_section: "1"
---

Let $R$ be a noetherian integral domain and let $a \in R$ be a non-unit.

\textbf{Step 1: Every non-unit has an irreducible divisor.}
Define a sequence $\{a_n\}$ by induction: set $a_1 = a$. Given $a_{n-1}$, if $a_{n-1}$ is not irreducible, let $a_n$ be a proper divisor of $a_{n-1}$ (so $Ra_{n-1} \subsetneq Ra_n$). The ideals $Ra_n$ form a strictly ascending chain. By the a.c.c., this chain must be finite, so the sequence terminates at some $a_m$ which is irreducible and divides $a$.

\textbf{Step 2: Factorization.}
Define a second sequence $\{b_n\}$: set $b_1 = a$. Having defined $b_{n-1}$ (a non-unit), let $p_n$ be an irreducible divisor of $b_{n-1}$ (which exists by Step 1) and write $b_{n-1} = p_n b_n$. The ideals $Rb_n$ form an ascending chain $Rb_1 \subseteq Rb_2 \subseteq \cdots$ which stabilizes by the a.c.c. Hence there exists $N$ such that $Rb_N = Rb_{N+1} = \cdots$. If $b_N$ is not a unit, we could continue, which would contradict the stabilization unless $b_N$ is in fact a unit. But the chain $Rb_n$ is strictly ascending unless some $b_n$ is a unit, so by the a.c.c. the process must terminate with $b_r$ being a unit. Then $a = p_1 p_2 \cdots p_r \cdot b_r$ with $b_r$ a unit, and $p_1 p_2 \cdots p_r$ is a product of irreducibles. Absorbing the unit factor, we obtain $a$ as a product of irreducible elements.
