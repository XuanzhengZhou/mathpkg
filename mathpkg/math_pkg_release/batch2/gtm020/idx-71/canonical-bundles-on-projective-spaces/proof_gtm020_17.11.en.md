---
role: proof
locale: en
of_concept: canonical-bundles-on-projective-spaces
source_book: gtm020
source_chapter: "17. Chern Classes and Stiefel-Whitney Classes"
source_section: "11"
---

For (1), we recall that $H^2(\mathbb{RP}^{2n-1}, \mathbb{Z}) = \mathbb{Z}_2$ for $n \geq 2$. Since complex line bundles are classified up to isomorphism by their first Chern class $c_1$, we need show only that $c_1(q^*(\eta)) \neq 0$ and $c_1(\varepsilon_U(\xi)) \neq 0$. Since $c_1(\eta)$ generates $H^2(\mathbb{CP}^{n-1})$ and since $q^*: H^2(\mathbb{CP}^{n-1}) \to H^2(\mathbb{RP}^{2n-1})$ is an epimorphism, we have $c_1(q^*(\eta)) = q^*(c_1(\eta)) \neq 0$. Since $\varepsilon_0\varepsilon_U(\xi) = \xi \oplus \xi$, it suffices to show that $\xi \oplus \xi$ is nontrivial. But we have $w(\varepsilon_0\varepsilon_U(\xi)) = w(\xi \oplus \xi) = w(\xi)w(\xi) = (1+x)^2 = 1+x^2$ and $x^2 \neq 0$. Therefore, $\varepsilon_U(\xi)$ is nontrivial, and we have $c_1(\varepsilon_U(\xi)) \neq 0$.

For (2), we observe that $q^*(\varepsilon_0(\eta))$ equals $\varepsilon_0(\varepsilon_U(\xi))$, and therefore $q^*(w(\varepsilon_0(\eta))) = w(\varepsilon_0\varepsilon_U(\xi)) = 1 + x^2$. Since $q^*$ is injective in mod 2 cohomology (for $n \geq 2$), we have $w(\varepsilon_0(\eta)) = 1 + y$, where $y$ is the mod 2 generator with $q^*(y) = x^2$. But $c_1(\eta)$ reduces mod 2 to $y$, so $w_2(\varepsilon_0(\eta))$ equals the mod 2 reduction of $c_1(\eta)$.

For (3), to show that $c_1(\eta) = e(\varepsilon_0(\eta))$, we use the splitting principle. A real vector bundle $\xi$ is orientable if and only if $w_1(\xi) = 0$. Since $\varepsilon_0(\eta)$ has vanishing $w_1$, it is orientable. The Euler class $e(\varepsilon_0(\eta))$ is the obstruction to an everywhere-nonzero cross section. By the naturality of characteristic classes, $c_1(\eta) = e(\varepsilon_0(\eta))$.
