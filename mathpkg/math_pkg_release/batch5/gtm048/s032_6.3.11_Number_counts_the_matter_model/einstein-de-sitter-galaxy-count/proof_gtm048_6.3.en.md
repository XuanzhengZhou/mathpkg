---
role: proof
locale: en
of_concept: einstein-de-sitter-galaxy-count
source_book: gtm048
source_chapter: "6"
source_section: "6.3.11"
---

Since $\operatorname{div}(\eta P) = 0$, we have $N = -\int_{\mathcal{B}'} \eta \, i(P) \, \Omega$ by Stokes' theorem. By Exercise 3.2.5, the number-density form is

$$\eta = \frac{1}{m} n(u^4 z) (u^4 z)^2 (u^4)^{-2}.$$

Now $i(P) \Omega = m \, i(\partial_4) \Omega = -m (u^4)^2 \, du^1 \wedge du^2 \wedge du^3$, where we have used Lemma 6.2.6 for the volume form $\Omega$. Combining these:

$$\eta \, i(P) \Omega = \frac{1}{m} n(u^4 z) (u^4 z)^2 (u^4)^{-2} \cdot \bigl(-m (u^4)^2\bigr) \, du^1 \wedge du^2 \wedge du^3 = -n(u^4 z) (u^4 z)^2 \, du^1 \wedge du^2 \wedge du^3.$$

Hence

$$N = -\int_{\mathcal{B}'} \eta \, i(P) \Omega = n(u^4 z) (u^4 z)^2 \int_{\mathcal{B}'} du^1 \wedge du^2 \wedge du^3.$$

The integral $\int_{\mathcal{B}'} du^1 \wedge du^2 \wedge du^3$ over the lightlike 3-submanifold $\mathcal{B}'$ (diffeomorphic to $S^2 \times \mathbb{R}$ and forming the lateral boundary of the compact region $\mathcal{A}$ in the causal past) evaluates to the comoving 3-volume of a ball of comoving radius $d(\tau_0) / (u^4 z)$. In the Einstein--de Sitter model the scale factor is $a(t) \propto t^{2/3}$, so the comoving radial coordinate corresponding to the angular-diameter distance $d(\tau_0)$ is $d(\tau_0) / (u^4 z)$, giving

$$\int_{\mathcal{B}'} du^1 \wedge du^2 \wedge du^3 = \frac{4\pi}{3} \left( \frac{d(\tau_0)}{u^4 z} \right)^3.$$

Substituting back:

$$N = n(u^4 z) (u^4 z)^2 \cdot \frac{4\pi}{3} \frac{d(\tau_0)^3}{(u^4 z)^3} = \frac{4\pi}{3} n(u^4 z) \, d(\tau_0)^3.$$

Using the relation $\tau_0 d(\tau_0) = d_0$ (Proposition 6.3.8), we have $d(\tau_0) = d_0 / \tau_0$, and therefore

$$N = \frac{4\pi}{3} n(u^4 z) \frac{d_0^3}{\tau_0^3},$$

which completes the proof.
