---
role: proof
locale: en
of_concept: adjoint-equivalence
source_book: gtm005
source_chapter: "IV"
source_section: "4"
---

We prove the three directions of the equivalence.

(i) $\Rightarrow$ (iii): If $S$ is part of an adjoint equivalence $\langle T, S; \eta, \varepsilon \rangle: C \to A$ with $\eta: I_C \cong ST$ and $\varepsilon: TS \cong I_A$ natural isomorphisms, then $S$ is essentially surjective because each $c \in C$ is isomorphic to $S(Tc)$ via $\eta_c$. To show $S$ is faithful, suppose $Sf = Sf'$. Then $TSf = TSf'$, and by naturality of $\varepsilon$, $f \circ \varepsilon_a = \varepsilon_{a'} \circ TSf = \varepsilon_{a'} \circ TSf' = f' \circ \varepsilon_a$. Since $\varepsilon_a$ is an isomorphism, $f = f'$. The proof that $S$ is full uses that any $h: Sa \to Sa'$ yields $f = \varepsilon_{a'} \circ Th \circ \varepsilon_a^{-1}$ with $Sf = h$ (since $T$ is faithful, $TSf = Th$ implies $Sf = h$).

(iii) $\Rightarrow$ (ii): If $S$ is full, faithful, and essentially surjective, construct a left adjoint $T$. For each $c \in C$, choose $T_0c \in A$ and an isomorphism $\eta_c: c \cong S(T_0c)$. For any $f: c \to Sa$, since $S$ is full, $f \circ \eta_c^{-1} = Sg$ for some $g: T_0c \to a$, unique because $S$ is faithful. Hence $\eta_c$ is universal from $c$ to $S$, so $T_0$ extends uniquely to a functor $T$ left adjoint to $S$ with unit $\eta$. The counit $\varepsilon$ satisfies $S\varepsilon_a = (\eta_{Sa})^{-1}$, so $\varepsilon$ is a natural isomorphism since $S$ is full and faithful. Thus $\langle T, S; \eta, \varepsilon \rangle$ is an adjoint equivalence.

(ii) $\Rightarrow$ (i): If $\langle F, G; \eta, \varepsilon \rangle: X \to A$ is an adjunction with $\eta, \varepsilon$ natural isomorphisms, then $F$ and $G$ form an equivalence with $G$ as the quasi-inverse. The unit and counit being isomorphisms directly give the required natural isomorphisms $I_X \cong GF$ and $FG \cong I_A$.
