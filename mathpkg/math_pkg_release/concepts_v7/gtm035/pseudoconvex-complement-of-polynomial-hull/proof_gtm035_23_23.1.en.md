---
role: proof
locale: en
of_concept: pseudoconvex-complement-of-polynomial-hull
source_book: gtm035
source_chapter: "23"
source_section: "23.1"
---
# Proof of Pseudoconvexity of Complement of Polynomial Hull

**Theorem 23.1.** Fix a compact set $Y$ in $\mathbb{C}^2$ and fix a point $p^0 \in \hat{Y} \setminus Y$. Let $B$ be an open ball in $\mathbb{C}^2$, centered at $p^0$, such that $\bar{B}$ does not meet $Y$. Then each connected component of $B \setminus \hat{Y}$ is pseudoconvex.

*Proof.* We first give a heuristic argument showing why the result should be expected. Let $Y$ be a smooth closed curve in $\mathbb{C}^2$ with $\hat{Y} \setminus Y$ nonempty. Then $\hat{Y} \setminus Y$ is a one-dimensional analytic variety by Chapter 12. Fix $p^0 \in \hat{Y} \setminus Y$. In a small ball $B$ centered at $p^0$, $\hat{Y}$ is defined by an equation

$$F(z_1, z_2) = 0,$$

where $F$ is analytic in $\bar{B}$. Put $\psi(z_1, z_2) = -\log |F(z_1, z_2)| - \log \delta(z_1, z_2)$, where $\delta$ is the distance function to the boundary of $B$. By the proposition of Section 23.2, $-\log \delta(z_1, z_2)$ is plurisubharmonic on $B$. Also, $\log |F|$ is pluriharmonic on $B \setminus \hat{Y}$.

Fix $z' \in \partial(B \setminus \hat{Y})$ and let $z^{(n)}$ be a sequence of points in $B \setminus \hat{Y}$ converging to $z'$. Either $z' \in \partial B$ or $z' \in \hat{Y}$. In the first case $-\log(\delta(z^{(n)})) \to +\infty$, and in the second case $-\log |F(z^{(n)})| \to +\infty$. In either case $\psi(z^{(n)}) \to +\infty$. It follows that the sublevel sets $\{\psi \leq c\}$ are compact. So $\psi$ is a plurisubharmonic exhaustion function for $B \setminus \hat{Y}$, and thus $B \setminus \hat{Y}$ is pseudoconvex.

The rigorous proof of Theorem 23.1 relies on the following lemma, which is the core geometric argument.

**Lemma 23.2.** Let $W \subseteq B$ be a domain in $\mathbb{C}^2$, where $B$ is a ball. If $W$ is not pseudoconvex, then there exists a proper holomorphic map from the unit disk into $\mathbb{C}^2$ whose boundary lies in $W$ but whose image meets $\mathbb{C}^2 \setminus W$, i.e., the Kontinuitätssatz fails.

*Proof of Lemma 23.2.* (Following Hörmander, Theorem 2.6.7 in [Hö2]) Assume $W$ is not pseudoconvex. Let $\delta(z)$ denote the distance from $z$ to $\partial W$. Then $-\log \delta$ is not plurisubharmonic in $W$. Consequently, there exists a complex line $L$ and a disk $D_0 \subseteq W \cap L$ such that $-\log \delta$, restricted to $L$, violates the sub-mean-value inequality on $D_0$. Write $D_0: z = z^0 + \tau \omega$, $|\tau| \leq r$, where $z^0$ and $\omega$ are fixed vectors in $\mathbb{C}^2$. Hence there exists a nonconstant polynomial $f$ such that

$$-\log \delta(z^0 + \tau \omega) \leq \operatorname{Re} f(\tau), \quad |\tau| = r, \tag{3}$$

$$-\log \delta(z^0) > \operatorname{Re} f(0). \tag{4}$$

Indeed, one first obtains (3) and (4) with $\operatorname{Re} f$ replaced by a harmonic function $h(\tau)$, then approximates $h$ by the real part of a polynomial $f$. We may assume $f(0)$ is real. By (4),

$$\delta(z^0) < e^{-\operatorname{Re} f(0)} = e^{-f(0)}.$$

Choose $\epsilon > 0$ small enough so that

$$\delta(z^0) < (1 - \epsilon) e^{-f(0)}. \tag{5}$$

Fix a unit vector $a \in \mathbb{C}^2$ with $\sum a_j \bar{\omega}_j \neq 0$ (so $a$ is not orthogonal to $\omega$ in the Hermitian sense). For $0 \leq \lambda \leq 1$ and $|\tau| \leq r$, define

$$z_\lambda(\tau) = z^0 + \tau \omega + \lambda e^{-f(\tau)} a,$$

and set $D_\lambda = \{z_\lambda(\tau) : |\tau| \leq r\}$.

For each $\lambda$, we have

$$z_\lambda(0) = z^0 + \lambda e^{-f(0)} a.$$

When $\lambda = 0$, $z_0(0) = z^0$; when $\lambda = 1$, $z_1(0) = z^0 + e^{-f(0)} a =: \tilde{z}$. Since $z_\lambda(0)$ moves continuously with $\lambda$ along the segment from $z^0$ to $\tilde{z}$, and since $z^0 \in W$ while $\tilde{z} \notin \bar{W}$ (by the choice of $a$ and the inequality (5)), there exists a point $z' \in \partial W$ and a $\lambda_0 \in (0,1]$ such that $z_{\lambda_0}(0) = z'$, and hence $D_{\lambda_0}$ contains $z'$.

Let $\lambda_1$ be the smallest $\lambda$ such that $D_\lambda$ meets $\partial W$. Then

$$0 < \lambda_1 \leq \lambda_0 \leq 1.$$

Consider the map

$$\Phi(\tau, \lambda) = z^0 + \tau \omega + \lambda e^{-f(\tau)} a$$

defined on a neighborhood of $\{|\tau| \leq r\} \times \{\lambda_1\}$ in $\mathbb{C}^2$. For each $\lambda$, $D_\lambda$ is the image of $\{|\tau| \leq r\} \times \{\lambda\}$ under $\Phi$.

The determinant of the Jacobian matrix of $\Phi$ is

$$\det \begin{pmatrix}
\omega_1 - \lambda f'(\tau) e^{-f(\tau)} a_1 & e^{-f(\tau)} a_1 \\
\omega_2 - \lambda f'(\tau) e^{-f(\tau)} a_2 & e^{-f(\tau)} a_2
\end{pmatrix}
= \det \begin{pmatrix}
\omega_1 & e^{-f(\tau)} a_1 \\
\omega_2 & e^{-f(\tau)} a_2
\end{pmatrix}
= e^{-f(\tau)} \det \begin{pmatrix}
\omega_1 & a_1 \\
\omega_2 & a_2
\end{pmatrix}.$$

Since $\omega$ and $a$ are chosen not to be parallel (as vectors in $\mathbb{C}^2$), this determinant is nonzero. Hence $\Phi$ is a local biholomorphism near $\{|\tau| < r\} \times \{\lambda_1\}$. The image of $\{|\tau| < r\} \times \{\lambda_1\}$ under $\Phi$ is therefore an embedded analytic disk whose boundary (the image of $\{|\tau| = r\} \times \{\lambda_1\}$) lies in $W$, but the disk meets $\partial W$. By the construction, $\Phi$ maps $\{|\tau| \leq r\} \times [0, \lambda_1)$ into $W$, so this is the desired family of analytic disks. This proves Lemma 23.2.

*Completion of the proof of Theorem 23.1.* Let $W$ be a connected component of $B \setminus \hat{Y}$. Suppose, for contradiction, that $W$ is not pseudoconvex. By Lemma 23.2, there exists a proper holomorphic map from the unit disk whose boundary lies in $W$ but whose image meets $\partial W$. In the language of the lemma, there is a biholomorphic map $\Phi$ defined near $\{|\tau| \leq r\} \times [0, \lambda_1]$ giving a family of analytic disks $D_\lambda$ with $D_0 \subseteq W$, and $D_{\lambda_1}$ meeting $\partial W$ while $\partial D_{\lambda_1} \subseteq W$.

Now $W \subseteq B \setminus \hat{Y}$, so $W \subseteq B$ and $W \cap \hat{Y} = \emptyset$. The boundary of $W$ relative to $B$ consists of points in $\hat{Y} \cap B$. Hence $\partial W \cap B \subseteq \hat{Y}$. By the maximum principle (or the definition of polynomial hull), $\hat{Y}$ satisfies a local maximum modulus principle: on $\hat{Y} \setminus Y$, one has the maximum principle for holomorphic functions. Since $\Phi$ is a biholomorphism, the local maximum modulus principle also holds on the compact set $K = \Phi(\{|\tau| \leq r\} \times [0, \lambda_1])$.

After a suitable rescaling in $z_2$, we may assume that $K$ meets the set $\{|z_2| < 1\}$ at some point $(a, b)$. Since the local maximum modulus principle holds on $\hat{Y} \setminus Y$, it follows, since $\Phi$ is a biholomorphism, that it also holds on $K$. Namely, if $g$ is holomorphic on a neighborhood of $K$, then, because $K \cap \partial P = K \cap \{|z_2| = 1\}$ (where $P$ is a suitable polydisk containing $K$),

$$|g|_K \leq |g|_{K \cap \{|z_2| = 1\}}.$$

Applying this to $g(z) \equiv 1/z_2$ yields $1/|b| \leq 1$, i.e., $|b| \geq 1$. But by construction $|b| < 1$, a contradiction. Therefore $W$ must be pseudoconvex, completing the proof of Theorem 23.1.
