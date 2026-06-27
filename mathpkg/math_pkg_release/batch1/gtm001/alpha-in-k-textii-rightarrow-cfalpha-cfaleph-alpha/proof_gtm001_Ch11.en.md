---
role: proof
locale: en
of_concept: alpha-in-k-textii-rightarrow-cfalpha-cfaleph-alpha
source_book: gtm001
source_chapter: "11"
source_section: ""
---

If $\alpha \in K_{\text{II}}$, then $\aleph_\alpha$ is cofinal with $\alpha$ by Proposition 11.6. Since $\alpha$ is cofinal with $cf(\alpha)$ it follows from Proposition 11.5 that $\aleph_\alpha$ is cofinal with $cf(\alpha)$. Thus

(1) $cf(\aleph_\alpha) \leq cf(\alpha)$.

But $\aleph_\alpha$ is also cofinal with $cf(\aleph_\alpha)$ and so by Proposition 11.9

($\exists \eta \leq cf(\aleph_\alpha))[cof(cf(\alpha), \eta)]$.

But

(By contradiction). Suppose that $\aleph_{\alpha+1}$ is singular. That is, suppose that $\aleph_{\beta} = \text{cf}(\aleph_{\alpha+1}) < \aleph_{\alpha+1}$. Then $(\exists h)[h: \aleph_{\beta} \rightarrow \aleph_{\alpha+1} = \cup(h' \aleph_{\beta})]$. Furthermore $(\forall \delta < \aleph_{\beta})[h' \delta < \aleph_{\alpha+1}]$ and so $\overline{h' \delta} \leq \aleph_{\alpha}$. Then from Proposition 10.48

$$\aleph_{\alpha+1} = \overline{\cup(h' \aleph_{\beta})} \leq \aleph_{\alpha} \times \aleph_{\beta} = \aleph_{\alpha}.$$

From this contradiction we conclude that $\text{cf}(\aleph_{\alpha+1}) = \aleph_{\alpha+1}$. $\square$

Remark. Let us now summarize what we know about regular and singular cardinals. We know that $\aleph_{\alpha}$ is regular if $\alpha \in K_I$. If $\alpha \in K_{II}$ we know that $\aleph_{\alpha}$ is cofinal with $\alpha$ and so $\text{cf}(\aleph_{\alpha}) \leq \alpha$. We also know that $\alpha \leq \aleph_{\alpha}$. If $\alpha < \aleph_{\alpha}$, then $\aleph_{\alpha}$ is singular. But if $\alpha = \aleph_{\alpha}$ we do not know whether $\aleph_{\alpha}$ is regular or singular. Do there exist ordinals $\alpha$ for which $\alpha = \aleph_{\alpha}$? Yes. To prove this we first prove the following result.
