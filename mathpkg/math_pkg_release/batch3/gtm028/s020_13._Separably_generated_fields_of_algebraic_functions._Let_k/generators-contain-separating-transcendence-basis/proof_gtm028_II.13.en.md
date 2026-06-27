---
role: proof
locale: en
of_concept: generators-contain-separating-transcendence-basis
source_book: gtm028
source_chapter: "II"
source_section: "§13. Separably generated fields of algebraic functions"
---

\begin{proof}
We proceed by induction on the transcendence degree $r = \operatorname{tr. deg.} K/k$.

\noindent \textbf{Case $r = 1$.} By assumption, there exists in $K$ a separating transcendental element $z$. We have $z \notin k(z^p)$, since $z$ is a transcendental. Hence, by Theorem 7, \S 5, the polynomial $X^p - z^p$ is irreducible over $k(z^p)$. Since $z$ is a root of this polynomial, it follows that $z$ is inseparable over $k(z^p)$. Since $z \in k(x_1, x_2, \cdots, x_n)$, we conclude by Theorem 10, \S 5, that at least one of the $n$ elements $x_i$ must be inseparable over $k(z^p)$. Let, say, $x_1$ be inseparable over $k(z^p)$. We shall now prove that $x_1$ is a separating transcendental of $K/k$.

Let $f(X, Z)$ be an irreducible polynomial in $k[X, Z]$ such that $f(x_1, z) = 0$. By Lemma 1 it follows that $f(X, Z)$ is irreducible in $k(Z)[X]$ (since $f(X, Z)$ must be of positive degree in $X$). Since $z$ is a transcendental over $k$, it follows that also the polynomial $f(X, z)$ is irreducible over $k(z)$ and differs therefore from the minimal polynomial of $x_1$ over $k(z)$ only by a constant factor. Since $x_1$ is inseparable over $k(z^p)$, $f(X, z)$ must be a polynomial in $X^p$. Consequently $f(X, Z)$ is a polynomial in $X^p$ and $Z^p$, i.e., $f(X, Z) = g(X^p, Z^p)$ for some $g \in k[X, Z]$. Since $f$ is irreducible, so is $g$, and $g(x_1^p, z^p) = 0$. Hence $x_1^p$ and $z^p$ are algebraically dependent over $k$.

Now $\operatorname{tr. deg.} K/k = 1$, so $x_1$ is either algebraic or transcendental over $k$. If $x_1$ were algebraic over $k$, then $z$ would be algebraic over $k(x_1)$, hence over $k$, contradicting that $z$ is transcendental. Thus $x_1$ is transcendental over $k$, and $\{x_1\}$ is a transcendence basis of $K/k$. Moreover, since $z$ is a separating transcendental, $K$ is separable over $k(z)$. By the relation $f(x_1, z) = 0$ with $f$ irreducible, $z$ is algebraic over $k(x_1)$, and the separability of $K/k(z)$ together with the algebraic relation implies that $K$ is separable over $k(x_1)$ as well. Therefore $x_1$ is a separating transcendental element of $K/k$.

\noindent \textbf{Induction step.} Assume the theorem holds for transcendence degree $r-1$ ($r > 1$). Let $\{z_1, z_2, \cdots, z_r\}$ be a separating transcendence basis of $K/k$. If we set $k_1 = k(z_1)$, then $K$ can be regarded, over $k_1$, as a field of algebraic functions of $r-1$ independent variables. Moreover, we have $K = k_1(x_1, x_2, \cdots, x_n)$, and $\{z_2, z_3, \cdots, z_r\}$ is a separating transcendence basis of $K/k_1$. By our induction hypothesis, $r-1$ of the elements $x_i$ will form a separating transcendence basis of $K/k_1$. Let, say, $\{x_1, x_2, \cdots, x_{r-1}\}$ be a separating transcendence basis of $K/k_1$. If we set $k' = k(x_1, x_2, \cdots, x_{r-1})$, then $K = k'(x_r, x_{r+1}, \cdots, x_n)$ and $K$ is a field of algebraic functions of one variable, over $k'$. Moreover, $z_1$ is a separating element of $K/k'$. Hence, by the case $r = 1$, one of the elements $x_r, x_{r+1}, \cdots, x_n$ will also be a separating element of $K/k'$. If, say, $x_r$ is such an element, then the $r$ elements $x_1, x_2, \cdots, x_{r-1}, x_r$ form a separating transcendence basis for $K/k$. This completes the proof.
\end{proof}
