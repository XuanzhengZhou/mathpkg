---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.3"
proof_technique: baer-criterion
locale: en
content_hash: ""
written_against: ""
---
($\Rightarrow$) If $D$ is injective and $d \in D$, define $f: \langle n \rangle \to D$ by $f(n) = d$. By Lemma 3.8, extend to $h: \mathbb{Z} \to D$. Let $x = h(1)$; then $nx = nh(1) = h(n) = f(n) = d$, so $D$ is divisible.

($\Leftarrow$) If $D$ is divisible and $f: \langle n \rangle \to D$, there exists $x \in D$ with $nx = f(n)$. Define $h: \mathbb{Z} \to D$ by $1 \mapsto x$, which extends $f$. By Lemma 3.8, $D$ is injective.
