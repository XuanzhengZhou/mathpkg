---
role: proof
locale: en
of_concept: n0j-fourier-integral-formula
source_book: gtm040
source_chapter: "10"
source_section: "13"
---

Call the right side of the claimed formula $h_j$. Denote the cube $[-1/2, 1/2]^3$ by $E$. Then

$$(I - P)_{m\cdot} h_\cdot = h_m - \frac{1}{6} \sum_s h_{m+a_s}$$

$$= 3 \int_E (3 - \cos 2\pi x_1 - \cos 2\pi x_2 - \cos 2\pi x_3)^{-1}$$

$$\times \left( e^{-2\pi i(m \cdot x)} - \frac{1}{6} \sum_s e^{-2\pi i(m+a_s) \cdot x} \right) dx$$

$$= 3 \int_E (3 - \cos 2\pi x_1 - \cos 2\pi x_2 - \cos 2\pi x_3)^{-1}$$

$$\times e^{-2\pi im \cdot x} \left( 1 - \frac{1}{6} \sum_s e^{-2\pi i a_s \cdot x} \right) dx$$

$$= \int_E e^{-2\pi im \cdot x} dx$$

$$= \delta_{m0}.$$

Now $N_{0\cdot}$ is also a function tending to zero (see Proposition 7-10) and satisfying

$$(I - P)_{m\cdot} N_{0\cdot} = \delta_{m0},$$

and thus $N_{0\cdot} - h_\cdot$ is a bounded regular function. By Proposition 5-20 (which states that the only bounded regular functions for this process are the constants) it must be constant, and that constant must be zero, since both functions vanish at infinity. Thus the formula for $N_{0j}$ is established.
