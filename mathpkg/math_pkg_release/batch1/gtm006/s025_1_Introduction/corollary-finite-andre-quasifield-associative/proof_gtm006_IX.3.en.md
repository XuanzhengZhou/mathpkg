---
role: proof
locale: en
of_concept: corollary-finite-andre-quasifield-associative
source_book: gtm006
source_chapter: "IX"
source_section: "3"
---

From the parent discussion: associativity in $F_{\phi}$ requires that $\alpha_{xy} = \alpha_x \alpha_y$, meaning $\alpha$ is an anti-homomorphism. But $\nu$ is a homomorphism by construction, so $\phi$ must be an anti-homomorphism for associativity to hold.

Since $F$ is finite, $\Gamma$ is a cyclic group (the Galois group of a finite extension). In any cyclic group, every anti-homomorphism is a homomorphism, because for a cyclic group $\langle g \rangle$, an anti-homomorphism $f$ satisfies $f(g^n) = f(g)^n$ (since $f(g^n) = f(g^{n-1}g) = f(g)f(g^{n-1}) = \cdots = f(g)^n$, which coincides with the homomorphism property in the abelian setting of a cyclic group).

Thus in the finite case, $\phi$ being an anti-homomorphism is equivalent to $\phi$ being a homomorphism.

That $N = K^*$ follows by comparing the orders of these groups (see Exercise 9.4): in a finite field extension, the norm map is surjective onto the base field, so the image $N$ equals all of $K^*$.
