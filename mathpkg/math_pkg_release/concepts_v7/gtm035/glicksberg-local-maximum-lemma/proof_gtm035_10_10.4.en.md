---
role: proof
locale: en
of_concept: glicksberg-local-maximum-lemma
source_book: gtm035
source_chapter: "Chapter 10"
source_section: "10.4"
---
# Proof of Glicksberg Local Maximum Lemma

**Lemma 10.4 (Glicksberg).** Let $\mathfrak{A}$ be a uniform algebra on a compact space $X_0$ and let $X$ be a boundary for $\mathfrak{A}$. Let $E$ be a closed subset of $X_0$ with $X \subseteq E$. Fix $x \in X_0$ and $f \in \mathfrak{A}$ such that $f(x) \neq 0$ and $f = 0$ on $E$. Then for every $g \in \mathfrak{A}$,

$$|g(x)| \leq \sup_{X_0 \setminus E} |g|.$$

**Proof.** Since $f$ vanishes on $E$, the product $fg$ also vanishes on $E$. Because $X$ is a boundary for $\mathfrak{A}$, we have

$$|f(x)g(x)| \leq \max_X |fg|.$$

Since $fg = 0$ on $E$ and $X \subseteq E$, the maximum of $|fg|$ on $X$ is attained on $X \setminus E \subseteq X_0 \setminus E$. Thus

$$|f(x)g(x)| \leq \sup_{X \setminus E} |fg| \leq \sup_{X_0 \setminus E} |f| \cdot \sup_{X_0 \setminus E} |g|.$$

Dividing by $|f(x)| \neq 0$, we obtain

$$|g(x)| \leq K \sup_{X_0 \setminus E} |g|,$$

where

$$K = \frac{\sup_{X_0 \setminus E} |f|}{|f(x)|}.$$

Now apply the inequality to $g^n$ in place of $g$, for $n = 1, 2, \ldots$:

$$|g(x)|^n = |g^n(x)| \leq K \sup_{X_0 \setminus E} |g^n| = K \Bigl(\sup_{X_0 \setminus E} |g|\Bigr)^n.$$

Taking $n$-th roots yields

$$|g(x)| \leq K^{1/n} \sup_{X_0 \setminus E} |g|.$$

Letting $n \to \infty$, we have $K^{1/n} \to 1$ (since $K > 0$), and therefore

$$|g(x)| \leq \sup_{X_0 \setminus E} |g|,$$

which is the desired local maximum principle. ∎
