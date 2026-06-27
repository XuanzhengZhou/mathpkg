---
role: proof
locale: en
of_concept: higher-cohomology-of-maximal-ideal-space
source_book: gtm035
source_chapter: "15"
source_section: "15.8"
---
# Proof Sketch of Higher Cohomology of the Maximal Ideal Space

**Theorem 15.8.** Let $\mathfrak{A}$ be a Banach algebra with $n$ generators. Then

$$H^p(\mathcal{M}(\mathfrak{A}), \mathbb{Z}) = 0 \quad \text{for all } p > n.$$

In other words, the Čech cohomology of the maximal ideal space vanishes in dimensions strictly greater than the number of generators.

## Note on the Proof

The source text (GTM035, Section 15) only states this result and notes that no analogous algebraic interpretation of the higher cohomology groups $H^p(\mathcal{M}, \mathbb{Z})$, $p > 1$, had been obtained at the time of writing. The full proof is not included in the section.

The underlying idea is as follows (see Royden, *Function algebras*, Bull. Amer. Math. Soc. 69 (1963), 281–298): Let the $n$ generators of $\mathfrak{A}$ be denoted $x_1, \ldots, x_n$. Their Gelfand transforms $\hat{x}_1, \ldots, \hat{x}_n$ embed $\mathcal{M}(\mathfrak{A})$ into $\mathbb{C}^n$ as the joint spectrum. Then $\mathcal{M}$ can be covered by $n+1$ open sets (e.g., preimages under the joint spectrum map of open hemispheres covering $\mathbb{C}^n$), each of which has trivial cohomology in positive degrees (being essentially open subsets of a simplex / contractible). By standard results in Čech cohomology, the nerve of such a covering has dimension at most $n$, hence $H^p$ vanishes for $p > n$.

The result implies that for finitely generated Banach algebras, the only cohomological invariant that carries algebraic information is $H^1$, which is the group classified by the Arens–Royden theorem (Theorem 15.3).
