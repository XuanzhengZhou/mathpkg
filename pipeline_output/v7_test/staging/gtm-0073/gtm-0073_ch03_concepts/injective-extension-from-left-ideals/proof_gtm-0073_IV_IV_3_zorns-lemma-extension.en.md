---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.3"
proof_technique: zorns-lemma-extension
locale: en
content_hash: ""
written_against: ""
---
If $J$ is injective, the extension property holds by definition. Conversely, suppose $J$ has the extension property for left ideals. Given a diagram with $g: A \to B$ mono and $f: A \to J$, let $\mathcal{S}$ be all homomorphisms $h: C \to J$ where $\operatorname{Im} g \subset C \subset B$, partially ordered by extension. Zorn's Lemma gives a maximal element $h: H \to J$. If $H \neq B$, pick $b \in B - H$. Then $L = \{r \in R \mid rb \in H\}$ is a left ideal. The map $L \to J$, $r \mapsto h(rb)$, extends to $k: R \to J$ by hypothesis. With $c = k(1_R)$, define $\bar{h}: H + Rb \to J$ by $a + rb \mapsto h(a) + rc$, which extends $h$ properly, contradicting maximality. Hence $H = B$.
