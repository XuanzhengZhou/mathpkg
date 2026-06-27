---
role: proof
locale: en
of_concept: weak-compactness-equicontinuous-closure
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

By Proposition 4.3, the closure \(\overline{H}\) of \(H\) in \(F^E = \mathbb{K}^E\) (where \(\mathbb{K}\) is the scalar field) is equicontinuous and contained in \(\mathcal{L}(E, \mathbb{K}) = E'\). 

Since \(H\) is equicontinuous, there exists a \(0\)-neighborhood \(U\) in \(E\) such that \(|u(x)| \leq 1\) for all \(u \in H\) and \(x \in U\). For any \(x_0 \in E\), there exists \(\lambda > 0\) with \(\lambda x_0 \in U\), so \(|u(x_0)| \leq \lambda^{-1}\) for all \(u \in H\). Thus for each \(x \in E\), the set \(\{u(x) : u \in H\}\) is bounded in \(\mathbb{K}\), so its closure is compact. By Tychonoff's theorem, the closure of \(H\) in the product space \(\mathbb{K}^E\) is compact. But this closure equals \(\overline{H}\) (the pointwise closure), which is contained in \(E'\) by the first part. Hence \(\overline{H}\) is compact in \(E'\) with the weak topology \(\sigma(E', E)\).
