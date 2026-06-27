---
role: proof
locale: en
of_concept: delbar-product-rule
source_book: gtm035
source_chapter: "Chapter 5"
source_section: "5.5"
---
# Proof of the $\bar{\partial}$ Product Rule for Differential Forms

Let $\omega^k \in \wedge^k(\Omega)$ and $\omega^l \in \wedge^l(\Omega)$. By Definition 5.4, write these forms in terms of the standard basis:

$$\omega^k = \sum_{I,J} a_{IJ} \, dz_I \wedge d\bar{z}_J, \qquad
\omega^l = \sum_{K,L} b_{KL} \, dz_K \wedge d\bar{z}_L,$$

where $I, K$ are ordered multi-indices for the holomorphic basis and $J, L$ for the antiholomorphic basis. The sums run over all indices with $|I| + |J| = k$ and $|K| + |L| = l$ respectively.

---

**Step 1: Wedge product.** By bilinearity of $\wedge$,

$$\omega^k \wedge \omega^l = \sum_{\substack{I,J \\ K,L}} a_{IJ} b_{KL} \; (dz_I \wedge d\bar{z}_J) \wedge (dz_K \wedge d\bar{z}_L).$$

---

**Step 2: Apply $\bar{\partial}$.** Using Definition 5.4, $\bar{\partial}$ acts on each term via the Leibniz-type rule $\bar{\partial}(u \, \alpha) = \bar{\partial}u \wedge \alpha$ (since $\alpha = dz_I \wedge d\bar{z}_J \wedge dz_K \wedge d\bar{z}_L$ has constant coefficients):

$$\bar{\partial}(\omega^k \wedge \omega^l) = \sum_{I,J,K,L} \bar{\partial}(a_{IJ} b_{KL}) \wedge dz_I \wedge d\bar{z}_J \wedge dz_K \wedge d\bar{z}_L.$$

---

**Step 3: Leibniz rule for functions.** For the $C^\infty$ coefficient functions, the ordinary product rule for $\bar{\partial}$ gives

$$\bar{\partial}(a_{IJ} b_{KL}) = (\bar{\partial} a_{IJ}) \cdot b_{KL} + a_{IJ} \cdot (\bar{\partial} b_{KL}).$$

Thus

$$\bar{\partial}(\omega^k \wedge \omega^l) = \underbrace{\sum_{I,J,K,L} (\bar{\partial}a_{IJ}) b_{KL} \wedge dz_I \wedge d\bar{z}_J \wedge dz_K \wedge d\bar{z}_L}_{(A)}
+ \underbrace{\sum_{I,J,K,L} a_{IJ} (\bar{\partial}b_{KL}) \wedge dz_I \wedge d\bar{z}_J \wedge dz_K \wedge d\bar{z}_L}_{(B)}.$$

---

**Step 4: Identify the first term.** Term (A) is

$$(A) = \left( \sum_{I,J} \bar{\partial}a_{IJ} \wedge dz_I \wedge d\bar{z}_J \right) \wedge \left( \sum_{K,L} b_{KL} \, dz_K \wedge d\bar{z}_L \right) = (\bar{\partial}\omega^k) \wedge \omega^l,$$

since all forms in the second factor have even total degree with respect to the coefficients already in place.

---

**Step 5: Identify the second term.** In term (B), we must move the 1-form $\bar{\partial}b_{KL}$ past $dz_I \wedge d\bar{z}_J$. Note that $dz_I \wedge d\bar{z}_J$ has total degree $k = |I| + |J|$. Since $\bar{\partial}b_{KL}$ is a 1-form (of type $(0,1)$), moving it past a $k$-form introduces a sign of $(-1)^{k \cdot 1} = (-1)^k$:

$$a_{IJ} (\bar{\partial}b_{KL}) \wedge dz_I \wedge d\bar{z}_J \wedge dz_K \wedge d\bar{z}_L
= (-1)^k \, a_{IJ} \, dz_I \wedge d\bar{z}_J \wedge (\bar{\partial}b_{KL}) \wedge dz_K \wedge d\bar{z}_L.$$

But note: $\bar{\partial}b_{KL}$ is not simply a 1-form; it is $\bar{\partial}b_{KL} = \sum_m \frac{\partial b_{KL}}{\partial \bar{z}_m} d\bar{z}_m$, which is indeed a $(0,1)$-form, i.e., a 1-form. Moving a 1-form past a $k$-form yields sign $(-1)^k$ by Lemma 4.5. Therefore

$$(B) = (-1)^k \left( \sum_{I,J} a_{IJ} \, dz_I \wedge d\bar{z}_J \right) \wedge \left( \sum_{K,L} \bar{\partial}b_{KL} \wedge dz_K \wedge d\bar{z}_L \right) = (-1)^k \, \omega^k \wedge (\bar{\partial}\omega^l).$$

---

**Step 6: Conclusion.** Combining (A) and (B) yields the product rule:

$$\bar{\partial}(\omega^k \wedge \omega^l) = \bar{\partial}\omega^k \wedge \omega^l + (-1)^k \, \omega^k \wedge \bar{\partial}\omega^l.$$
