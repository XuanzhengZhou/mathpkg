---
role: proof
locale: en
of_concept: structure-theorem-fg-lambda-modules
source_book: gtm059
source_chapter: "5"
source_section: "5"
---
The proof proceeds via an analogue of the Smith normal form algorithm over the Iwasawa algebra. Given a finite set of generators $u_1, \dots, u_m$ for $M$ and a matrix of relations $R$, one defines admissible operations on $R$ corresponding to: (O1) replacing a row with first entry not divisible by $p$ by a normalized one, (O2) adding a new generator to embed $M$ in a larger module with finite cokernel, and (O3) replacing a row by a combination with another row.

Using these operations and the Weierstrass Preparation Theorem as a substitute for the Euclidean algorithm, one transforms the relation matrix into a diagonal form with distinguished polynomials (or powers of $p$) on the diagonal. This corresponds to the quasi-isomorphism stated. The final decomposition into irreducible factors uses that if $f, g$ are relatively prime distinguished polynomials, the natural map $\Lambda/(fg) \to \Lambda/(f) \oplus \Lambda/(g)$ is an embedding with finite cokernel.
