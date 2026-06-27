---
role: proof
locale: en
of_concept: theorem-zariski-ring
source_book: gtm029
source_chapter: "VIII"
source_section: "1"
---

Our hypothesis signifies that $f(E) = g^{-1}(0)$ and implies that $g(f(x)) = 0$ for every $x$ in $E$. Hence, by continuity, we have $\bar{g}(\bar{f}(\xi)) = 0$ for every $\xi$ in $\hat{E}$. Thus the kernel $\bar{g}^{-1}(0)$ of $\bar{g}$ contains the image $\bar{f}(\hat{E})$ of $\bar{f}$. We have to prove that these two submodules of $\hat{F}$ are equal, i.e., that every element $\eta$ of $\hat{F}$ such that $\bar{g}(\eta) = 0$ is in $\bar{f}(\hat{E})$.

The submodule $G' = g(F)$ of $G$ has the $\mathfrak{m}$-topology as induced topology (§2, Theorem 4). Thus its completion $\hat{G}'$ is identical with its closure in $\hat{G}$. By continuity $\bar{g}$ maps $\hat{F}$ into $\hat{G}'$, and, since $\bar{g}(\hat{F})$ is a closed submodule of $\hat{G}'$ (as $\hat{A}$ is a Zariski ring) which contains $g(F) = G'$, we have $\bar{g}(\hat{F}) = \hat{G}'$.

Consider now an element $\eta$ of $\hat{F}$ such that $\bar{g}(\eta) = 0$. We approximate $\eta$ by an element $y_n$ of $F$ such that $\eta - y_n \in \hat{A}\mathfrak{m}^n\hat{F} = \mathfrak{m}^n\hat{F}$. Then, since $\bar{g}(\eta) = 0$, we have $g(y_n) \in \mathfrak{m}^n\bar{g}(\hat{F}) \cap g(F) = \mathfrak{m}^n\hat{G}' \cap G' = \mathfrak{m}^n\hat{G}'$ (by Theorem 9, $(a')) = \mathfrak{m}^n g(F) = g(\mathf

module of relations satisfied by the $x_i$ over $\hat{A}$. As $\hat{R} = \hat{A}R$ (§2, Theorem 5), our assertion is proved.

We point out that Corollary 1 together with Theorem 5, §2, imply that the completion $\hat{E}$ is isomorphic to the tensor product $\hat{A} \otimes_A E$. The preservation of exactness proved in Theorem 11 is not a general property of tensor products; the fact that exactness is preserved in the present case means that the torsion functor $\text{Tor}_1^A(\hat{A}, E)$ is 0 for every finite $A$-module $E$.
