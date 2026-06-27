---
role: proof
locale: en
of_concept: james-theorem
source_book: gtm024
source_chapter: "III"
source_section: "§19. The Theorem of James"
---

The proof proceeds by contrapositive. Assume $B_X$ is not weakly compact. Then there exists a sequence $(x_n) \subset B_X$ with no weak cluster point. By the Eberlein-Smulian theorem, we may assume $(x_n)$ has no weakly convergent subsequence. One constructs a sequence of functionals $(\phi_n) \subset B_{X'}$ and a $\theta > 0$ such that $\phi_n(x_n) \geqslant \theta$ while $\phi_n(x_m) \to 0$ for each fixed $m$. Then define $\psi = \sum \lambda_n \phi_n$ with suitable $(\lambda_n)$. By careful choice of the $\lambda_n$, one shows that $\psi$ does not attain its supremum on $B_X$, contradicting the hypothesis. The construction relies on the geometric properties of the unit ball and the separation theorem. The converse direction (reflexivity implies weak compactness of $B_X$) follows from the Banach-Alaoglu theorem and the fact that the canonical embedding is a weak-to-weak* homeomorphism.
