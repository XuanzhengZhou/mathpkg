---
role: proof
locale: en
of_concept: dedekind-eta-functional-equation-lemma-2
source_book: gtm041
source_chapter: "3"
source_section: "Supplement"
---

We consider the case $d > 0$ first. Using the representation
$$
AS = \begin{pmatrix} -b & a \\ -d & c \end{pmatrix},
$$
and the fact that $s(-c, d) = -s(c, d)$ by Theorem 3.5(a), the reciprocity law for Dedekind sums gives
$$
s(c, d) + s(d, c) = \frac{c}{12d} + \frac{d}{12c} - \frac{1}{4} + \frac{1}{12cd}.
$$
Replace $1$ in the numerator of the last term by $ad - bc$ and rearrange:
$$
\frac{b-c}{12d} + s(c, d) = \frac{a+d}{12c} - s(d, c) - \frac{1}{4}.
$$
Substituting this into the expression for $\varepsilon(AS)$ yields $\varepsilon(AS) = e^{-\pi i/4} \varepsilon(A)$.

If $d < 0$, we use $AS = \begin{pmatrix} -b & a \\ -d & c \end{pmatrix}$ and the reciprocity law in the form
$$
s(c, -d) + s(-d, c) = \frac{c}{-12d} - \frac{d}{12c} - \frac{1}{4} - \frac{ad-bc}{12cd}.
$$
Rearranging and using $s(-d, c) = -s(d, c)$ gives $\varepsilon(AS) = e^{\pi i/4} \varepsilon(A)$.
