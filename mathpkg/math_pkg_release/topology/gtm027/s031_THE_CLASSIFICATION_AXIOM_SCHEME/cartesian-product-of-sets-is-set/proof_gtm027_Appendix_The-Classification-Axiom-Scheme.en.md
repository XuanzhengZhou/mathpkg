---
role: proof
locale: en
of_concept: cartesian-product-of-sets-is-set
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Cartesian Product of Sets is a Set

PROOF Let $f$ be the function such that domain $f = x$ and $f(u) = \{u\} \times y$ for $u$ in $x$. (There is a unique function of this sort; namely, $f = \{(u,z): u \in x \text{ and } z = \{u\} \times y\}$.) Because of the axiom of substitution, range $f$ is a set. By a direct computation range $f = \{z: \text{for some } u, u \in x \text{ and } z = \{u\} \times y\}$. Consequently range $f$, which by the axiom of amalgamation is a set, is $x \times y$.
