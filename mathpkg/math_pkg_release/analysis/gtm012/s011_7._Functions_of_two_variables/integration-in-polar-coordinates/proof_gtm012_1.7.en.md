---
role: proof
locale: en
of_concept: integration-in-polar-coordinates
source_book: gtm012
source_chapter: "1"
source_section: "7. Functions of two variables"
---

# Proof of Theorem 7.4: Integration in Polar Coordinates

**Theorem 7.4.** Suppose $f$ is a continuous complex-valued function defined on the disc

$$D_R = \{(x, y) \mid x^2 + y^2 < R\}.$$

Suppose $g$ is related to $f$ by

$$g(r, \theta) = f(r \cos \theta, r \sin \theta). \tag{7.5}$$

Then

$$\iint_{D_R} f(x, y) \, dx \, dy = \int_0^R \int_0^{2\pi} g(r, \theta) \, r \, dr \, d\theta.$$

More explicitly,

$$\int_{-R}^R \left\{ \int_{-(R^2 - y^2)^{1/2}}^{(R^2 - y^2)^{1/2}} f(x, y) \, dx \right\} dy = \int_0^R \left\{ \int_0^{2\pi} g(r, \theta) \, d\theta \right\} r \, dr.$$

**Proof (sketch).** The transformation from Cartesian to polar coordinates is given by

$$x = r \cos \theta, \quad y = r \sin \theta,$$

with the inverse relations

$$r = (x^2 + y^2)^{1/2}, \quad \theta = \tan^{-1}(y/x).$$

Any point $p$ of the plane other than the origin is determined uniquely either by its Cartesian coordinates $(x, y)$ or by its polar coordinates $(r, \theta)$ with $r > 0$ and $0 \leq \theta < 2\pi$.

The proof proceeds by partitioning the disc $D_R$ into annular sectors and approximating the double integral by Riemann sums in polar coordinates. The area element in polar coordinates is $r \, dr \, d\theta$, which accounts for the Jacobian factor $r$ appearing in the transformed integral.

For each small annular region $r_0 \leq r \leq r_0 + \Delta r$, $\theta_0 \leq \theta \leq \theta_0 + \Delta\theta$, the area is approximately $r_0 \, \Delta r \, \Delta\theta$, and the contribution to the Riemann sum is approximately $f(r_0 \cos\theta_0, r_0 \sin\theta_0) \cdot r_0 \, \Delta r \, \Delta\theta = g(r_0, \theta_0) \, r_0 \, \Delta r \, \Delta\theta$.

Passing to the limit as the partition is refined yields the iterated integral

$$\int_0^R \left( \int_0^{2\pi} g(r, \theta) \, d\theta \right) r \, dr.$$

Equality with the Cartesian iterated integral

$$\int_{-R}^R \left( \int_{-\sqrt{R^2 - y^2}}^{\sqrt{R^2 - y^2}} f(x, y) \, dx \right) dy$$

follows from the fact that both integrals represent the same geometric quantity: the integral of $f$ over the disc $D_R$. The change of variables is justified by the continuity of $f$ and the fact that the mapping $(r, \theta) \mapsto (r \cos\theta, r \sin\theta)$ is a bijection from $(0, R) \times [0, 2\pi)$ onto $D_R \setminus \{(0,0)\}$, with the origin (a set of measure zero) contributing nothing to the integral. $\square$
