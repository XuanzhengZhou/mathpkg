---
role: proof
locale: en
of_concept: extension-to-product-space
source_book: gtm015
source_chapter: "3"
source_section: "34"
---

# Proof of Extension of continuous linear maps to product spaces

Suppose $E$ is a locally convex TVS over $\mathbb{K}$, $I$ is a nonempty set of indices, and $\mathbb{K}^I$ is the product TVS $\prod_{\iota \in I} E_{\iota}$, where $E_{\iota} = \mathbb{K}$ for all $\iota \in I$. If $M$ is a linear subspace of $E$ and $u: M \rightarrow \mathbb{K}^I$ is a continuous linear mapping, then $u$ may be extended to a continuous linear mapping $\bar{u}: E \rightarrow \mathbb{K}^I$.

For each $\iota \in I$, let $\pi_{\iota}: \mathbb{K}^I \rightarrow \mathbb{K}$ be the $\iota$-th coordinate projection, and set $f_{\iota} = \pi_{\iota} \circ u$. Thus, $u = (f_{\iota})_{\iota \in I}$, that is,

$$u(y) = (f_{\iota}(y))_{\iota \in I} \quad (y \in M).$$

Since $\pi_{\iota}$ is a continuous linear form on $\mathbb{K}^I$, $f_{\iota}$ is a continuous linear form on $M$. Citing (34.8), there exists a continuous linear form $\bar{f}_{\iota}$ on $E$ extending $f_{\iota}$. Define $\bar{u}(x) = (\bar{f}_{\iota}(x))_{\iota \in I}$ for $x \in E$. Then $\bar{u}$ is linear, continuous (since each coordinate is continuous), and extends $u$.
