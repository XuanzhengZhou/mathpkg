---
role: proof
locale: en
of_concept: course-of-values-closure
source_book: gtm037
source_chapter: "2"
source_section: "Elementary Recursive and Primitive Recursive Functions"
---

($\Rightarrow$) Assume $f \in A$. Define $\tilde{f}$ by:

$$\tilde{f}(x_0, \ldots, x_{m-2}, 0) = 1,$$
$$\tilde{f}(x_0, \ldots, x_{m-2}, \delta y) = \prod_{i < \delta y} p_i^{f(x_0, \ldots, x_{m-2}, i)+1}$$
$$= \tilde{f}(x_0, \ldots, x_{m-2}, y) \cdot p_y^{f(x_0, \ldots, x_{m-2}, y)+1}$$
$$= h(x_0, \ldots, x_{m-2}, y, \tilde{f}(x_0, \ldots, x_{m-2}, y)),$$

where $h(z_0, \ldots, z_m) = z_m \cdot p_{z_{m-1}}^{f(z_0, \ldots, z_{m-1})+1}$. The function $h$ is built from $f$ together with multiplication, prime exponentiation ($p_y$), and the successor function, all of which are in $A$ (or primitive recursive and hence in $A$). Since $A$ is closed under composition and primitive recursion, $\tilde{f} \in A$.

($\Leftarrow$) Assume $\tilde{f} \in A$. Then $f$ can be recovered from $\tilde{f}$ via $f(x_0, \ldots, x_{m-1}) = (\tilde{f}(x_0, \ldots, x_{m-2}, x_{m-1}+1))_{x_{m-1}} - 1$, where $(n)_i$ extracts the exponent of $p_i$ in $n$. Since the exponent-extraction function is primitive recursive (hence in $A$), and $\tilde{f} \in A$, composition yields $f \in A$.
