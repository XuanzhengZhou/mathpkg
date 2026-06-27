---
role: proof
locale: en
of_concept: trigonometric-polynomial-sandwich
source_book: gtm060
source_chapter: "10"
source_section: "51"
---

**Case 1: $f$ is continuous.** By the Weierstrass approximation theorem for the torus, there exists a trigonometric polynomial $P$ such that $|f - P| < \varepsilon/2$ uniformly on $T^n$. Set $P_1 = P - \varepsilon/2$ and $P_2 = P + \varepsilon/2$. Then $P_1 < f < P_2$ pointwise, and

$$\frac{1}{(2\pi)^n} \int_{T^n} (P_2 - P_1) d\varphi = \frac{1}{(2\pi)^n} \int_{T^n} \varepsilon \, d\varphi = \varepsilon.$$

**Case 2: $f$ is Riemann integrable but not necessarily continuous.** By the definition of Riemann integrability, there exist two continuous functions $f_1$ and $f_2$ on $T^n$ such that $f_1 < f < f_2$ and

$$\frac{1}{(2\pi)^n} \int_{T^n} (f_2 - f_1) d\varphi < \frac{\varepsilon}{3}.$$

Now apply Case 1 to $f_1$ and $f_2$ separately: there exist trigonometric polynomials $P_1, P_2'$ such that $P_1 < f_1$, $f_2 < P_2'$, and

$$\frac{1}{(2\pi)^n} \int_{T^n} (f_1 - P_1) d\varphi < \frac{\varepsilon}{3}, \quad \frac{1}{(2\pi)^n} \int_{T^n} (P_2' - f_2) d\varphi < \frac{\varepsilon}{3}.$$

Set $P_2 = P_2'$. Then $P_1 < f_1 < f < f_2 < P_2$ and

$$\frac{1}{(2\pi)^n} \int_{T^n} (P_2 - P_1) d\varphi = \frac{1}{(2\pi)^n} \int_{T^n} (P_2 - f_2) d\varphi + \frac{1}{(2\pi)^n} \int_{T^n} (f_2 - f_1) d\varphi + \frac{1}{(2\pi)^n} \int_{T^n} (f_1 - P_1) d\varphi < \varepsilon.$$
