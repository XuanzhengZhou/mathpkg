---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.4"
proof_technique: kernel-chase
locale: en
content_hash: ""
written_against: ""
---
($\Rightarrow$) (i) $\operatorname{Ker} \bar{\varphi} = 0$: if $\varphi f = 0$, then $\varphi(f(x)) = 0$ for all $x$. Since $\varphi$ is mono, $f(x) = 0$, so $f = 0$. (ii) $\operatorname{Im} \bar{\varphi} \subset \operatorname{Ker} \bar{\psi}$: $\psi\varphi = 0$ implies $\bar{\psi}\bar{\varphi} = 0$. (iii) $\operatorname{Ker} \bar{\psi} \subset \operatorname{Im} \bar{\varphi}$: if $\psi g = 0$, then $\operatorname{Im} g \subset \operatorname{Ker} \psi = \operatorname{Im} \varphi$. Since $\varphi$ is mono, for each $d \in D$ there is a unique $a \in A$ with $g(d) = \varphi(a)$. Define $f(d) = a$; verify $f$ is a homomorphism and $\bar{\varphi}(f) = g$.

($\Leftarrow$) Given exactness of Hom for all $D$, take $D = \operatorname{Ker} \varphi$ to show $\varphi$ is mono, and $D = B/\operatorname{Im} \varphi$ to show $\operatorname{Im} \varphi = \operatorname{Ker} \psi$.
