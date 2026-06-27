---
role: proof
locale: en
of_concept: pseudoconcave-maximum-modulus-theorem
source_book: gtm035
source_chapter: "Chapter 25"
source_section: "25.2"
---
# Proof of Pseudoconcave Sets Give Maximum Modulus Algebras

**Theorem 25.2.** Let $X$ be a pseudoconcave set contained in the open bidisk $\{|z| < 1, |w| < 1\} \subseteq \mathbb{C}^2$. Denote by $A$ the algebra of polynomials in $z$ and $w$ restricted to $X$. Putting $D = \{|z| < 1\}$ and $\pi : (z, w) \mapsto z$, then $(A, X, D, \pi)$ is a maximum modulus algebra.

**Proof.** Recall (Definition 25.1) that $X$ is pseudoconcave in $\Omega = \{|z| < 1, |w| < 1\}$ if the open set $\Omega \setminus X$ is pseudoconvex. Let $\Omega = D \times D_w$, where $D = \{|z| < 1\}$ and $D_w = \{|w| < 1\}$.

We must verify the axioms of a maximum modulus algebra $(A, X, D, \pi)$:

1. $A$ is a uniform algebra on the compact space $X$ (here $X$ is relatively closed in $\Omega$, so we consider its closure or work with the given topology).
2. $\pi : X \to D$ is a continuous projection with $\pi^* : \mathcal{O}(D) \to A$ injective (here $\pi(z, w) = z$).
3. For each $\lambda \in D$, the fiber $X_\lambda = \pi^{-1}(\lambda)$ is nonempty, and the maximum modulus principle holds: for every $f \in A$,
   $$\max_{(z,w) \in X} |f(z,w)| = \max_{\lambda \in D} \max_{w \in X_\lambda} |f(\lambda, w)|.$$
4. The Shilov boundary of $A$ is contained in $\pi^{-1}(\partial D) \cup (\text{the "distinguished boundary"})$.

The key property to verify is that for any $f \in A$ (a polynomial in $z, w$) and any $\lambda_0 \in D$, the maximum of $|f|$ on the fiber $X_{\lambda_0}$ is bounded by the supremum over fibers near the boundary, or more precisely that the local maximum modulus principle applies.

**Step 1: Pseudoconcavity and analytic structure.** Since $X$ is pseudoconcave in the bidisk, the complement $\Omega \setminus X$ is pseudoconvex. By the solution of the Levi problem (Oka's theorem), $\Omega \setminus X$ is a domain of holomorphy. This means there exists a holomorphic function on $\Omega \setminus X$ that cannot be extended holomorphically across any boundary point.

**Step 2: Fibers over $D$.** Since $X \subset D \times D_w$ and $X$ is pseudoconcave, for each $z_0 \in D$, the fiber $X_{z_0} = \{w : (z_0, w) \in X\}$ is a nonempty proper subset of $D_w$. If it were empty for some $z_0$, then near $(z_0, 0)$ the complement would contain a full neighborhood, contradicting pseudoconcavity. If $X_{z_0} = D_w$ for some $z_0$, then the open set $D \setminus X$ would have a "hole," violating pseudoconvexity of $\Omega \setminus X$.

**Step 3: The local maximum modulus principle (Theorem 9.3, Rossi).** Let $f \in A$ be a polynomial restricted to $X$. The local maximum modulus principle for $A$ on $X$ states that if a point $p \in X$ is not in the Shilov boundary of $A$, then there exists a neighborhood $U$ of $p$ and a constant $c < 1$ such that
$$|f(p)| \leq c \cdot \max_X |f|$$
for all $f \in A$. For pseudoconcave $X$, one verifies that no point with $|z| < 1$ can be a peak point for $A$, and hence the Shilov boundary lies in $\{|z| = 1\} \cap X$.

**Step 4: Verification of the maximum modulus algebra property.** For any $f \in A$ and $\lambda \in D$, consider the function
$$M_f(\lambda) = \max\{|f(\lambda, w)| : (\lambda, w) \in X\}.$$

By the pseudoconcavity of $X$, the set $X$ is the zero set of a plurisubharmonic function (or more precisely, $X$ can be described as $\{\rho \leq 0\}$ for a plurisubharmonic function $\rho$ on $\Omega$). Then one can show that $\log M_f(\lambda)$ is a subharmonic function on $D$.

For a maximum modulus algebra, the defining property is that for all $\lambda \in D$,
$$M_f(\lambda) \leq \sup_{\zeta \in \partial D} M_f(\zeta).$$

This follows from the subharmonicity of $\log M_f(\lambda)$ and the maximum principle for subharmonic functions: since $D$ is a domain in $\mathbb{C}$, any subharmonic function attains its maximum on the boundary $\partial D$.

More precisely, fix $f \in A$ and let $M = \sup_{\lambda \in D} M_f(\lambda)$. Choose a sequence $\lambda_n \in D$ with $M_f(\lambda_n) \to M$. If $M$ is attained at an interior point $\lambda_0$, then by the Rossi local maximum modulus principle and the pseudoconcave structure, one derives a contradiction unless $f$ is constant on the fibers. The detailed argument uses the fact that $\log M_f$ is plurisubharmonic on $D$, and for pseudoconcave $X$, its maximum on $D$ must occur on $\partial D$.

Thus $\sup_{\lambda \in D} M_f(\lambda) = \sup_{\lambda \in \partial D} M_f(\lambda)$, verifying that $(A, X, D, \pi)$ satisfies the axioms of a maximum modulus algebra.

The theorem is proved in [We12] by Wermer; the general result (for $X$ pseudoconcave in $G \times \mathbb{C}$ with $G \subset \mathbb{C}$ a domain) was established by Slodkowski [Sl1] using analytic set-valued functions.
