---
role: proof
locale: en
of_concept: strongly-compact-implies-strong-limit
source_book: gtm037
source_chapter: "31"
source_section: "5"
---

Suppose that $m$ is not a strong limit cardinal. We shall show that it is not strongly compact. Clearly there is a cardinal $n < m$ such that $m \leq 2^n$. Let $\mathcal{L}$ be a first-order language with unary relation symbols $P_{\xi\varepsilon}$ for each $\xi < n$ and $\varepsilon < 2$. Let $\Gamma$ consist of the following sentences:

(1) $\bigwedge_{\xi < n} \bigvee_{\varepsilon < 2} \forall v_0 P_{\xi\varepsilon} v_0$;
(2) $\forall v_0 \forall v_1 (v_0 = v_1)$;
(3) $\neg \bigwedge_{\xi < n} \forall v_0 P_{\xi, f\xi} v_0$ (for each $f \in {}^n 2$).

Suppose $\Gamma$ has a model, $\mathfrak{A} = \langle \{a\}, P_{\xi\varepsilon}^{\mathfrak{A}} \rangle_{\xi < n, \varepsilon < 2}$. By (1), there is a function $f \in {}^n 2$ such that $P_{\xi, f\xi}^{\mathfrak{A}} = \{a\}$ for every $\xi < n$. This contradicts (3).

Now let $\Delta$ be any subset of $\Gamma$ of power $< m$. Since $m \leq 2^n$, there is then a function $f \in {}^n 2$ such that the corresponding sentence of type (3) is not in $\Delta$. Let $A = \{0\}$, and for $\xi < n, \varepsilon < 2$, let
$$P_{\xi\varepsilon}^{\mathfrak{A}} = \{0\} \quad \text{if } f\xi = \varepsilon,$$
$$P_{\xi\varepsilon}^{\mathfrak{A}} = \emptyset \quad \text{if } f\xi \neq \varepsilon.$$

Clearly then $\mathfrak{A}$ is a model of $\Delta$. Thus $\Gamma$ is a counterexample to $(m,\infty)$-compactness, so $m$ is not strongly compact.
