---
role: proof
locale: en
of_concept: proposition-16-2-annihilator-closure-properties
source_book: gtm055
source_chapter: "16"
source_section: "16.2"
---

**Proof of (i).** Let $M \subset \mathcal{E}$ and let $\mathcal{M}$ be the smallest closed linear manifold in $\mathcal{E}$ containing $M$. From the definition it is clear that $M \subset \,^a(M^a)$. On the other hand, if $x_0 \in \mathcal{E}$ does not belong to $\mathcal{M}$, then by the Hahn–Banach theorem (Proposition 14.13) there exists an element $f_0 \in M^a$ such that $f_0(x_0) \neq 0$. But then $x_0 \notin \,^a(M^a)$. Hence $\mathcal{M} = \,^a(M^a)$.

**Proof of (ii).** Let $M \subset \mathcal{E}^*$ and let $\mathcal{M}$ be the smallest weak$^*$ closed linear submanifold of $\mathcal{E}^*$ containing $M$. Clearly $M \subset (^a M)^a$. If $f_0 \in \mathcal{E}^*$ does not belong to $\mathcal{M}$, then there exists a vector $x_0 \in \,^a M$ such that $f_0(x_0) \neq 0$ (this uses the fact that the weak$^*$ continuous linear functionals on $\mathcal{E}^*$ are precisely those of the form $F_x$, $x \in \mathcal{E}$, cf. Problem 15J). Thus $f_0 \notin (^a M)^a$, and it follows that $\mathcal{M} = (^a M)^a$.
