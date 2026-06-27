---
role: proof
locale: en
of_concept: existence-and-uniqueness-of-invariant-measure
source_book: gtm042
source_chapter: "4"
source_section: "4.2 Invariant measure on a compact group"
---

The proof of the existence and uniqueness of the Haar measure on a compact group is a classical result in harmonic analysis. For the complete proof, see the references cited in the bibliography of Serre's text: [1], [4], [6].

We give two examples to illustrate the measure:

(1) If $G$ is finite of order $g$, the measure $dt$ is obtained by assigning to each element $t \in G$ a mass equal to $1/g$. Then for any function $f$,
\[
\int_G f(t)\,dt = \frac{1}{g} \sum_{t \in G} f(t),
\]
which satisfies both right-invariance and total mass $1$.

(2) If $G$ is the group $C_\infty$ of rotations in the plane, and we represent the elements $t \in G$ in the form $t = e^{i\alpha}$ (with $\alpha$ taken modulo $2\pi$), the invariant measure is $\frac{1}{2\pi}\,d\alpha$. The factor $1/2\pi$ is used to insure condition (ii), i.e., total mass equal to $1$.
