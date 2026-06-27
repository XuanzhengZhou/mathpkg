```yaml
---
role: proof
source_book: gtm-0073
chapter: I
section: "I.5"
proof_technique: equivalence-chain
locale: en
content_hash: ""
written_against: ""
---
The proof proceeds by showing (i) $\Rightarrow$ (ii) $\Rightarrow$ (iii) $\Rightarrow$ (iv) $\Rightarrow$ (i).

(i) $\Rightarrow$ (ii): For $a \in G$, the left coset $aN$ is the equivalence class of $a$ under left congruence; the right coset $Na$ is the class under right congruence. Since the relations coincide, the cosets are equal.

(ii) $\Rightarrow$ (iii): For any $n \in N$ and $a \in G$, $an \in aN = Na$, so $an = n'a$ for some $n' \in N$. Hence $ana^{-1} = n' \in N$, proving $aNa^{-1} \subseteq N$.

(iii) $\Rightarrow$ (iv): Apply (iii) to $a^{-1}$ to get $a^{-1}Na \subseteq N$, whence $N = a(a^{-1}Na)a^{-1} \subseteq aNa^{-1}$. Together with (iii) this yields $aNa^{-1} = N$.

(iv) $\Rightarrow$ (i): $a \equiv_r b \pmod{N} \iff ab^{-1} \in N$. Also $a \equiv_l b \pmod{N} \iff a^{-1}b \in N \iff b^{-1}a \in N \iff a^{-1}(ab^{-1})a \in N$. By (iv), $ab^{-1} \in N$ if and only if $a^{-1}(ab^{-1})a \in N$, so the two congruence relations coincide.
