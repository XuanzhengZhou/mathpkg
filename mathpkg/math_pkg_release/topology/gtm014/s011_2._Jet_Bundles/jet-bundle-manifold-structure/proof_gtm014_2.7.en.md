---
role: proof
locale: en
of_concept: jet-bundle-manifold-structure
source_book: gtm014
source_chapter: "2"
source_section: "2. Jet Bundles"
---

(1) By Lemma 2.6, the charts $\tau_{U,V}$ provide local bijections from open subsets $J^k(U, V) \subset J^k(X, Y)$ to $U \times V \times B_{n,m}^k$, and the transition maps $\tau_{U_1,V_1} \circ \tau_{U,V}^{-1}$ are smooth. Therefore $\{J^k(U, V), \tau_{U,V}\}$ forms a smooth atlas for $J^k(X, Y)$, making it a smooth manifold.

In these local coordinates, the source map $\alpha$ corresponds to projection onto $U$, and the target map $\beta$ corresponds to projection onto $V$. Specifically, for $\tau_{U,V}(\sigma) = (x_0, y_0, D)$, we have $\alpha(\sigma) = x_0$ and $\beta(\sigma) = y_0$. Since these are projections onto factors of a product, they are smooth submersions.

(2) The map $\Pi = \alpha \times \beta: J^k(X, Y) \to X \times Y$ is given by $\Pi(\sigma) = (\alpha(\sigma), \beta(\sigma))$. The fiber over $(p, q) \in X \times Y$ is

$$\Pi^{-1}(p, q) = J^k(X, Y)_{p,q}.$$

In a local chart $J^k(U, V)$ with $p \in U$, $q \in V$, the restriction of $\tau_{U,V}$ gives a diffeomorphism

$$J^k(U, V)_{p,q} \cong \{p\} \times \{q\} \times B_{n,m}^k \cong B_{n,m}^k.$$

For any $(p, q) \in X \times Y$, choose coordinate charts $U$ around $p$ and $V$ around $q$. Then $\Pi^{-1}(U \times V) = J^k(U, V)$, and the composition

$$J^k(U, V) \xrightarrow{\tau_{U,V}} U \times V \times B_{n,m}^k \xrightarrow{\mathrm{pr}_{12}} U \times V$$

equals the restriction of $\Pi$ to $J^k(U, V)$. The map $\tau_{U,V}$ is a diffeomorphism onto its image, and $\mathrm{pr}_{12}$ is the projection of a product. Therefore $\Pi$ is locally trivial, so $J^k(X, Y)$ is a fiber bundle over $X \times Y$ with fiber $B_{n,m}^k$.

The dimension of the jet bundle is

$$\dim J^k(X, Y) = \dim(X \times Y) + \dim B_{n,m}^k = n + m + m \cdot \binom{n+k}{k} - m.$$

Note: $J^k(X, Y)$ is a fiber bundle with Euclidean space as fiber but is not a vector bundle (except for $k = 1$, where $J^1(X, Y)$ is an affine bundle modeled on $T^*X \otimes TY$). The failure to be a vector bundle for $k > 1$ comes from the fact that the change of coordinates involves higher derivatives nonlinearly.
