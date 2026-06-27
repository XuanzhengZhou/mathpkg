---
role: proof
locale: en
of_concept: finite-dim-algebra-without-zero-divisors-is-division-ring
source_book: gtm032
source_chapter: "Introduction"
source_section: "2"
---

Let $\mathfrak{A}$ be a finite-dimensional algebra over $\Phi$ without zero divisors. For any non-zero $a \in \mathfrak{A}$, consider the left multiplication map $a_L: x \mapsto ax$. Since $\mathfrak{A}$ has no zero divisors, $a_L(x) = 0$ implies $x = 0$, so $a_L$ is an injective linear transformation of the finite-dimensional vector space $\mathfrak{A}/\Phi$. By finite-dimensionality, $a_L$ is also surjective, so there exists $b \in \mathfrak{A}$ with $a_L(b) = ab = 1$. Thus $a$ has a right inverse $b$.

Similarly, the right multiplication $a_R: x \mapsto xa$ is injective (since $xa = 0$ implies $x = 0$), hence surjective, giving $c \in \mathfrak{A}$ with $ca = 1$. Then $c = c(ab) = (ca)b = b$, so $b = c$ is a two-sided inverse. Thus every non-zero element is a unit and $\mathfrak{A}$ is a division ring.
