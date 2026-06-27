---
role: proof
locale: en
of_concept: affine-classes-of-quadrics
source_book: gtm023
source_chapter: "X. Quadrics"
source_section: "§3. Affine equivalence of quadrics"
---

By the criterion in sec. 10.15, two quadrics with center are affine equivalent if and only if their associated bilinear functions have the same rank $r$ and the same index $s$. For a fixed rank $r$, the index $s$ can range from $1$ to $r$, giving $N_1(r) = r$ distinct classes.

By the criterion in sec. 10.16, two quadrics without center (written in the form $\Phi(x) + 2\langle a^*, x \rangle = 0$) are affine equivalent if and only if their bilinear functions have the same rank $r$ and the same index $s$, with the additional constraint $r \leq 2s$. For a fixed rank $r$, the admissible indices are $s = \lceil r/2 \rceil, \ldots, r$. The number of such integers is:
- If $r$ is odd: $r - \frac{r+1}{2} + 1 = \frac{r+1}{2}$,
- If $r$ is even: $r - \frac{r}{2} + 1 = \frac{r+2}{2}$.

Hence $N_2(r) = \frac{r+1}{2}$ for odd $r$ and $N_2(r) = \frac{r+2}{2}$ for even $r$, where $1 \leq r \leq n-1$.

The two families of normal forms displayed are obtained by choosing coordinates adapted to an orthogonal basis diagonalizing the bilinear form, with the linear part reduced to a single coordinate in the centerless case. These forms are pairwise inequivalent since they have distinct parameters $(r, s)$.
