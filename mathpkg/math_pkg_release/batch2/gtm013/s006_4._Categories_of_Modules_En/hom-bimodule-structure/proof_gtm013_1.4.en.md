---
role: proof
locale: en
of_concept: hom-bimodule-structure
source_book: gtm013
source_chapter: "1"
source_section: "4"
---

(1) Suppose $_R M_S$ and $_R N_T$ are bimodules. For $f \in \operatorname{Hom}_R(M,N)$, $s \in S$, $t \in T$, define $sf$ and $ft$ by $(sf)(x) = f(xs)$ and $(ft)(x) = f(x)t$ for $x \in M$.

We check $sf$ is an $R$-homomorphism: for $r \in R$, $x \in M$,
$(sf)(rx) = f((rx)s) = f(r(xs)) = rf(xs) = r((sf)(x))$.

For $ft$: $(ft)(rx) = f(rx)t = (rf(x))t = r(f(x)t) = r((ft)(x))$.

The left $S$-module axioms: for $s, s' \in S$,
$((s+s')f)(x) = f(x(s+s')) = f(xs + xs') = f(xs) + f(xs') = (sf)(x) + (s'f)(x) = (sf + s'f)(x)$.
$(s(s'f))(x) = (s'f)(xs) = f((xs)s') = f(x(ss')) = ((ss')f)(x)$.

The right $T$-module axioms are verified similarly. That the left $S$-action and right $T$-action commute follows from the associativity in the bimodules: $((sf)t)(x) = (sf)(x)t = f(xs)t = (s(ft))(x)$.

(2) The verification for $_S M_R$, $_T N_R$ is dual, using left action on $N$ and right action on $M$.
