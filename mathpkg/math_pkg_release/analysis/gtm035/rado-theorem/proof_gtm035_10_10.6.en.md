---
role: proof
locale: en
of_concept: rado-theorem
source_book: gtm035
source_chapter: "Chapter 10"
source_section: "10.6"
---
# Proof of Radó's Theorem on Continuous Analytic Functions

**Theorem 10.6 (Radó).** Let $h$ be a continuous function on the closed unit disk $D$ and let $Z = \{z \in D : h(z) = 0\}$ be the zero set of $h$. Suppose $Z$ is a relatively closed subset of $D$ of Lebesgue (area) measure zero, and that $h$ is analytic on $D \setminus Z$. Then $h$ is analytic on all of $D$ (in particular, $h \in A(D)$).

**Proof.** Form the algebra $\mathcal{L}$ consisting of all polynomials in $h$ and the coordinate function $z$ with complex coefficients, and let $\overline{\mathcal{L}}$ be its uniform closure in $C(D)$. The algebra $\overline{\mathcal{L}}$ is a uniform algebra on $D$ containing $z$, and we shall show that it satisfies the maximum principle relative to $\Gamma = \partial D$.

We apply Lemma 10.4 (Glicksberg) with the following choices:

- $X_0 = \Gamma \cup Z$ (where $\Gamma$ is the unit circle),
- $\mathfrak{A} = \overline{\mathcal{L}}|_{X_0}$,
- $X = \Gamma$ (which is a boundary for $\mathfrak{A}$, since the Shilov boundary of $\overline{\mathcal{L}}$ is contained in $\Gamma \cup Z$ and the maximum of any function in $\overline{\mathcal{L}}$ on $X_0$ occurs on $\Gamma$),
- $E = Z$.

The function $h$ belongs to $\overline{\mathcal{L}}$ and satisfies $h = 0$ on $Z$ by definition of $Z$. For any point $x \in D \setminus Z$, we have $h(x) \neq 0$. Thus the hypotheses of Lemma 10.4 are satisfied at every $x \in D \setminus Z$.

For any $g \in \overline{\mathcal{L}}$, Lemma 10.4 yields

$$|g(x)| \leq \sup_{X_0 \setminus E} |g| = \sup_{\Gamma} |g|, \quad \text{for all } x \in D \setminus Z.$$

By continuity of $g$, the same inequality holds for every $x \in D$ (the set $D \setminus Z$ is dense in $D$ because $Z$ has measure zero). Thus $\overline{\mathcal{L}}$ satisfies the maximum principle relative to $\Gamma$:

$$|g(x)| \leq \max_{\Gamma} |g|, \quad \text{for all } x \in D,\; g \in \overline{\mathcal{L}}.$$

Now $\overline{\mathcal{L}}$ satisfies the hypotheses of Theorem 10.3 (Rudin):
- (a) $z \in \overline{\mathcal{L}}$ by construction,
- (b) $\overline{\mathcal{L}}$ satisfies the maximum principle relative to $\Gamma$.

Applying Theorem 10.3, we conclude $\overline{\mathcal{L}} \subseteq A(D)$. In particular, $h \in A(D)$, so $h$ is analytic on $\mathring{D}$ and continuous on $D$. ∎

**Remark.** Radó's theorem is the fundamental result that allows one to remove "thin" singularities of continuous analytic-type functions. Theorem 10.5 (the boundary uniqueness theorem) follows immediately from Radó's theorem, since a function in $A(\Omega)$ vanishing on a boundary arc $U \cap \partial \Omega$ can be extended by zero across that arc, and Radó's theorem then forces the function to vanish identically.
