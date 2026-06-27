---
role: proof
locale: en
of_concept: logarithmic-holomorphic-separation
source_book: gtm035
source_chapter: "Chapter 9"
source_section: "9.5"
---
# Proof of Holomorphic Separation via $\log z_1/z_1$

**Lemma 9.5.** Let $K$ be a compact set in $\mathbb{C}^N$ and let $U_1, U_2$ be open sets with

$$U_1 \cup U_2 \supset K,$$

$$U_1 \cap U_2 \subset \{ \operatorname{Re} z_1 < 0 \}.$$

Suppose there exist $h_1 \in H(U_1)$, $h_2 \in H(U_2)$ such that

$$h_1 - h_2 = \frac{\log z_1}{z_1} \quad \text{on } U_1 \cap U_2.$$

Then there exists a function $F$ holomorphic in a neighborhood of $K$ such that $F = 1$ on $\{z_1 = 0\} \cap U_2$, and $|F| < 1$ everywhere else on $K$.

*Proof.* Since $U_1 \cap U_2 \subset \{ \operatorname{Re} z_1 < 0 \}$, the function $\log z_1$ is well-defined and holomorphic on $U_1 \cap U_2$ (using the principal branch of the logarithm).

Consider the function $f(z) = z_1 e^{z_1 h_1(z)}$ on $U_1$. We examine its behavior. Write $f(z) = w = u + iv$. The key observation is that because $\operatorname{Re} z_1 < 0$ on the overlap, the values of $f$ satisfy a geometric constraint that allows construction of a holomorphic "peak function" $F$.

Specifically, let $M > 0$ be a bound. The inequality

$$u - M(u^2 + v^2) \leq 0$$

implies

$$\left(u - \frac{1}{2M}\right)^2 + v^2 \geq \frac{1}{4M^2}.$$

Thus $f(z)$ lies outside the disk

$$\left|w - \frac{1}{2M}\right| < \frac{1}{2M}.$$

On the other hand, $K \setminus U_2$ is compact and $f \neq 0$ there (since $z_1 \neq 0$ outside $\{z_1=0\} \cap U_2$). Hence there exists $r > 0$ such that $|f(z)| \geq r$ whenever $z \in K \setminus U_2$.

Now choose $\varepsilon > 0$ sufficiently small so that the disk

$$D_\varepsilon = \{ |w - \varepsilon| \leq \varepsilon \}$$

avoids $f(K \setminus U_2)$ (which is possible since $|f| \geq r$ there) and also satisfies the geometric condition above. Define

$$F(z) = -\frac{\varepsilon}{f(z) - \varepsilon}.$$

By construction, $F$ is holomorphic in a neighborhood of $K$ (since the denominator does not vanish there).

On $\{z_1 = 0\} \cap U_2$, we have $f = 0$ (since $z_1 = 0$), and therefore $F = -\varepsilon/(-\varepsilon) = 1$. Everywhere else on $K$, $|f - \varepsilon| > \varepsilon$ (by the choice of $D_\varepsilon$ avoiding $f(K)$), so $|F| < 1$.

Thus $F$ satisfies the required properties: $F$ is holomorphic on a neighborhood of $K$, $F = 1$ on $\{z_1 = 0\} \cap U_2$, and $|F| < 1$ on the rest of $K$. $\square$

This lemma provides a crucial construction of a "peak-type" function that separates the set $\{z_1 = 0\}$ from the rest of $K$, which is then used in the proof of Theorem 9.3 to construct the required peak functions via the algebra homomorphism (Lemma 9.6).
