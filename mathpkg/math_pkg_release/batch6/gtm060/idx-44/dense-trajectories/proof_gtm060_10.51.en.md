---
role: proof
locale: en
of_concept: dense-trajectories
source_book: gtm060
source_chapter: "10"
source_section: "51"
---

Assume the contrary: there exists a neighborhood $D$ of some point of the torus $T^n$ that contains no point of the trajectory $\{\varphi(t) = \varphi_0 + \omega t\}$. Construct a continuous function $f$ on $T^n$ equal to zero outside $D$ and with space average $\bar{f} = 1$ (this is possible by taking a suitable bump function supported in $D$, normalized so that $(2\pi)^{-n}\int fd\varphi = 1$).

The time average $f^*(\varphi_0)$ along the trajectory $\varphi(t)$ is $0$, since $f$ vanishes at every point $\varphi(t)$ visited by the trajectory. This gives $f^*(\varphi_0) = 0 \neq 1 = \bar{f}$, contradicting the theorem on averages which asserts equality of time and space averages when the frequencies are independent. Therefore the trajectory must be dense.
