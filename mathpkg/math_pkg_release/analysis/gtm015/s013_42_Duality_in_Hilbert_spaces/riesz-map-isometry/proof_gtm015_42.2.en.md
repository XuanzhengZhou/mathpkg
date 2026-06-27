---
role: proof
locale: en
of_concept: riesz-map-isometry
source_book: gtm015
source_chapter: "42. Duality in Hilbert spaces"
source_section: "42.2"
---

# Proof of The Riesz Map is Conjugate-Linear and Isometric

Let $E$ be an inner product space. For each $y \in E$, define $y' \in E'$ by $y'(x) = (x|y)$ for all $x \in E$.

**Conjugate-linearity.** For $y, z \in E$ and $\lambda \in \mathbb{C}$, we have for all $x \in E$:

$$(y+z)'(x) = (x|y+z) = (x|y) + (x|z) = y'(x) + z'(x) = (y'+z')(x),$$

hence $(y+z)' = y' + z'$. Also,

$$(\lambda y)'(x) = (x|\lambda y) = \lambda^* (x|y) = \lambda^* y'(x) = (\lambda^* y')(x),$$

hence $(\lambda y)' = \lambda^* y'$. Thus the map $y \mapsto y'$ is conjugate-linear.

**Isometry.** By the Cauchy-Schwarz inequality (41.7),

$$|y'(x)| = |(x|y)| \leq \|x\| \|y\|$$

for all $x \in E$, whence $\|y'\| \leq \|y\|$. On the other hand,

$$\|y'\| \|y\| \geq |y'(y)| = |(y|y)| = \|y\|^2,$$

from which $\|y'\| \geq \|y\|$ (if $y \neq \theta$; the case $y = \theta$ is trivial). Therefore $\|y'\| = \|y\|$, establishing that the Riesz map $y \mapsto y'$ is isometric.
