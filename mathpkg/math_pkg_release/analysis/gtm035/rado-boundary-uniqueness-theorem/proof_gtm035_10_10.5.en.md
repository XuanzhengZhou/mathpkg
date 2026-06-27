---
role: proof
locale: en
of_concept: rado-boundary-uniqueness-theorem
source_book: gtm035
source_chapter: "Chapter 10"
source_section: "10.5"
---
# Proof of Radó Boundary Uniqueness Theorem

Let $\Omega$ be a bounded plane region and $z_0$ a nonisolated boundary point of $\Omega$. Let $U$ be a neighborhood of $z_0$ in $\mathbb{C}$.

**Theorem 10.5.** Let $f \in A(\Omega)$ (the algebra of functions analytic on $\Omega$ and continuous on $\overline{\Omega}$) and assume that $f = 0$ on $\partial \Omega \cap U$. Then $f \equiv 0$ in $\Omega$.

**Proof.** We give a proof using Lemma 10.4 that requires the additional geometric hypothesis:

$$\exists \text{ a sequence } \{z_n\} \text{ in } \mathbb{C} \setminus \overline{\Omega} \text{ with } z_n \to z_0.$$

Set $X_0 = \overline{\Omega}$ and $\mathfrak{A} = A(\Omega)$. Then $\partial \Omega$ is a boundary (in fact, the Shilov boundary) for $\mathfrak{A}$. Set $E = \partial \Omega \cap U$, a closed subset of $X_0$.

For the points $z_n$ from the hypothesis, define

$$g_n(z) = \frac{1}{z - z_n}.$$

Each $g_n$ is analytic on $\overline{\Omega}$ (since $z_n \notin \overline{\Omega}$), so $g_n \in \mathfrak{A}$.

Choose $\varepsilon > 0$ small enough that the disk $\{z : |z - z_0| < \varepsilon\}$ is contained in $U$. For any $x \in \Omega$ with $|x - z_0| < \varepsilon$, we have, as $n$ grows large (so that $z_n$ is very close to $z_0$),

$$|g_n(x)| > \sup_{\partial \Omega \setminus E} |g_n|.$$

This inequality holds because $1/(x - z_n)$ becomes large when $z_n$ is near $z_0$ (which is near $x$), while on $\partial \Omega \setminus E$ (points of the boundary outside $U$), the denominator $z - z_n$ is bounded away from $0$.

Now suppose, for contradiction, that $f$ does not vanish identically on $\Omega$. Then there exists $x \in \Omega$ with $f(x) \neq 0$ and $|x - z_0| < \varepsilon$. The function $f$ vanishes on $E = \partial \Omega \cap U$ by hypothesis, so we may apply Lemma 10.4 with this $x$ and this $f$ to obtain

$$|g_n(x)| \leq \sup_{\partial \Omega \setminus E} |g_n| \quad \text{for all } n.$$

But this contradicts the strict inequality established above for large $n$. Hence $f(x) = 0$ for all $x \in \Omega$ with $|x - z_0| < \varepsilon$.

Since the zero set of the analytic function $f$ has a limit point in $\Omega$ (namely $z_0$ is a boundary accumulation point of the zero set), the identity theorem for analytic functions forces $f \equiv 0$ throughout $\Omega$. ∎

**Remark.** Theorem 10.5 follows immediately from Radó's Theorem (Theorem 10.6), which is a stronger result that does not require the geometric hypothesis (4). The proof above, using Glicksberg's lemma, illustrates the power of the local maximum modulus principle.
