---
role: proof
locale: en
of_concept: general-dirichlet-series-abscissa-of-convergence
source_book: gtm041
source_chapter: "8"
source_section: "8.2"
---

**Proof.** We know from Theorem 8.1 that the series converges for all $s$ with $\sigma > L$ and that $L$ cannot be negative. Let $S$ be the set of all $\sigma > 0$ such that the series converges for some $s$ with real part $\sigma$. The set $S$ is nonempty (by hypothesis) and bounded below (by $0$). Let $\sigma_c$ be the greatest lower bound of $S$. Then $\sigma_c \geq 0$.

Each $\sigma$ in $S$ satisfies $L \leq \sigma$, since if the series converges at some $s$ with $\operatorname{Re}(s) = \sigma$, then by Theorem 8.1 it converges for all $s$ with $\operatorname{Re}(s) > \sigma$, and $L$ must be $\leq \sigma$. Hence $L \leq \sigma_c$.

If we had $\sigma_c > L$, there would be a $\sigma$ in the interval $L < \sigma < \sigma_c$. For this $\sigma$ we would also have convergence for all $s$ with real part $\sigma$ (by Theorem 8.1), contradicting the definition of $\sigma_c$ as the greatest lower bound of all such $\sigma$. Hence $\sigma_c = L$.

But the definition of $\sigma_c$ shows that the series diverges for all $s$ with $0 \leq \sigma < L$. By hypothesis it also diverges for all $s$ with $\sigma < 0$. Hence it diverges for all $s$ with $\sigma < L$. This completes the proof. $\square$
