---
role: proof
locale: en
of_concept: orthonormal-basis-simultaneous-eigenforms
source_book: gtm041
source_chapter: "6"
source_section: "6.14"
---

The Petersson inner product on $M_{2k,0}$ is defined by
$$\langle f, g \rangle = \iint_{R_\Gamma} f(\tau) \overline{g(\tau)} v^{2k-2} \, du \, dv,$$
where $R_\Gamma$ is a fundamental domain for the modular group $\Gamma = \text{SL}_2(\mathbb{Z})$.

The Hecke operators $T_n$ for $(n, 1) = 1$ are Hermitian with respect to this inner product:
$$\langle T_n f, g \rangle = \langle f, T_n g \rangle.$$

Moreover, the Hecke operators commute with each other:
$$T_m T_n = T_n T_m = \sum_{d \mid (m,n)} d^{2k-1} T_{mn/d^2}.$$

By the spectral theorem for commuting Hermitian operators on a finite-dimensional inner product space, there exists an orthonormal basis of $M_{2k,0}$ consisting of simultaneous eigenvectors for all $T_n$. These eigenvectors are called simultaneous eigenforms.

Each such eigenform can be normalized so that its first Fourier coefficient is 1, yielding a basis of normalized simultaneous eigenforms. Since the $T_n$ are Hermitian, the corresponding eigenvalues are real. The orthogonal (but not necessarily orthonormal) basis property follows from the fact that eigenvectors corresponding to different systems of eigenvalues are orthogonal.

For detailed proofs, see Hecke [11], Petersson [32], or Ogg [26].
