---
role: proof
locale: en
of_concept: maximality-of-disk-algebra
source_book: gtm035
source_chapter: "Chapter 10"
source_section: "10.2"
---
# Proof of Maximality of the Disk Algebra on the Circle

Let $D$ be the closed unit disk in the $z$-plane and $\Gamma$ the unit circle. Let

$$\mathfrak{A}_0 = A(D)|_\Gamma$$

be the disk algebra restricted to $\Gamma$, consisting of those functions in $C(\Gamma)$ that admit an analytic extension to $|z| < 1$. $\mathfrak{A}_0$ is a uniform algebra on $\Gamma$ (isomorphic and isometric to $A(D)$).

**Theorem 10.2 (Wermer).** Let $B$ be a uniform algebra on $\Gamma$ with

$$\mathfrak{A}_0 \subseteq B \subseteq C(\Gamma).$$

Then either $\mathfrak{A}_0 = B$ or $B = C(\Gamma)$.

**Proof.** We use Lemma 10.1 (Cohen's lemma). Assume $B \neq \mathfrak{A}_0$. The functions

$$e^{in\theta}, \quad n = 0, \pm 1, \pm 2, \ldots$$

span a dense subspace of $C(\Gamma)$, while $\mathfrak{A}_0$ contains exactly those $e^{in\theta}$ with $n \geq 0$. Since $B \neq \mathfrak{A}_0$, there exists $g \in B$ having a nonzero negative Fourier coefficient.

Choose an integer $N$ large enough and a trigonometric polynomial

$$T = \sum_{\nu=-N}^{-2} T_\nu e^{i\nu\theta} + 1 + \sum_{\nu=0}^{N} T_\nu e^{i\nu\theta}$$

that approximates $g$ so closely that $\|g - T\| < 1$. (The constant term is normalized to $1$ after scaling.)

Writing $z = e^{i\theta}$, we have

$$zT = z\sum_{\nu=-N}^{-2} T_\nu z^\nu + z + z\sum_{\nu=0}^{N} T_\nu z^\nu$$

$$= \sum_{\nu=-N}^{-2} T_\nu z^{\nu+1} + 1 + z\sum_{\nu=0}^{N} T_\nu z^\nu$$

$$= \bar{z} \cdot \overline{P} + 1 + zQ,$$

where $P$ and $Q$ are polynomials in $z$. Specifically, $P(z) = \sum_{\nu=2}^{N} \overline{T}_{-\nu} z^{\nu-1}$ and $Q(z) = \sum_{\nu=0}^{N} T_\nu z^\nu$, so that $\overline{P} = \sum_{\nu=-N}^{-2} \overline{T}_\nu \bar{z}^{-\nu}$ and $z \cdot \overline{P}$ reproduces the negative-degree terms.

From $\|g - T\| < 1$ we obtain $\|zg - zT\| < 1$, i.e.,

$$\big\|z(Q - g) + \bar{z}\,\overline{P} + 1\big\| < 1.$$

Now $Q - g \in B$ (since $Q \in \mathfrak{A}_0 \subseteq B$ and $g \in B$) and $P \in \mathfrak{A}_0 \subseteq B$, so taking $a = z(Q - g)$ and $b = \bar{z}\,\overline{P}$, we have $a, b \in B$ and $\|1 + a + \bar{b}\| < 1$. By Lemma 10.1, $a + b = z(Q - g) + \bar{z}\,\overline{P}$ is invertible in $B$.

Since $z(Q - g) + \bar{z}\,\overline{P}$ is invertible in $B$, the element

$$\bar{z} = \big(z(Q - g) + \bar{z}\,\overline{P}\big)^{-1} \cdot \big(z^2(Q - g)\overline{P}^{-1} + \cdots\big) \in B$$

(by algebraic manipulation using the fact that $\overline{P}$ and the inverse are in $B$). Thus $\bar{z} \in B$, and together with $\mathfrak{A}_0 \subseteq B$, it follows that $B$ contains all trigonometric polynomials, hence $B = C(\Gamma)$ by the Stone–Weierstrass theorem. ∎
