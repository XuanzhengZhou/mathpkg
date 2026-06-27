---
role: proof
locale: en
of_concept: functoriality-of-jet-bundles
source_book: gtm014
source_chapter: "2"
source_section: "2. Jet Bundles"
---

(1) To show $h_*$ is well-defined: if $f_1, f_2: X \to Y$ both represent $\sigma$, then $f_1 \sim_k f_2$ at $p$. By Lemma 2.4(1), $h \circ f_1 \sim_k h \circ f_2$ at $p$, so $h \circ f_1$ and $h \circ f_2$ define the same $k$-jet in $J^k(X, Z)_{p, h(q)}$. Hence $h_*(\sigma)$ is independent of the choice of representative.

(2) To show $g^*$ is well-defined: if $f_1, f_2: X \to Y$ both represent $\tau$, then $f_1 \sim_k f_2$ at $p$. By Lemma 2.4(2) with the diffeomorphism $g$, we have $f_1 \circ g \sim_k f_2 \circ g$ at $g^{-1}(p)$. Hence $g^*(\tau)$ is well-defined in $J^k(Z, Y)_{g^{-1}(p), q}$.

(3) For any $\sigma = [f] \in J^k(X, Y)_{p,q}$, we have
$$a_*(h_*(\sigma)) = a_*([h \circ f]) = [a \circ (h \circ f)] = [(a \circ h) \circ f] = (a \circ h)_*(\sigma).$$
Also $(\mathrm{id}_Y)_*(\sigma) = [\mathrm{id}_Y \circ f] = [f] = \sigma$, so $(\mathrm{id}_Y)_* = \mathrm{id}_{J^k(X, Y)}$.

If $h$ is a diffeomorphism with inverse $h^{-1}$, then $(h^{-1})_* \circ h_* = (h^{-1} \circ h)_* = (\mathrm{id}_Y)_* = \mathrm{id}$, and similarly $h_* \circ (h^{-1})_* = \mathrm{id}$. Thus $h_*$ is a bijection.

(4) For any $\tau = [f] \in J^k(X, Y)_{p,q}$,
$$a^*(g^*(\tau)) = a^*([f \circ g]) = [(f \circ g) \circ a] = [f \circ (g \circ a)] = (g \circ a)^*(\tau).$$
Also $(\mathrm{id}_X)^*(\tau) = [f \circ \mathrm{id}_X] = [f] = \tau$, so $(\mathrm{id}_X)^* = \mathrm{id}_{J^k(X, Y)}$, and $g^*$ is a bijection whenever $g$ is a diffeomorphism.
