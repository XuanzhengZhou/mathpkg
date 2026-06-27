---
role: proof
locale: en
of_concept: fundamental-theorem-surface-theory
source_book: gtm051
source_chapter: "3"
source_section: "3.8.8"
---

**Existence.** The structural equations of (3.8.1) may be considered as a system of linear partial differential equations for the three $\mathbb{R}^3$-valued functions $f_1(u), f_2(u), n(u)$. The integrability conditions $f_{i,jk} = f_{i,kj}$ and $n_{i,j} = n_{j,i}$ are satisfied — this is precisely the content of the Gauss and Codazzi-Mainardi equations. By the Frobenius theorem (see Flanders, pp. 92-101, or Spivak, Vol. I, ch. 6), there exists a unique solution to this system satisfying any given initial conditions
$$f_i(u_0) = X_i, \quad n(u_0) = N,$$
where $X_i \cdot X_k = g_{ik}(u_0)$, $X_i \cdot N = 0$, $|N| = 1$, and $(X_1, X_2, N)$ is positively oriented.

Choose $x_0 \in \mathbb{R}^3$, and let
$$f(u) = \int_{u_0}^{u} \sum_i f_i(u) \, du^i + x_0.$$

Since $f_{1,2} = f_{2,1}$, this integral is independent of path and therefore $f(u)$ is well-defined. To show that $f$ is the desired surface, consider the functions $f_i \cdot f_j(u)$, $n \cdot f_j(u)$, $n \cdot n(u)$. Because $f_i$ and $n$ satisfy the differential equations (3.8.1), we have
$$(f_i \cdot f_j)_{,k} = \sum_l \Gamma_{ik}^l (f_l \cdot f_j) + \sum_l \Gamma_{jk}^l (f_i \cdot f_l) + h_{ik} (n \cdot f_j) + h_{jk} (f_i \cdot n).$$

Together with analogous equations for $n \cdot f_j$ and $n \cdot n$, and using the initial conditions, these PDEs have the unique solution $f_i \cdot f_j = g_{ij}$, $f_i \cdot n = 0$, $n \cdot n = 1$, confirming that $g_{ij}$ and $h_{ij}$ are indeed the first and second fundamental forms of $f$.

**Uniqueness.** Since $dB f_i, dB n$ and $\tilde{f}_i, \tilde{n}$ satisfy the same system of differential equations with the same initial conditions at $u = u_0$, it follows that $dB f_i = \tilde{f}_i$. Therefore,
$$B f(u) = B f(u_0) + \tilde{f}(u) - \tilde{f}(u_0) = \tilde{f}(u).$$
