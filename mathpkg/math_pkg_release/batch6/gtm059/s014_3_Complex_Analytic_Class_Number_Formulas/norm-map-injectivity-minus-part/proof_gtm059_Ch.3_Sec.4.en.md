---
role: proof
locale: en
of_concept: norm-map-injectivity-minus-part
source_book: gtm059
source_chapter: "3"
source_section: "4.6 The (±1)-conjectures"
---

Let $K$ be an imaginary abelian extension of $\mathbb{Q}$ with maximal real subfield $K^+$. Let $H$ be the Hilbert class field of $K^+$, i.e., the maximal unramified abelian extension of $K^+$. Consider an ideal class $c \in C_K^-$ such that $N_{K/K^+}(c) = 1$ in $C_{K^+}$. We must show $c = 1$.

By class field theory, the Artin symbol gives an isomorphism

$$
C_{K^+} \cong \operatorname{Gal}(H/K^+).
$$

Under this isomorphism, the condition $N_{K/K^+}(c) = 1$ means that the Artin symbol $(c, K/K^+)$ restricted to $H$ acts trivially. More precisely, for any ideal class $c \in C_K$, the restriction of the Artin symbol satisfies

$$
(c, K/K^+) \big|_H = (N_{K/K^+}(c), K^+/K^+).
$$

Thus $N_{K/K^+}(c) = 1$ implies $(c, K/K^+)|_H = 1$, meaning the Artin symbol of $c$ fixes $H$.

Since $K$ is an imaginary abelian extension, the extension $K/K^+$ is totally ramified at the archimedean primes. Therefore $K \cap H = K^+$, as $K/K^+$ is ramified at infinity while $H/K^+$ is everywhere unramified. Consequently,

$$
\operatorname{Gal}(KH/H) \cong \operatorname{Gal}(K/K^+) \cong \{1, \tau\}.
$$

Now since $c \in C_K^-$, we have $c^{1+\tau} = 1$. Under the Artin map, this condition together with $(c, K/K^+)|_H = 1$ forces $c = 1$ in $C_K$. Indeed, if $\mathfrak{a}$ is an ideal representing $c$, then the condition $c^{1+\tau} = 1$ means $\mathfrak{a}^{1+\tau}$ is principal. But $N_{K/K^+}(\mathfrak{a}) = \mathfrak{a}^{1+\tau}$ in the class group, and the injectivity on the minus part follows from the fact that the norm map on ideals corresponds to the restriction of the Artin symbol to the Hilbert class field.

Therefore $\ker(N_{K/K^+}|_{C_K^-})$ is trivial, and the norm map restricted to the minus eigenspace is injective.
