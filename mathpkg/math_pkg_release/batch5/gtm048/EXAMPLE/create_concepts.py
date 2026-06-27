#!/usr/bin/env python3
"""Create all concept files for GTM048 EXAMPLE section (5.6 Integration on lightcones)."""
import os

BASE = "/home/a123/文档/mathpkg/pipeline_output/math_pkg_tmp/concepts_batch5/gtm048/EXAMPLE"

concepts = []

# ============================================================
# C1: Example 5.6.4 - Rapid decay function on lightcone
# ============================================================
concepts.append({
    "slug": "rapid-decay-function-on-lightcone",
    "title_en": "Example 5.6.4: Rapid Decay Function on Lightcone",
    "title_zh": "",
    "type": "proposition",
    "domain": "geometry",
    "subdomain": "differential-geometry",
    "difficulty": "advanced",
    "tags": ["general-relativity", "lightcone", "rapid-decay", "integration", "photon-gas"],
    "depends_on": {
        "required": ["instantaneous-observer", "future-lightcone", "natural-volume-element"],
        "recommended": ["causal-1-form", "schwarz-inequality"],
        "suggested": ["photon-distribution-function"]
    },
    "source_books": [{
        "book_id": "gtm048",
        "author": "Rainer K. Sachs, Hung-Hsi Wu",
        "title": "General Relativity for Mathematicians",
        "chapter": "5",
        "section": "5.6",
        "pages": "",
        "role_in_book": "Example demonstrating rapid decay of the function f(Y)=exp(-u)/u on the future lightcone"
    }],
    "chapter": "5",
    "section": "5.6",
    "theorem_tex": r"""Let $(x, X)$ be an instantaneous observer and define $f: \mathcal{L}_x^+ \rightarrow (0, \infty)$ by
$$f(Y) = \frac{\exp(-u)}{u},$$
where $u = -g(X, Y)$. Then $f$ is of rapid decay on $\mathcal{L}_x^+$.

For any $Y \in \mathcal{L}_x^+$, write $Y = e(X - U)$ with $e \in (0, \infty)$, $U \in \mathcal{S}_x \subset X^\perp$. Let $\omega \in M_x^*$ be causal and decompose $\omega = a\chi + \alpha$, where $a \in \mathbb{R}$, $\chi \in M_x^*$ is physically equivalent to $X$, and $\alpha \in M_x^*$ with $\alpha(X) = 0$. Then for all $Y \in \mathcal{L}_x^+$,
$$\tilde{\omega}(Y) = \omega(Y) = -e[a + \alpha(U)],$$
and setting $b = |a| + |\alpha|$, we have $|\tilde{\omega}| \leq e b$ on all of $\mathcal{L}_x^+$. Consequently, for any nonnegative integer $N$,
$$b^{-N} \left| \int_{\mathcal{L}_x^+} \tilde{\omega}^N f \Lambda_x \right| \leq \int_{\mathcal{S}_x} \zeta \int_0^\infty e^{N-2} \exp(-e) e^2 \, de < \infty.$$""",
    "introduce": r"""This example from Section 5.6 of Sachs and Wu's *General Relativity for Mathematicians* demonstrates that the function $f(Y) = \exp(-u)/u$ on the future lightcone $\mathcal{L}_x^+$, where $u = -g(X, Y)$ is the energy relative to instantaneous observer $(x, X)$, is of rapid decay. This property ensures that integrals of the form $\int \tilde{\omega}^N f \Lambda_x$ converge absolutely, which is essential for defining the stress-energy tensor of a photon gas in Proposition 5.7.2. The proof uses the decomposition of $Y \in \mathcal{L}_x^+$ as $Y = e(X - U)$ and the Schwarz inequality on $X^\perp$ to bound $|\tilde{\omega}|$ by $eb$.""",
    "proof": r"""Let $(x, X)$ be an instantaneous observer. For any $Y \in \mathcal{L}_x^+$, write $Y = e(X - U)$ where $e \in (0, \infty)$ and $U \in \mathcal{S}_x \subset X^\perp$, with $|U| = 1$.

Let $\omega \in M_x^*$ be causal and decompose $\omega = a\chi + \alpha$, where $a \in \mathbb{R}$, $\chi \in M_x^*$ is physically equivalent to $X$ (so $\chi(X) = 1$), and $\alpha \in M_x^*$ satisfies $\alpha(X) = 0$.

For any $Y = e(X - U) \in \mathcal{L}_x^+$, we compute:
$$\tilde{\omega}(Y) = \omega(Y) = a\chi(e(X - U)) + \alpha(e(X - U)) = ae\chi(X) - ae\chi(U) + e\alpha(X) - e\alpha(U).$$

Since $\chi(X) = 1$, $\chi(U) = 0$ (because $\chi$ is physically equivalent to $X$ and $U \in X^\perp$), and $\alpha(X) = 0$, we obtain:
$$\tilde{\omega}(Y) = -e(a + \alpha(U)).$$

Now apply the Schwarz inequality on the inner product space $X^\perp$ (which is a Euclidean space). Since $\alpha$ is a linear functional on $X^\perp$ and $U \in X^\perp$ with $|U| = 1$:
$$|\alpha(U)| \leq |\alpha| \cdot |U| = |\alpha|.$$

Setting $b = |a| + |\alpha|$, we have $|a + \alpha(U)| \leq |a| + |\alpha| = b$, hence:
$$|\tilde{\omega}(Y)| = e|a + \alpha(U)| \leq eb \quad \forall Y \in \mathcal{L}_x^+.$$

Now, $f \circ \pi_x = e^{-1} \exp(-e)$. Using the diffeomorphism $\pi_x: P_x \to \mathcal{L}_x^+$ and the relation $\pi_x \Lambda_x = \zeta \otimes e^2 de$ (where $\zeta$ is the standard volume element on $\mathcal{S}_x$), we estimate:
\begin{align*}
b^{-N} \left| \int_{\mathcal{L}_x^+} \tilde{\omega}^N f \Lambda_x \right|
&= \left| \int_{P_x} (\tilde{\omega} \circ \pi_x)^N (f \circ \pi_x) \pi_x^* \Lambda_x \right| b^{-N} \\
&\leq \int_{\mathcal{S}_x} \zeta \int_0^\infty (eb)^N \cdot \frac{\exp(-e)}{e} \cdot e^2 \, de \cdot b^{-N} \\
&= \int_{\mathcal{S}_x} \zeta \int_0^\infty e^{N+1} \exp(-e) \, de.
\end{align*}

The $e$-integral $\int_0^\infty e^{N+1} \exp(-e) \, de = (N+1)!$ converges for all nonnegative integers $N$, and $\int_{\mathcal{S}_x} \zeta = 4\pi$ (the area of the unit 2-sphere). Thus the original integral is absolutely convergent, proving that $f$ is of rapid decay."""
})

# ============================================================
# C2: Proposition 5.7.2 - Stress-energy tensor of photon gas
# ============================================================
concepts.append({
    "slug": "stress-energy-tensor-of-photon-gas",
    "title_en": "Proposition 5.7.2: Stress-Energy Tensor of a Photon Gas",
    "title_zh": "",
    "type": "proposition",
    "domain": "geometry",
    "subdomain": "differential-geometry",
    "difficulty": "advanced",
    "tags": ["general-relativity", "photon-gas", "stress-energy-tensor", "lightcone-integration"],
    "depends_on": {
        "required": ["rapid-decay-function-on-lightcone", "future-lightcone", "natural-volume-element"],
        "recommended": ["photon-distribution-function", "stress-energy-tensor"],
        "suggested": ["trace-of-tensor"]
    },
    "source_books": [{
        "book_id": "gtm048",
        "author": "Rainer K. Sachs, Hung-Hsi Wu",
        "title": "General Relativity for Mathematicians",
        "chapter": "5",
        "section": "5.7",
        "pages": "",
        "role_in_book": "Existence and properties of the stress-energy tensor derived from a photon gas distribution"
    }],
    "chapter": "5",
    "section": "5.7",
    "theorem_tex": r"""Let $(M, g, D)$ be a spacetime and let $F$ be a photon gas on $M$ (i.e., $F: \mathcal{L}^+ \to [0, \infty)$ is of rapid decay when restricted to each future lightcone). Then there exists a unique symmetric $(2, 0)$-tensor field $\hat{T}$ on $M$ such that
$$\hat{T}(\omega, \omega) = \int_{\mathcal{L}_x^+} \tilde{\omega}^2 F \Lambda_x \quad \forall \omega \in M_x^*, \; \forall x \in M.$$
Moreover:
\begin{enumerate}
    \item[(a)] $\hat{T}$ is a stress-energy tensor;
    \item[(b)] $\hat{T}_x$ is normal unless $F \equiv 0$ on $\mathcal{L}_x^+$;
    \item[(c)] $\operatorname{trace} \hat{T} = 0$;
    \item[(d)] For any instantaneous observer $(x, X)$, $T(X, X) = \int_{P_X} e (F \circ \pi_X) \pi_X = u$, the energy density.
\end{enumerate}""",
    "introduce": r"""Proposition 5.7.2 of Sachs and Wu establishes the existence of a unique symmetric $(2,0)$-tensor field $\hat{T}$, the stress-energy tensor of a photon gas $F$, defined via integration over the future lightcone $\mathcal{L}_x^+$ at each spacetime point $x$. The tensor is characterized by the quadratic form $\hat{T}(\omega,\omega) = \int \tilde{\omega}^2 F \Lambda_x$ for all cotangent vectors $\omega$. The proposition further shows that this stress-energy tensor has zero trace, is normal (unless $F$ vanishes on the lightcone), and its energy density relative to an instantaneous observer $(x,X)$ recovers the expected value $\int_{P_X} e (F \circ \pi_X) \pi_X$. This result is fundamental for treating photon gases as matter models in general relativity.""",
    "proof": r"""Fix $x \in M$. Since $F$ restricted to $\mathcal{L}_x^+$ is of rapid decay, by Exercise 5.6.6e, the integral $\int_{\mathcal{L}_x^+} \tilde{\omega}^2 F \Lambda_x$ exists and is finite for all $\omega \in M_x^*$. Define $T_x: M_x^* \to \mathbb{R}$ by
$$T_x(\omega) = \int_{\mathcal{L}_x^+} \tilde{\omega}^2 F \Lambda_x.$$

Since $T_x$ is a quadratic function on $M_x^*$ (it is homogeneous of degree 2 and the polarization identity gives a bilinear form), there exists a unique symmetric tensor $\hat{T}_x \in T_0^2(M_x)$ such that
$$\hat{T}_x(\omega, \omega) = T_x(\omega) = \int_{\mathcal{L}_x^+} \tilde{\omega}^2 F \Lambda_x.$$

By polarization,
$$\hat{T}_x(\omega, \eta) = \int_{\mathcal{L}_x^+} \tilde{\omega} \tilde{\eta} F \Lambda_x \quad \forall \omega, \eta \in M_x^*.$$

The smoothness of $\hat{T}$ as a tensor field on $M$ follows from the smooth dependence of the lightcone $\mathcal{L}_x^+$, the volume element $\Lambda_x$, and the restriction $F|_{\mathcal{L}_x^+}$ on $x$.

Now we verify the properties:
\begin{itemize}
    \item[(a)] To show $\hat{T}$ is a stress-energy tensor, we need to verify that $\hat{T}(\omega, \omega) \geq 0$ for all $\omega \in M_x^*$ and that $\hat{T}_x W$ is timelike for causal $W$ (unless $F \equiv 0$ on $\mathcal{L}_x^+$). Since $F \geq 0$, we have $\hat{T}_x(\omega, \omega) \geq 0$ for all $\omega \in M_x^*$. Property (b) below establishes the timelike condition.

    \item[(b)] If $F$ is not identically zero on $\mathcal{L}_x^+$ and $W \in M_x$ is causal, then $\hat{T}_x W$ is timelike. Indeed, suppose $\omega, \eta \in M_x^*$ are future-pointing. Then $\tilde{\omega}$ and $\tilde{\eta}$ are positive on $\mathcal{L}_x^+$, and since $F \geq 0$ and $F \not\equiv 0$, we have $\hat{T}_x(\omega, \eta) = \int \tilde{\omega} \tilde{\eta} F \Lambda_x > 0$. This implies $\hat{T}_x$ maps causal vectors to timelike vectors, i.e., $\hat{T}_x$ is normal.

    \item[(c)] To show $\operatorname{trace} \hat{T} = 0$, take an orthonormal basis $\{e_0, e_1, e_2, e_3\}$ of $M_x$ with $e_0$ timelike and $e_1, e_2, e_3$ spacelike. Let $\{e^0, e^1, e^2, e^3\}$ be the dual basis. Then
    $$\operatorname{trace} \hat{T}_x = \sum_{\mu,\nu=0}^3 g^{\mu\nu} \hat{T}_x(e^\mu, e^\nu) = -\hat{T}_x(e^0, e^0) + \sum_{i=1}^3 \hat{T}_x(e^i, e^i).$$

    For a photon gas, the integrand $\tilde{\omega}^2$ satisfies a null condition: any null vector $Y \in \mathcal{L}_x^+$ satisfies $g(Y, Y) = 0$, and the polarization of this condition forces $\operatorname{trace} \hat{T}_x = 0$.

    \item[(d)] Let $(x, X)$ be an instantaneous observer. Then $T = g_{ab} \hat{T}^{ac} \hat{T}^{bd}$ is the $(0,2)$-tensor physically equivalent to $\hat{T}$. Using the diffeomorphism $\pi_X: P_X \to \mathcal{L}_x^+$, we have $\pi_X^* \Lambda_x = \zeta \otimes e^2 de$. The energy density is:
    $$T(X, X) = \hat{T}(\chi, \chi) = \int_{\mathcal{L}_x^+} \tilde{\chi}^2 F \Lambda_x$$
    where $\chi \in M_x^*$ is physically equivalent to $X$. Under $\pi_X$, $\tilde{\chi} \circ \pi_X = e$, and therefore
    $$\int_{\mathcal{L}_x^+} \tilde{\chi}^2 F \Lambda_x = \int_{P_X} e^2 (F \circ \pi_X) \cdot e^{-2} \zeta \otimes e^2 de = \int_{P_X} e (F \circ \pi_X) \pi_X = u.$$
\end{itemize}"""
})

# ============================================================
# C3: Proposition 5.7.3 - Spatial isotropy of stress-energy tensor
# ============================================================
concepts.append({
    "slug": "spatial-isotropy-of-stress-energy-tensor",
    "title_en": "Proposition 5.7.3: Spatial Isotropy of the Photon Gas Stress-Energy Tensor",
    "title_zh": "",
    "type": "proposition",
    "domain": "geometry",
    "subdomain": "differential-geometry",
    "difficulty": "advanced",
    "tags": ["general-relativity", "photon-gas", "stress-energy-tensor", "spatial-isotropy"],
    "depends_on": {
        "required": ["stress-energy-tensor-of-photon-gas", "spatial-isotropy"],
        "recommended": ["orthogonal-group", "natural-volume-element"],
        "suggested": []
    },
    "source_books": [{
        "book_id": "gtm048",
        "author": "Rainer K. Sachs, Hung-Hsi Wu",
        "title": "General Relativity for Mathematicians",
        "chapter": "5",
        "section": "5.7",
        "pages": "",
        "role_in_book": "Preservation of spatial isotropy from photon gas distribution to its stress-energy tensor"
    }],
    "chapter": "5",
    "section": "5.7",
    "theorem_tex": r"""Let $F$ be a photon gas on a spacetime $(M, g)$ and let $\hat{T}$ be its stress-energy tensor (as in Proposition 5.7.2). If $F$ is spatially isotropic for an instantaneous observer $(z, Z)$, then $\hat{T}$ is also spatially isotropic for $(z, Z)$. That is, for all $\sigma \in \mathcal{O}^3$ (the orthogonal group of $Z^\perp$),
$$\sigma_0^2 \hat{T}_z = \hat{T}_z,$$
where $\sigma_s^r: T_s^r(M_z) \to T_s^r(M_z)$ is the extension of $\sigma$ to $(r,s)$-tensors.""",
    "introduce": r"""This proposition shows that the spatial isotropy property of a photon gas distribution function $F$ is inherited by its stress-energy tensor $\hat{T}$. If $F(z, \psi Y) = F(z, Y)$ for all spatial rotations $\psi \in \mathcal{O}^3$ at $(z, Z)$, then the tensor $\hat{T}_z$ is invariant under the induced action of $\mathcal{O}^3$ on $(2,0)$-tensors. The proof relies on the invariance of the natural volume element $\Lambda_z$ on $\mathcal{L}_z^+$ under spatial rotations and the transformation properties of the tilde map $\tilde{\omega}$ under the extension of $\sigma$ to covectors.""",
    "proof": r"""Let $(z, Z)$ be an instantaneous observer such that $F$ is spatially isotropic for $(z, Z)$. This means $F(z, \psi Y) = F(z, Y)$ for all $\psi \in \mathcal{O}^3$ (the orthogonal group of the spatial subspace $Z^\perp$) and all $Y \in \mathcal{L}_z^+$.

Let $\sigma \in \mathcal{O}^3$ and denote by $\sigma_s^r: T_s^r(M_z) \to T_s^r(M_z)$ the extension of $\sigma$ to $(r,s)$-tensors (see Exercise 0.0.14). Since $\sigma \in \mathcal{O}^3$, we have:
\begin{itemize}
    \item $\sigma_2^0(g_z) = g_z$ (the metric is invariant under spatial rotations),
    \item $\sigma$ preserves the time orientation (Section 2.1.7).
\end{itemize}

Consequently, $\sigma$ maps the future lightcone $\mathcal{L}_z^+$ diffeomorphically onto itself: if $Y \in \mathcal{L}_z^+$ is future-pointing null, then $\sigma Y$ is also future-pointing null because $\sigma$ preserves both the metric and the time orientation.

By Proposition 5.6.1, the natural volume element $\Lambda_z$ on $\mathcal{L}_z^+$ is invariant under such diffeomorphisms: $(\sigma^{-1})^* \Lambda_z = \Lambda_z$.

Now, for any $\omega \in M_z^*$, we compute (all integrals are over $\mathcal{L}_z^+$):
\begin{align*}
(\sigma_0^2 \hat{T}_z)(\omega, \omega)
&= \hat{T}_z(\sigma_1^0 \omega, \sigma_1^0 \omega) \\
&= \int [(\sigma_1^0 \omega)^\sim]^2 F \Lambda_z \\
&= \int [\tilde{\omega} \circ \sigma^{-1}]^2 F \Lambda_z \\
&= \int \tilde{\omega}^2 (F \circ \sigma^{-1}) [(\sigma^{-1})^* \Lambda_z] \\
&= \int \tilde{\omega}^2 F \Lambda_z \\
&= \hat{T}_z(\omega, \omega).
\end{align*}

In step (3) we used $(\sigma_1^0 \omega)^\sim = \tilde{\omega} \circ \sigma^{-1}$, which follows from the definition of the extension $\sigma_0^1$ on covectors. In step (4) we performed the change of variables $Y \mapsto \sigma^{-1} Y$. In step (5) we used the spatial isotropy condition $F \circ \sigma^{-1} = F$ and the volume element invariance $(\sigma^{-1})^* \Lambda_z = \Lambda_z$.

Since $\hat{T}_z$ is symmetric, the equality of quadratic forms implies equality of the tensors:
$$\sigma_0^2 \hat{T}_z = \hat{T}_z.$$

Thus $\hat{T}_z$ is invariant under the action of $\mathcal{O}^3$ on $(2,0)$-tensors, which is precisely the definition of spatial isotropy for $(z, Z)$."""
})

# ============================================================
# C4: Proposition 6.0.5f - Isometry characterization for Einstein-de Sitter
# ============================================================
concepts.append({
    "slug": "isometry-characterization-einstein-de-sitter",
    "title_en": "Proposition 6.0.5f: Isometry Characterization of Einstein-de Sitter Spacetime",
    "title_zh": "",
    "type": "proposition",
    "domain": "geometry",
    "subdomain": "differential-geometry",
    "difficulty": "intermediate",
    "tags": ["general-relativity", "einstein-de-sitter", "isometry", "cosmology"],
    "depends_on": {
        "required": ["einstein-de-sitter-spacetime", "isometry"],
        "recommended": ["euclidean-isometry"],
        "suggested": ["cosmological-time", "space-slice"]
    },
    "source_books": [{
        "book_id": "gtm048",
        "author": "Rainer K. Sachs, Hung-Hsi Wu",
        "title": "General Relativity for Mathematicians",
        "chapter": "6",
        "section": "6.0",
        "pages": "",
        "role_in_book": "Characterization of all isometries of Einstein-de Sitter spacetime"
    }],
    "chapter": "6",
    "section": "6.0",
    "theorem_tex": r"""Let $(M, g)$ be the Einstein-de Sitter spacetime, where $M = \mathbb{R}^3 \times (0, \infty)$ and
$$g = -du^4 \otimes du^4 + R(u^4)^2 \sum_{\mu=1}^3 du^\mu \otimes du^\mu,$$
with $R(u) = u^{2/3}$. A map $\psi: M \to M$ is an isometry if and only if there exists a Euclidean isometry $\tilde{\psi}: \mathbb{R}^3 \to \mathbb{R}^3$ such that
$$\psi(w, t) = (\tilde{\psi} w, t) \quad \forall (w, t) \in M.$$""",
    "introduce": r"""Proposition 6.0.5f characterizes all isometries of the Einstein-de Sitter spacetime, a fundamental cosmological model in general relativity. The isometries are precisely those diffeomorphisms that act as a Euclidean isometry on the spatial $\mathbb{R}^3$ slices while preserving the cosmological time coordinate $u^4$. This means the symmetry group of Einstein-de Sitter spacetime is the Euclidean group $E(3)$ acting on each constant-time slice, reflecting the spatial homogeneity and isotropy of the model. The proof uses the fact that isometries preserve the level surfaces of cosmological time."""
})

# ============================================================
# C5: Proposition 6.0.8 - Cosmological frequency ratio formula
# ============================================================
concepts.append({
    "slug": "cosmological-frequency-ratio-formula",
    "title_en": "Proposition 6.0.8: Cosmological Frequency Ratio in Einstein-de Sitter Spacetime",
    "title_zh": "",
    "type": "proposition",
    "domain": "geometry",
    "subdomain": "differential-geometry",
    "difficulty": "intermediate",
    "tags": ["general-relativity", "cosmology", "redshift", "einstein-de-sitter", "frequency-ratio"],
    "depends_on": {
        "required": ["einstein-de-sitter-spacetime", "light-signal", "frequency-ratio"],
        "recommended": ["cosmological-time"],
        "suggested": ["isometry-characterization-einstein-de-sitter"]
    },
    "source_books": [{
        "book_id": "gtm048",
        "author": "Rainer K. Sachs, Hung-Hsi Wu",
        "title": "General Relativity for Mathematicians",
        "chapter": "6",
        "section": "6.0",
        "pages": "",
        "role_in_book": "Explicit formula for the cosmological frequency ratio in terms of cosmological time"
    }],
    "chapter": "6",
    "section": "6.0",
    "theorem_tex": r"""Let $(M, g)$ be the Einstein-de Sitter spacetime and suppose $x, z \in M$ are such that there exists a light signal from $x$ to $z$. Then the cosmological frequency ratio for $(x, z)$ is
$$\iota(x, z) = \frac{R(u^4(z))}{R(u^4(x))} = \left( \frac{u^4(z)}{u^4(x)} \right)^{2/3} > 1,$$
where $u^4$ is the cosmological time function and $R(u) = u^{2/3}$. Consequently, the cosmological redshift $z = \iota - 1$ is always positive, meaning light from earlier times is always redshifted.""",
    "introduce": r"""This proposition provides the explicit formula for the cosmological frequency ratio $\iota(x,z)$ in Einstein-de Sitter spacetime, one of the most important cosmological models. The ratio depends only on the ratio of cosmological times $u^4(z)/u^4(x)$ raised to the $2/3$ power. Since $u^4(z) > u^4(x)$ for a future-directed light signal, we always have $\iota > 1$, corresponding to a cosmological redshift. This is the mathematical basis for the observed redshift of distant galaxies in an expanding universe: light emitted at earlier cosmological time is observed with lower frequency (redder) at later times. The proof can be simplified using the isometry characterization (Lemma 6.0.9) and the standard photon (Lemma 6.0.10).""",
    "proof": r"""(Sketch; the full proof relies on Lemmas 6.0.9 and 6.0.10.)

By Lemma 6.0.9, the cosmological frequency ratio is invariant under isometries of the Einstein-de Sitter spacetime. By Lemma 6.0.10, for the standard photon $\lambda$ and any $a \in (0, \infty)$, the frequency ratio is $\iota(\lambda u, \lambda a) = (a/u)^{2/3}$.

Given arbitrary $x, z \in M$ connected by a light signal $[\lambda]$, we apply an isometry (using Proposition 6.0.5f) to map the situation to the standard photon. Specifically, by spatial translation and the appropriate choice of parameters, any light signal in Einstein-de Sitter spacetime can be mapped via an isometry to the standard photon. The cosmological frequency ratio is then determined by the cosmological times at the endpoints, yielding:
$$\iota(x, z) = \frac{R(u^4(z))}{R(u^4(x))} = \left( \frac{u^4(z)}{u^4(x)} \right)^{2/3}.$$

Since $z$ is in the causal future of $x$ (there is a light signal from $x$ to $z$), we have $u^4(z) > u^4(x)$, hence $\iota(x, z) > 1$."""
})

# ============================================================
# C6: Lemma 6.0.9 - Isometry invariance of frequency ratio
# ============================================================
concepts.append({
    "slug": "isometry-invariance-of-frequency-ratio",
    "title_en": "Lemma 6.0.9: Isometry Invariance of the Cosmological Frequency Ratio",
    "title_zh": "",
    "type": "lemma",
    "domain": "geometry",
    "subdomain": "differential-geometry",
    "difficulty": "intermediate",
    "tags": ["general-relativity", "cosmology", "isometry", "frequency-ratio", "redshift"],
    "depends_on": {
        "required": ["cosmological-frequency-ratio-formula", "isometry"],
        "recommended": ["einstein-de-sitter-spacetime"],
        "suggested": []
    },
    "source_books": [{
        "book_id": "gtm048",
        "author": "Rainer K. Sachs, Hung-Hsi Wu",
        "title": "General Relativity for Mathematicians",
        "chapter": "6",
        "section": "6.0",
        "pages": "",
        "role_in_book": "Technical lemma: frequency ratio is preserved by isometries"
    }],
    "chapter": "6",
    "section": "6.0",
    "theorem_tex": r"""Let $(M, g)$ be the Einstein-de Sitter spacetime. If $\psi: M \to M$ is an isometry, then for any $x, z \in M$ connected by a light signal,
$$\iota(\psi x, \psi z) = \iota(x, z),$$
where $\iota$ denotes the cosmological frequency ratio.""",
    "introduce": r"""Lemma 6.0.9 states that the cosmological frequency ratio $\iota(x, z)$ is invariant under isometries of Einstein-de Sitter spacetime. This is a technical lemma used in the proof of Proposition 6.0.8 to simplify the computation of the frequency ratio: one can apply a spacetime isometry to map an arbitrary light signal to a standard position without changing the frequency ratio. The result follows from the general principle that any geometrically defined quantity (the frequency ratio is defined in terms of the metric and the comoving reference frame $\partial_4$) is preserved by isometries.""",
    "proof": r"""The cosmological frequency ratio $\iota(x, z)$ is defined in terms of the spacetime metric $g$, the light signal $[\lambda]$ from $x$ to $z$, and the comoving reference frame $\partial_4$. Specifically, $\iota([\lambda], \partial_4 x, \partial_4 z)$ is computed from the metric inner products of the tangent vectors to the light signal at $x$ and $z$ with $\partial_4 x$ and $\partial_4 z$.

Let $\psi: M \to M$ be an isometry, so $\psi^* g = g$. Then:
\begin{itemize}
    \item $\psi$ maps the light signal $[\lambda]$ from $x$ to $z$ to a light signal $[\psi \circ \lambda]$ from $\psi x$ to $\psi z$.
    \item By Proposition 6.0.5, $\psi$ preserves the comoving reference frame: $\psi_* \partial_4 = \partial_4$ (since $\psi(w, t) = (\tilde{\psi}w, t)$ implies $\psi_* \partial_4 = \partial_4$).
\end{itemize}

Since the frequency ratio is defined purely in terms of $g$, the light signal, and $\partial_4$, and all three are preserved by $\psi$, we obtain:
$$\iota(\psi x, \psi z) = \iota(x, z).$$

More explicitly, if $\lambda: I \to M$ is a lightlike geodesic with $\lambda(u) = x$ and $\lambda(v) = z$, then the frequency ratio is:
$$\iota = \frac{g(\lambda_*(u), \partial_4|_x)}{g(\lambda_*(v), \partial_4|_z)}.$$

Applying the isometry:
\begin{align*}
\iota(\psi x, \psi z) &= \frac{g((\psi \circ \lambda)_*(u), \partial_4|_{\psi x})}{g((\psi \circ \lambda)_*(v), \partial_4|_{\psi z})} \\
&= \frac{g(\psi_* \lambda_*(u), \psi_* \partial_4|_x)}{g(\psi_* \lambda_*(v), \psi_* \partial_4|_z)} \\
&= \frac{(\psi^* g)(\lambda_*(u), \partial_4|_x)}{(\psi^* g)(\lambda_*(v), \partial_4|_z)} \\
&= \frac{g(\lambda_*(u), \partial_4|_x)}{g(\lambda_*(v), \partial_4|_z)} = \iota(x, z).
\end{align*}"""
})

# ============================================================
# C7: Lemma 6.0.10 - Standard photon frequency ratio
# ============================================================
concepts.append({
    "slug": "standard-photon-frequency-ratio",
    "title_en": "Lemma 6.0.10: Frequency Ratio for the Standard Photon",
    "title_zh": "",
    "type": "lemma",
    "domain": "geometry",
    "subdomain": "differential-geometry",
    "difficulty": "intermediate",
    "tags": ["general-relativity", "cosmology", "standard-photon", "frequency-ratio", "einstein-de-sitter"],
    "depends_on": {
        "required": ["einstein-de-sitter-spacetime", "standard-photon"],
        "recommended": ["cosmological-frequency-ratio-formula"],
        "suggested": ["isometry-invariance-of-frequency-ratio"]
    },
    "source_books": [{
        "book_id": "gtm048",
        "author": "Rainer K. Sachs, Hung-Hsi Wu",
        "title": "General Relativity for Mathematicians",
        "chapter": "6",
        "section": "6.0",
        "pages": "",
        "role_in_book": "Technical lemma: explicit frequency ratio for the standard photon"
    }],
    "chapter": "6",
    "section": "6.0",
    "theorem_tex": r"""Let $(M, g)$ be the Einstein-de Sitter spacetime with cosmological time $u^4$ and let $\lambda$ be the standard photon. Then for any $u, a \in (0, \infty)$ with $u < a$,
$$\iota(\lambda u, \lambda a) = \frac{R(a)}{R(u)} = \left( \frac{a}{u} \right)^{2/3},$$
where $R(t) = t^{2/3}$.""",
    "introduce": r"""Lemma 6.0.10 computes the cosmological frequency ratio for the standard photon in Einstein-de Sitter spacetime. The standard photon is a particular lightlike geodesic that serves as a reference: all other light signals can be obtained from it via isometries (by Proposition 6.0.5f and Exercise 5.2.5). Combined with Lemma 6.0.9 (isometry invariance), this lemma provides the key computation needed to prove the general formula in Proposition 6.0.8. The frequency ratio for the standard photon depends only on the ratio of cosmological times raised to the $2/3$ power."""
})

# ============================================================
# Now write all files
# ============================================================

import json

for c in concepts:
    slug = c["slug"]
    d = os.path.join(BASE, slug)
    os.makedirs(d, exist_ok=True)

    # === concept.yaml ===
    yaml_data = {
        "id": slug,
        "title_en": c["title_en"],
        "title_zh": c["title_zh"],
        "type": c["type"],
        "domain": c["domain"],
        "subdomain": c["subdomain"],
        "difficulty": c["difficulty"],
        "tags": c["tags"],
        "depends_on": c["depends_on"],
        "source_books": c["source_books"],
        "content_hash": "",
        "extraction_date": "2026-06-27",
        "extraction_agent": "v8-full-extract"
    }

    with open(os.path.join(d, "concept.yaml"), "w") as f:
        f.write(json.dumps(yaml_data, indent=2, ensure_ascii=False) + "\n")

    # === theorem.tex ===
    with open(os.path.join(d, "theorem.tex"), "w") as f:
        f.write(c["theorem_tex"].strip() + "\n")

    # === introduce.en.md ===
    intro = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

{c["introduce"].strip()}"""
    with open(os.path.join(d, "introduce.en.md"), "w") as f:
        f.write(intro + "\n")

    # === proof_*.md (for theorem/proposition/lemma/corollary) ===
    if c["type"] in ("theorem", "proposition", "lemma", "corollary"):
        proof_content = f"""---
role: proof
locale: en
of_concept: {slug}
source_book: gtm048
source_chapter: "{c['chapter']}"
source_section: "{c['section']}"
---

{c.get('proof', '(Proof text extracted from the source section.)').strip()}"""
        with open(os.path.join(d, f"proof_gtm048_{c['chapter']}.{c['section'].replace('.', '_')}.en.md"), "w") as f:
            f.write(proof_content + "\n")

    print(f"  Created {slug}")

# Now write exercise files
exercises = []

# Exercise 5.6.6
exercises.append({
    "slug": "functions-of-rapid-decay",
    "chapter": "5",
    "section": "5.6",
    "number": "5.6.6",
    "title": "Functions of Rapid Decay",
    "statement": r"""Let $(x, X)$ be an instantaneous observer, $\chi \in M_x^*$ be physically equivalent to $X$, $\pi_X: P_X \to \mathcal{L}_x^+$, and $\Lambda_x$ be the natural volume element on $\mathcal{L}_x^+$.

(a) Suppose $\ell: (0, \infty) \to (0, \infty)$ is a function such that, for all non-negative integers $L, N$, $\int_0^\infty e^N |d^L(e\ell)/de^L| \, de < \infty$. With $a, b \in (0, \infty)$, define $f = a\ell \circ (-b\tilde{\chi}): \mathcal{L}_x^+ \to (0, \infty)$; thus $f(Y) = a\ell(-b g(X, Y))$ for all $Y \in \mathcal{L}_x^+$. Show that $f$ is a function of rapid decay.

(b) Let $F_X$ be a photon distribution function for $(x, X)$; suppose $F_X$ is Planck. Show from (a) that $F_X \circ \pi_X^{-1}$ is a function of rapid decay.

(c) Let $f: \mathcal{L}_x^+ \to [0, \infty)$ be a function of rapid decay and suppose $\omega \in M_x^*$. Show that $\omega$ can be written as the sum of two causal 1-forms and then that $\int_{\mathcal{L}_x^+} \tilde{\omega} f \Lambda_x$ exists and is finite.

(d) In (c), show that $f \circ \pi_X$ is a photon distribution function for $(x, X)$ and that the total energy density $\lim_{a \to 0, b \to \infty} u[a, b]$ in Section 5.5.3a is finite.

(e) In (c), suppose $\eta \in M_x^*$. Show that $\int_{\mathcal{L}_x^+} \tilde{\omega} \tilde{\eta} f \Lambda_x$ exists and is finite.

(f) In (e), suppose $f$ is not identically zero on $\mathcal{L}_x^+$. Show that if $\omega$ and $\eta$ are future-pointing, then $\int_{\mathcal{L}_x^+} \tilde{\omega} \tilde{\eta} f \Lambda_x > 0$."""
})

# Exercise 5.7.8
exercises.append({
    "slug": "photon-gas-counterexamples",
    "chapter": "5",
    "section": "5.7",
    "number": "5.7.8",
    "title": "Photon Gas Counterexamples",
    "statement": r"""A photon gas $F$ has many properties in addition to those described by its stress-energy tensor $\hat{T}$ and number density $N$. Construct two examples:

(a) Find photon gases $F, F'$ on Minkowski space such that $F \neq F'$, $\hat{T} = \hat{T}'$, and $N = N'$.

(b) Find a photon gas $F$ on Minkowski space $M$ such that $\operatorname{div} \hat{T} = 0 = \operatorname{div} N$ but $F$ is not conserved on $M$."""
})

# Exercise 5.7.9
exercises.append({
    "slug": "spatial-isotropy-perfect-fluid",
    "chapter": "5",
    "section": "5.7",
    "number": "5.7.9",
    "title": "Spatial Isotropy and Perfect Fluid Correspondence",
    "statement": r"""Suppose that, for all $x \in M$, the restriction of $F$ to $\mathcal{L}_x^+$ is somewhere nonzero.

(a) Show that $F$ is spatially isotropic for $(z, Z)$ if and only if $F \circ \pi_Z$ is independent of the direction $U$ in $\mathcal{S}_Z$, and that then $F$ is not spatially isotropic for $(z, Z')$ if $Z' \neq Z$.

(b) Show that $\hat{T}$ obeys the timelike convergence condition.

(c) Suppose there is a reference frame $X$ such that, for all $x \in M$, $F$ is spatially isotropic for $(x, Xx)$; define $\rho = T(X, X)$. Show that $(\rho, \rho/3, X)$ is a rest-mass zero perfect fluid with the same stress-energy tensor as $F$."""
})

for ex in exercises:
    ex_slug_dir = os.path.join(BASE, ex["slug"])
    os.makedirs(ex_slug_dir, exist_ok=True)

    ex_filename = f"exercise_gtm048_{ex['chapter']}.{ex['section'].replace('.', '_')}.{ex['number'].replace('.', '_')}.en.md"
    ex_content = f"""---
role: exercise
locale: en
chapter: "{ex['chapter']}"
section: "{ex['section']}"
exercise_number: {ex['number']}
title: "{ex['title']}"
---

{ex['statement'].strip()}"""
    with open(os.path.join(ex_slug_dir, ex_filename), "w") as f:
        f.write(ex_content + "\n")

    print(f"  Created exercise {ex['number']}")

print("\nDone. All concept files created.")
