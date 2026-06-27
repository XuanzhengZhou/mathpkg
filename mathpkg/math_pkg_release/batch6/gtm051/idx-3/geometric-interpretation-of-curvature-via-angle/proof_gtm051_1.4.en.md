---
role: proof
locale: en
of_concept: geometric-interpretation-of-curvature-via-angle
source_book: gtm051
source_chapter: "1"
source_section: "1.4"
---

Differentiate the defining equations for $\theta(t)$ with respect to $t$:

$$-\sin \theta(t) \dot{\theta}(t) = \dot{e}_1(t) \cdot v,$$
$$\cos \theta(t) \dot{\theta}(t) = -\dot{e}_2(t) \cdot v.$$

Using the Frenet equations for plane curves, $\dot{e}_1(t) = \omega_{12}(t) e_2(t)$ and $\dot{e}_2(t) = -\omega_{12}(t) e_1(t)$, we substitute:

$$-\sin \theta(t) \dot{\theta}(t) = \omega_{12}(t) e_2(t) \cdot v.$$

From the definition of $\theta(t)$, $\sin \theta(t) = -e_2(t) \cdot v$, so $e_2(t) \cdot v = -\sin \theta(t)$. Hence

$$-\sin \theta(t) \dot{\theta}(t) = \omega_{12}(t) (-\sin \theta(t)),$$

which gives $\dot{\theta}(t) = \omega_{12}(t)$. By definition of curvature, $\kappa(t) = \omega_{12}(t)/|\dot{c}(t)|$, so $\dot{\theta}(t) = \kappa(t) |\dot{c}(t)|$. When $|\dot{c}(t)| = 1$, this reduces to $\kappa(t) = \dot{\theta}(t)$.
