---
role: proof
locale: en
of_concept: semisimple-nilpotent-decomposition
source_book: gtm023
source_chapter: "12"
source_section: "4. The structure of factor algebras"
---

**1. Existence.** Identify the subalgebra $\Gamma(x)$ with the factor algebra $\Gamma(\bar{t}) = \Gamma[t]/I_f$ via $x = \bar{t}$. Lemma IV (cf. sec. 12.17) yields elements $u \in \Gamma[t]$ and $\omega \in \Gamma[t]$ with the following properties:

(i) $g^k \mid g(u)$,
(ii) $u + \omega = t$,
(iii) $g$ divides $\omega$.

Projection onto the quotient algebra yields the relations

$$g(\bar{u}) = 0 \tag{12.25}$$

$$\bar{\omega}^k = 0, \tag{12.26}$$

and

$$\bar{u} + \bar{\omega} = \bar{t}. \tag{12.27}$$

Now set $x_S = \bar{u}$ and $x_N = \bar{\omega}$. Then $g(x_S) = 0$, so the minimum polynomial of $x_S$ divides $g$. Since $g$ is the product of distinct irreducible polynomials, $x_S$ is semisimple. Relation (12.26) shows that $x_N$ is nilpotent with $x_N^k = 0$, and (12.27) gives $x = x_S + x_N$. The minimum polynomial of $x_S$ is exactly $g$ (otherwise a proper divisor would annihilate $x$, contradicting that $f$ is the minimum polynomial), and the minimum polynomial of $x_N$ is $t^k$.

**2. Uniqueness.** Suppose $x = x_S' + x_N'$ is another such decomposition. Since $x_S$ and $x_S'$ are polynomials in $x$ (they are obtained from $x$ via polynomial expressions), they commute with each other and with $x_N, x_N'$. Then $x_S - x_S' = x_N' - x_N$ is both semisimple and nilpotent, hence must be zero. Thus $x_S = x_S'$ and $x_N = x_N'$.
