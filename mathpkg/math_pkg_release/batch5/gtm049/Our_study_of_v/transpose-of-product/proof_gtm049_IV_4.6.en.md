---
role: proof
locale: en
of_concept: transpose-of-product
source_book: gtm049
source_chapter: "IV"
source_section: "4.6"
---
Let $$f: V \to V'$$ and $$g: V' \to V''$$ be linear mappings with transposes $$f^t: (V')^* \to V^*$$ and $$g^t: (V'')^* \to (V')^*$$. For any $$\varphi \in (V'')^*$$ and $$v \in V$$:

$$v((fg)^t \varphi) = (v(fg))\varphi = ((vf)g)\varphi$$
$$= (vf)(g^t \varphi) = v(f^t(g^t \varphi))$$
$$= v((f^t g^t) \varphi).$$

Since this holds for all $$v$$ and $$\varphi$$, we have $$(fg)^t = g^t f^t$$ (note the reversed order). In matrix language, if $$A, B$$ are the matrices of $$f, g$$ with respect to appropriate bases, then $$(AB)^t = B^t A^t$$.
