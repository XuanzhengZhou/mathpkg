---
role: proof
locale: en
of_concept: wagners-theorem
source_book: gtm006
source_chapter: "XIV"
source_section: "7"
---

Assume $\mathcal{A}$ has odd order $n$ (otherwise Lemma 14.8 proves the result immediately). The proof shows $n$ must be a prime power, after which Lemma 14.8 completes the argument.

**Setup.** Write $\mathcal{A} = \mathcal{P}^{l_\infty}$ where $\mathcal{P}$ is the projective completion. Let $\mathcal{Q}$ be a minimal $2$-subplane with respect to $\Pi$, and let $\mathcal{B} = \mathcal{Q}^{l_\infty}$ (note that $\Pi$ fixes $l_\infty$, so $l_\infty$ lies in $\mathcal{Q}$). Let $\Gamma$ be a maximal $2$-subgroup of $\Pi$ whose fixed elements are the points and lines of $\mathcal{Q}$. Let $\Sigma$ be the subgroup of $\Pi$ leaving $\mathcal{Q}$ invariant.

**Step 1 (Lemma 14.12).** Regarding $\Sigma$ as a collineation group of $\mathcal{B}$:
(i) For every affine flag in $\mathcal{B}$, there is an involutory homology in $\Sigma$ fixing that flag.
(ii) If $A, B$ are special points of $\mathcal{B}$ with $l$ an affine line through $B$, and there is an involutory homology fixing $A, B, l$, then for any other affine line $m$ through $B$, there exists an involutory homology fixing $A, B, m$.

The proof uses Sylow $2$-subgroup arguments: since $\Gamma$ fixes $\mathcal{Q}$ pointwise and has maximal order among such subgroups, extending $\Gamma$ by an index-2 subgroup yields the required involutory homologies via properties of Frobenius groups (Results 14.1-14.2).

**Step 2 (Lemma 14.13).** A finite affine plane $\mathcal{B}$ with a collineation group $\Sigma$ satisfying properties (i) and (ii) of Lemma 14.12 is either a translation plane, the dual of a translation plane, or of type $\mathcal{H}$ (a specific exceptional type). The proof is a detailed case analysis based on the configuration of involutory homology centers.

**Step 3.** Apply induction on the exponent $g$ from Theorem 14.10 ($n = m^{2^g}$). For the minimal $2$-subplane $\mathcal{Q}$, either $g = 0$ (so $\mathcal{Q} = \mathcal{P}$) or $g > 0$.

If $\mathcal{Q} = \mathcal{P}$, the $2$-group $\Gamma$ acts trivially, so the involutory homologies from Lemma 14.12 exist in $\Pi$ itself. Lemma 14.13 then forces $\mathcal{B} = \mathcal{A}$ to be a translation plane (or dual/type $\mathcal{H}$), and further arguments using Result 14.5 and the Frobenius group structure (Result 14.4) force $n$ to be a prime power.

If $g > 0$, the induction hypothesis applied to $\mathcal{B}$ (which has order $m = n^{1/2^g} < n$) shows $\mathcal{B}$ is a translation plane. Properties of the larger group $\Pi$ then force $n$ to be a prime power.

In all cases, $n$ is a prime power, and Lemma 14.8 yields that $\mathcal{A}$ is a translation plane. $\square$
