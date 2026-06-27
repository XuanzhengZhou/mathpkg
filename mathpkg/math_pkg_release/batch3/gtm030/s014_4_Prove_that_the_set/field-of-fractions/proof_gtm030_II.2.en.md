---
role: proof
locale: en
of_concept: field-of-fractions
source_book: gtm030
source_chapter: "II"
source_section: "2"
---

Let $\mathfrak{B}$ be the set of pairs $(a,b)$ with $a,b \in \mathfrak{A}, b \neq 0$. Define $(a,b) \equiv (a',b')$ if $ab' = ba'$. This is an equivalence relation: reflexivity and symmetry are clear; for transitivity, if $ab' = ba'$ and $a'b'' = b'a''$, then $ab'b'' = ba'b'' = bb'a''$, and since $b' \neq 0$ and $\mathfrak{A}$ is an integral domain, $ab'' = ba''$.

Denote the equivalence class of $(a,b)$ by $a/b$. Define addition and multiplication by:
$$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}, \qquad \frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}.$$

If $a/b = a'/b'$ and $c/d = c'/d'$, then $ab' = ba'$ and $cd' = dc'$. Computing:
$$(ad+bc)b'd' = ab'dd' + cd'bb' = ba'dd' + dc'bb' = (a'd'+b'c')bd,$$
so addition is well-defined. Similarly, $acb'd' = a'c'bd$ shows multiplication is well-defined.

The set of these fractions with the given operations forms a commutative ring with identity $1 = b/b$ and zero $0 = 0/b$. If $a/b \neq 0$, then $a \neq 0$, so $b/a$ is a fraction and $(a/b)(b/a) = ab/ab = 1$. Thus every nonzero element is a unit, so $\mathfrak{F}$ is a field.

The map $a \mapsto \bar{a} = ab/b$ (for any $b \neq 0$) is well-defined, injective (since $ab/b = a'b'/b'$ implies $ab' = a'b$, and since $\mathfrak{A}$ is an integral domain, $a = a'$), and a homomorphism (since $\overline{a + a'} = (a+a')b/b = ab/b + a'b/b$ and $\overline{aa'} = aa'b^2/b^2 = (ab/b)(a'b/b)$). Thus $\mathfrak{A} \cong \bar{\mathfrak{A}} \subseteq \mathfrak{F}$, completing the proof.
