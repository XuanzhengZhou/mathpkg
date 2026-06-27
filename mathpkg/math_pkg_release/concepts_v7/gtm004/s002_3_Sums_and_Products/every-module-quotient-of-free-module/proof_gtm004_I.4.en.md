---
role: proof
locale: en
of_concept: every-module-quotient-of-free-module
source_book: gtm004
source_chapter: "I. Modules"
source_section: "4. Free and Projective Modules"
---

# Proof that Every Module is a Quotient of a Free Module

Let $S$ be a set of generators of $A$ (for instance, we may take $S = A$ itself). For each $s \in S$, let $\Lambda_s = \Lambda$ as a left $\Lambda$-module. Form the free module

$$P = \bigoplus_{s \in S} \Lambda_s.$$

By Proposition 4.1, $P$ is free on the set $\{1_{\Lambda_s} : s \in S\}$. Define a function $f : S \to A$ by $f(s) = s$ for all $s \in S$. By Proposition 4.2 (universal property of the free module), $f$ extends uniquely to a $\Lambda$-module homomorphism

$$\varphi : P \to A, \qquad \varphi(1_{\Lambda_s}) = s.$$

Since $S$ generates $A$, every element of $A$ is a finite $\Lambda$-linear combination of elements of $S$, hence lies in the image of $\varphi$. Thus $\varphi$ is surjective, and $A \cong P / \ker \varphi$ is a quotient of the free module $P$.
