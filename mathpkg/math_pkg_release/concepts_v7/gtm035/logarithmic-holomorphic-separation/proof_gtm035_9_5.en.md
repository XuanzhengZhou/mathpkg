---
role: proof
locale: en
of_concept: logarithmic-holomorphic-separation
source_book: gtm035
source_chapter: "Chapter 9"
source_section: "9.5"
---
# Proof of Holomorphic Separation via $\log z_1/z_1$

Let $K$ be a compact set in $\mathbb{C}^N$ and $U_1, U_2$ open sets satisfying:

1. $U_1 \cup U_2 \supset K$,
2. $U_1 \cap U_2 \subset \{\operatorname{Re} z_1 < 0\}$,
3. There exist $h_1 \in H(U_1)$, $h_2 \in H(U_2)$ with $h_1 - h_2 = \frac{\log z_1}{z_1}$ in $U_1 \cap U_2$,
4. $K \cap U_2 \subset \{\operatorname{Re} z_1 \leq 0\}$.

We construct $F$ holomorphic in a neighborhood of $K$ such that $F = 1$ on $K \cap \{z_1 = 0\} \cap U_2$ and $|F| < 1$ elsewhere on $K$.

**Step 1: A global holomorphic function.** From $h_1 - h_2 = \frac{\log z_1}{z_1}$, we have $z_1 h_1 - z_1 h_2 = \log z_1$, so

$$e^{z_1 h_1} = z_1 e^{z_1 h_2}.$$

Define a function $f$ on $U_1 \cup U_2$ by

$$f = \begin{cases} e^{z_1 h_1} & \text{in } U_1 \\ z_1 e^{z_1 h_2} & \text{in } U_2 \end{cases}.$$

The identity above shows that $f$ is well-defined on $U_1 \cap U_2$, so $f \in H(U_1 \cup U_2)$. Moreover,

$$f \text{ never vanishes on } K \setminus (\{z_1 = 0\} \cap U_2).$$

**Step 2: Geometric separation.** We claim there exists $\varepsilon > 0$ such that if $z \in K \setminus (\{z_1 = 0\} \cap U_2)$, then $f(z)$ lies outside the disk $D_\varepsilon = \{|w - \varepsilon| \leq \varepsilon\}$.

Consider first $z \in U_2$. From $f = z_1 e^{z_1 h_2}$, we have $z_1 = e^{-z_1 h_2} f$, hence $z_1 h_2 = e^{-z_1 h_2} h_2 f = C f$ with $C \in H(U_2)$, giving $z_1 = f e^{-C f} = f + k f^2$ for some $k \in H(U_2)$. Shrinking $U_2$, we may assume $|k| \leq M$ on $U_2$.

Since $\operatorname{Re} z_1 \leq 0$ on $K \cap U_2$ (hypothesis 4),

$$0 \geq \operatorname{Re} f + \operatorname{Re}(k f^2) \geq \operatorname{Re} f - |f|^2 |k| \geq \operatorname{Re} f - M|f|^2.$$

Writing $f(z) = w = u + iv$, this gives $u - M(u^2 + v^2) \leq 0$, or

$$\left(u - \frac{1}{2M}\right)^2 + v^2 \geq \frac{1}{4M^2}.$$

Thus $f(z)$ lies outside the disk $|w - \frac{1}{2M}| < \frac{1}{2M}$.

For $z \in K \setminus U_2$, the set is compact and $f \neq 0$ there, so there exists $r > 0$ with $|f(z)| \geq r$ on $K \setminus U_2$. Choosing $\varepsilon$ small enough, the union of both "outside" regions covers all of $K \setminus (\{z_1 = 0\} \cap U_2)$, and we obtain the claimed $D_\varepsilon$.

**Step 3: Construction of $F$.** Define

$$F = -\frac{\varepsilon}{f - \varepsilon}.$$

By choice of $D_\varepsilon$, $F$ is holomorphic in a neighborhood of $K$. On $\{z_1 = 0\} \cap U_2$, $f = z_1 e^{z_1 h_2} = 0$, so $F = -\varepsilon/(0 - \varepsilon) = 1$. Everywhere else on $K$, $f - \varepsilon$ lies outside $D_\varepsilon$, so $|f - \varepsilon| > \varepsilon$, giving $|F| < 1$. $\square$
