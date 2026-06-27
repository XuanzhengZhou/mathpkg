---
role: proof
locale: en
of_concept: theorem-isotone-functions-chain
source_book: gtm027
source_chapter: "0"
source_section: "Orderings"
---

# Proof of Theorem 11: Uniqueness of Isotone Functions on a Chain

Suppose that $f$ and $g$ are isotone functions on a chain $X$ to a chain $Y$, and that $f$ and $g$ agree on a dense subset $X_0$ of $X$. We must show that $f(x) = g(x)$ for every $x \in X$.

Assume, for contradiction, that there exists $x \in X$ such that $f(x) \neq g(x)$. Since $Y$ is a chain, we may suppose without loss of generality that $f(x) < g(x)$.

Consider the sets:

$$
L = \{w \in X_0 : w \leq x\}, \qquad R = \{w \in X_0 : w \geq x\}.
$$

Since $X$ is a chain, every element of $X_0$ belongs either to $L$ or to $R$ (or both, if it equals $x$ in the case $x \in X_0$). Because $f$ and $g$ agree on $X_0$, we have $f(w) = g(w)$ for all $w \in L \cup R = X_0$.

By isotonicity, $f(w) \leq f(x)$ for every $w \in L$. Hence $f[L]$ is bounded above by $f(x)$. On the other hand, for $w \in R$, isotonicity of $g$ gives $g(x) \leq g(w) = f(w)$. Thus $f[R]$ is bounded below by $g(x)$, and consequently $f[R]$ is contained in $\{y \in Y : y \geq g(x)\}$.

Now observe that no element of $f[X_0]$ lies strictly between $f(x)$ and $g(x)$. For if $w \in L$, then $f(w) \leq f(x)$; and if $w \in R$, then $f(w) \geq g(x) > f(x)$.

Since $X_0$ is dense in $X$, for any $y \in X$ with $y > x$ there exists $w \in X_0$ such that $x < w < y$. Then $f(w) = g(w)$ and $f(w) \geq g(x) > f(x)$. By isotonicity of $f$, $f(y) \geq f(w) > f(x)$. Hence $f(y) > f(x)$ for all $y > x$.

Similarly, for any $y \in X$ with $y < x$, density of $X_0$ provides $w \in X_0$ with $y < w < x$, whence $f(y) \leq f(w) = g(w) \leq g(x)$. But also $f(w) \leq f(x)$, so $f(y) \leq f(x)$.

Now consider the image of the set $R$ under $f$. Every member of $f[R]$ is at least $g(x)$, which is strictly greater than $f(x)$. But by the argument above, $f$ is strictly greater than $f(x)$ on all points of $X$ that exceed $x$. In particular, the gap $(f(x), g(x))$ in $Y$ contains no values of $f$ on $X_0$, yet $f$ maps points of $X_0$ (specifically those in $R$) into the set

$$
\{y : f(x) < y < g(x)\} \cup \{y : y \geq g(x)\}
$$

which is precisely $\{y : y > f(x)\}$. But since $f(w) \geq g(x)$ for $w \in R$, the image $f[R]$ in fact lies in $\{y : y \geq g(x)\}$, avoiding the open interval $(f(x), g(x))$ entirely.

The density of $X_0$ now forces a contradiction: pick any $z \in X_0$ with $z > x$ (such $z$ exists because otherwise $x$ would be an upper bound of $X_0$, and then by density $x$ would be the maximum of $X$, in which case $f(x) = g(x)$ follows from the agreement on $X_0$ together with the definition of the isotone extension in Theorem 10). The value $f(z) = g(z)$ lies in the image of $f$ on $X_0$, and we have seen that $f(z) \geq g(x)$. Meanwhile, all values of $f$ on $L$ are $\leq f(x) < g(x)$. Thus the image of $X_0$ under $f$ is separated by a gap, which is impossible for a function isotone on a chain with dense domain.

The contradiction shows that our assumption $f(x) < g(x)$ is false. Hence $f(x) = g(x)$ for all $x \in X$, and the theorem is proved.
