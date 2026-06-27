---
role: proof
locale: en
of_concept: arens-royden-theorem
source_book: gtm035
source_chapter: "15"
source_section: "15.4"
---
# Proof of the Arens-Royden Theorem

**Theorem 15.3 (Arens-Royden).** Let $\mathfrak{A}$ be a commutative Banach algebra with maximal ideal space $X = \mathcal{M}(\mathfrak{A})$. Then the natural map

$$\Phi : \mathfrak{A}^{-1} \to H^1(X, \mathbb{Z})$$

induces an isomorphism

$$\mathfrak{A}^{-1} / \exp \mathfrak{A} \cong H^1(X, \mathbb{Z}).$$

Here $\mathfrak{A}^{-1} = \{x \in \mathfrak{A} : \exists\, x^{-1} \in \mathfrak{A}\}$ is the group of invertible elements, and $\exp \mathfrak{A} = \{e^y : y \in \mathfrak{A}\}$.

## Proof

The proof proceeds in several steps, building on Theorem 15.4 and an approximation argument via the Gelfand transform.

**Step 1: The base case $\mathfrak{A} = C(X)$.** By Theorem 15.4, for $X = \mathcal{M}(\mathfrak{A})$, there exists a natural homomorphism $\eta : C(X)^{-1} \to H^1(X, \mathbb{Z})$ that is surjective with kernel $\exp C(X)$. Hence the theorem holds for $C(X)$ itself.

**Step 2: Definition of $\Phi$ for general $\mathfrak{A}$.** For $x \in \mathfrak{A}^{-1}$, let $\hat{x} \in C(X)$ be its Gelfand transform. By the Gelfand representation theorem, $\hat{x} \in C(X)^{-1}$ (since $\hat{x}$ is nonvanishing on $X$). Define

$$\Phi(x) = \eta(\hat{x}) \in H^1(X, \mathbb{Z}).$$

One verifies that $\Phi$ is a group homomorphism and that $\Phi(e^y) = \eta(\widehat{e^y}) = \eta(e^{\hat{y}}) = 0$, so $\exp \mathfrak{A} \subseteq \ker \Phi$.

**Step 3: Approximation by exponentials.** Fix $x \in \ker \Phi$, so $\eta(\hat{x}) = 0$. Choose $g = e^h$ with $h \in \mathfrak{A}$ sufficiently close to $x$:

$$|\hat{x}(p) - \hat{g}(p)| < \frac{1}{3} \inf_{q \in X} |\hat{x}(q)| \quad \text{for all } p \in X.$$

This is possible by the Stone–Weierstrass theorem and the density of $\widehat{\mathfrak{A}}$ in $C(X)$ (since $\mathfrak{A}$ is a uniform algebra).

Then on $X$,

$$|\hat{g}(p)| > \frac{2}{3} \inf_X |\hat{x}|, \quad \text{so} \quad \frac{1}{|\hat{g}(p)|} < \frac{3}{2} \cdot \frac{1}{\inf_X |\hat{x}|}.$$

Consequently,

$$|1 - \hat{x}(p) \hat{g}^{-1}(p)| = |\hat{x}(p) - \hat{g}(p)| \cdot |\hat{g}^{-1}(p)| < \frac{1}{2}.$$

**Step 4: Logarithmic series.** Since $\|1 - x g^{-1}\| < 1$, for sufficiently large $n$,

$$\|(1 - x g^{-1})^n\|^{1/n} < \frac{3}{4} < 1.$$

The series

$$-\sum_{n=1}^{\infty} \frac{1}{n} (1 - x g^{-1})^n$$

converges absolutely in $\mathfrak{A}$ to an element $k$. Using the identity

$$\log(1 - z) = -\sum_{n=1}^{\infty} \frac{1}{n} z^n \quad \text{for } |z| < 1,$$

we obtain $k = \log(x g^{-1})$, i.e., $x g^{-1} = e^k$.

**Step 5: Conclusion.** Then $x = e^{k+h} \in \exp \mathfrak{A}$. Hence $\ker \Phi = \exp \mathfrak{A}$, as claimed.

**Step 6: Surjectivity.** Fix $\gamma \in H^1(X, \mathbb{Z})$. By surjectivity of $\eta : C(X)^{-1} \to H^1(X, \mathbb{Z})$ (Theorem 15.4), there exists $f \in C(X)^{-1}$ with $\eta(f) = \gamma$. Since $\widehat{\mathfrak{A}}$ is dense in $C(X)$, we can approximate $f$ by $\hat{x}$ for some $x \in \mathfrak{A}^{-1}$, and the homotopy invariance of $\eta$ (via $K^{\mathcal{U},\mathcal{V}}$) ensures $\Phi(x) = \gamma$. Thus $\Phi$ is surjective.

Therefore $\Phi$ induces the desired isomorphism $\mathfrak{A}^{-1} / \exp \mathfrak{A} \cong H^1(X, \mathbb{Z})$.
