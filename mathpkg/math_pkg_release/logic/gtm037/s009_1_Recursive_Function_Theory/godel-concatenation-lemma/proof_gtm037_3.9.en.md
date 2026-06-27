---
role: proof
locale: en
of_concept: godel-concatenation-lemma
source_book: gtm037
source_chapter: "3"
source_section: "9"
---

Recall the definition of $hk$ from 1.11. By Definition 3.28, $gh = \prod_{i < \operatorname{Dmn}(h)} p_i^{h_i + 1}$ and $gk = \prod_{i < \operatorname{Dmn}(k)} p_i^{k_i + 1}$. By Definition 3.30, $\operatorname{Cat}(x, y) = x \cdot \prod_{i \leq \operatorname{lh}(y)} p_{\operatorname{lh}(x) + i + 1}^{(y)_i}$. Then

$$g(hk) = \prod_{i < \operatorname{Dmn}(h) + \operatorname{Dmn}(k)} p_i^{(hk)_i + 1} = \left(\prod_{i < \operatorname{Dmn}(h)} p_i^{h_i + 1}\right) \cdot \left(\prod_{i < \operatorname{Dmn}(k)} p_{\operatorname{Dmn}(h) + i}^{k_i + 1}\right) = gh \cdot \prod_{i < \operatorname{Dmn}(k)} p_{\operatorname{Dmn}(h) + i}^{k_i + 1} = \operatorname{Cat}(gh, gk).$$
