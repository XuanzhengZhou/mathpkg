---
role: exercise
locale: en
chapter: "II"
section: "6"
exercise_number: 11
---
**The Grothendieck Group of a Nonsingular Curve.** Let $X$ be a nonsingular curve over an algebraically closed field $k$. We will show that $K(X) \cong \text{Pic} X \oplus \mathbb{Z}$, in several steps.

(a) For any divisor $D = \sum n_i P_i$ on $X$, let $\psi(D) = \sum n_i \gamma(k(P_i)) \in K(X)$, where $k(P_i)$ is the skyscraper sheaf $k$ at $P_i$ and $0$ elsewhere. If $D$ is an effective divisor, let $\mathcal{O}_D$ be the structure sheaf of the associated subscheme of codimension 1, and show that $\psi(D) = \gamma(\mathcal{O}_D)$. Then use (6.18) to show that for any $D$, $\psi(D)$ depends only on the linear equivalence class of $D$, so $\psi$ defines a homomorphism $\psi: \text{Cl} X \to K(X)$.

(b) Show that the composition $\text{Cl} X \xrightarrow{\psi} K(X) \xrightarrow{\text{rank}} \mathbb{Z}$ is the degree map, so the image of $\psi$ is contained in the kernel of the rank map.

(c) Using the exact sequence of (c) in the previous exercise for a suitable subscheme, show that $\psi$ and the rank map together give an isomorphism $K(X) \cong \text{Pic} X \oplus \mathbb{Z}$.

For further information about $K(X)$, and its applications to the generalized Riemann-Roch theorem, see Borel-Serre [1], Manin [1], and Appendix A.
