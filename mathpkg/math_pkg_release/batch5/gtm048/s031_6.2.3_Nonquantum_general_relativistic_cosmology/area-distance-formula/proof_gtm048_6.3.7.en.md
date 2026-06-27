---
role: proof
locale: en
of_concept: area-distance-formula
source_book: gtm048
source_chapter: "6"
source_section: "6.3.7"
---

By the definition of $A$ (Corollary 6.3.5) and the results in the proof of Proposition 6.3.4, we compute:

\begin{align*}
A &= 4\pi (u^4 x)^{4/3} \delta^2(x, z) \\
  &= 4\pi \tau^{-2} \left(\frac{2t}{3}\right)^{4/3} \cdot 9 \left[ \left(\frac{2t}{3}\right)^{1/3} - \tau^{-1/2}\left(\frac{2t}{3}\right)^{1/3} \right]^2 \\
  &= 16\pi \tau^{-2} \bigl[t(1 - \tau^{-1/2})\bigr]^2 \\
  &= 4\pi \tau^{-2} d^2(\tau).
\end{align*}

Since $\Omega / A = 4\pi / A$ by Proposition 6.3.5a (the spherical symmetry of $S$ about $z$), substituting the expression for $A$ gives
$$\frac{\Omega}{A} = \frac{4\pi}{4\pi \tau^{-2} d^2} = \left(\frac{\tau}{d}\right)^2.$$

By the operational definition of area-distance (Section 6.1.6b),
$$d_A = \left(\frac{A}{\Omega}\right)^{1/2} = \frac{d}{\tau}.$$
