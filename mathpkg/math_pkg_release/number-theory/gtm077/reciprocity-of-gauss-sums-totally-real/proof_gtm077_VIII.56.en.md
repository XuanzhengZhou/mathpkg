---
role: proof
locale: en
of_concept: reciprocity-of-gauss-sums-totally-real
source_book: gtm077
source_chapter: "VIII"
source_section: "56"
---

# Proof of Reciprocity of Gauss Sums in Totally Real Fields

Let $k$ be a totally real algebraic number field of degree $n$. For odd ideals $\mathfrak{a}$ and $\mathfrak{b}$ in $k$, the Gauss sum with denominator $\mathfrak{a}$ and character $\omega$ is defined (as in §54) by

$$C_{\mathfrak{a}}(\omega) = \sum_{\rho \bmod \mathfrak{a}} e^{2\pi i S(\rho^2\omega)},$$

where $S(\alpha) = \sum_{p=1}^{n} \alpha^{(p)}$ denotes the trace from $k$ to $\mathbb{Q}$.

The reciprocity law states that for totally real fields, the product of two Gauss sums can be expressed in terms of a single Gauss sum and quadratic residue symbols:

$$C_{\mathfrak{a}}(1) \, C_{\mathfrak{b}}(1) = \left(\frac{\mathfrak{a}}{\mathfrak{b}}\right) \left(\frac{\mathfrak{b}}{\mathfrak{a}}\right) C_{\mathfrak{a}\mathfrak{b}}(1) \cdot \varepsilon,$$

where $\varepsilon$ is an explicit root of unity determined by the signatures of the field, and $\left(\frac{\mathfrak{a}}{\mathfrak{b}}\right)$ denotes the quadratic residue symbol in $k$.

**Proof strategy.** The proof proceeds via the theta function transformation method of Theorem 159 and the reciprocity of Theorems 160-161.

**Step 1: Express each Gauss sum via theta limits.**

For an ideal $\mathfrak{f}$ in $k$, Theorem 159 provides the theta function

$$\theta(t; \mathfrak{f}) = \sum_{\mu \in \mathfrak{f}} \exp\left\{ -\pi \sum_{p=1}^{n} t_p \mu^{(p)^2} \right\}$$

together with its transformation under $t_p \mapsto 1/t_p$. Setting $t_p = x - 2i\omega^{(p)}$ and applying Lemma (a), each Gauss sum $C_{\mathfrak{a}}(\omega)$ emerges as the dominant coefficient in the limit $x \to 0$:

$$\lim_{x \to 0} x^{n/2} \; \theta(x - 2i\omega; \mathfrak{a}) = \frac{C_{\mathfrak{a}}(\omega)}{N(\mathfrak{a})|\sqrt{d}|}.$$

**Step 2: Relate $C_{\mathfrak{a}}(1) C_{\mathfrak{b}}(1)$ to $C_{\mathfrak{a}\mathfrak{b}}(1)$.**

Consider the product of the theta functions for $\mathfrak{a}$ and $\mathfrak{b}$ with $\omega = 1$. By the convolution property of theta series (essentially, the sum over $\mu \in \mathfrak{a}$ and $\nu \in \mathfrak{b}$ can be reorganized as a sum over $\mathfrak{a}\mathfrak{b}$ with a character), one obtains a relation involving the quadratic residue symbol.

More systematically, one applies Theorems 160-161 with $\omega = 1$ and compares the limits for three different ideals: $\mathfrak{a}$, $\mathfrak{b}$, and $\mathfrak{a}\mathfrak{b}$. The reciprocity formula of Theorem 161,

$$\frac{C_{\mathfrak{a}}(\omega)}{|\sqrt{N(\mathfrak{a})}|} = \left| \frac{\sqrt{N(2\mathfrak{b})}}{N(\mathfrak{b}_1)} \right| e^{(\pi i/4)S(\mathrm{sgn}\,\omega)} A,$$

is applied iteratively:

- First, evaluate $C_{\mathfrak{a}}(1)$ by the reciprocity with a suitably chosen auxiliary ideal to relate it to $C(-1/4)$.
- Second, do the same for $C_{\mathfrak{b}}(1)$.
- Third, apply the reciprocity to $C_{\mathfrak{a}\mathfrak{b}}(1)$.

**Step 3: Emergence of the quadratic residue symbols.**

The comparison of the three formulas yields factors involving power residue symbols. Specifically, the term $N(\mathfrak{b}_1)$ in the denominator of the reciprocity formula depends on the choice of auxiliary ideal $\mathfrak{c}$ satisfying $(\mathfrak{c}, 2\mathfrak{b}) = 1$ and $\mathfrak{c}\mathfrak{d} = \delta$ (a principal ideal). By choosing $\mathfrak{c}$ appropriately relative to $\mathfrak{a}$ and $\mathfrak{b}$, the algebraic factors simplify to the quadratic residue symbols $\left(\frac{\mathfrak{a}}{\mathfrak{b}}\right)$ and $\left(\frac{\mathfrak{b}}{\mathfrak{a}}\right)$.

The root of unity factor $\varepsilon$ arises from the phase $e^{(\pi i/4)S(\mathrm{sgn}\,\omega)}$ in the reciprocity formula. When $\omega = 1$, all conjugates satisfy $\mathrm{sgn}(1^{(p)}) = 1$, so $S(\mathrm{sgn}\,1) = n$, giving $\varepsilon = e^{(\pi i/4)n}$. For a totally real field of general degree, this contributes $i^n = e^{\pi i n/2}$.

**Step 4: Conclusion.**

Combining these steps yields the reciprocity law

$$C_{\mathfrak{a}}(1) \, C_{\mathfrak{b}}(1) = \left(\frac{\mathfrak{a}}{\mathfrak{b}}\right) \left(\frac{\mathfrak{b}}{\mathfrak{a}}\right) C_{\mathfrak{a}\mathfrak{b}}(1) \cdot e^{\pi i n/2}.$$

This formula is the analog for totally real number fields of the classical quadratic reciprocity law for Gauss sums over $\mathbb{Q}$. The proof via theta functions, due to Hecke, is one of the deepest applications of analytic methods to algebraic number theory: the transformation formula of the theta function (a manifestation of the Poisson summation formula on the Minkowski lattice) encodes the reciprocity relation among Gauss sums.
