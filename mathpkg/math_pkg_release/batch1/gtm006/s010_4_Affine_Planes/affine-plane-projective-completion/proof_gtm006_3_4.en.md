---
role: proof
locale: en
of_concept: affine-plane-projective-completion
source_book: gtm006
source_chapter: "3"
source_section: "4"
---

**Proof.** We first construct a projective plane $\mathcal{P}$ from $\mathcal{A}$.

*Construction of $\mathcal{P}$:* The points of $\mathcal{P}$ are of two types:
\begin{itemize}
\item The points of $\mathcal{A}$ (affine points).
\item For each parallel class of lines of $\mathcal{A}$, a new point (called a point at infinity).
\end{itemize}
The lines of $\mathcal{P}$ are of two types:
\begin{itemize}
\item The lines of $\mathcal{A}$ (affine lines), each augmented with the point at infinity corresponding to its parallel class.
\item One new line $l_\infty$ (the line at infinity) consisting of all the points at infinity.
\end{itemize}
Incidence in $\mathcal{P}$ is defined as follows: an affine point is incident with an affine line if it was incident in $\mathcal{A}$; an affine point is not incident with $l_\infty$; a point at infinity $A^*$ is incident with every affine line in the parallel class $A^*$ and with $l_\infty$.

*Verification that $\mathcal{P}$ is a projective plane:* Any two affine points determine a unique line (the affine line through them). An affine point $X$ and a point at infinity $A^*$ determine the unique affine line through $X$ that belongs to the parallel class $A^*$ (which exists by Playfair's axiom). Two distinct points at infinity determine the line $l_\infty$. Thus any two points determine a unique line.

Now verify that any two lines intersect in a unique point. Two affine lines from different parallel classes intersect in $\mathcal{A}$ (by definition of parallel class). Two affine lines from the same parallel class intersect at their common point at infinity. An affine line and $l_\infty$ intersect at the point at infinity of the parallel class of that affine line. Thus any two lines intersect in a unique point.

Since $\mathcal{A}$ contains three non-collinear points $X, Y, Z$, let $XY \cap l_\infty = A^*$ and $YZ \cap l_\infty = B^*$. Since $XY$ is not parallel to $YZ$, $A^* \neq B^*$, and $X, Z, A^*, B^*$ form a quadrangle. Thus $\mathcal{P}$ is a projective plane, and by construction $\mathcal{A} = \mathcal{P}^{l_\infty}$.

*Uniqueness:* Suppose $\mathcal{A} = \mathcal{P}^l = \mathcal{Q}^m$ for two projective planes $\mathcal{P}, \mathcal{Q}$ with lines $l, m$. We need to show $\mathcal{P} \cong \mathcal{Q}$. This follows from Lemma 3.11, which shows that $\mathcal{P}^l \cong \mathcal{P}^m$ if and only if there is an automorphism of $\mathcal{P}$ sending $l$ to $m$. Since the identity on $\mathcal{A}$ extends to an isomorphism $\mathcal{P}^l \to \mathcal{Q}^m$, we obtain the desired isomorphism $\mathcal{P} \cong \mathcal{Q}$. $\square$
