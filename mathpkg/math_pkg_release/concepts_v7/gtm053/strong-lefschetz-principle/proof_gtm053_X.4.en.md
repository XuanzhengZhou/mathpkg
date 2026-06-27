---
role: proof
locale: en
of_concept: strong-lefschetz-principle
source_book: gtm053
source_chapter: "X"
source_section: "4"
---

# Proof of the Strong Lefschetz Principle

**Corollary (Strong Lefschetz Principle).** For an $L_1\mathrm{Ar}$-sentence $P$, the following are equivalent:

(i) $\mathbb{C} \models P$;

(ii) $F \models P$, for any algebraically closed field $F$ of characteristic $0$;

(iii) $\tilde{\mathbb{F}}_p \models P$, for all but finitely many primes $p$, where $\tilde{\mathbb{F}}_p$ is the algebraic closure of the $p$-element field $\mathbb{F}_p$.

*Proof.* (i) $\iff$ (ii) follows from the completeness of $\mathrm{ACF}_0$ (Theorem 4.2). Since $\mathbb{C}$ is an algebraically closed field of characteristic $0$, any sentence true in $\mathbb{C}$ is true in all models of $\mathrm{ACF}_0$.

For the equivalence with (iii), we use the ultraproduct construction. Consider the family $\{\tilde{\mathbb{F}}_p : p \in \text{Primes}\}$ and a nonprincipal ultrafilter $U$ on the set of primes. By the remark after the axioms of $\mathrm{ACF}$, the ultraproduct $\prod_{p \in \text{Primes}} \tilde{\mathbb{F}}_p / U$ is a model of $\mathrm{ACF}_0$. (The axioms of fields and algebraic closedness are preserved under ultraproducts by Loś's theorem; the characteristic becomes $0$ because for any prime $q$, the sentence $\neg(\underbrace{1+\cdots+1}_{q}=0)$ holds in all $\tilde{\mathbb{F}}_p$ for $p \neq q$, hence in $U$-almost all factors.)

Now, if $P$ holds in all but finitely many $\tilde{\mathbb{F}}_p$, then by Loś's theorem, $P$ holds in the ultraproduct $\prod \tilde{\mathbb{F}}_p / U$, and hence by completeness of $\mathrm{ACF}_0$, $P$ holds in all algebraically closed fields of characteristic $0$, including $\mathbb{C}$.

Conversely, if $P$ holds in $\mathbb{C}$ (hence in all models of $\mathrm{ACF}_0$), suppose for contradiction that $P$ fails in infinitely many $\tilde{\mathbb{F}}_p$. Then the set of primes where $\tilde{\mathbb{F}}_p \models \neg P$ is infinite. This set can be extended to an ultrafilter $V$, and the corresponding ultraproduct would be a model of $\mathrm{ACF}_0$ satisfying $\neg P$, contradicting completeness. Therefore $\neg P$ can hold in at most finitely many $\tilde{\mathbb{F}}_p$, i.e., $P$ holds in all but finitely many. $\square$
