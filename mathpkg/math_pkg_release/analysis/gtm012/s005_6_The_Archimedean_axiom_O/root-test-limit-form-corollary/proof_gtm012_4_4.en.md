---
role: proof
locale: en
of_concept: root-test-limit-form-corollary
source_book: gtm012
source_chapter: "4"
source_section: "4. Series"
---

# Proof of Root test — limit form (Corollary 4.7)

**Corollary 4.7.** If $\lim_{n \to \infty} |z_n|^{1/n}$ exists, then the series $\sum z_n$

- converges (absolutely) if the limit is $< 1$,
- diverges if the limit is $> 1$.

**Proof.** If $\lim |z_n|^{1/n} = L$ exists, then in particular $(|z_n|^{1/n})$ is a bounded sequence, so both $\limsup |z_n|^{1/n}$ and $\liminf |z_n|^{1/n}$ exist. When the limit exists, we have

$$\limsup_{n \to \infty} |z_n|^{1/n} = \liminf_{n \to \infty} |z_n|^{1/n} = \lim_{n \to \infty} |z_n|^{1/n} = L.$$

Now apply Proposition 4.5 (root test):

- If $L < 1$, then $\limsup |z_n|^{1/n} = L < 1$, so by Proposition 4.5(a) the series converges absolutely.
- If $L > 1$, then $\limsup |z_n|^{1/n} = L > 1$, so by Proposition 4.5(b) the series diverges. $\square$

**Remark.** The test is inconclusive when $L = 1$. For example, both $\sum 1/n$ and $\sum 1/n^2$ have $\lim |z_n|^{1/n} = 1$ (see Exercise 4 of §3), yet the former diverges while the latter converges.
