---
role: proof
locale: en
of_concept: "direct-limits-exist-in-algebraic-categories"
source_book: gtm022
source_chapter: "VII"
source_section: "6"
---
Proof. Let $\{M_i, f_j^i\}$ be a direct family in $\operatorname{Mod}(\mathcal{T})$. Construct a limit as a subultraproduct: put $F_i = \{j \in I \mid j \geqslant i\}$ and let $\mathcal{F}$ be any filter containing all $F_i$. Put $S = \{f: I \to \bigcup M_i \mid f(i) \in M_i \text{ and there exists } i_0 \text{ with } f_j^{i}(f(i)) = f(j) \text{ for all } j \geqslant i \geqslant i_0\}$. Then $S/\mathcal{F}$ is a model of $\mathcal{T}$ and is a direct limit. If a direct limit exists, it must be isomorphic to $S/\mathcal{F}$. $\square$
