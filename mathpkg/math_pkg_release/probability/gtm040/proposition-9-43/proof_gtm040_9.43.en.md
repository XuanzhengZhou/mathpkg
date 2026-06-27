---
role: proof
locale: en
of_concept: proposition-9-43
source_book: gtm040
source_chapter: "9"
source_section: "43"
---

**Proof:** Let $g = B^Ex - (\lambda^Ex)1$. Then $g$ is bounded, and

$$(I - P)g = \binom{(I - P^E)x_E}{0};$$

therefore $g$ is regular on $\tilde{E}$. Since $\lambda^Eg = 0, g$ is a potential with support in $E$, by Proposition 9-42; and $g$ differs from $x$ by the constant $\lambda^Ex$ on $E$.

For uniqueness, let $g'$ be another such potential. Then $g_E - g'_E = k1$ and $g - g' = B^Eg - B^Eg'$. Then $g - g' = k1$. Since $P^n(g - g') \to 0$, we must have $k = 0$. Hence $g = g'$.

The result to follow is the total-charge-zero version of the Princ

PROOF: For existence, let $x$ be a function which is 1 on $E$ and 0 on $F$, and set $h = B^{E \cup F}x$. By Proposition 9-43, (1) and (3) are satisfied and $f$ has support in $E \cup F$. For (2) we note that, if $i \in E$, then $f_i$ is the probability of return to $F$ before $E$ and, if $i \in F$, then $-f_i$ is the probability of return to $E$ before $F$.

For uniqueness, let $x$ be a function satisfying (1), (2), and (3). Then $x = g + c1$, where $g$ is a potential, by (3). By (2),

$$(I - P)g = (I - P)x$$

vanishes outside of $E \cup F$ so that $g$ has support in $E \cup F$. Hence $g = B^{E \cup F}g$. Therefore,

$$B^{E \cup F}x = B^{E \cup F}g + B^{E \cup F}(c1) = g + c1 = x,$$

and $x$ is uniquely determined by its values on $E \cup F$, which are fixed by (1).

We conclude this section with some results about normal chains which will be needed later.
