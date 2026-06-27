---
role: proof
locale: en
of_concept: integrable-potentials-characterization
source_book: gtm040
source_chapter: "9"
source_section: "3"
---

Set $f = (I - P)g$. Then $\alpha f = \alpha[(I - P)g] = \alpha g - \alpha(Pg) = \alpha g - \alpha g = 0$ since $\alpha P = \alpha$. By Proposition 9-44, $f$ is a charge. The potential of $f$ is

$$\lim P^n \, ^{0}\!N f = \lim P^n (g - P^n g) = \lim (P^n g - P^{2n} g) = 0$$

by Lemma 9-52, since $\alpha g$ is finite. Therefore $g$ and $^{0}\!N f$ differ by a harmonic function. Since both have finite $\alpha$-means and the only bounded harmonic functions are constants, we obtain

$$g = \,^{0}\!N f - A\,^{0}\!N f = (I - A)\,^{0}\!N f.$$

For the converse, if $\alpha g = 0$, then setting $f = (I - P)g$ yields $\alpha f = 0$, and the construction above shows $g$ is a potential.
