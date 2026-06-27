---
role: proof
locale: en
of_concept: yoneda-corollary
source_book: gtm005
source_chapter: "III"
source_section: "2. The Yoneda Lemma"
---

Apply the Yoneda Lemma with $K = D(s, -)$. The bijection

$$
y \colon \operatorname{Nat}(D(r, -), D(s, -)) \xrightarrow{\cong} D(s, r)
$$

sends a natural transformation $\alpha \colon D(r, -) \to D(s, -)$ to $\alpha_r(1_r) \in D(s, r)$. Let $h = \alpha_r(1_r) \colon s \to r$. Then for any $f \colon r \to d$, naturality yields $\alpha_d(f) = D(s, f)(h) = f \circ h$. But $f \circ h = D(h, d)(f)$, so $\alpha = D(h, -)$. The Yoneda bijection guarantees that $h$ is uniquely determined by $\alpha$, completing the proof.
