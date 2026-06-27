---
role: exercise
locale: en
chapter: "1"
section: "007"
exercise_number: 3
---

$T: \text{Set} \longrightarrow \text{Set}$ is a faithful functor, that is, whenever $f, g: X \longrightarrow Y$ are distinct functions then $fT, gT: XT \longrightarrow YT$ are again distinct functions.

Proof. 1 implies 2. By hypothesis, some $T$-algebra has at least two elements. By forming a suitably large cartesian power (as in 4.27), for each set $X$ we can construct a $T$-algebra $(Y, \theta)$ and an injective function $f: X \longrightarrow Y$. From the naturality square (3.11) we have $X\eta.(fT.\theta) = f.Y\eta.\theta = f.\text{id}_Y = f$ is injective. As $X\eta$ is injective followed by some other function, $X\eta$ is itself surely injective.

2 implies 3. If $f \neq g$ and $Y\eta$ is injective then $f.Y\eta \neq g.Y\eta$, so $X\eta.fT \neq X\eta.gT$. Since $fT$ and $gT$ are $T$-homomorphisms, $fT \neq gT$.

3 implies 1. This is clear, since neither of the two functors involved in the trivial theories are faithful.

5.3 Definition Let $X$ be a set. For finitary $T$ (4.18), Theorem 4.25 allows us to treat elements of $XT$ as “$E$-equivalence classes of $T$-terms”; or “symbolic operations.” We view this as a linguistic or a syntactic concept. In general, let us call elements of $XT$ syntactic operations in $X$ (with respect to $T$). For example, $312 + 21 + + +$ is a syntactic operation in $X = \{1, 2, 3\}$ with respect

whenever $f: (Y, \theta) \longrightarrow (Y', \theta')$ is a $\mathbf{T}$-homomorphism (and $f^X$ sends the $X$-tuple $y: X \longrightarrow Y$ in $Y$ to the $X$-tuple $y.f: X \longrightarrow Y'$ in $Y'$, that is $f^X$ sends the $X$-tuple $(y_x: x \in X)$ in $Y$ to the $X$-tuple $(y_x f: x \in X)$ in $Y'$). Let us notice that "raising to the $X$th power" is a functor $(\cdot)^X: \mathbf{Set} \longrightarrow \mathbf{Set}$. Let us denote $U^T: \mathbf{Set}^T \longrightarrow \mathbf{Set}$ (as in 4.8) by $U$ for short, and the composite functor $U.(\cdot)^X: \mathbf{Set}^T \longrightarrow \mathbf{Set}$ by $U^X$. Then what we have stipulated about $\alpha$ may be summed up by saying: "$\alpha$ is a natural transformation from $U^X$ to $U$." Let this property define a semantic operation in $X$ (with respect to $\mathbf{T}$). To give credibility to this new point of view—that the operations may be defined after the homomorphisms are—we prove the following theorem:

5.5 Theorem. Let $\mathbf{T}$ be an algebraic theory in $\mathbf{Set}$ and let $X$ be a set. Let $\mathcal{O}_X(T)$ be the set of natural transformations from the functor $(\cdot)^X$ (as defined in 5.4) to $T$. Defining $U$ and $U^X$ as in 5.4, let $\mathcal{O}_X(T)$ be the set of natural transformations from $U^X$ to $U$ (that is, semantic operations in $X$). Then the passage

$$XT \longrightarrow \mathcal{O}_X(T)$$
$$\omega \vdash (\cdot)^X \xrightarrow{\bar{\omega}} T$$
$$\langle X \xrightarrow{

the naturality equation $X\alpha.fT = f^X.Y\alpha$, so that, defining $\omega = \langle \text{id}_X, X\alpha \rangle$, we have $\langle f, Y\hat{\omega} \rangle = \langle \langle \text{id}_X, X\alpha \rangle, fT \rangle = \langle \text{id}_X, f^X.Y\alpha \rangle = \langle f, Y\alpha \rangle$, that is $\hat{\omega} = \alpha$. Let us turn to 5.8 and 5.9. Starting with $\omega$, $\langle X\eta, (XT, X\mu)\tilde{\omega} \rangle = \langle X\eta, XT\hat{\omega}.X\mu \rangle = \langle \omega, X\eta.T.X\mu \rangle = \omega$ (by 3.16). Starting with $\alpha$, for each $f:X \longrightarrow Y$ and each T-algebra structure $\theta$ on $Y$ we have the T-homomorphic extension $f^\# = fT.\theta:(XT, X\mu) \longrightarrow (Y, \theta)$ of 4.13, and hence the naturality square

$$XT^X \longrightarrow Y^X \longrightarrow XT \longrightarrow Y \longrightarrow fT.\theta$$

Setting $\omega = \langle X\eta, (XT, X\mu)\alpha \rangle$, we have $\langle f, (Y, \theta)\tilde{\omega} \rangle = \langle f, Y\hat{\omega}.\theta \rangle = \langle X\eta, (XT, X\mu)\alpha.fT.\theta \rangle = \langle X\eta, (fT.\theta)^X.(Y, \theta)\alpha \rangle = \langle X\eta.fT.\theta, (Y, \theta)\alpha \rangle = \langle f.Y\eta.\theta, (Y, \theta)\alpha \rangle = \langle f, (Y, \theta)\alpha \rangle$.

Passages (5.7) and (5.9) say

S is a support of $\psi$ if such a factorization exists (and $\psi$ is independent of the elements of $X$ not in $S$). A subset $S$ of $X$ is a support of the semantic operation $\alpha: U^X \longrightarrow U$ if $S$ is a support of $(Y, \theta)\alpha: Y^X \longrightarrow Y$ for every T-algebra $(Y, \theta)$. The arity of $\alpha: U^X \longrightarrow U$ is defined by “$ar(\alpha) = \text{Min}(n:n$ is a cardinal and there exists a support of $\alpha$ of cardinal $n)$.” For example, let $x$ and $x'$ be distinct elements of $X$. Then sending $f: X \longrightarrow Y$ to $xf + x'f$ is a semantic operation in $X$ with respect to abelian group theory whose arity is 2. $S$ is a support if and only if $\{x, x'\} \subset S$. We must not infer from this example that the intersection of all supports is a support, however. For the ultrafilter theory of 3.21, if $U \in X\beta$, then the set of supports of the semantic operation is precisely $U!$ (See exercise 3.)

We now show that syntactic arity and semantic arity coincide:

5.11 Theorem. Let $T$ be an algebraic theory of sets, let $X$ be a set, and let $\omega \in XT$ be a syntactic operation in $X$ with corresponding semantic operation $\tilde{\omega}: U^X \longrightarrow U$ as in 5.5. Then $\omega$ and $\tilde{\omega}$ have the same arity.

Proof. $ar(\tilde{\omega}) \leqslant ar(\omega)$. There exist $f: ar(\omega) \longrightarrow X$ and $h \in (ar(\omega))T$ with $\langle h, fT \rangle = \omega$. Let $S = \{uf: u \in ar(\omega)\}$ be the image of $f$ with inclusion map $i: S \longrightarrow X$ and define $p: ar(\omega)

Define $\rho = \langle S\eta, \psi \rangle \in ST$. Then $\langle \rho, iT \rangle = \langle S\eta, \psi.iT \rangle = \langle i.g, \psi.iT \rangle = \langle g, (ST, S\mu)\tilde{\omega}.iT \rangle = \langle g, iT^X.(XT, X\mu)\tilde{\omega} \rangle = \langle g.iT, (XT, X\mu)\tilde{\omega} \rangle = \langle i.g.iT, \Gamma \rangle = \langle S\eta.iT, \Gamma \rangle = \langle i.X\eta, \Gamma \rangle = \langle X\eta, (XT, X\mu)\tilde{\omega} \rangle = \omega$. Now suppose that $\text{ar}(\tilde{\omega}) = 0$. The above argument is still valid—that is, $g$ still exists—providing $ST \neq \emptyset$ (where, now, $S = \emptyset$). Otherwise, $\emptyset$ is an algebra and there exists a factorization

which is a contradiction. $\square$

5.12 Example. Let $T$ be the algebraic theory obtained from the equational presentation of semigroups in 4.17 by adjoining the additional equation $\{v_1v_2v_3\**, v_1v_2*\}$. Let $X = \{v_1, v_2\}$, and set $\omega = v_1v_2^*$. It is clear that $\text{ar}(\omega) \leqslant 2$. The following model (which is actually the free $T$-algebra on two generators)

$$
\begin{array}{c c c c c c c c}
x & y & xy & yx & xx & yx \\
xx & xy & xx & xy & xx & xy \\
yx & yy & yx & yy & yx & yy \\
xy & xy & xy & xy & xy & xy \\
yx & yx & yx & yx &
