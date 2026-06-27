---
role: proof
locale: en
of_concept: banach-from-complete-subspace-and-quotient
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "16. Normed spaces, Banach spaces"
---

# Proof of Banach Space from Complete Subspace and Quotient

**Theorem (16.12).** If $E$ is a normed space and if $M$ is a closed linear subspace such that $M$ and $E/M$ are Banach spaces (for the relative norm and the quotient norm, respectively), then $E$ is a Banach space.

*Proof.* In view of (16.7) and (16.10), the theorem is immediate from (12.2). For a more direct proof, repeat (in additive notation) the argument in the proof of (9.2):

Let $(x_n)$ be a Cauchy sequence in $E$. Then $(\pi(x_n))$ is Cauchy in $E/M$, hence converges to some $u \in E/M$. Write $u = \pi(x)$ for some $x \in E$. Then $\pi(x_n - x) \to \theta_{E/M}$, so there exist $m_n \in M$ such that $x_n - x - m_n \to \theta$ in $E$. Since $(x_n)$ is Cauchy, $(m_n)$ is Cauchy in $M$, hence $m_n \to m \in M$ by completeness of $M$. Then $x_n \to x + m$ in $E$, proving completeness. $\square$
