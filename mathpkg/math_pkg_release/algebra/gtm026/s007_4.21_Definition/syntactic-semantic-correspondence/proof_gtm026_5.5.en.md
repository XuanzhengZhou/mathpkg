---
role: proof
locale: en
of_concept: syntactic-semantic-correspondence
source_book: gtm026
source_chapter: "5"
source_section: "5"
---

**Proof of Theorem 5.5.** 

Define two passages in opposite directions.

**From syntactic to semantic (5.7):** Given $\omega \in XT$, define a natural transformation $\tilde{\omega}: U^X \longrightarrow U$ by setting, for each $T$-algebra $(Y, \theta)$ and each $f: X \longrightarrow Y$:

$$\langle f, (Y, \theta)\tilde{\omega} \rangle = \langle \omega, fT \cdot \theta \rangle$$

The naturality of $\tilde{\omega}$ follows from the naturality of the construction: for any $T$-homomorphism $h: (Y, \theta) \to (Y', \theta')$,

$$\langle f, (Y, \theta)\tilde{\omega} \cdot h \rangle = \langle \omega, fT \cdot \theta \cdot h \rangle = \langle \omega, fT \cdot hT \cdot \theta' \rangle = \langle f \cdot h, (Y', \theta')\tilde{\omega} \rangle$$

**From semantic to syntactic (5.9):** Given a natural transformation $\alpha: U^X \longrightarrow U$, define an element $\omega \in XT$ by:

$$\omega = \langle X\eta, (XT, X\mu)\alpha \rangle$$

where $(XT, X\mu)$ is the free $T$-algebra on $X$ and $X\eta: X \to XT$ is the unit.

**Verification that the passages are inverse.** Starting with $\omega$, apply (5.9) to $\tilde{\omega}$:
$$\langle X\eta, (XT, X\mu)\tilde{\omega} \rangle = \langle X\eta, XT\hat{\omega} \cdot X\mu \rangle = \langle \omega, X\eta T \cdot X\mu \rangle = \omega$$
by the monad law (3.16).

Starting with $\alpha$, for each $f: X \to Y$ and $T$-algebra structure $\theta$ on $Y$, let $\omega = \langle X\eta, (XT, X\mu)\alpha \rangle$. Then:
$$\langle f, (Y, \theta)\tilde{\omega} \rangle = \langle f, Y\hat{\omega} \cdot \theta \rangle = \langle X\eta, (XT, X\mu)\alpha \cdot fT \cdot \theta \rangle$$
By naturality of $\alpha$ applied to the $T$-homomorphism $f^\# = fT \cdot \theta: (XT, X\mu) \to (Y, \theta)$:
$$= \langle X\eta, (fT \cdot \theta)^X \cdot (Y, \theta)\alpha \rangle = \langle X\eta \cdot fT \cdot \theta, (Y, \theta)\alpha \rangle = \langle f \cdot Y\eta \cdot \theta, (Y, \theta)\alpha \rangle = \langle f, (Y, \theta)\alpha \rangle$$

Thus the two passages are mutually inverse bijections. $\square$
