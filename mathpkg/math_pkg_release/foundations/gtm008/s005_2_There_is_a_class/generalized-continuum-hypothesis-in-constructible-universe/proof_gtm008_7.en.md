---
role: proof
locale: en
of_concept: generalized-continuum-hypothesis-in-constructible-universe
source_book: gtm008
source_chapter: "7"
source_section: "Relative Constructibility"
---
Let $b$ be transitive with $\bar{b} = \aleph_\alpha$. Let $A$ be the closure of $b$ under all of the functions in $F$. Then $\bar{A} = \bar{b} = \aleph_\alpha$ and, by Theorem 7.31

$$\langle A, \in, k \rangle \models ZF + V = L_k.$$

From the Lemma (Mostowski collapse) there exists a transitive set $a_0$ and a function $f$ from $A$ one-to-one onto $a_0$ such that $f$ preserves the $\in$-relation. Since $b$ is a transitive subset of $A$, $f$ is the identity function on $b$, in particular $f(k) = k$. Therefore $\langle a_0, \in, k \rangle \models ZF + V = L_k$. By Theorem 7.32

$$(\exists \beta)[a_0 = A_\beta].$$

But $\bar{a}_0 = \bar{A} = \aleph_\alpha$. Hence $\bar{\beta} \leq \aleph_\alpha$ i.e., $\beta < \aleph_{\alpha+1}$. Since $a = f(a) \in f''A = a_0$, this proves that $(\forall a \subseteq \aleph_\alpha)(\exists \beta < \aleph_{\alpha+1})[a \in A_\beta]$. Therefore

$$\mathcal{P}(\aleph_\alpha) \subseteq A_{\aleph_{\alpha+1}}.$$

But $\bar{A}_{\aleph_{\alpha+1}} = \aleph_{\alpha+1}$, so $\mathcal{P}(\aleph_\alpha) = \aleph_{\alpha+1}$.
