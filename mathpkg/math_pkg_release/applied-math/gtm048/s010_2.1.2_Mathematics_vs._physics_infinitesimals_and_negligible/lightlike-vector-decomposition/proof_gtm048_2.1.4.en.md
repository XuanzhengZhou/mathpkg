---
role: proof
locale: en
of_concept: lightlike-vector-decomposition
source_book: gtm048
source_chapter: "2"
source_section: "2.1.4"
---

Let $Z$ be a future-pointing unit timelike vector, so $g(Z, Z) = -1$. Decompose $Y$ with respect to the orthogonal direct sum $M_z = Z^\perp \oplus \operatorname{span} Z$:
$$Y = aZ + \tilde{U}, \qquad a \in \mathbb{R}, \quad \tilde{U} \in Z^\perp.$$

Since $Y$ is lightlike:
$$0 = g(Y, Y) = g(aZ + \tilde{U}, aZ + \tilde{U}) = a^2 g(Z, Z) + 2a g(Z, \tilde{U}) + g(\tilde{U}, \tilde{U}) = -a^2 + |\tilde{U}|^2,$$
where $|\tilde{U}|^2 = g(\tilde{U}, \tilde{U}) \ge 0$ by positive definiteness of $g|_{Z^\perp}$. Hence $|\tilde{U}|^2 = a^2$, so $|\tilde{U}| = |a|$.

Since $Y$ is future-pointing and $Z$ is future-pointing timelike, we have $g(Y, Z) < 0$. Computing:
$$g(Y, Z) = g(aZ + \tilde{U}, Z) = a \cdot g(Z, Z) + g(\tilde{U}, Z) = -a < 0,$$
where $g(\tilde{U}, Z) = 0$ since $\tilde{U} \in Z^\perp$. Therefore $a > 0$.

Set $e = a > 0$. Then $|\tilde{U}| = e$. Since $\tilde{U} \in Z^\perp$ is spacelike with norm $e$, define $U = -\tilde{U}/e$. Then $U \in Z^\perp$ satisfies $g(U, U) = g(-\tilde{U}/e, -\tilde{U}/e) = |\tilde{U}|^2/e^2 = 1$, so $U$ is a unit vector. Moreover,
$$Y = eZ + \tilde{U} = eZ - eU = e(Z - U).$$

\textbf{Uniqueness.} Suppose $Y = e_1(Z - U_1) = e_2(Z - U_2)$ with $e_1, e_2 > 0$ and $U_1, U_2 \in Z^\perp$ unit vectors. Then $(e_1 - e_2)Z = e_1 U_1 - e_2 U_2 \in Z^\perp \cap \operatorname{span} Z = \{0\}$, so $e_1 = e_2$ and $e_1 U_1 = e_2 U_2$, hence $U_1 = U_2$. The decomposition is therefore unique.

For two lightlike vectors $Y = e(Z - U)$ and $Y' = e'(Z - U')$, the Newtonian angle $\theta$ between them is determined by projecting onto $Z^\perp$. The projections are $pY = -eU$ and $pY' = -e'U'$, so
$$\cos \theta = \frac{g(pY, pY')}{|pY|\,|pY'|} = \frac{ee' g(U, U')}{e \cdot e'} = g(U, U').$$
Thus the Newtonian angle between two light particles equals the Euclidean angle between their direction vectors $U, U'$ in the observer's rest space.
