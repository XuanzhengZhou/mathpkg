---
role: proof
locale: en
of_concept: hardy-littlewood-lp-maximal-theorem
source_book: gtm025
source_chapter: "21"
source_section: "SS 21"
---

Using (21.72), (21.75.i), Fubini, and Holder:
$$\int_R (f^{\Lambda(j)})^p dx = \int_0^\infty p t^{p-1} \lambda(M_t^{(j)}) dt = p \int_0^\infty t^{p-2} \int_{M_t^{(j)}} f d\lambda dt$$
$$= p \int_R f(x) \int_0^{f^{\Lambda(j)}(x)} t^{p-2} dt dx = \frac{p}{p-1} \int_R f(x) f^{\Lambda(j)}(x)^{p-1} dx$$
$$\leq \frac{p}{p-1} \|f\|_p \|f^{\Lambda(j)}\|_p^{p-1}.$$
Dividing gives the result. Part (ii) uses (21.75.ii) similarly.
