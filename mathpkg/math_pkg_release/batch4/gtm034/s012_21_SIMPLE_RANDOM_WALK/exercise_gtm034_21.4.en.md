---
role: exercise
locale: en
chapter: "V"
section: "21"
exercise_number: 4
---

Show that the proper analogue of P22.3 for unsymmetrical random walk concerns a (uniquely determined) biorthogonal system of polynomials $q_n(z)$ and $r_n(z)$ such that
$$(2\pi)^{-1} \int_{-\pi}^{\pi} q_n(e^{i\theta}) \overline{r_m(e^{i\theta})} [1 - \phi(\theta)] \, d\theta = \delta_{m,n}.$$

Hint: Verify that these orthogonality relations hold if
$$q_{nk} = \sum_{v=0}^{\infty} P_k[x_v = n; \; x_j < n \text{ for } j = 1, 2, \ldots, v-1] \quad \text{for } n > k,$$
$$q_{nn} = 1,$$
and
$$r_{nk} = \sum_{v=0}^{\infty} P_n[x_v = k; \; x_j \leq n \text{ for } j = 1, 2, \ldots, v] \quad \text{for } n \geq k,$$
are defined as the coefficients of the polynomials
$$q_n(z) = \sum_{k=0}^{n} q_{nk} z^k, \quad r_n(z) = \sum_{k=0}^{n} r_{nk} z^k.$$

Using these polynomials one has
$$g_N(i,j) = \sum_{v=\max(i,j)}^{N} q_{vi} r_{vj}.$$
