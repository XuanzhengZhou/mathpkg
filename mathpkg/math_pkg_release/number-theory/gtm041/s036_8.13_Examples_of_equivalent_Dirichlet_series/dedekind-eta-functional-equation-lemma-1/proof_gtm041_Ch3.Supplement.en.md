---
role: proof
locale: en
of_concept: dedekind-eta-functional-equation-lemma-1
source_book: gtm041
source_chapter: "3"
source_section: "Supplement"
---

We have
$$
A T^m = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & m \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a & am+b \\ c & cm+d \end{pmatrix}.
$$
Therefore
$$
\varepsilon(A T^m) = \exp\left\{\pi i\left(\frac{a + cm + d}{12c} - s(cm+d, c)\right)\right\}.
$$
By Theorem 3.5(a), $s(cm+d, c) = s(d, c)$. Hence
$$
\varepsilon(A T^m) = \exp\left\{\pi i\left(\frac{a+d}{12c} - s(d,c) + \frac{m}{12}\right)\right\} = e^{\pi i m/12} \, \varepsilon(A).
$$
