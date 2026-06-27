---
role: proof
locale: en
of_concept: boolean-valued-extensionality
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

Let $u, v \in V_{\alpha}^{(B)}$. We need to show:
$$[\![(\forall x)[x \in u \leftrightarrow x \in v]\!]_{\alpha} \leq [\![u = v]\!]_{\alpha}.$$

By definition of the Boolean-valued universal quantifier:
$$[\![(\forall x)[x \in u \leftrightarrow x \in v]\!]_{\alpha} = \prod_{x \in V_{\alpha}^{(B)}} [\![x \in u \leftrightarrow x \in v]\!]_{\alpha}.$$

Now for any $x \in V_{\alpha}^{(B)}$:
$$[\![x \in u \leftrightarrow x \in v]\!]_{\alpha} = ([\![x \in u]\!]_{\alpha} \Rightarrow [\![x \in v]\!]_{\alpha}) \cdot ([\![x \in v]\!]_{\alpha} \Rightarrow [\![x \in u]\!]_{\alpha}).$$

In particular, for $x \in \mathcal{D}(u)$, we have $[\![x \in u]\!] \geq u(x)$ (by definition of membership and $[\![x = x]\!] = 1$). Thus the product over all $x \in V_{\alpha}^{(B)}$ is bounded above by:
$$\prod_{x \in \mathcal{D}(u)} (u(x) \Rightarrow [\![x \in v]\!]) \cdot \prod_{y \in \mathcal{D}(v)} (v(y) \Rightarrow [\![y \in u]\!]) = [\![u = v]\!].$$

Therefore $[\![(\forall x)[x \in u \leftrightarrow x \in v] \rightarrow u = v]\!]_{\alpha} = 1$.
