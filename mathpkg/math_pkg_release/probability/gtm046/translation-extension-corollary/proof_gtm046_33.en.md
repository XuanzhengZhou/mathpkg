---
role: proof
locale: en
of_concept: translation-extension-corollary
source_book: gtm046
source_chapter: "X"
source_section: "33"
---

A translation \(T\) on the space of indicator functions \(I_{\mathcal{A}} = \{I_A : A \in \mathcal{A}\}\) is a map satisfying \(T I_\Omega = 1\), \(T I_\emptyset = 0\), and for disjoint \(A, B\), \(T I_{A \cup B} = T I_A + T I_B\). By the defining properties of a translation in the ergodic context (as derived from a measure-preserving point transformation), \(T\) is a positive linear operator on the linear span of indicator functions (the simple functions).

**Extension to simple functions.** For a simple function \(f = \sum_{k=1}^{n} x_k I_{A_k}\) with disjoint \(A_k\), define

$$
Tf = \sum_{k=1}^{n} x_k T I_{A_k}.
$$

This definition is consistent (independent of the representation of \(f\)) because of the additivity and homogeneity properties of \(T\) on indicators. Moreover, \(T\) preserves linear combinations: \(T(c f + c' g) = c Tf + c' Tg\) for simple \(f, g\).

**Extension to all measurable functions.** Let \(\mathfrak{M}\) denote the space of all measurable functions. For any nonnegative measurable function \(\xi \geq 0\), there exists a sequence of simple functions \(0 \leq f_n \uparrow \xi\). Define

$$
T\xi = \lim_{n \to \infty} T f_n,
$$

where the limit exists (possibly infinite) because \(T\) is positive and \(f_n \uparrow\), so \(T f_n \uparrow\). For a general measurable \(\xi = \xi^+ - \xi^-\), define \(T\xi = T\xi^+ - T\xi^-\) (whenever the difference makes sense, e.g., for integrable functions). This extension is well-defined and unique.

**Properties of the extension.** The extended translation \(T\) on \(\mathfrak{M}\) satisfies:
- Linearity: \(T(a\xi + b\eta) = a T\xi + b T\eta\) a.s.
- Continuity: If \(\xi_n \to \xi\) in measure (or a.s.), then \(T\xi_n \to T\xi\) in the same sense.
- \(T1 = 1\) (preservation of the constant function 1).
- Multiplicative property on indicators: \(T I_{AB} = T I_A \cdot T I_B\) (for measure-preserving point transformations, this follows from \(T I_A = I_{T^{-1}A}\)).
- The translate of any measurable function \(\xi\) is the limit of the translates of any approximating sequence of simple functions.

The uniqueness follows because any two extensions must agree on simple functions (by linearity and additivity of the translation on indicators) and hence on all measurable functions (by monotone approximation).
