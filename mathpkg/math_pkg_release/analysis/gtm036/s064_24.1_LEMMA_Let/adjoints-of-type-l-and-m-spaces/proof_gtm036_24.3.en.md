---
role: proof
locale: en
of_concept: adjoints-of-type-l-and-m-spaces
source_book: gtm036
source_chapter: "24"
source_section: "24.3"
---

If $E$ is a normed lattice, then surely $E^*$ is a Banach space. If $f$ is a continuous positive linear functional on $E$, then
$$\|f\| = \sup \{f(x): x \geq 0 \text{ and } \|x\| \leq 1\}$$
because $\|x\| = \| |x| \| \geq \|x^+\| \vee \|x^-\|$ and one of the two numbers $f(x^+)$ and $f(x^-)$ is necessarily as great as $|f(x)|$. Consequently, if $f$ and $g$ are bounded positive functionals, then $f \wedge g$ is also bounded, and it follows that $E^*$ is a lattice. Moreover, since the meet of $f$ and $g$ in the order dual $E^*$ is identical with the meet in the adjoint $E^*$, it follows from the calculation made after 23.9 that, for a positive element $x$,
$$|f|(x) = \sup \{f(y): |y| \leq x\}.$$
Hence,
$$\|f\| = \sup \{|f|(x): x \geq 0 \text{ and } \|x\| \leq 1\} = \sup \{f(y): \|y\| \leq 1\} = \|f\|.$$

[The proof continues by verifying that if $E$ is an $M$ space, then $E^*$ satisfies the $L$ space norm condition $\|f + g\| = \|f\| + \|g\|$ for positive disjoint $f, g$, using the characterization of lattice homomorphisms from Theorem 24.2. Conversely, if $E$ is an $L$ space, then $E^*$ satisfies the $M$ space condition and possesses a unit given by the norm functional.]
