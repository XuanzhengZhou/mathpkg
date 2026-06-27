---
role: proof
locale: en
of_concept: keplers-first-law
source_book: gtm060
source_chapter: "2"
source_section: "Supplement: Kepler Problem"
---

Starting from conservation of angular momentum $M$ and energy $E$ in the central field $U(r) = -k/r$, the equation of motion in polar coordinates yields

$$\dot r = \sqrt{\frac{2}{m}\left(E + \frac{k}{r}\right) - \frac{M^2}{r^2}}.$$

By eliminating time using $dt = (r^2/M) d\varphi$, we obtain

$$\frac{dr}{d\varphi} = \frac{r^2}{M} \sqrt{2(E + k/r) - M^2/r^2}.$$

Separating variables and integrating gives

$$\varphi = \arccos \frac{\frac{M}{r} - \frac{k}{M}}{\sqrt{2E + \frac{k^2}{M^2}}}.$$

Defining the parameter $p = M^2/k$ and eccentricity $e = \sqrt{1 + 2EM^2/k^2}$, this simplifies to

$$\varphi = \arccos \frac{(p/r) - 1}{e},$$

or equivalently the focal equation

$$r = \frac{p}{1 + e \cos \varphi}.$$

When $E < 0$, we have $e < 1$ and the orbit is an ellipse with the center of force at one focus.
