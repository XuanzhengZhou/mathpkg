---
role: proof
locale: en
of_concept: spatial-rotation-characterization-of-redshift-surface
source_book: gtm048
source_chapter: "6"
source_section: "6.3.5"
---

($\Leftarrow$) Suppose such a spatial rotation $\psi$ exists. Then $\psi$ preserves the time orientation (Section 6.0.5c) as well as geodesics. By the definition of a light signal (Section 5.2), $\psi$ preserves light signals. Thus there is a light signal from $\psi x = y$ to $\psi z = z$. Moreover, by Lemma 6.0.9,
$$\tau(x, z) = \tau(\psi x, \psi z) = \tau(y, z).$$
Hence $y \in S$.

($\Rightarrow$) Conversely suppose $y \in S$. Let $\psi_y$ be an isometry that carries the light signal from $y$ to $z$ into the standard light signal (Exercise 5.2.5). Define $\psi_x$ similarly for the light signal from $x$ to $z$. Then
$$u^4 \psi_x z = u^4 z = u^4 \psi_y z$$
by Section 6.0.5; since $u^4$ increases monotonically along the standard photon, this implies $\psi_x z = \psi_y z$.

Similarly, the fact that $\tau$ is monotonic along the standard photon (Lemma 6.0.10) implies $\psi_x x = \psi_y y$. Thus the isometry $\psi = \psi_y^{-1} \circ \psi_x$ obeys $\psi z = z$ and $\psi x = y$. By definition, $\psi$ is a spatial rotation around $z$.
