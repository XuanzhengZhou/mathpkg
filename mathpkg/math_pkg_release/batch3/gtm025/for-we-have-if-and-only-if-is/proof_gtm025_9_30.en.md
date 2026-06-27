---
role: proof
locale: en
of_concept: "for-we-have-if-and-only-if-is"
source_book: gtm025
source_chapter: "Extending Functionals"
source_section: "9.30"
---

Let $A = \{x \in X : h(x) > 0\}$. The functions $nh, n = 1, 2, \ldots$, are all in $\mathfrak{F}^+$, and it is obvious that $\lim_{n \to \infty} nh \geq \xi_A$. Thus if $\bar{I}(h) = 0$, (9.17) shows that $\iota(A) = \bar{I}(\xi_A) \leq \bar{I}\left(\lim_{n \to \infty} nh\right) = \lim_{n \to \infty} n\bar{I}(h) = 0$. If $h$ is an $\iota$-null function, then $\iota(A) = 0$; using the inequality $h \leq \lim_{n \to \infty} n\xi_A$, we have $\bar{I}(h) \leq \lim_{n \to \infty} \bar{I}(n\xi_A) = \lim_{n \to \infty} n\bar{I}(A) = 0$.

Next suppose that $\bar{I}(h) < \infty$, and let $B = \{x \in X : h(x) = \infty\}$. For all $\varepsilon > 0$ we have $\xi_B \leq \varepsilon h$, and so $\iota(B) = \bar{I}(\xi_B) \leq \bar{I}(\varepsilon h) = \varepsilon\bar{I}(h)$.
and $(W^-)'$, it follows that $V \cap U' \subset W_0 \subset H$, and so

$$0 \leq \iota(W_0) - \iota(V \cap U') \leq \iota(H) - \iota(V \cap U') < \frac{\varepsilon}{4}.$$

Therefore

$$|\iota(W) + \iota(W_0) - (\iota(V \cap U) + \iota(V \cap U'))| \leq |\iota(W_0) - \iota(V \cap U')|$$

$$+ |\iota(W) - \iota(V \cap U)| < \frac{\varepsilon}{4} + \frac{\varepsilon}{4} = \frac{\varepsilon}{2}.$$

Combining this with the fact that $W \cup W_0 \subset V$ and using (9.22), we have

$$\iota(T) + \varepsilon > \iota(V) + \frac{\varepsilon}{2} \geq \iota(W \cup W_0) + \frac{\varepsilon}{2} = \iota(W) + \iota(W_0) + \frac{\varepsilon}{2}$$

$$> \iota(V \cap U) + \iota(V \cap U') \geq \iota(T \cap U) + \iota(T \cap U').$$

Since $\varepsilon$ is arbitrary, we conclude that

$$\iota(T) \geq \iota(T \cap U) + \iota(T \cap U').$$

(9.33) Exercise. Prove that:

(a) if $a < b$ in $R^\#$, then $\lambda([a, b]) = b - a$; and

(b) if $a < b$ in $R$, then $\lambda([a, b]) = \lambda([a, b]) = \lambda([a, b])$

$$= \lambda([a, b]) = b - a.$$

(9.34) Exercise. Let $A$ be a countable subset of $R$. Prove that $\lambda(A) = 0$.

(9.35) Exercise. Let $P$ be the Cantor ternary

be a nonnegative linear functional on $\mathfrak{C}_{00}(X^*)$ and let $\iota^*$ be the set function defined on the subsets of $X^*$ constructed as in (9.19) from the functional $I^*$.

(a) For a function $f$ on $X$, let $f^*$ be $f$ with its domain restricted to $X^*$. Prove that if $f \in \mathfrak{C}_{00}(X)$, then $f^* \in \mathfrak{C}_{00}(X^*)$.

(b) Let $g \in \mathfrak{C}_{00}(X^*)$. Prove that there is a function $f \in \mathfrak{C}_{00}(X)$ such that $g = f^*$. [Use Tietze's extension theorem (7.40).]

(c) For $f \in \mathfrak{C}_{00}(X)$, let $I(f) = I^*(f^*)$. Prove that $I$ is a nonnegative linear functional on $\mathfrak{C}_{00}(X)$.

(d) Let $\iota$ be the set function obtained from $I$ as in (9.19). Prove that $\iota(X^*) = 0$ and $\iota(A) = \iota(A \cap X^*) = \iota^*(A \cap X^*)$ for every $A \subset X$.

(9.41) Exercise. Let $X$ be the product space $R_d \times R$, where the first factor is the real line with the discrete topology and the second factor is the real line with its usual topology. For $x, a, b \in R$ with $a < b$, let

$$U(x, a, b) = \{(x, y) \in X : a < y < b\} = \{x\} \times ]a, b[.$$

(a) Show that $\{U(x, a, b) : x, a, b \in R$ and $a < b\}$ is a base for the product topology on $X$ (6.41).

(b) Prove that $X$

holds. [We have already proved (i) for functions in $\mathfrak{M}^+$.] The avenue we choose toward this goal is through abstract measures and integrals defined in terms of these abstract measures. The problem of finding a largest family of functions on $X$ for which (i) holds is unsolved and apparently very difficult. Our approach to the problem is not the only one possible, but it has the advantages of simplicity and also of introducing abstract integrals, which every reader should know about anyway.

The present section is mainly concerned with properties of the set function $\iota$ and in particular with its good behavior on a certain well-defined family of subsets of $X$. The properties of $\iota$ that we need in defining this family are set down in Theorem (9.21). It turns out that set functions enjoying properties (9.21.i)–(9.21.iv) can be studied in abstracto, with no reference to a topological space or to positive functionals. We make a formal definition, as follows.
