---
role: proof
locale: en
of_concept: dense-subalgebra-from-perturbation
source_book: gtm035
source_chapter: "14"
source_section: "14.3"
---
# Proof of Dense Subalgebra from Stone-Weierstrass Perturbation

Write $\mathfrak{A} = [z, \bar{z} + R(z)]$. Fix a point $a \in \mathbb{C}$. Let $\mu$ be a measure on $D$ with $\mu \perp \mathfrak{A}$. If $|a| > 1$, then the function $z \mapsto 1/(z-a)$ lies in $\mathfrak{A}$ (it is analytic on a neighborhood of $D$, hence uniformly approximable by polynomials in $z$). Therefore $\int_D \frac{1}{z-a} d\mu(z) = 0$.

Now suppose $a \in D$. We construct a sequence of functions $b_j \in \mathfrak{A}$ such that
$$
b_j(z) \to \frac{1}{z-a} \quad \text{pointwise on } D \setminus \{a\}
$$
and such that the $b_j$ are uniformly bounded by a multiple of $1/|z-a|$.

Define
$$
h(z) = (z-a)(\bar{z} + R(z) - (\bar{a} + R(a))).
$$

Then
$$
h(z) = |z-a|^2 + (z-a)(R(z) - R(a)) = |z-a|^2 + B(z).
$$

Because of the Lipschitz condition $|R(z) - R(z')| \leq k|z - z'|$ with $k < 1$, we have
$$
|B(z)| \leq k |z-a|^2 < |z-a|^2, \quad z \in D \setminus \{a\}.
$$

Hence
$$
\operatorname{Re} h(z) > 0, \quad z \in D \setminus \{a\}.
$$

It follows that $h(D)$ is a compact subset of $\{\operatorname{Re} w \geq 0\}$ and $h(D \setminus \{a\}) \subseteq \{\operatorname{Re} w > 0\}$. We fix a closed semidisk $S$ contained in $\{\operatorname{Re} w \geq 0\}$ that contains $h(D)$.

Next we choose polynomials $P_n$ by Lemma 14.2, satisfying $P_n(w) \to 1/w$ on $S \setminus \{0\}$ and $|P_n(w)| \leq C/|w|$ on $S \setminus \{0\}$. We then put, for $j = 1, 2, \ldots$,
$$
b_j(z) = [(\bar{z} + R(z)) - (\bar{a} + R(a))] P_j(h(z)).
$$

Since $z \in \mathfrak{A}$ and $\bar{z} + R(z) \in \mathfrak{A}$, and $P_j(h(z))$ is a polynomial in elements of $\mathfrak{A}$, we have $b_j \in \mathfrak{A}$.

Moreover,
$$
b_j(z) = \frac{(\bar{z} + R(z)) - (\bar{a} + R(a))}{h(z)} \cdot h(z) P_j(h(z))
= \frac{1}{z-a} \cdot h(z) P_j(h(z)),
$$
since $(\bar{z} + R(z)) - (\bar{a} + R(a)) = h(z)/(z-a)$.

Now by the properties of $P_j$, $h(z) P_j(h(z)) \to 1$ pointwise for $z \neq a$, and $|h(z) P_j(h(z))|$ is uniformly bounded. Hence
$$
b_j(z) \to \frac{1}{z-a}, \quad z \in D \setminus \{a\},
$$
with a dominated bound $|b_j(z)| \leq C'/|z-a|$.

Since $\mu \perp \mathfrak{A}$, we have $\int_D b_j(z) d\mu(z) = 0$ for all $j$. By dominated convergence,
$$
0 = \int_D b_j(z) d\mu(z) \to \int_D \frac{1}{z-a} d\mu(z).
$$

Thus $\int_D \frac{1}{z-a} d\mu(z) = 0$ for all $a \in D$, and hence for almost every $a \in \mathbb{C}$. By Lemma 2.7 (which states that if a finite measure has vanishing Cauchy transform almost everywhere, then the measure is zero), this implies that $\mu = 0$.

Therefore the only measure annihilating $\mathfrak{A}$ is the zero measure. By the Hahn-Banach and Riesz representation theorems, $\mathfrak{A}$ is dense in $C(D)$.

$\square$
