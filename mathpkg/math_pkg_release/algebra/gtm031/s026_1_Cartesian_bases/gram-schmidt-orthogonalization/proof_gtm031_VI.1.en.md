---
role: proof
locale: en
of_concept: gram-schmidt-orthogonalization
source_book: gtm031
source_chapter: "VI"
source_section: "1"
---

Let $(e_1, e_2, \cdots, e_n)$ be any basis for the Euclidean space $\Re$. Since the scalar product is positive definite, $(e_1, e_1) > 0$. Define

$$u_1 = (e_1, e_1)^{-1/2} e_1.$$

Then $(u_1, u_1) = (e_1, e_1)^{-1}(e_1, e_1) = 1$, and $[u_1] = [e_1]$.

Assume by induction that $(u_1, \ldots, u_k)$ have been determined so that $(u_i, u_j) = \delta_{ij}$ and $[u_1, \ldots, u_i] = [e_1, \ldots, e_i]$ for all $i \leq k$. Form the vector

$$f_{k+1} = e_{k+1} - (e_{k+1}, u_1)u_1 - (e_{k+1}, u_2)u_2 - \cdots - (e_{k+1}, u_k)u_k.$$

For any $i \in \{1, \ldots, k\}$, using bilinearity and the orthonormality condition $(u_i, u_j) = \delta_{ij}$:

$$(f_{k+1}, u_i) = (e_{k+1}, u_i) - \sum_{j=1}^{k} (e_{k+1}, u_j)(u_j, u_i) = (e_{k+1}, u_i) - (e_{k+1}, u_i) \cdot 1 = 0.$$

Thus $f_{k+1}$ is orthogonal to $u_1, \ldots, u_k$. Moreover, $f_{k+1} \neq 0$ since $e_{k+1} \notin [e_1, \ldots, e_k] = [u_1, \ldots, u_k]$, and $f_{k+1}$ differs from $e_{k+1}$ by a linear combination of $u_1, \ldots, u_k$. Hence $(f_{k+1}, f_{k+1}) > 0$ by positive definiteness. Set

$$u_{k+1} = (f_{k+1}, f_{k+1})^{-1/2} f_{k+1}.$$

Then $(u_{k+1}, u_{k+1}) = 1$ and $(u_{k+1}, u_i) = 0$ for $i \leq k$, so $(u_1, \ldots, u_{k+1})$ is orthonormal. Furthermore, $[u_1, \ldots, u_{k+1}] = [e_1, \ldots, e_{k+1}]$ since $f_{k+1}$ and $e_{k+1}$ span the same space when adjoined to $[u_1, \ldots, u_k] = [e_1, \ldots, e_k]$.

By induction, this process yields $u_1, \ldots, u_n$ satisfying $(u_i, u_j) = \delta_{ij}$ and spanning $\Re$, hence $(u_1, \ldots, u_n)$ is a Cartesian basis.
