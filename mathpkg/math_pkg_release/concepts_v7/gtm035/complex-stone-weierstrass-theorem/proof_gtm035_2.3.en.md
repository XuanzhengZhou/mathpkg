---
role: proof
locale: en
of_concept: complex-stone-weierstrass-theorem
source_book: gtm035
source_chapter: "2"
source_section: "2.3"
---

# Proof of Complex Stone-Weierstrass Theorem

**Theorem 2.3 (Complex Stone-Weierstrass Theorem).** Let $\mathfrak{A}$ be a subalgebra of $C(X)$ containing the constants and separating the points of $X$. If

$$f \in \mathfrak{A} \implies \overline{f} \in \mathfrak{A},$$

then $\mathfrak{A}$ is dense in $C(X)$.

## Proof

Let $\mathcal{L}$ consist of all real-valued functions in $\mathfrak{A}$. Since $\mathfrak{A}$ is closed under conjugation, for each $f \in \mathfrak{A}$ we have $\operatorname{Re} f = (f + \overline{f})/2 \in \mathcal{L}$ and $\operatorname{Im} f = (f - \overline{f})/(2i) \in \mathcal{L}$.

The set $\mathcal{L}$ is a real subalgebra of $C_{\mathbb{R}}(X)$ that contains the constants (since $\mathfrak{A}$ contains constants) and separates the points of $X$ (because $\operatorname{Re} f$ and $\operatorname{Im} f$ separate points whenever $f$ does).

By the Real Stone-Weierstrass Theorem (Theorem 2.1), $\mathcal{L}$ is dense in $C_{\mathbb{R}}(X)$. Consequently, $\mathcal{L} + i\mathcal{L} = \mathfrak{A}$ is dense in $C_{\mathbb{R}}(X) + i C_{\mathbb{R}}(X) = C(X)$.

Indeed, any $f \in C(X)$ can be written as $f = u + iv$ with $u, v \in C_{\mathbb{R}}(X)$. Choose sequences $\{u_n\}, \{v_n\} \subset \mathcal{L}$ with $u_n \to u$, $v_n \to v$ uniformly. Then $u_n + i v_n \in \mathfrak{A}$ and $u_n + i v_n \to f$ uniformly, so $\mathfrak{A}$ is dense in $C(X)$. $\square$
