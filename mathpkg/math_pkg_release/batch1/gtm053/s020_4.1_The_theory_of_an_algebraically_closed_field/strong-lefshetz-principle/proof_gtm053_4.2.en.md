---
role: proof
locale: en
of_concept: strong-lefshetz-principle
source_book: gtm053
source_chapter: "4"
source_section: "4.2"
---

The equivalence follows directly from the completeness of $\text{ACF}_0$ and the ultraproduct construction.

(i) $\Rightarrow$ (ii): Since $\mathbf{C}$ is an algebraically closed field of characteristic $0$, any sentence $P$ true in $\mathbf{C}$ must be true in all models of $\text{ACF}_0$, because $\text{ACF}_0$ is complete (Theorem 4.2). Hence $F \vDash P$ for every algebraically closed field $F$ of characteristic $0$.

(ii) $\Rightarrow$ (iii): Suppose $P$ holds in all algebraically closed fields of characteristic $0$. If (iii) failed, there would be infinitely many primes $p$ for which $\tilde{F}_p \nvDash P$, i.e., $\tilde{F}_p \vDash \neg P$. Taking an ultraproduct of these $\tilde{F}_p$ over a nonprincipal ultrafilter would yield a model of $\text{ACF}_0$ in which $\neg P$ holds (by Łoś's theorem), contradicting (ii). Hence $P$ must hold in $\tilde{F}_p$ for all but finitely many $p$.

(iii) $\Rightarrow$ (i): If $P$ holds in $\tilde{F}_p$ for all but finitely many $p$, then taking an ultraproduct of these models yields a model of $\text{ACF}_0$ satisfying $P$. By completeness of $\text{ACF}_0$, this implies $\mathbf{C} \vDash P$.

The original Lefschetz principle is an informally established fact known to algebraic geometers: an algebro-geometric statement proven in the context of complex algebraic geometry holds also for any abstract algebraically closed field of characteristic zero.
