---
role: proof
locale: en
of_concept: stable-subspace-decomposition-via-generalized-eigenspaces
source_book: gtm023
source_chapter: "13"
source_section: "13.6"
---
Since the projection operators $\pi_i$ are polynomials in $\varphi$ (Theorem 13.5), it follows that $F$ is stable under each $\pi_i$. Indeed, for any $x \in F$, we have $\pi_i(x) = p_i(\varphi)(x)$ for some polynomial $p_i$, and since $F$ is stable under $\varphi$, it is stable under any polynomial in $\varphi$, hence under $\pi_i$.

Now for each $x \in F$, we have
$$x = \iota x = \sum_i \pi_i x,$$
and
$$\pi_i x \in F \cap E_i,$$
because $\pi_i$ maps into $E_i$ and preserves $F$. It follows that $x \in \sum_i F \cap E_i$, whence
$$F \subset \sum_i F \cap E_i.$$

The reverse inclusion $\sum_i F \cap E_i \subset F$ is obvious since each $F \cap E_i \subset F$ and $F$ is a subspace. Therefore
$$F = \sum_i (F \cap E_i),$$
establishing the decomposition (13.22).
