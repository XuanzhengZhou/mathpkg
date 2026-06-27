---
role: proof
locale: en
of_concept: ideal-distributivity
source_book: gtm028
source_chapter: "V"
source_section: "7"
---

By Theorem 11, every fractionary ideal $\mathfrak{a}$ in a Dedekind domain has a unique factorization $\mathfrak{a} = \prod_{\mathfrak{p}} \mathfrak{p}^{n_{\mathfrak{p}}(\mathfrak{a})}$ with integer exponents. Under this correspondence:
- $\mathfrak{a} + \mathfrak{b}$ corresponds to $\min(n_{\mathfrak{p}}(\mathfrak{a}), n_{\mathfrak{p}}(\mathfrak{b}))$,
- $\mathfrak{a} \cap \mathfrak{b}$ corresponds to $\max(n_{\mathfrak{p}}(\mathfrak{a}), n_{\mathfrak{p}}(\mathfrak{b}))$.

Thus the distributivity law $\mathfrak{a} + (\mathfrak{b} \cap \mathfrak{b}') = (\mathfrak{a} + \mathfrak{b}) \cap (\mathfrak{a} + \mathfrak{b}')$ translates to the identity
$$\max\{n_{\mathfrak{p}}(\mathfrak{a}), \min(n_{\mathfrak{p}}(\mathfrak{b}), n_{\mathfrak{p}}(\mathfrak{b}'))\} = \min\{\max(n_{\mathfrak{p}}(\mathfrak{a}), n_{\mathfrak{p}}(\mathfrak{b})), \max(n_{\mathfrak{p}}(\mathfrak{a}), n_{\mathfrak{p}}(\mathfrak{b}'))\}$$
for every prime $\mathfrak{p}$. Similarly, the dual distributivity law $\mathfrak{a} \cap (\mathfrak{b} + \mathfrak{b}') = (\mathfrak{a} \cap \mathfrak{b}) + (\mathfrak{a} \cap \mathfrak{b}')$ translates to
$$\min\{n_{\mathfrak{p}}(\mathfrak{a}), \max(n_{\mathfrak{p}}(\mathfrak{b}), n_{\mathfrak{p}}(\mathfrak{b}'))\} = \max\{\min(n_{\mathfrak{p}}(\mathfrak{a}), n_{\mathfrak{p}}(\mathfrak{b})), \min(n_{\mathfrak{p}}(\mathfrak{a}), n_{\mathfrak{p}}(\mathfrak{b}'))\}.$$

Both identities hold because in the set of ordinary integers, the operations $\min$ and $\max$ are distributive with respect to each other. This is easily verified by checking the six possible orderings of the three integers involved.
