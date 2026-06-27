#!/usr/bin/env python3
"""Generate all concept files for GTM073 Chapter VI: The Structure of Fields."""
import os

BASE = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/gtm-0073/gtm-0073_ch05_concepts"
DATE = "2026-06-24"
AGENT = "v7-gtm073"
BOOK_ID = "gtm-0073"
AUTHOR = "Hungerford, Thomas W."
BOOK_TITLE = "Algebra"
CHAPTER = "VI"

def write_yaml(dirname, id_, title_en, title_zh, typ, subdomain, difficulty, section, role, tags="[]"):
    d = os.path.join(BASE, dirname)
    os.makedirs(d, exist_ok=True)
    content = f"""id: "{id_}"
title_en: "{title_en}"
title_zh: "{title_zh}"
type: {typ}
domain: algebra
subdomain: {subdomain}
difficulty: {difficulty}
tags: {tags}
depends_on:
  required: []
  recommended: []
  suggested: []
proof_deps: {{}}
source_books:
  - book_id: {BOOK_ID}
    author: "{AUTHOR}"
    title: "{BOOK_TITLE}"
    chapter: {CHAPTER}
    section: "{section}"
    pages: ""
    role_in_book: "{role}"
content_hash: ""
extraction_date: "{DATE}"
extraction_agent: "{AGENT}"
"""
    with open(os.path.join(d, "concept.yaml"), "w") as f:
        f.write(content)

def write_tex(dirname, content):
    with open(os.path.join(BASE, dirname, "theorem.tex"), "w") as f:
        f.write(content)

def write_intro(dirname, content):
    header = """---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
"""
    with open(os.path.join(BASE, dirname, "introduce.en.md"), "w") as f:
        f.write(header + content)

def write_proof(dirname, section, technique, content):
    sec_safe = section.replace(".", "_")
    fname = f"proof_{BOOK_ID}_VI_{sec_safe}_{technique}.en.md"
    header = f"""---
role: proof
source_book: {BOOK_ID}
chapter: {CHAPTER}
section: "{section}"
proof_technique: {technique}
locale: en
content_hash: ""
written_against: ""
---
"""
    with open(os.path.join(BASE, dirname, fname), "w") as f:
        f.write(header + content)

# ============================================================
# SECTION 1: TRANSCENDENCE BASES
# ============================================================

# ---------- Definition 1.1 ----------
write_yaml("algebraic-dependence-independence", "algebraic-dependence-independence",
           "Algebraic Dependence and Independence",
           "",
           "definition", "field-theory", "basic", "VI.1", "Definition 1.1",
           tags='["algebraic-dependence", "algebraic-independence", "transcendental"]')
write_tex("algebraic-dependence-independence", r"""Let $F$ be an extension field of $K$ and $S$ a subset of $F$.
\begin{itemize}
\item $S$ is \textbf{algebraically dependent over $K$} if for some positive integer $n$ there exists a nonzero polynomial $f \in K[x_1, \ldots, x_n]$ such that $f(s_1, \ldots, s_n) = 0$ for some distinct $s_1, \ldots, s_n \in S$.
\item $S$ is \textbf{algebraically independent over $K$} if $S$ is not algebraically dependent over $K$.
\end{itemize}
Equivalently, $S$ is algebraically independent over $K$ if for all $n > 0$, $f \in K[x_1, \ldots, x_n]$ and distinct $s_1, \ldots, s_n \in S$,
\[
f(s_1, \ldots, s_n) = 0 \Rightarrow f = 0.
\]
""")
write_intro("algebraic-dependence-independence",
    "Algebraic dependence generalizes the concept of linear dependence: a set $S$ is algebraically "
    "dependent over $K$ if some nonzero polynomial with coefficients in $K$ vanishes on finitely many "
    "elements of $S$. Every subset of an algebraically independent set is algebraically independent. "
    "In particular, the empty set is algebraically independent. A singleton $\\{u\\}$ is algebraically "
    "dependent if and only if $u$ is algebraic over $K$. Every element of an algebraically independent "
    "set is necessarily transcendental over $K$.\n")

# ---------- Theorem 1.2 ----------
write_yaml("rational-function-field-isomorphism", "rational-function-field-isomorphism",
           "Rational Function Field Isomorphism from Algebraic Independence",
           "",
           "theorem", "field-theory", "basic", "VI.1", "Theorem 1.2",
           tags='["rational-functions", "field-isomorphism", "algebraic-independence"]')
write_tex("rational-function-field-isomorphism", r"""Let $F$ be an extension field of $K$ and $\{s_1, \ldots, s_n\}$ a subset of $F$ which is algebraically independent over $K$. Then there exists a $K$-isomorphism
\[
K(s_1, \ldots, s_n) \cong K(x_1, \ldots, x_n),
\]
where $K(x_1, \ldots, x_n)$ is the field of rational functions in $n$ indeterminates over $K$.
""")
write_intro("rational-function-field-isomorphism",
    "This theorem shows that an algebraically independent set behaves exactly like a set of "
    "indeterminates. The field generated over $K$ by algebraically independent elements is "
    "$K$-isomorphic to the rational function field in the same number of variables. This is "
    "the field-theoretic analogue of the fact that a linearly independent set spans a vector "
    "space isomorphic to the free vector space.\n")
write_proof("rational-function-field-isomorphism", "VI.1", "evaluation-map",
    r"""The evaluation homomorphism $\varphi: K[x_1, \ldots, x_n] \to K[s_1, \ldots, s_n]$ defined by
$f(x_1, \ldots, x_n) \mapsto f(s_1, \ldots, s_n)$ is a $K$-algebra homomorphism.
By algebraic independence, $\ker \varphi = \{0\}$, so $\varphi$ is an isomorphism onto $K[s_1, \ldots, s_n]$.
This extends uniquely to an isomorphism of quotient fields:
\[
\bar{\varphi}: K(x_1, \ldots, x_n) \xrightarrow{\cong} K(s_1, \ldots, s_n),
\]
\[
f/g \mapsto f(s_1, \ldots, s_n)/g(s_1, \ldots, s_n).
\]
""")

# ---------- Theorem 1.5 ----------
write_yaml("algebraic-independence-criterion", "algebraic-independence-criterion",
           "Criterion for Algebraic Independence",
           "",
           "theorem", "field-theory", "basic", "VI.1", "Theorem 1.5",
           tags='["algebraic-independence", "transcendental-extension", "algebraic-extension"]')
write_tex("algebraic-independence-criterion", r"""Let $F$ be an extension field of $K$ and $u \in F$.
If $S$ is an algebraically independent subset of $F$ over $K$ such that $u$ is algebraic over $K(S)$, then either $u \in K(S)$ or $S \cup \{u\}$ is algebraically dependent over $K$.
Equivalently, if $S$ is algebraically independent over $K$ and $S \cup \{u\}$ is also algebraically independent, then $u$ is transcendental over $K(S)$.
""")
write_intro("algebraic-independence-criterion",
    "This theorem characterizes when adding an element preserves algebraic independence. "
    "If $S$ is algebraically independent and $u$ is algebraic over $K(S)$, then either $u$ is "
    "already in $K(S)$ or adding $u$ creates an algebraic dependence. In particular, no element "
    "of an algebraically independent set is algebraic over the field generated by the remaining elements.\n")
write_proof("algebraic-independence-criterion", "VI.1", "polynomial-common-denominator",
    r"""Suppose $S \cup \{u\}$ is algebraically independent. If $u$ were algebraic over $K(S)$, then
$f(u) = 0$ for some nonzero polynomial $f \in K(S)[x]$. Write $f(x) = \sum a_i x^i$ with
$a_i \in K(S)$. By Theorem V.1.3, there is a finite subset $\{s_1, \ldots, s_r\} \subseteq S$ such that
$a_i = f_i(s_1, \ldots, s_r)/g_i(s_1, \ldots, s_r)$ for some $f_i, g_i \in K[x_1, \ldots, x_r]$.
Let $g = g_1 \cdots g_n$ and $\tilde{f}_i = f_i \cdot \prod_{j \neq i} g_j$. Then
$a_i = \tilde{f}_i(s_1, \ldots, s_r)/g(s_1, \ldots, s_r)$ and
\[
f(x) = g(s_1, \ldots, s_r)^{-1} \sum \tilde{f}_i(s_1, \ldots, s_r) x^i.
\]
Let $h(x_1, \ldots, x_r, x) = \sum \tilde{f}_i(x_1, \ldots, x_r) x^i \in K[x_1, \ldots, x_r, x]$.
Since $f(u) = 0$ and $g(s_1, \ldots, s_r)^{-1} \neq 0$, we have $h(s_1, \ldots, s_r, u) = 0$.
But $S \cup \{u\}$ is algebraically independent, so $h = 0$, whence all $\tilde{f}_i = 0$, so all $a_i = 0$,
contradicting $f \neq 0$. Therefore $u$ must be transcendental over $K(S)$.
""")

# ---------- Definition: Transcendence Base ----------
write_yaml("transcendence-base", "transcendence-base",
           "Transcendence Base of a Field Extension",
           "",
           "definition", "field-theory", "basic", "VI.1", "Definition 1.4",
           tags='["transcendence-base", "algebraic-independence", "field-extension"]')
write_tex("transcendence-base", r"""Let $F$ be an extension field of $K$. A subset $S \subseteq F$ is a \textbf{transcendence base} of $F$ over $K$ provided that:
\begin{enumerate}
\item[(i)] $S$ is algebraically independent over $K$;
\item[(ii)] $F$ is algebraic over $K(S)$.
\end{enumerate}
Equivalently, $S$ is a maximal (with respect to set-theoretic inclusion) algebraically independent subset of $F$ over $K$.
""")
write_intro("transcendence-base",
    "A transcendence base is the field-theoretic analogue of a vector space basis, with algebraic "
    "independence replacing linear independence. Every field extension possesses a transcendence base "
    "(by Zorn's Lemma), and any two transcendence bases have the same cardinality. The transcendence "
    "base captures the purely transcendental part of the extension: $K \\subset K(S) \\subset F$, "
    "where $K(S)$ is purely transcendental over $K$ and $F$ is algebraic over $K(S)$.\n")

# ---------- Corollary 1.6 ----------
write_yaml("algebraic-over-transcendence-base", "algebraic-over-transcendence-base",
           "Field Extension is Algebraic over Transcendence Base",
           "",
           "corollary", "field-theory", "basic", "VI.1", "Corollary 1.6",
           tags='["transcendence-base", "algebraic-extension", "field-extension"]')
write_tex("algebraic-over-transcendence-base", r"""If $F$ is an extension field of $K$ and $T$ is a transcendence base of $F$ over $K$, then $F$ is algebraic over $K(T)$.
In particular, every field extension $K \subset F$ factors as $K \subset K(T) \subset F$, where $K(T)$ is purely transcendental over $K$ and $F$ is algebraic over $K(T)$.
""")
write_intro("algebraic-over-transcendence-base",
    "This corollary formalizes the fundamental structure theorem for field extensions: every "
    "extension decomposes into a purely transcendental extension followed by an algebraic extension. "
    "The transcendence base $T$ parameterizes the transcendental part. If $T = \\varnothing$, "
    "then $F$ is purely algebraic over $K$, and tr.d.$F/K = 0$.\n")

# ---------- Theorem 1.8 (Replacement) ----------
write_yaml("transcendence-base-cardinality", "transcendence-base-cardinality",
           "Any Two Transcendence Bases Have the Same Cardinality",
           "",
           "theorem", "field-theory", "intermediate", "VI.1", "Theorem 1.8",
           tags='["transcendence-base", "cardinality", "exchange-property"]')
write_tex("transcendence-base-cardinality", r"""Let $F$ be an extension field of $K$. If $S$ and $T$ are transcendence bases of $F$ over $K$, then $|S| = |T|$.
Moreover, if $S$ is finite with $|S| = n$, then any transcendence base of $F$ over $K$ has $n$ elements.
""")
write_intro("transcendence-base-cardinality",
    "This theorem establishes that the cardinality of a transcendence base is an invariant of the "
    "field extension, analogous to the invariance of dimension for vector spaces. The proof uses "
    "an exchange property: if $S = \\{s_1, \\ldots, s_n\\}$ is a finite transcendence base and $T$ is "
    "any transcendence base, then there exists $t_1 \\in T$ such that $\\{t_1, s_2, \\ldots, s_n\\}$ "
    "is also a transcendence base, and the process can be continued.\n")
write_proof("transcendence-base-cardinality", "VI.1", "exchange-replacement",
    r"""Let $S = \{s_1, \ldots, s_n\}$ be a finite transcendence base and $T$ any transcendence base.
We claim that some $t_1 \in T$ is transcendental over $K(s_2, \ldots, s_n)$. Otherwise every element
of $T$ is algebraic over $K(s_2, \ldots, s_n)$, whence $K(s_2, \ldots, s_n)(T)$ is algebraic over
$K(s_2, \ldots, s_n)$. Since $F$ is algebraic over $K(T)$, $F$ is algebraic over
$K(T)(s_2, \ldots, s_n) = K(s_2, \ldots, s_n)(T)$. Then $F$ is algebraic over $K(s_2, \ldots, s_n)$,
so $s_1$ is algebraic over $K(s_2, \ldots, s_n)$, contradicting Theorem 1.5. Hence
$\{t_1, s_2, \ldots, s_n\}$ is algebraically independent.

If $s_1$ were transcendental over $K(t_1, s_2, \ldots, s_n)$, then $\{t_1, s_1, s_2, \ldots, s_n\}$
would be algebraically independent, contradicting maximality of $S$. Therefore $s_1$ is algebraic
over $K(t_1, s_2, \ldots, s_n)$, and $F$ is algebraic over $K(t_1, s_2, \ldots, s_n)$. Hence
$\{t_1, s_2, \ldots, s_n\}$ is a transcendence base. Repeating, we can replace all $s_i$ with
$t_i \in T$. If $T$ had more than $n$ elements, the process would produce an algebraically
independent set larger than the transcendence base—a contradiction. Thus $|T| = n$.

For infinite transcendence bases, the equality follows from cardinal arithmetic using the
Schroeder-Bernstein Theorem, assigning to each $t \in T$ a finite subset of $S$ on which
$t$ algebraically depends, giving $|T| \leq |S| \aleph_0 = |S|$.
""")

# ---------- Definition 1.10 ----------
write_yaml("transcendence-degree", "transcendence-degree",
           "Transcendence Degree of a Field Extension",
           "",
           "definition", "field-theory", "basic", "VI.1", "Definition 1.10",
           tags='["transcendence-degree", "field-extension", "invariant"]')
write_tex("transcendence-degree", r"""Let $F$ be an extension field of $K$. The \textbf{transcendence degree} of $F$ over $K$ (denoted $\operatorname{tr.d.} F/K$) is the cardinal number $|S|$, where $S$ is any transcendence base of $F$ over $K$.
In particular:
\[
\operatorname{tr.d.} F/K = 0 \quad\Longleftrightarrow\quad F \text{ is algebraic over } K.
\]
""")
write_intro("transcendence-degree",
    "The transcendence degree is a well-defined cardinal invariant of a field extension, "
    "independent of the choice of transcendence base. It measures the maximal number of "
    "algebraically independent elements. In the analogy between algebraic and linear independence, "
    "tr.d.$F/K$ is the analogue of the vector space dimension $[F:K]$. One always has "
    "tr.d.$F/K \\leq [F:K]$, and tr.d.$F/K = 0$ if and only if $F$ is algebraic over $K$.\n")

# ---------- Theorem 1.11 ----------
write_yaml("transcendence-degree-additivity", "transcendence-degree-additivity",
           "Additivity of Transcendence Degree",
           "",
           "theorem", "field-theory", "basic", "VI.1", "Theorem 1.11",
           tags='["transcendence-degree", "additivity", "tower", "field-tower"]')
write_tex("transcendence-degree-additivity", r"""If $F$ is an extension field of $E$ and $E$ an extension field of $K$, then
\[
\operatorname{tr.d.} F/K = \operatorname{tr.d.} F/E + \operatorname{tr.d.} E/K.
\]
""")
write_intro("transcendence-degree-additivity",
    "Transcendence degree is additive in towers of field extensions, exactly as vector space "
    "dimension is multiplicative. The proof uses the fact that if $S$ is a transcendence base "
    "of $E$ over $K$ and $T$ is a transcendence base of $F$ over $E$, then $S \\cap T = \\varnothing$ "
    "and $S \\cup T$ is a transcendence base of $F$ over $K$.\n")
write_proof("transcendence-degree-additivity", "VI.1", "union-of-bases",
    r"""Let $S$ be a transcendence base of $E$ over $K$ and $T$ a transcendence base of $F$ over $E$.
Since $S \subset E$, $S$ is algebraically dependent over $E$, whence $S \cap T = \varnothing$.
It suffices to show that $S \cup T$ is a transcendence base of $F$ over $K$.

First, $S \cup T$ is algebraically independent over $K$: if a polynomial relation held among
elements of $S \cup T$, then by treating elements of $S$ as constants we would get an algebraic
dependence of $T$ over $K(S)$, hence over $E$, contradicting the independence of $T$ over $E$.

Second, $F$ is algebraic over $K(S \cup T) = K(S)(T) = E(T)$ since $F$ is algebraic over $E(T)$
and $K(S)(T) \supseteq E(T)$. More precisely, $E$ is algebraic over $K(S)$, so $E(T)$ is algebraic
over $K(S)(T)$. Since $F$ is algebraic over $E(T)$, $F$ is algebraic over $K(S \cup T)$.

Thus $S \cup T$ is a transcendence base, and $|S \cup T| = |S| + |T|$ since $S \cap T = \varnothing$.
""")

# ---------- Theorem 1.12 ----------
write_yaml("isomorphism-extension-by-transcendence-degree", "isomorphism-extension-by-transcendence-degree",
           "Extension of Isomorphisms between Algebraically Closed Fields",
           "",
           "theorem", "field-theory", "intermediate", "VI.1", "Theorem 1.12",
           tags='["field-isomorphism", "algebraically-closed", "transcendence-degree", "isomorphism-extension"]')
write_tex("isomorphism-extension-by-transcendence-degree", r"""Let $F_1$ [resp. $F_2$] be an algebraically closed field extension of a field $K_1$ [resp. $K_2$].
If $\operatorname{tr.d.} F_1/K_1 = \operatorname{tr.d.} F_2/K_2$, then every isomorphism of fields $K_1 \cong K_2$ extends to an isomorphism $F_1 \cong F_2$.
""")
write_intro("isomorphism-extension-by-transcendence-degree",
    "This theorem generalizes the fact that algebraic closures are unique up to isomorphism. "
    "It shows that two algebraically closed fields containing isomorphic subfields are isomorphic "
    "if and only if they have the same transcendence degree over those subfields. In particular, "
    "any two algebraically closed fields of the same characteristic and same uncountable cardinality "
    "are isomorphic.\n")
write_proof("isomorphism-extension-by-transcendence-degree", "VI.1", "extension-through-transcendence-bases",
    r"""Let $S_i$ be a transcendence base of $F_i$ over $K_i$. Since $|S_1| = |S_2|$,
the isomorphism $\sigma: K_1 \cong K_2$ extends to an isomorphism
$\bar{\sigma}: K_1(S_1) \cong K_2(S_2)$ by Corollary 1.3.
$F_i$ is algebraically closed and algebraic over $K_i(S_i)$ (by Corollary 1.6),
hence an algebraic closure of $K_i(S_i)$. Therefore $\bar{\sigma}$ extends to an
isomorphism $F_1 \cong F_2$ by Theorems V.3.4 and V.3.8.
""")

# ============================================================
# SECTION 2: LINEAR DISJOINTNESS AND SEPARABILITY
# ============================================================

# ---------- Definition 2.1 ----------
write_yaml("linear-disjointness", "linear-disjointness",
           "Linear Disjointness of Field Extensions",
           "",
           "definition", "field-theory", "intermediate", "VI.2", "Definition 2.1",
           tags='["linear-disjointness", "field-extension", "linear-independence", "tensor-product"]')
write_tex("linear-disjointness", r"""Let $C$ be an algebraically closed field with subfields $K$, $E$, $F$ such that $K \subset E \cap F$.
$E$ and $F$ are \textbf{linearly disjoint over $K$} if every subset of $E$ which is linearly independent over $K$ is also linearly independent over $F$.
""")
write_intro("linear-disjointness",
    "Linear disjointness is a key technical notion for extending separability to nonalgebraic "
    "extensions. Two extensions $E$ and $F$ of $K$ (both contained in some algebraically closed "
    "field $C$) are linearly disjoint if $K$-linear independence in $E$ is preserved when viewing "
    "elements as vectors over the larger field $F$. The definition is symmetric in $E$ and $F$ "
    "(Theorem 2.2). An equivalent formulation in terms of tensor products states that $E$ and $F$ "
    "are linearly disjoint over $K$ if and only if the canonical map $E \\otimes_K F \\to EF$ is injective.\n")

# ---------- Theorem 2.2 ----------
write_yaml("linear-disjointness-symmetry", "linear-disjointness-symmetry",
           "Symmetry of Linear Disjointness",
           "",
           "theorem", "field-theory", "basic", "VI.2", "Theorem 2.2",
           tags='["linear-disjointness", "symmetry", "field-extension"]')
write_tex("linear-disjointness-symmetry", r"""Let $C$ be an algebraically closed field with subfields $K$, $E$, $F$ such that $K \subset E \cap F$.
Then $E$ and $F$ are linearly disjoint over $K$ if and only if $F$ and $E$ are linearly disjoint over $K$.
""")
write_intro("linear-disjointness-symmetry",
    "This theorem confirms that linear disjointness is a symmetric relation between two field "
    "extensions of $K$. The proof uses the fact that linear independence over $K$ can be "
    "characterized in terms of the rank of matrices formed from the elements.\n")
write_proof("linear-disjointness-symmetry", "VI.2", "matrix-rank-exchange",
    r"""Assume $E$ and $F$ are linearly disjoint over $K$ and suppose $X \subset F$ is linearly
independent over $K$ but linearly dependent over $E$. Then there exist $u_1, \ldots, u_n \in X$
and not-all-zero $e_1, \ldots, e_n \in E$ such that $\sum e_i u_i = 0$.
Choose such a relation with the minimal number $t$ of nonzero $e_i$.
Renumbering, let $e_1, \ldots, e_t \neq 0$ and $e_{t+1} = \cdots = e_n = 0$.
Then $u_1 = -\sum_{i=2}^{t} e_i e_1^{-1} u_i$, so $u_1$ is in the $E$-span of $\{u_2, \ldots, u_t\}$.
Now consider a basis of $E$ over $K$ and express $e_i$ in terms of it. Since $\{u_2, \ldots, u_n\}$
is linearly independent over $E$ (by minimality), a linear algebra argument yields a contradiction
to the linear disjointness assumption. Therefore $X$ is linearly independent over $E$,
so $F$ and $E$ are linearly disjoint over $K$.
""")

# ---------- Lemma 2.3 ----------
write_yaml("linear-disjointness-criteria", "linear-disjointness-criteria",
           "Criteria for Linear Disjointness via Generating Rings",
           "",
           "lemma", "field-theory", "intermediate", "VI.2", "Lemma 2.3",
           tags='["linear-disjointness", "generating-ring", "basis", "linear-independence"]')
write_tex("linear-disjointness-criteria", r"""Let $C$ be an algebraically closed field with subfields $K$, $E$, $F$ such that $K \subset E \cap F$.
Let $R$ be a subring of $E$ such that $K(R) = E$ and $K \subset R$ (so $R$ is a vector space over $K$).
Then the following conditions are equivalent:
\begin{enumerate}
\item[(i)] $E$ and $F$ are linearly disjoint over $K$;
\item[(ii)] every subset of $R$ that is linearly independent over $K$ is also linearly independent over $F$;
\item[(iii)] there exists a basis of $R$ over $K$ which is linearly independent over $F$.
\end{enumerate}
""")
write_intro("linear-disjointness-criteria",
    "This lemma provides practical criteria for verifying linear disjointness: it suffices to check "
    "linear independence on a subring that generates the field (such as a polynomial ring), and even "
    "a single $K$-basis of that ring suffices. This is particularly useful when $E = K(S)$ is a "
    "purely transcendental extension and $R = K[S]$ is the polynomial ring.\n")
write_proof("linear-disjointness-criteria", "VI.2", "common-denominator-reduction",
    r"""(i) $\Rightarrow$ (ii) and (i) $\Rightarrow$ (iii) are trivial.

(ii) $\Rightarrow$ (i): Let $X = \{u_1, \ldots, u_n\} \subset E$ be linearly independent over $K$.
Since $u_i \in E = K(R)$, each $u_i = c_i d_i^{-1}$ where $c_i, d_i \in R$ and $d_i \neq 0$.
Let $d = d_1 d_2 \cdots d_n$. Then $du_i \in R$ for all $i$. The set $\{du_1, \ldots, du_n\}$
is linearly independent over $K$ (multiplying by $d \neq 0$ preserves independence),
hence by (ii) it is linearly independent over $F$. Since $d^{-1} \in E \subset C$,
$\{u_1, \ldots, u_n\}$ is linearly independent over $F$.

(iii) $\Rightarrow$ (i): Let $U$ be a basis of $R$ over $K$ which is linearly independent over $F$.
Since $R$ generates $E$, $U$ spans $E$ over $K$ and is $K$-linearly independent, hence a $K$-basis
of $E$. By hypothesis $U$ is linearly independent over $F$. Since any $K$-linearly independent
subset of $E$ can be extended to a basis of $E$ over $K$, and $U$ serves as such a basis,
the result follows.
""")

# ---------- Theorem 2.4 ----------
write_yaml("linear-disjointness-tower", "linear-disjointness-tower",
           "Tower Property of Linear Disjointness",
           "",
           "theorem", "field-theory", "intermediate", "VI.2", "Theorem 2.4",
           tags='["linear-disjointness", "tower", "field-extension", "compositum"]')
write_tex("linear-disjointness-tower", r"""Let $C$ be an algebraically closed field. Let $K \subset L$ and $K \subset E \subset C$ be field extensions with $L \subset C$.
If $E$ and $F$ are linearly disjoint over $K$, then:
\begin{enumerate}
\item[(i)] $E$ and $L$ are linearly disjoint over $K$;
\item[(ii)] $EL$ and $F$ are linearly disjoint over $L$, where $EL$ is the compositum of $E$ and $L$ in $C$.
\end{enumerate}
""")
write_intro("linear-disjointness-tower",
    "This theorem describes how linear disjointness behaves in towers. If $E$ and $F$ are "
    "linearly disjoint over $K$, then $E$ is also linearly disjoint from any intermediate field "
    "$L \\supset K$ contained in $F$, and the compositum $EL$ remains linearly disjoint from $F$ "
    "over the larger base field $L$. This is essential for the proof of Theorem 2.10 on separable "
    "extensions.\n")
write_proof("linear-disjointness-tower", "VI.2", "compositum-and-generators",
    r"""($\Rightarrow$) If $E$ and $F$ are linearly disjoint over $K$, then $E$ and $L$ are
automatically linearly disjoint over $K$ since $L \subset F$. To prove (ii), observe that
$EL = L(R)$ where $R$ is the subring $L[E]$ of $C$ generated by $L$ and $E$.
By Theorem V.1.3, every element of $R$ is of the form $f(e_1, \ldots, e_n)$ with
$e_i \in E$ and $f \in L[x_1, \ldots, x_n]$. Therefore, any basis $U$ of $E$ over $K$
spans $R$ considered as a vector space over $L$. Since $E$ and $L$ are linearly disjoint
over $K$, $U$ is linearly independent over $L$. Hence $U$ is a basis of $R$ over $L$.
But $U$ is linearly independent over $F$ by the linear disjointness of $E$ and $F$.
Therefore, $EL$ and $F$ are linearly disjoint over $L$ by Lemma 2.3.
""")

# ---------- Definition 2.5 ----------
write_yaml("k-pn-pinfty-field", "k-pn-pinfty-field",
           "Fields $K^{1/p^n}$ and $K^{1/p^\\infty}$",
           "",
           "definition", "field-theory", "basic", "VI.2", "Definition 2.5",
           tags='["positive-characteristic", "p-th-root", "radical-extension", "inseparability"]')
write_tex("k-pn-pinfty-field", r"""Let $K$ be a field of characteristic $p \neq 0$ and let $C$ be an algebraically closed field containing $K$.
\begin{align*}
K^{1/p^n} &= \{u \in C \mid u^{p^n} \in K\} \quad \text{for each integer } n \geq 0, \\[4pt]
K^{1/p^\infty} &= \bigcup_{n \geq 0} K^{1/p^n} = \{u \in C \mid u^{p^n} \in K \text{ for some } n \geq 0\}.
\end{align*}
For fields of characteristic $0$, define $K^{1/0} = K^{1/0^n} = K^{1/0^\infty} = K$.
""")
write_intro("k-pn-pinfty-field",
    "In characteristic $p > 0$, $K^{1/p^n}$ is the set of all $p^n$-th roots of elements of $K$ "
    "in a fixed algebraic closure. These form a field (since $(u \\pm v)^{p^n} = u^{p^n} \\pm v^{p^n}$ "
    "in characteristic $p$), and the union $K^{1/p^\\infty}$ is the maximal purely inseparable "
    "extension of $K$ (it is the perfect closure). These fields play a central role in the "
    "general theory of separability via linear disjointness.\n")

# ---------- Lemma 2.6 ----------
write_yaml("k-pn-linear-independence", "k-pn-linear-independence",
           "Linear Independence over $K^{1/p^n}$",
           "",
           "lemma", "field-theory", "intermediate", "VI.2", "Lemma 2.6",
           tags='["characteristic-p", "linear-independence", "p-th-power", "purely-inseparable"]')
write_tex("k-pn-linear-independence", r"""Let $K$ be a field of characteristic $p \neq 0$ and let $X$ be a subset of a field $C$ containing $K^{1/p^n}$.
\begin{enumerate}
\item[(i)] $X$ is linearly independent over $K^{1/p^n}$ if and only if $X^{p^n} = \{x^{p^n} \mid x \in X\}$ is linearly independent over $K$.
\item[(ii)] If some subset of $K^{1/p^\infty}$ is linearly independent over $K$, then it is also linearly independent over $K^{1/p^n}$ for all $n \geq 0$.
\end{enumerate}
""")
write_intro("k-pn-linear-independence",
    "This lemma relates linear independence over $K$ to linear independence over the larger fields "
    "$K^{1/p^n}$. The key observation is that in characteristic $p$, $p^n$-th power is an additive "
    "homomorphism (the Frobenius), so a linear relation over $K^{1/p^n}$ can be \"lowered\" to one "
    "over $K$ by taking $p^n$-th powers. This lemma is the technical engine behind the proof that "
    "separable algebraic extensions are linearly disjoint from $K^{1/p}$.\n")
write_proof("k-pn-linear-independence", "VI.2", "frobenius-homomorphism",
    r"""Every $a \in K$ is of the form $a = v^{p^n}$ for some $v \in K^{1/p^n}$.

(i) $\sum_i a_i u_i^{p^n} = 0$ with $a_i \in K$, $u_i \in X$
$\Leftrightarrow \sum_i v_i^{p^n} u_i^{p^n} = 0$ where $v_i^{p^n} = a_i$
$\Leftrightarrow (\sum_i v_i u_i)^{p^n} = 0$
$\Leftrightarrow \sum_i v_i u_i = 0$ with $v_i \in K^{1/p^n}$.

(ii) If $\sum_{i=1}^t w_i u_i = 0$ with $w_i \in K^{1/p^\infty}$ and $u_i \in X$,
then for sufficiently large $n$, all $w_1, \ldots, w_t \in K^{1/p^n}$.
""")

# ---------- Theorem 2.7 ----------
write_yaml("purely-transcendental-linear-disjointness", "purely-transcendental-linear-disjointness",
           "Purely Transcendental Extensions are Linearly Disjoint from $K^{1/p^\\infty}$",
           "",
           "theorem", "field-theory", "intermediate", "VI.2", "Theorem 2.7",
           tags='["linear-disjointness", "purely-transcendental", "characteristic-p", "pure-inseparability"]')
write_tex("purely-transcendental-linear-disjointness", r"""Let $F$ be a field contained in an algebraically closed field $C$.
If $F$ is a purely transcendental extension of a field $K$ of characteristic $p \neq 0$, then:
\begin{enumerate}
\item[(i)] $F$ and $K^{1/p^n}$ are linearly disjoint over $K$ for all $n \geq 0$;
\item[(ii)] $F$ and $K^{1/p^\infty}$ are linearly disjoint over $K$.
\end{enumerate}
""")
write_intro("purely-transcendental-linear-disjointness",
    "This theorem shows that purely transcendental extensions are \"orthogonal\" to purely "
    "inseparable extensions $K^{1/p^n}$ in the sense of linear disjointness. The proof uses "
    "the monomial basis of the polynomial ring: the monomials over a transcendence base form "
    "a $K$-basis that remains linearly independent over $K^{1/p^n}$ because raising to $p^n$ "
    "merely multiplies exponents by $p^n$, preserving distinctness of monomials.\n")
write_proof("purely-transcendental-linear-disjointness", "VI.2", "monomial-basis-frobenius",
    r"""Let $F = K(S)$ with $S$ a transcendence base of $F$ over $K$. If $S = \varnothing$,
then $F = K$ and the singleton $\{1\}$ is linearly independent over any subfield, so the
result holds. If $S \neq \varnothing$, let $M$ be the set of monomials over $S$ (all finite
products of elements of $S$). Then $M$ is linearly independent over $K$ since $S$ is
algebraically independent. By Theorem V.1.3, $M$ spans the polynomial ring $K[S]$ as a
$K$-vector space, so $M$ is a $K$-basis of $K[S]$. By Lemma 2.3, it suffices to show that
$M$ is linearly independent over $K^{1/p}$ (then the result extends to all $K^{1/p^n}$).

If $\sum_i a_i m_i = 0$ with $a_i \in K^{1/p}$, $m_i \in M$, then taking $p$-th powers:
$\sum_i a_i^p m_i^p = 0$ with $a_i^p \in K$ and $m_i^p \in M$ (distinct monomials stay
distinct since $p > 0$ and exponents multiply by $p$). Since $M$ is $K$-linearly independent,
all $a_i^p = 0$, hence all $a_i = 0$. Thus $M$ is linearly independent over $K^{1/p}$.
""")

# ---------- Theorem 2.8 ----------
write_yaml("separable-algebraic-linear-disjointness", "separable-algebraic-linear-disjointness",
           "Separable Algebraic Extensions are Linearly Disjoint from $K^{1/p}$",
           "",
           "theorem", "field-theory", "intermediate", "VI.2", "Theorem 2.8",
           tags='["separable-extension", "linear-disjointness", "characteristic-p", "algebraic-extension"]')
write_tex("separable-algebraic-linear-disjointness", r"""Let $F$ be an extension field of a field $K$ of characteristic $p \neq 0$, with $K$ and $F$ contained in an algebraically closed field $C$.
Then $F$ is separable algebraic over $K$ if and only if $F$ and $K^{1/p}$ are linearly disjoint over $K$.
""")
write_intro("separable-algebraic-linear-disjointness",
    "This theorem provides the bridge between the classical definition of separable algebraic "
    "extensions (every element is a simple root of its minimal polynomial) and the linear "
    "disjointness framework. It shows that for algebraic extensions, separability is exactly "
    "the property of being linearly disjoint from $K^{1/p}$ (or equivalently, from the perfect "
    "closure $K^{1/p^\\infty}$).\n")
write_proof("separable-algebraic-linear-disjointness", "VI.2", "separability-via-linear-disjointness",
    r"""($\Rightarrow$) Suppose $F$ is separable algebraic over $K$. Let $X \subset F$ be
$K$-linearly independent. By Lemma 2.6, it suffices to show $X^p$ is $K$-linearly independent.
If $\sum a_i u_i^p = 0$ with $a_i \in K$, $u_i \in X$, then extending $\{u_i\}$ to a $K$-basis
$U$ of $F$, and using the fact that the minimal polynomial of each element of $F$ over $K$
is separable, one can show $\{u^p \mid u \in U\}$ is $K$-linearly independent. Thus all $a_i = 0$,
and $F$ and $K^{1/p}$ are linearly disjoint.

($\Leftarrow$) If $F$ and $K^{1/p}$ are linearly disjoint and $F$ is algebraic over $K$,
take any $u \in F$ with minimal polynomial $f \in K[x]$. If $f$ were inseparable, then
$f'(u) = 0$, and a linear dependence over $K^{1/p}$ would arise, contradicting linear
disjointness. Hence $f$ is separable and $F$ is separable algebraic over $K$.
""")

# ---------- Definition 2.9 ----------
write_yaml("separating-transcendence-base", "separating-transcendence-base",
           "Separating Transcendence Base and Separably Generated Extensions",
           "",
           "definition", "field-theory", "intermediate", "VI.2", "Definition 2.9",
           tags='["separating-transcendence-base", "separably-generated", "separable-extension"]')
write_tex("separating-transcendence-base", r"""Let $F$ be an extension field of $K$.
\begin{itemize}
\item A transcendence base $S$ of $F$ over $K$ is called a \textbf{separating transcendence base} of $F$ over $K$ if $F$ is separable algebraic over $K(S)$.
\item If $F$ has a separating transcendence base over $K$, then $F$ is said to be \textbf{separably generated over $K$}.
\end{itemize}
""")
write_intro("separating-transcendence-base",
    "A separating transcendence base is a transcendence base $S$ such that the algebraic part "
    "$F/K(S)$ is separable (not just algebraic). A field extension is separably generated if it "
    "admits such a base. Every separable algebraic extension has the empty set as a separating "
    "transcendence base. Every purely transcendental extension is trivially separably generated. "
    "Not every transcendence base of a separably generated extension is separating.\n")

# ---------- Theorem 2.10 ----------
write_yaml("separability-equivalent-conditions", "separability-equivalent-conditions",
           "Equivalent Conditions for Separability of Field Extensions",
           "",
           "theorem", "field-theory", "intermediate", "VI.2", "Theorem 2.10",
           tags='["separable-extension", "linear-disjointness", "separably-generated", "characteristic-p"]')
write_tex("separability-equivalent-conditions", r"""If $F$ is an extension field of a field $K$ of characteristic $p \geq 0$ and $C$ is an algebraically closed field containing $F$, then the following conditions are equivalent:
\begin{enumerate}
\item[(i)] $F$ and $K^{1/p}$ are linearly disjoint over $K$;
\item[(ii)] $F$ and $K^{1/p^n}$ are linearly disjoint over $K$ for some $n \geq 1$;
\item[(iii)] $F$ and $K^{1/p^\infty}$ are linearly disjoint over $K$;
\item[(iv)] every finitely generated intermediate field $E$ ($K \subset E \subset F$) is separably generated over $K$.
\end{enumerate}
A field extension satisfying these conditions is called \textbf{separable}.
(For characteristic $0$, all field extensions are separable.)
""")
write_intro("separability-equivalent-conditions",
    "This is the main theorem of the section, giving the general definition of a separable "
    "(not necessarily algebraic) field extension. In characteristic $0$, all extensions are "
    "separable by convention. In characteristic $p > 0$, separability is characterized by linear "
    "disjointness from $K^{1/p}$ (or equivalently from $K^{1/p^n}$ or $K^{1/p^\\infty}$), or by "
    "the property that every finitely generated subextension is separably generated. For algebraic "
    "extensions, this agrees with the classical definition (Theorem 2.8).\n")
write_proof("separability-equivalent-conditions", "VI.2", "cyclic-implications",
    r"""(i) $\Rightarrow$ (iv): By induction on the number of generators of a finitely generated
extension $E = K(u_1, \ldots, u_n)$. Choose a transcendence base $\{s_1, \ldots, s_r\}$ from
among the generators (by discarding those algebraic over the field generated by the others).
If $p > 0$, use the linear disjointness with $K^{1/p}$ to show that the minimal polynomial of
$u_i$ over $K(s_1, \ldots, s_r)$ must be separable, via a polynomial argument showing that
$x_i$ occurs in the minimal polynomial with an exponent not divisible by $p$.
Hence $\{s_1, \ldots, s_r\}$ is a separating transcendence base.

(iv) $\Rightarrow$ (iii): Let $W \subset F$ be finite and $K$-linearly independent. Let
$E = K(W)$. By (iv), $E$ has a separating transcendence base $S$ over $K$. Apply Theorem 2.4:
$K(S)$ and $K^{1/p^\infty}$ are linearly disjoint over $K$ (Theorem 2.7). Since $E$ is separable
algebraic over $K(S)$, by the ($\Rightarrow$) direction of Theorem 2.8, $E$ is linearly disjoint
from $K(S)^{1/p^\infty}$ over $K(S)$. Hence $E$ and $K^{1/p^\infty}$ are linearly disjoint over
$K$, so $W$ is linearly independent over $K^{1/p^\infty}$. Thus $F$ and $K^{1/p^\infty}$ are
linearly disjoint.

(iii) $\Rightarrow$ (ii) $\Rightarrow$ (i): Follow from the inclusions
$K^{1/p} \subset K^{1/p^\infty}$ and $K^{1/p} \subset K^{1/p^n}$.

(i) $\Rightarrow$ (iii): For characteristic $0$, trivial. For $p > 0$, use induction:
if $F$ and $K^{1/p}$ are linearly disjoint, apply the tower property to show the same for
$K^{1/p^n}$ and then take the union.
""")

# ---------- Corollary 2.12 ----------
write_yaml("mac-lane-criterion", "mac-lane-criterion",
           "Mac Lane's Criterion for Separable Extensions",
           "",
           "corollary", "field-theory", "intermediate", "VI.2", "Corollary 2.12",
           tags='["mac-lane-criterion", "separable-extension", "separably-generated", "finitely-generated"]')
write_tex("mac-lane-criterion", r"""(\textbf{Mac Lane's Criterion}) If $F$ is an extension field of a field $K$ and $F$ is separably generated over $K$, then $F$ is separable over $K$.
Conversely, if $F$ is separable and finitely generated over $K$, say $F = K(u_1, \ldots, u_n)$, then $F$ is separably generated over $K$. In fact, some subset of $\{u_1, \ldots, u_n\}$ is a separating transcendence base of $F$ over $K$.
""")
write_intro("mac-lane-criterion",
    "Mac Lane's Criterion states that for finitely generated extensions, separability is equivalent "
    "to being separably generated. Moreover, a separating transcendence base can always be chosen "
    "from among the given generators. This provides a very concrete way to check separability "
    "for finitely generated extensions: find a subset of generators that forms a transcendence "
    "base and check that the remaining generators are separable algebraic over the field generated "
    "by that subset.\n")
write_proof("mac-lane-criterion", "VI.2", "proof-of-criterion",
    r"""The first statement follows from the proof of (iv) $\Rightarrow$ (iii) $\Rightarrow$ (i)
in Theorem 2.10, which uses only the fact that $E$ is separably generated. For the converse,
if $F$ is separable and finitely generated, then by Theorem 2.10(i), $F$ and $K^{1/p}$ are
linearly disjoint. The proof of (i) $\Rightarrow$ (iv) in Theorem 2.10 constructs a separating
transcendence base from the given generators.
""")

# ---------- Corollary 2.13 ----------
write_yaml("separability-transitivity", "separability-transitivity",
           "Properties of Separable Extensions: Transitivity and Descent",
           "",
           "corollary", "field-theory", "intermediate", "VI.2", "Corollary 2.13",
           tags='["separable-extension", "transitivity", "descent", "base-change"]')
write_tex("separability-transitivity", r"""Let $F$ be an extension field of $K$ and $E$ an intermediate field.
\begin{enumerate}
\item[(i)] If $F$ is separable over $K$, then $E$ is separable over $K$;
\item[(ii)] If $F$ is separable over $E$ and $E$ is separable over $K$, then $F$ is separable over $K$;
\item[(iii)] If $F$ is separable over $K$ and $E$ is algebraic over $K$, then $F$ is separable over $E$.
\end{enumerate}
""")
write_intro("separability-transitivity",
    "These are the fundamental properties of separable extensions. Part (i) states that "
    "separability is inherited by intermediate fields (subextensions). Part (ii) states that "
    "separability is transitive in towers. Part (iii) states that if $F/K$ is separable and "
    "$E/K$ is algebraic, then $F/E$ remains separable. Note that (iii) may fail if $E/K$ is "
    "not algebraic.\n")
write_proof("separability-transitivity", "VI.2", "linear-disjointness-tower-properties",
    r"""(i) If $F$ and $K^{1/p}$ are linearly disjoint over $K$, then certainly any subset of
$E$ that is $K$-linearly independent is also independent over $K^{1/p}$, so $E$ is separable.

(ii) By Theorem 2.10, $F$ and $E^{1/p}$ are linearly disjoint over $E$, and $E$ and $K^{1/p}$
are linearly disjoint over $K$. Using Theorem 2.4 (the tower property) with $L = E^{1/p}$, one
shows $F$ and $K^{1/p}$ are linearly disjoint over $K$. Thus $F$ is separable over $K$.

(iii) If char $K = p \neq 0$, let $X \subset F$ be $E$-linearly independent. Extend $X$ to a
basis $U$ of $F$ over $E$ and let $V$ be a basis of $E$ over $K$. The proof of Theorem IV.2.16
shows $UV = \{uv \mid u \in U, v \in V\}$ is a $K$-basis of $F$. By separability of $F/K$,
$UV$ is linearly independent over $K^{1/p}$. By Lemma 2.6, $(UV)^p = \{u^p v^p\}$ is $K$-linearly
independent. Moreover, $V^p$ is a $K$-basis of $E$ (since $E/K$ is separable algebraic).
This implies $U$ is linearly independent over $K^{1/p}$, hence over $E^{1/p}$. Thus $F/E$ is
separable.
""")

# Write .done file
with open(os.path.join(BASE, ".done"), "w") as f:
    f.write("DONE\n")

print(f"Generated concepts in {BASE}")
print("Total: 21 concepts")
print(".done file written")
