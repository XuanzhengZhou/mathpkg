#!/usr/bin/env python3
"""Write all concept files for s033 section of GTM016."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def w(relpath, content):
    path = os.path.join(BASE, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"  OK: {relpath}")

# ====================== THEOREM 6.3.11 ======================
SLUG = "toral-centralizer-subbiring-theorem"

w(f"{SLUG}/theorem.tex",
  "Let $K/k$ be a finite dimensional radical extension and let $T$ be any toral $k$-subcoring in $H(K/k)$. "
  "Then $H(K/k)^T$ is a $K^T$-subbiring of $H(K)$ and $H(K/k) = K\\,H(K/k)^T$ ($K$-span of $H(K/k)^T$).\n")

w(f"{SLUG}/introduce.en.md",
  "---\n"
  "role: introduce\n"
  "locale: en\n"
  "content_hash: \"\"\n"
  "written_against: \"\"\n"
  "---\n"
  "\n"
  "This theorem describes the structure of the higher derivation algebra $H(K/k)$ of a finite dimensional "
  "radical field extension $K/k$ in the presence of a toral $k$-subcoring $T$. The centralizer $H(K/k)^T$ "
  "of $T$ in $H(K/k)$ is shown to be a $K^T$-subbiring of the full higher derivation algebra $H(K)$ of $K$. "
  "Moreover, the full $H(K/k)$ is recovered as the $K$-span of its $T$-centralizer: "
  "$H(K/k) = K \\cdot H(K/k)^T$. This provides a key structural decomposition that underpins the study of "
  "radical extensions via torus actions.\n")

w(f"{SLUG}/proof_gtm016_6.3.en.md",
  "---\n"
  "role: proof\n"
  "locale: en\n"
  "of_concept: toral-centralizer-subbiring-theorem\n"
  "source_book: gtm016\n"
  "source_chapter: \"6\"\n"
  "source_section: \"6.3\"\n"
  "---\n"
  "\n"
  "Let $H = H(K/k)$. We first consider the case in which $T$ is diagonalizable. "
  "Since $K/k$ is radical, $T$ is coradical (see 6.3.2) and has a $p$-filtration $T_i$ (see 6.3.3). "
  "We prove by induction on $n$ that $H^{T_n}$ is a $K^{T_n}$-subbiring of $H(K)$ for all $n$. "
  "By the induction hypothesis, the elements of $H^{T_n}$ are contained in $H^{T_{n-1}}$, "
  "which is a $K^{T_{n-1}}$-subbiring of $H(K)$. It remains only to show that "
  "$\\varepsilon(H^{T_n}) \\subset K^{T_n}$. For this, let $x \\in H^{T_n}$, $t \\in T_n$ and $b \\in K$. Then\n"
  "\n"
  "$$t(x(1)b) = \\sum_i t(x_i(1))t_i(b) = \\sum_i x_i(t(1))t_i(b)$$\n"
  "\n"
  "$$= \\sum_i x(1)_i t(1)_i t_i(b) = x(1)t(b)$$\n"
  "\n"
  "since $t(1) \\in k$ for all $i$. Thus, $x(1) \\in K^{T_n}$ for $x \\in H^{T_n}$, so that "
  "$\\varepsilon(H^{T_n}) \\subset K^{T_n}$. We have now shown that $H^{T_n}$ is a $K^{T_n}$-subbiring "
  "of $H(K)$ for all $n$, hence that $H^T$ is a $K^T$-subbiring of $H(K)$ for any diagonalizable "
  "toral $k$-subcoring $T$ of $H(K/k)$.\n"
  "\n"
  "We finally drop the assumption that $T$ be diagonalizable. Following the terminology of 6.3.4, "
  "$\\bar{T}$ is a diagonalizable $k$-subcoring of $\\bar{H} = H(\\bar{K}/k)$, "
  "$\\bar{H}^{\\bar{T}}$ is therefore a $\\bar{K}^{\\bar{T}}$-subbiring of $H(\\bar{K})$ and "
  "$\\bar{H} = \\bar{K}\\bar{H}^{\\bar{T}}$. Since $H^T = (\\bar{H}^{\\bar{T}})^G$ and "
  "$K^T = (\\bar{K}^{\\bar{T}})^G$ where $G = \\operatorname{Aut}_k L = \\operatorname{Aut}_k \\bar{k} "
  "= \\operatorname{Aut}_k \\bar{K}$, $H^T$ is a $K^T$-form of $\\bar{H}^{\\bar{T}}$ as "
  "$\\bar{K}^{\\bar{T}}$-space. Consequently, $H^T$ is a $K^T$-form of $\\bar{H}$ as $\\bar{K}$-space, "
  "hence a $K^T$-form of $H$ as $K$-space, so that $H = KH^T$.\n")

# ====================== THEOREM 6.4.1 ======================
SLUG2 = "restriction-map-surjectivity-theorem"

w(f"{SLUG2}/concept.yaml",
  "id: restriction-map-surjectivity-theorem\n"
  "title_en: \"Theorem 6.4.1 — K^T is stable under H(K/k)^T and the restriction map to H(K^T/k) is a surjective homomorphism\"\n"
  "title_zh: \"\"\n"
  "type: theorem\n"
  "domain: algebra\n"
  "subdomain: field-theory\n"
  "difficulty: advanced\n"
  "tags: [radical-extension, toral-subbiring, centralizer, restriction-map, coalgebra-homomorphism, positive-characteristic]\n"
  "depends_on:\n"
  "  required: []\n"
  "  recommended: []\n"
  "  suggested: []\n"
  "source_books:\n"
  "  - book_id: gtm016\n"
  "    author: \"David J. Winter\"\n"
  "    title: \"The Structure of Fields\"\n"
  "    chapter: \"6\"\n"
  "    section: \"6.4\"\n"
  "    pages: \"\"\n"
  "    role_in_book: \"Compares the K^T-birings H(K^T/k) and H(K/k)^T, establishing that the restriction map from the centralizer onto H(K^T/k) is a surjective homomorphism of k-algebras and K^T-coalgebras.\"\n"
  "content_hash: \"\"\n"
  "extraction_date: \"2026-06-27\"\n"
  "extraction_agent: \"v8-full-extract\"\n")

w(f"{SLUG2}/theorem.tex",
  "Let $K/k$ be a finite dimensional radical extension and let $T$ be a toral $k$-subbiring of $H(K/k)$. "
  "Then $K^T$ is stable under $H(K/k)^T$ and the restriction mapping $x \\mapsto x|_{K^T}$ from "
  "$H(K/k)^T$ to $H(K^T/k)$ is a surjective homomorphism of $k$-algebras and $K^T$-coalgebras.\n")

w(f"{SLUG2}/introduce.en.md",
  "---\n"
  "role: introduce\n"
  "locale: en\n"
  "content_hash: \"\"\n"
  "written_against: \"\"\n"
  "---\n"
  "\n"
  "This theorem compares the two $K^T$-birings that arise from a finite dimensional radical extension "
  "$K/k$ and a toral $k$-subbiring $T$: the centralizer $H(K/k)^T$ and the higher derivation algebra "
  "$H(K^T/k)$ of the fixed field. It shows that $K^T$ is stable under the action of $H(K/k)^T$, and that "
  "restricting each operator to $K^T$ yields a surjective homomorphism onto $H(K^T/k)$. This provides a "
  "crucial link between the toral structure and the Galois correspondence for radical extensions.\n")

w(f"{SLUG2}/proof_gtm016_6.4.en.md",
  "---\n"
  "role: proof\n"
  "locale: en\n"
  "of_concept: restriction-map-surjectivity-theorem\n"
  "source_book: gtm016\n"
  "source_chapter: \"6\"\n"
  "source_section: \"6.4\"\n"
  "---\n"
  "\n"
  "It is clear that $K^T$ is stable under $H(K/k)^T$ and that $x \\mapsto x|_{K^T}$ is a $K^T$-linear "
  "$k$-algebra homomorphism.\n"
  "\n"
  "*(The proof continues by induction on the dimension of a coradical coalgebra $C$ over $K$, using the "
  "existence of a nonzero primitive element in $C$ to construct a derivation and a torus, reducing to the "
  "induction hypothesis via the centralizer $C^{T_\\pi}$ of a diagonalizable torus $T_\\pi$. The "
  "surjectivity of the restriction map follows from the fact that $\\bar{H} = \\bar{K}\\bar{H}^{\\bar{T}}$ "
  "and the Galois descent argument as in the proof of Theorem 6.3.11.)*\n")

# ====================== EXERCISES ======================
exercises = {
    "1": (
        "Let $t$ be a linear transformation of a vector space $V$ over an algebraically closed field "
        "$k$ of characteristic $p > 0$. Show that $t^{p^e}$ is diagonalizable for some $e$. "
        "(Hint: Consider the Jordan Canonical Form.)\n"
    ),
    "2": (
        "Show that if $S$ is a set of pairwise commuting semisimple linear transformations of a finite "
        "dimensional vector space $V$ over a field $k$ of characteristic $p > 0$, then $\\langle S "
        "\\rangle_p$ (defined following 6.1.7) is a $k$-torus on $V$. Show that $\\langle S \\rangle_p$ "
        "is diagonalizable if every element of $S$ is diagonalizable. (Hint: The eigenspaces of any "
        "element $s$ of $S$ are invariant under $S$.)\n"
    ),
    "3": (
        "Let $K/k$ be a finite dimensional radical extension. Show that for any separable algebraic "
        "extension $L$ of $k$, there is a bijective $k$-linear mapping from $L \\otimes_k "
        "\\operatorname{End}_k K$ to $\\operatorname{End}_{L \\otimes_k k} L \\otimes_k K$ mapping "
        "$x \\otimes T$ to $(x\\,\\mathrm{id}_L) \\otimes T$ for $x \\in L, T \\in \\operatorname{End}_k K$.\n"
    ),
    "4": (
        "Under what conditions on a finite dimensional extension $K/k$ is $KI$ ($K$-span of "
        "$I \\in \\operatorname{End}_k K$) a $k$-torus? Show that the diagonalizability of $T$ in 6.2 "
        "characterizes those finite dimensional radical extensions $K/k$ for which $KI$ is a $k$-torus.\n"
    ),
    "12": (
        "(Sequence of Divided Powers). In a coalgebra $C$ over $k$, a sequence of divided powers is a "
        "sequence $D_0, \\ldots, D_m$ of elements of $C$ such that "
        "$\\Delta D_s = \\sum_{r=0}^s D_{s-r} \\otimes D_r$ for $0 \\leq s \\leq m$. Show that if "
        "$D_0, \\ldots, D_m$ is a sequence of divided powers, then the $k$-span of $D_0, \\ldots, D_m$ "
        "is a colocal cocommutative subcoalgebra $D$ of $C$ and for any measuring representation "
        "$f: D \\rightarrow \\operatorname{End}_k K$ of $D$ on a field extension $K/k$ mapping $D_0$ "
        "to $I$, the sequence $f(D_0), f(D_1), \\ldots, f(D_m)$ is a higher derivation on $K$.\n"
    ),
    "13": (
        "Let $K/k$ be a finite dimensional field extension and suppose that $k$ is the subfield of "
        "constants of the set of higher derivations of $K$ over $k$, that is, for each $a \\in K - k$, "
        "there exists a higher derivation $D = (D_0, D_1, \\ldots, D_m)$ such that $D_i(a) \\neq 0$ for "
        "some $i$ with $1 \\leq i \\leq m$. Show that $K/k$ is a radical extension. (Hint: Show for a "
        "fixed higher derivation $D = (D_0, D_1, \\ldots, D_m)$ that $K$ is a radical extension of the "
        "field $K^D = \\{c \\in K \\mid D_i(c) = 0 \\text{ for } 1 \\leq i \\leq m\\}$ by showing that "
        "the $K$-span $C$ of $\\{D_0, D_1, \\ldots, D_m\\}$ is a colocal subcoalgebra of $H(K/k)$.)\n"
    ),
    "14": (
        "Let $K/k$ be a radical extension. Elements $y_1, \\ldots, y_s$ of $K$ are $p$-independent over "
        "$k$ if $[k(y_1, \\ldots, y_s) : k] = p^s$ and $y_i^p \\in k$ for $1 \\leq i \\leq s$.\n\n"
        "(e) If $y_1, \\ldots, y_s$ are $p$-independent elements of $\\sqrt[p]{K}$ over $\\sqrt[p]{k}$, "
        "then $y_1^p, \\ldots, y_s^p$ are $p$-independent elements of $\\sqrt[p]{K}$ over $\\sqrt[p]{k}$.\n\n"
        "(f) Choosing $m$ such that $K = \\sqrt[p^m]{k} \\supseteq \\sqrt[p^{m-1}]{k} \\supseteq \\cdots "
        "\\supseteq \\sqrt[p]{k} \\supseteq k$, there exist elements "
        "$y_1, \\ldots, y_{s_m}, y_{s_m+1}, \\ldots, y_{s_{m-1}}, \\ldots, y_{s_2+1}, \\ldots, y_{s_1}$ "
        "of $K$ such that $y_1, \\ldots, y_{s_m}$ is a $p$-basis for $K$ over $\\sqrt[p]{k}$; "
        "$y_1^p, \\ldots, y_{s_m}^p, y_{s_m+1}, \\ldots, y_{s_{m-1}}$ is a $p$-basis for $\\sqrt[p]{k}$ "
        "over $\\sqrt[p^2]{k}$; ... and "
        "$y_1^{p^{m-1}}, \\ldots$ is a $p$-basis for $\\sqrt[p^{m-1}]{k}$ over $k$.\n\n"
        "(g) $K = k(y_1) \\otimes_k \\cdots \\otimes_k k(y_{s_1})$ (internal tensor product over $k$) "
        "where the $y_1, \\ldots, y_{s_1}$ are as described in part (f).\n"
    ),
    "15": (
        "(Dual of Measuring Representation). Let $\\rho: C \\rightarrow \\operatorname{End}_k K$ be a "
        "measuring representation of a finite dimensional colocal $k$-coalgebra $C$ with grouplike "
        "element $e$ on an extension $K/k$ such that $\\rho(e) = I$. Let $A = C^*$ be the dual "
        "$k$-algebra of $C$ and let $\\alpha: K \\rightarrow A \\otimes_k K$ be the $k$-algebra "
        "homomorphism dual to $\\rho$. Show that $\\alpha$ is a $k$-algebra homomorphism and describe "
        "the relationship between the measuring representation and its dual.\n"
    ),
    "16": (
        "Let $K/k$ be a finite dimensional radical extension, $C$ a finite dimensional colocal "
        "$k$-coalgebra with grouplike element $e$, and $\\rho: C \\rightarrow \\operatorname{End}_k K$ "
        "a measuring representation such that $\\rho(e) = I$ and $K^C = k$. Let $A$ be the dual "
        "$k$-algebra of $C$ and $\\alpha: K \\rightarrow A \\otimes_k K$ the $k$-algebra homomorphism "
        "dual to $\\rho$.\n\n"
        "(a) Let $x_1, \\ldots, x_m$ be a $p$-basis for $\\sqrt{K}/K$. Let $X = \\{X_1, \\ldots, X_m\\}$ "
        "and let $I$ be the ideal of $K[X]$ generated by $\\{X_i^p - x_i^p \\mid 1 \\leq i \\leq m\\}$. "
        "Let $\\bar{X}_i = X_i + I$ and $K[\\bar{X}] = K[X]/I$. Show that there is a $K$-linear "
        "isomorphism from $K[\\bar{X}]$ to $\\sqrt{K}$ sending $\\bar{X}_i$ to $x_i$ for "
        "$1 \\leq i \\leq m$.\n\n"
        "(b) Show that there exists an integer $n$ and elements $u_{ij} \\in \\operatorname{Nil} A$, "
        "$x_{ij} \\in \\sqrt{K}$ such that "
        "$\\alpha(x_i^p) = 1_A \\otimes x_i^p + \\sum_j u_{ij} \\otimes x_{ij}^p$ for "
        "$1 \\leq i \\leq m$.\n\n"
        "(c) Let $Y = \\{Y_{ij} \\mid 1 \\leq i \\leq m, 1 \\leq j \\leq n\\}$ and $J$ be the ideal of "
        "$A[Y]$ generated by $\\{Y_{ij}^p - u_{ij} \\mid 1 \\leq i \\leq m, 1 \\leq j \\leq n\\}$. Let "
        "$\\sqrt{u_{ij}} = Y_{ij} + J$ and $\\sqrt{A} = A[Y]/J$. Show that $\\beta: A \\rightarrow "
        "\\sqrt{A}$ is an embedding.\n"
    ),
    "17": (
        "Let $K/k$ be a finite dimensional radical extension. Show that there exists a finite dimensional "
        "cocommutative colocal $k$-coalgebra $C$ with grouplike element $e$ and measuring representation "
        "$\\rho: C \\rightarrow \\operatorname{End}_k K$ such that $\\rho(e) = I$ and the commutant "
        "$K^C = k$. Show this as follows.\n\n"
        "(a) Let $K_i = k(K^{p^i})$ for $i = 0, 1, 2, \\ldots$ and let $\\sqrt{K_i} = K_{i-1}$ for "
        "$i \\geq 1$. Show that $K = K_0 \\supset K_1 \\supset \\cdots \\supset K_m = k$ for some $m$ "
        "and $K_i = k((\\sqrt{K_i})^p)$ for all $i$.\n\n"
        "(b) For each $i$, there exists a finite dimensional cocommutative $k$-coalgebra $C_i$ with "
        "grouplike element $e_i$ and measuring representation $\\rho_i: C_i \\rightarrow "
        "\\operatorname{End}_k \\sqrt{K_i}$ such that $\\rho(e_i) = I$ and $\\sqrt{K_i}^{C_i} = K_i$. "
        "(Use E.6.18.)\n\n"
        "(c) For each $i$, there exists a finite dimensional cocommutative colocal $k$-coalgebra "
        "$\\sqrt{\\sqrt{C_i}}$ with grouplike element $\\sqrt{\\sqrt{e_i}}$ and measuring representation "
        "$\\sqrt{\\sqrt{\\rho_i}}: \\sqrt{\\sqrt{C_i}} \\rightarrow \\operatorname{End}_k K$ such that "
        "$K^{\\sqrt{\\sqrt{C_i}}} \\cap \\sqrt{K_i} = K_i$.\n\n"
        "(d) Show that if $D_1, D_2$ are cocommutative colocal $k$-coalgebras with grouplike elements "
        "$f_1, f_2$, then the $k$-span $P = k(f_1 - f_2)$ is a coideal of $D_1 \\otimes_k D_2$.\n"
    ),
    "18": (
        "(Sweedler). Let $A$ be a commutative $k$-algebra. A cosplit cocommutative $k$-coalgebra on $A$ "
        "is a pair $(C, \\rho)$ where $C$ is a cocommutative colocal $k$-coalgebra with grouplike "
        "element $e$ and $\\rho: C \\rightarrow \\operatorname{End}_k A$ is a measuring representation "
        "of $C$ on $A$ such that $\\rho(e) = I$ and $A^C = k$. A universal cosplit cocommutative "
        "$k$-coalgebra on $A$ is a cosplit cocommutative $k$-coalgebra $(C, \\rho)$ on $A$ such that "
        "for any cosplit cocommutative $k$-coalgebra $(C', \\rho')$ on $A$, there is a unique morphism "
        "$\\varphi$ from $(C', \\rho')$ to $(C, \\rho)$. Show the existence of a universal cosplit "
        "cocommutative $k$-coalgebra on $K$ for a finite dimensional radical extension $K/k$.\n"
    ),
    "22": (
        "(Sweedler). Let $K/k$ be a radical extension. Show that there exists a $K$-measuring "
        "$k$-bialgebra $H_k(K)$ such that $K^{H_k(K)} = k$.\n"
    ),
    "25": (
        "(Mordeson and Vinograd). Let $K/k$ be a radical extension of infinite dimension. Assuming that "
        "$K^{p^n} \\subset k$ for some $n$, prove (a), (b), (c) of the preceding exercise in the "
        "present context. What can be said for arbitrary radical extensions $K/k$?\n"
    ),
    "26": (
        "(Haddix, Mordeson, Sweedler, Vinograd). A subbase of a radical extension $K/k$ is a subset $S$ "
        "of $K-k$ such that $K = k(S)$ and $k(S_0) = k(s_1) \\otimes_k \\cdots \\otimes_k k(s_n)$ "
        "(internal tensor product over $k$) for any finite subset $S_0 = \\{s_1, \\ldots, s_n\\}$ of $S$. "
        "Show that if $K^{p^n} \\subset k$ for some $n$, then the following conditions are equivalent, "
        "using the ideas described in E.6.14.\n\n"
        "(a) $K/k$ has a subbase;\n\n"
        "(b) $K^{p^i}$ and $k$ are linearly disjoint over $K^{p^i} \\cap k$ for all $i$;\n\n"
        "(c) for any canonical generating system $T_1, T_2, \\ldots$ of $K/k$, "
        "$T_i^{p^i} \\subset (K^{p^i} \\cap k) \\bigcup_{j>i} T_j^{p^i}$.\n\n"
        "Finally, show that $K/k$ is not diagonalizable.\n"
    ),
    "30": (
        "Show that there is a finite dimensional radical extension which is not toral. (Hint: Let $L$ be "
        "the separable closure of $k$ and let $\\bar{K} = L \\otimes_k K$, $\\bar{k} = L \\otimes_k k$ "
        "where $K/k$ is the extension constructed in E.6.28. Show that the dimensions indicated by the "
        "diagram are correct. Finally, using E.6.28, show that $K/k$ is not toral.)\n"
    ),
    "31": (
        "Let $K/k$ be a radical extension. Let $C$ be a finite dimensional $K$-subspace of "
        "$\\operatorname{End}_k K$ such that $[x, y] \\in C$ and $x^p \\in C$ for all $x, y \\in C$. "
        "Letting $L$ be a separable extension of $k$, $\\bar{K} = L \\otimes_k K$, "
        "$\\bar{k} = L \\otimes_k k$, $\\bar{C} = L \\otimes_k C$, show that $\\bar{C}$ is a finite "
        "dimensional $\\bar{K}$-subspace of $\\operatorname{End}_{\\bar{k}} \\bar{K}$ such that "
        "$[x, y] \\in \\bar{C}$ and $x^p \\in \\bar{C}$ for all $x, y \\in \\bar{C}$. (Hint: After "
        "showing that the $\\bar{k}$-span $[\\bar{C}, \\bar{C}]$ is a subset of $\\bar{C}$, show that "
        "if $x, y \\in \\bar{C}$ and $x^p, y^p \\in \\bar{C}$, then $(x + y)^p \\in \\bar{C}$ because "
        "$(x + y)^p \\equiv x^p + y^p \\pmod{[\\bar{C}, \\bar{C}]}$.)\n"
    ),
    "32": (
        "Show that if $K/k$ is an Abelian-extension of finite degree not divisible by $p$, then the "
        "$k$-span $T$ of $\\operatorname{Aut}_k K$ is a toral $k$-subbiring of $H(K/k)$.\n"
    ),
    "35": (
        "Let $K = k(x)$ where $x \\in K-k$ and $x^p \\in k$. Let $s$ and $t$ be the derivations of "
        "$K/k$ such that\n\n"
        "$$s(x^i) = ix^i$$\n"
        "$$t((x+1)^i) = i(x+1)^i$$\n\n"
        "for all $i$. Let $S$ be the $k$-span of $I, s, \\ldots, s^{p-1}$ and let $T$ be the $k$-span "
        "of $I, t, \\ldots, t^{p-1}$. Show that $S$ and $T$ are two distinct cosplit $k$-forms of the "
        "$K/k$-bialgebra $H(K/k)$.\n"
    ),
    "36": (
        "Let $K/k$ be a finite dimensional radical extension of exponent one. Prove the following.\n\n"
        "(a) If $T$ is a maximal finite dimensional diagonalizable toral $k$-subring of $H(K/k)$, then "
        "$K^T = k$.\n\n"
        "(b) If $S$ is a diagonalizable $k$-torus in $\\operatorname{Der}_k K$, then there exists a "
        "diagonalizable $k$-torus $S'$ in $\\operatorname{Der}_k K$ such that $S \\cap S' = \\{0\\}$, "
        "$T = S + S'$ (direct) is a maximal $k$-torus in $\\operatorname{Der}_k K$ and, consequently, "
        "$K^T = k$ and $K = K^S K^{S'}$ (internal tensor product over $k$).\n\n"
        "(c) For any subfield $k'$ of $K$ containing $k$, there is a subfield $k''$ of $K$ containing "
        "$k$ such that $K = k' k''$ (internal tensor product over $k$).\n"
    ),
    "37": (
        "Let $K/k$ be a finite dimensional radical extension of characteristic $p > 0$ and let "
        "$D \\in \\operatorname{Der}_k K$. Show that for some $e$, the $k$-span $\\langle D^{p^e} "
        "\\rangle$ of $D^{p^e}, D^{p^{e+1}}, \\ldots$ is a toral $k$-subcoalgebra of $H(K/k)$.\n"
    ),
}

for num, text in exercises.items():
    fname = f"exercise_gtm016_6.E.{num}.en.md"
    content = (
        "---\n"
        "role: exercise\n"
        "locale: en\n"
        f"chapter: \"6\"\n"
        "section: \"E.6\"\n"
        f"exercise_number: {num}\n"
        "---\n"
        "\n"
        f"{text}"
    )
    w(fname, content)

print(f"\n=== DONE: {len(exercises)} exercises written ===")
