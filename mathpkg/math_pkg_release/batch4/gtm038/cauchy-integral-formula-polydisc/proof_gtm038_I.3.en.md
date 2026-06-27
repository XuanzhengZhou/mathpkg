---
role: proof
locale: en
of_concept: cauchy-integral-formula-polydisc
source_book: gtm038
source_chapter: "I"
source_section: "3. The Cauchy Integral"
---
**Proof.** This theorem is a generalization of the familiar 1-dimensional Cauchy integral formula. The function $f_n^*$ with $f_n^*(z_n) := f(\xi_1, \ldots, \xi_{n-1}, z_n)$ is complex differentiable for fixed $(\xi_1, \ldots, \xi_{n-1}) \in \mathbb{C}^{n-1}$ in $B_n := \{z_n \in \mathbb{C}: (\xi_1, \ldots, \xi_{n-1}, z_n) \in E_n \cap B\}$, where $E_n$ is the plane $\{\mathfrak{z} \in \mathbb{C}^n: z_\lambda = \xi_\lambda \text{ for } \lambda \neq n\}$. But then $f_n^*$ is holomorphic in $B_n$. $B_n$ is an open set in $\mathbb{C}$. $K_n := \{z_n \in \mathbb{C}: |\xi_n| = r_n\}$ is contained in $B_n$, and the Cauchy integral formula for a single variable says

$$f_n^*(z_n) = \frac{1}{2\pi i} \int_{|\xi_n|=r_n} \frac{f_n^*(\xi_n)}{\xi_n - z_n} d\xi_n.$$

Applying this iteratively for each variable yields the Cauchy integral formula on the polydisc:

$$f(\mathfrak{z}) = \left(\frac{1}{2\pi i}\right)^n \int_{|\xi_1|=r_1} \cdots \int_{|\xi_n|=r_n} \frac{f(\xi_1, \ldots, \xi_n)}{(\xi_1 - z_1) \cdots (\xi_n - z_n)} d\xi_n \cdots d\xi_1$$

for all $\mathfrak{z} \in P$. $\square$
