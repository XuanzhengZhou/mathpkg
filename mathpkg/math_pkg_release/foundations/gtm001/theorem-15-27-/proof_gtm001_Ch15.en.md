---
role: proof
locale: en
of_concept: theorem-15-27-
source_book: gtm001
source_chapter: "15"
source_section: ""
---

Propositions 15.22, 15.25, 15.26, and Theorem 14.11. $\square$

Remark. We have now shown that $L$ is a model of ZF and for each $a \subseteq \omega$, $L_a$ is a model of ZF; but are these models different? It is not difficult to show that if $a$ is constructible then $L_a = L$. Do there exist nonconstructible sets? From Cohen’s work we know that this question is undecidable in ZF.

The assumption that every set is constructible is called the Axiom

ZF. This is done by proving that $L$ is a model of $V = L$. To prove this we must prove in ZF that

$$[V = L]^L$$

that is, since $L = \{x | (\exists \alpha)[x = F' \alpha]\}$ we must prove that

$$L = \{x \in L | (\exists \alpha \in L)[x = F' \alpha]^L\}.$$

Since On $\subseteq L$ it is sufficient to prove that $x = F' \alpha$ is absolute with respect to $L$. This we will do by proving that $x = F' \alpha$ is absolute with respect to every standard transitive model of ZF. We need the following lemmas in which $M$ is a standard transitive model of ZF and $G$ is as given in Definition 15.13.
