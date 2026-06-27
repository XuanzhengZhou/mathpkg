---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.1"
proof_technique: diagram-chase
locale: en
content_hash: ""
written_against: ""
---
(i) $\Rightarrow$ (ii) Given $h : C \to B$ with $gh = 1_C$, for $b \in B$, note that $b - hg(b) \in \operatorname{Ker} g = \operatorname{Im} f$ since $g(b - hg(b)) = g(b) - ghg(b) = g(b) - g(b) = 0$. Define $k(b)$ as the unique $a \in A$ with $f(a) = b - hg(b)$; verify $k$ is a homomorphism and $kf = 1_A$.

(ii) $\Rightarrow$ (iii) Define $\varphi : B \to A \oplus C$ by $\varphi(b) = (k(b), g(b))$ and $\psi : A \oplus C \to B$ by $\psi(a,c) = f(a) + h(c)$. By the Short Five Lemma, $\varphi$ and $\psi$ are isomorphisms.

(iii) $\Rightarrow$ (i), (ii) The canonical injection and projection of the direct sum pull back to give the required maps.
