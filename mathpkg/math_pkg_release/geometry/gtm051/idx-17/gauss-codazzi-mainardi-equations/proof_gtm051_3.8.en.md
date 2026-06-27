---
role: proof
locale: en
of_concept: gauss-codazzi-mainardi-equations
source_book: gtm051
source_chapter: "3"
source_section: "3.8"
---

**Proof of Theorem 3.8.3 (Integrability Conditions).**

The proof proceeds by analyzing the compatibility conditions $f_{ijk} = f_{ikj}$ and $n_{ij} = n_{ji}$ using the Gauss-Weingarten equations.

**Part 1: Derivation of the Gauss equation (i).**

From the Gauss formula (Theorem 3.8.1), we have $f_{ik} = \sum_l \Gamma_{ik}^l f_l + h_{ik} n$. Differentiating with respect to $u^j$:

$$
f_{ikj} = \sum_l (\Gamma_{ik,j}^l f_l + \Gamma_{ik}^l f_{lj}) + h_{ik,j} n + h_{ik} n_j.
$$

Substituting the Gauss-Weingarten expressions for $f_{lj}$ and $n_j$:

$$
f_{ikj} = \sum_l \Gamma_{ik,j}^l f_l + \sum_l \Gamma_{ik}^l \left(\sum_m \Gamma_{lj}^m f_m + h_{lj} n\right) + h_{ik,j} n + h_{ik} \left(-\sum_{m,p} h_{jp} g^{pm} f_m\right).
$$

Collecting the coefficients of the tangent basis vectors $f_m$ and equating $f_{ikj} = f_{ikj}$ with the analogous expression for $f_{ikj}$ (obtained by swapping $j \leftrightarrow k$), the equality of the $f_m$-components yields equation (i).

**Part 2: Derivation of the Codazzi-Mainardi equations (ii).**

Define the tensor $B_{ijk}$ from the expression for $n_i$ in the Weingarten formula:

$$
n_i = -\sum_{l,k} h_{il} g^{lk} f_k.
$$

Differentiating $n_i$ with respect to $u^j$ and using the Gauss-Weingarten equations, then imposing $n_{ij} = n_{ji}$, yields condition (ii). More precisely, one verifies that $B_{ijk} = B_{ikj}$ is equivalent to the Codazzi-Mainardi equations. The symmetry $B_{ijk} = B_{ikj}$ follows from the equality of mixed partials $n_{ij} = n_{ji}$ and the symmetry of the Christoffel symbols.

**Part 3: Equivalence argument.**

Define

$$
C_{ij}^k = -\left(\sum_l h_{il} g^{lk}\right)_{,j} - \sum_{l,m} h_{il} g^{lm} \Gamma_{mj}^k.
$$

Using the expression $(**)$ for $\Gamma_{mj}^k$ from Theorem 3.8.1, and the identity

$$
\sum_k g_{,j}^{mk} g_{kl} = -\sum_k g^{mk} g_{kl,j}
$$

(obtained by differentiating $\sum_k g^{mk} g_{kl} = \delta_l^m$), one concludes that $C_{ij}^k = C_{ji}^k$. This symmetry is equivalent to condition (ii), establishing the Codazzi-Mainardi equations.
