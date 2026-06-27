---
role: proof
locale: en
of_concept: formal-character-decomposition-into-composition-factors
source_book: gtm009
source_chapter: "24"
source_section: "Appendix (steps 3-4)"
---

**Proof.** The proof proceeds by induction on the length of a composition series for the standard cyclic module $Z = Z(\lambda)$.

**Step 3 (Induction).** Consider a standard cyclic module $Z$ of highest weight $\lambda \in \Lambda^+$. Let $v^+$ be a maximal vector generating $Z$. The Casimir element $c$ acts on all of $Z$ as the scalar $\chi_\lambda(c) = (\lambda + \delta, \lambda + \delta) - (\delta, \delta)$ (by the computation of step 2).

If $Z \cong V(\lambda)$ is irreducible, then the composition series consists of the single factor $V(\lambda)$ and there is nothing to prove; the multiplicity $a_{\lambda\lambda} = 1$.

Otherwise, $Z$ contains a proper nonzero submodule. Let $W \subset Z$ be a maximal proper submodule. The quotient $Z/W$ is irreducible, hence isomorphic to $V(\mu)$ for some $\mu \in \Lambda^+$ with $\mu \preceq \lambda$. Because $c$ acts as the same scalar $\chi_\lambda(c)$ on both $Z$ and all its subquotients, we must have $(\mu + \delta, \mu + \delta) = (\lambda + \delta, \lambda + \delta)$ (i.e., condition $(*)$ holds). Moreover, $W$ is itself a standard cyclic module (being a submodule of a standard cyclic module) of some highest weight $\nu \prec \lambda$ also satisfying $(*)$. By induction on the length, both $Z/W \cong V(\mu)$ and $W$ possess composition series whose factors are irreducible modules $V(\tau)$ with $\tau \preceq \lambda$ and $(\tau + \delta, \tau + \delta) = (\lambda + \delta, \lambda + \delta)$. Fitting these together yields a composition series for $Z$ of the required type.

Thus we obtain: for each $\mu_j$ in the set $\{\mu_1, \ldots, \mu_t\}$ of weights satisfying $(*)$ and $\mu \preceq \lambda$, the formal character of the standard cyclic module $Z(\mu_j)$ can be expressed as:
$$
\operatorname{ch}'_{\mu_j} = \sum_{i \leq j} a_{ij} \operatorname{ch}_{\mu_i},
$$
with $a_{ij} \in \mathbb{Z}^+$ (nonnegative integers) and $a_{jj} = 1$. For $i > j$, we set $a_{ij} = 0$.

**Step 4 (Inversion).** The matrix $A = (a_{ij})_{1 \leq i,j \leq t}$ is upper triangular with 1s on the diagonal, hence $\det A = 1$. Consequently, $A$ is invertible over $\mathbb{Z}$. Its inverse $B = (b_{ij})$ also has integer entries. Applying $B$ yields:
$$
\operatorname{ch}_{\mu_i} = \sum_{j} b_{ij} \operatorname{ch}'_{\mu_j}.
$$

In particular, for $\mu_i = \lambda$ (which corresponds to the maximal index since $\mu_i \prec \mu_j$ implies $i \leq j$), we obtain:
$$
\operatorname{ch}_{\lambda} = \sum_{\mu \prec \lambda} c(\mu) \, \operatorname{ch}'_{\mu},
$$
where the sum is taken over all $\mu \in \Lambda$ satisfying $(\mu + \delta, \mu + \delta) = (\lambda + \delta, \lambda + \delta)$, and the coefficients satisfy $c(\mu) \in \mathbb{Z}$ with $c(\lambda) = 1$. $\square$
