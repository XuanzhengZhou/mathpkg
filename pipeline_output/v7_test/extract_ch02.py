#!/usr/bin/env python3
"""Extract all concepts from GTM073 Chapter II into v7 staging format."""
import os
import json

STAGING = "/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/gtm-0073/gtm-0073_ch02_concepts"
ROLE = "gtm-0073"
AUTHOR = "Hungerford, Thomas W."
TITLE = "Algebra"
DATE = "2026-06-24"
AGENT = "v7-gtm073"

# ─── Section info ───
SECTIONS = {
    "II.1": "Free Abelian Groups",
    "II.2": "Finitely Generated Abelian Groups",
    "II.3": "The Krull-Schmidt Theorem",
    "II.4": "The Action of a Group on a Set",
    "II.5": "The Sylow Theorems",
    "II.6": "Classification of Finite Groups",
    "II.7": "Nilpotent and Solvable Groups",
    "II.8": "Normal and Subnormal Series",
}


def source(sec, role):
    return [{
        "book_id": ROLE,
        "author": AUTHOR,
        "title": TITLE,
        "chapter": "II",
        "section": sec,
        "pages": "",
        "role_in_book": role,
    }]


def write_concept(slug, title_en, ctype, subdomain, difficulty, sec, role_name,
                  latex, introduce, proof_text=None, proof_deps=None,
                  depends_on=None, tags=None, title_zh=""):
    folder = os.path.join(STAGING, slug)
    os.makedirs(folder, exist_ok=True)

    # concept.yaml
    yaml_lines = [
        f"id: {slug}",
        f'title_en: "{title_en}"',
        f'title_zh: "{title_zh}"',
        f"type: {ctype}",
        "domain: algebra",
        f"subdomain: {subdomain}",
        f"difficulty: {difficulty}",
        f"tags: {json.dumps(tags or [])}",
    ]
    if depends_on:
        yaml_lines.append(f"depends_on:")
        for k in ["required", "recommended", "suggested"]:
            items = depends_on.get(k, [])
            yaml_lines.append(f"  {k}: {json.dumps(items)}")
    else:
        yaml_lines.append("depends_on:")
        yaml_lines.append("  required: []")
        yaml_lines.append("  recommended: []")
        yaml_lines.append("  suggested: []")
    yaml_lines.append(f"proof_deps: {json.dumps(proof_deps or {})}")
    yaml_lines.append("source_books:")
    for s in source(sec, role_name):
        yaml_lines.append(f"  - book_id: {s['book_id']}")
        yaml_lines.append(f'    author: "{s["author"]}"')
        yaml_lines.append(f'    title: "{s["title"]}"')
        yaml_lines.append(f'    chapter: "{s["chapter"]}"')
        yaml_lines.append(f'    section: "{s["section"]}"')
        yaml_lines.append(f'    pages: "{s["pages"]}"')
        yaml_lines.append(f'    role_in_book: "{s["role_in_book"]}"')
    yaml_lines.append('content_hash: ""')
    yaml_lines.append(f"extraction_date: \"{DATE}\"")
    yaml_lines.append(f"extraction_agent: \"{AGENT}\"")
    with open(os.path.join(folder, "concept.yaml"), "w") as f:
        f.write("\n".join(yaml_lines) + "\n")

    # theorem.tex
    with open(os.path.join(folder, "theorem.tex"), "w") as f:
        f.write(latex.strip() + "\n")

    # introduce.en.md
    intro_md = f"""---
role: introduce
locale: en
content_hash: ""
written_against: ""
---
{introduce.strip()}
"""
    with open(os.path.join(folder, "introduce.en.md"), "w") as f:
        f.write(intro_md)

    # proof file (if proof_text provided)
    if proof_text:
        technique = proof_deps.get("technique", "direct") if proof_deps else "direct"
        proof_fn = f"proof_{ROLE}_II_{slug}.en.md"
        proof_md = f"""---
role: proof
source_book: {ROLE}
chapter: II
section: "{sec}"
proof_technique: {technique}
locale: en
content_hash: ""
written_against: ""
---
{proof_text.strip()}
"""
        with open(os.path.join(folder, proof_fn), "w") as f:
            f.write(proof_md)

    print(f"  ✓ {slug}")


# ═══════════════════════════════════════════════════════════════
# SECTION 1: Free Abelian Groups
# ═══════════════════════════════════════════════════════════════

write_concept(
    "basis-of-an-abelian-group",
    "Basis of an Abelian Group",
    "definition", "group_theory", "basic", "II.1", "Definition (p.71)",
    r"""A basis of an abelian group $F$ is a subset $X$ of $F$ such that:
\begin{enumerate}
\item $F = \langle X \rangle$;
\item for distinct $x_1, x_2, \ldots, x_k \in X$ and $n_i \in \mathbb{Z}$,
$$n_1x_1 + n_2x_2 + \cdots + n_kx_k = 0 \Rightarrow n_i = 0 \text{ for every } i.$$
\end{enumerate}""",
    "A basis of an abelian group is a linearly independent generating set, analogous to a basis of a vector space but with integer coefficients."
)

write_concept(
    "characterization-of-free-abelian-groups",
    "Characterization of Free Abelian Groups",
    "theorem", "group_theory", "intermediate", "II.1", "Theorem 1.1",
    r"""The following conditions on an abelian group $F$ are equivalent:
\begin{enumerate}
\item[(i)] $F$ has a nonempty basis.
\item[(ii)] $F$ is the (internal) direct sum of a family of infinite cyclic subgroups.
\item[(iii)] $F$ is (isomorphic to) a direct sum of copies of the additive group $\mathbb{Z}$ of integers.
\item[(iv)] There exists a nonempty set $X$ and a function $\iota: X \to F$ with the following property: given an abelian group $G$ and function $f: X \to G$, there exists a unique homomorphism of groups $\bar{f}: F \to G$ such that $\bar{f}\iota = f$.
\end{enumerate}""",
    "An abelian group is free if and only if it has a nonempty basis, which is equivalent to being a direct sum of infinite cyclic groups, a direct sum of copies of Z, or a free object on a set in the category of abelian groups.",
    proof_deps={"technique": "constructive"}
)

write_concept(
    "invariance-of-rank-of-free-abelian-groups",
    "Invariance of Rank of Free Abelian Groups",
    "theorem", "group_theory", "intermediate", "II.1", "Theorem 1.2",
    r"""If $F$ is a free abelian group, then any two bases of $F$ have the same cardinality. This common cardinality is called the \emph{rank} of $F$. More generally, if $F$ is free abelian with an infinite basis $X$, then every basis of $F$ has the same cardinality as $X$.""",
    "Any two bases of a free abelian group have the same cardinality, called the rank of the group. This is analogous to the dimension of a vector space.",
    proof_deps={"technique": "cardinality-argument"}
)

write_concept(
    "free-abelian-groups-isomorphic-iff-same-rank",
    "Free Abelian Groups: Isomorphic iff Same Rank",
    "proposition", "group_theory", "basic", "II.1", "Proposition 1.3",
    r"""Let $F_1$ be the free abelian group on the set $X_1$ and $F_2$ the free abelian group on the set $X_2$. Then $F_1 \cong F_2$ if and only if $F_1$ and $F_2$ have the same rank (that is, $|X_1| = |X_2|$).""",
    "Two free abelian groups are isomorphic precisely when they have the same rank, i.e., bases of equal cardinality.",
    proof_deps={"technique": "basis-transport"}
)

write_concept(
    "every-abelian-group-is-homomorphic-image-of-free-abelian-group",
    "Every Abelian Group is Homomorphic Image of a Free Abelian Group",
    "theorem", "group_theory", "intermediate", "II.1", "Theorem 1.4",
    r"""Every abelian group $G$ is the homomorphic image of a free abelian group of rank $|X|$, where $X$ is a set of generators of $G$.""",
    "Every abelian group can be expressed as a quotient of a free abelian group whose rank equals the cardinality of a generating set.",
    proof_deps={"technique": "universal-property"}
)

write_concept(
    "basis-transformation-in-free-abelian-groups",
    "Basis Transformation in Free Abelian Groups",
    "lemma", "group_theory", "basic", "II.1", "Lemma 1.5",
    r"""If $\{x_1, \ldots, x_n\}$ is a basis of a free abelian group $F$ and $a \in \mathbb{Z}$, then for all $i \neq j$,
$$\{x_1, \ldots, x_{j-1}, x_j + ax_i, x_{j+1}, \ldots, x_n\}$$
is also a basis of $F$.""",
    "In a free abelian group, replacing a basis element by itself plus an integer multiple of another basis element yields another basis.",
    proof_deps={"technique": "elementary-transformation"}
)

write_concept(
    "structure-of-subgroups-of-free-abelian-groups",
    "Structure of Subgroups of Free Abelian Groups",
    "theorem", "group_theory", "advanced", "II.1", "Theorem 1.6",
    r"""If $F$ is a free abelian group of rank $n$ and $G$ is a nonzero subgroup of $F$, then there exists a basis $\{x_1, \ldots, x_n\}$ of $F$, an integer $r$ $(1 \leq r \leq n)$, and positive integers $d_1, \ldots, d_r$ such that $d_1 \mid d_2 \mid \cdots \mid d_r$ and $G$ is isomorphic to the free abelian group with basis $\{d_1x_1, \ldots, d_rx_r\}$. In particular, $G$ is free of rank $r \leq n$.""",
    "Every subgroup of a finitely generated free abelian group is itself free abelian, with a basis whose elements are integer multiples of a basis of the containing group arranged in a divisibility chain.",
    proof_deps={"technique": "induction-and-division-algorithm"}
)

# ═══════════════════════════════════════════════════════════════
# SECTION 2: Finitely Generated Abelian Groups
# ═══════════════════════════════════════════════════════════════

write_concept(
    "invariant-factor-decomposition",
    "Invariant Factor Decomposition of Finitely Generated Abelian Groups",
    "theorem", "group_theory", "advanced", "II.2", "Theorem 2.1",
    r"""Every finitely generated abelian group $G$ is (isomorphic to) a finite direct sum of cyclic groups in which the finite cyclic summands (if any) are of orders $m_1, \ldots, m_t$, where $m_1 > 1$ and
$$m_1 \mid m_2 \mid \cdots \mid m_t.$$
That is,
$$G \cong \mathbb{Z} \oplus \cdots \oplus \mathbb{Z} \oplus \mathbb{Z}_{m_1} \oplus \cdots \oplus \mathbb{Z}_{m_t}.$$""",
    "Every finitely generated abelian group decomposes uniquely into a direct sum of infinite cyclic groups and finite cyclic groups whose orders form a divisibility chain, called the invariant factors.",
    proof_deps={"technique": "structure-theorem-for-submodules"}
)

write_concept(
    "elementary-divisor-decomposition",
    "Elementary Divisor Decomposition of Finitely Generated Abelian Groups",
    "theorem", "group_theory", "advanced", "II.2", "Theorem 2.2",
    r"""Every finitely generated abelian group $G$ is (isomorphic to) a finite direct sum of cyclic groups, each of which is either infinite or of order a power of a prime. That is,
$$G \cong \mathbb{Z} \oplus \cdots \oplus \mathbb{Z} \oplus \mathbb{Z}_{p_1^{n_1}} \oplus \cdots \oplus \mathbb{Z}_{p_k^{n_k}}$$
where the $p_i$ are primes (not necessarily distinct) and $n_i > 0$. The prime powers $p_i^{n_i}$ are called the \emph{elementary divisors} of $G$.""",
    "Every finitely generated abelian group decomposes into a direct sum of infinite cyclic groups and cyclic groups of prime power order, with uniqueness up to isomorphism.",
    proof_deps={"technique": "primary-decomposition"}
)

write_concept(
    "decomposition-of-cyclic-group-by-coprime-orders",
    "Decomposition of Cyclic Group by Coprime Orders",
    "lemma", "group_theory", "basic", "II.2", "Lemma 2.3",
    r"""If $m$ is a positive integer and $m = p_1^{n_1}p_2^{n_2}\cdots p_t^{n_t}$ ($p_1, \ldots, p_t$ distinct primes and each $n_i > 0$), then
$$\mathbb{Z}_m \cong \mathbb{Z}_{p_1^{n_1}} \oplus \mathbb{Z}_{p_2^{n_2}} \oplus \cdots \oplus \mathbb{Z}_{p_t^{n_t}}.$$
More generally, $\mathbb{Z}_{rn} \cong \mathbb{Z}_r \oplus \mathbb{Z}_n$ whenever $(r,n) = 1$.""",
    "A cyclic group of composite order decomposes as a direct sum of cyclic groups of prime power orders, and more generally as a direct sum of cyclic groups of coprime orders.",
    proof_deps={"technique": "bezout-identity"}
)

write_concept(
    "subgroups-of-finite-abelian-groups",
    "Subgroups of Finite Abelian Groups of Every Divisor Order",
    "corollary", "group_theory", "basic", "II.2", "Corollary 2.4",
    r"""If $G$ is a finite abelian group of order $n$, then $G$ has a subgroup of order $m$ for every positive integer $m$ that divides $n$.""",
    "Every finite abelian group contains subgroups of every possible order dividing the group order, generalizing a property of cyclic groups.",
    proof_deps={"technique": "structure-decomposition"}
)

write_concept(
    "torsion-subgroup-and-p-primary-components",
    "Torsion Subgroup and p-Primary Components",
    "lemma", "group_theory", "intermediate", "II.2", "Lemma 2.5",
    r"""For an abelian group $G$, define:
\begin{itemize}
\item $G_t = \{g \in G \mid ng = 0 \text{ for some } n \in \mathbb{N}^*\}$, the \emph{torsion subgroup} of $G$;
\item $G(p) = \{g \in G \mid p^ng = 0 \text{ for some } n \geq 0\}$, the \emph{$p$-primary component} of $G$.
\end{itemize}
Then $G_t$ is a fully invariant subgroup of $G$, and $G(p)$ is a fully invariant subgroup of $G_t$. If $f: G \to H$ is a homomorphism, then $f(G_t) \subset H_t$ and $f(G(p)) \subset H(p)$. If $f$ is an isomorphism, these are equalities.""",
    "The torsion subgroup consists of all elements of finite order; the p-primary component consists of elements whose order is a power of p. Both are fully invariant and preserved by homomorphisms.",
    proof_deps={"technique": "order-arguments"}
)

write_concept(
    "uniqueness-of-invariant-factors-and-elementary-divisors",
    "Uniqueness of Invariant Factors and Elementary Divisors",
    "theorem", "group_theory", "advanced", "II.2", "Theorem 2.6",
    r"""Two finitely generated abelian groups are isomorphic if and only if they have the same rank and the same invariant factors (up to order). Equivalently, two finitely generated abelian groups are isomorphic if and only if they have the same rank and the same elementary divisors (up to order). The invariant factors $m_1, \ldots, m_t$ and the elementary divisors are uniquely determined by the group.""",
    "The invariant factors and elementary divisors are complete isomorphism invariants for finitely generated abelian groups, providing a full classification.",
    proof_deps={"technique": "p-primary-component-comparison"}
)

# ═══════════════════════════════════════════════════════════════
# SECTION 3: The Krull-Schmidt Theorem
# ═══════════════════════════════════════════════════════════════

write_concept(
    "indecomposable-group",
    "Indecomposable Group",
    "definition", "group_theory", "basic", "II.3", "Definition 3.1",
    r"""A group $G$ is \emph{indecomposable} if $G \neq \langle e \rangle$ and $G$ is not the (internal) direct product of two of its proper subgroups. Equivalently, $G \neq \langle e \rangle$ and $G \cong H \times K$ implies $H = \langle e \rangle$ or $K = \langle e \rangle$.""",
    "A nontrivial group is indecomposable if it cannot be expressed as a direct product of two proper subgroups. Every simple group is indecomposable, but not conversely."
)

write_concept(
    "ascending-and-descending-chain-conditions",
    "Ascending and Descending Chain Conditions on Normal Subgroups",
    "definition", "group_theory", "basic", "II.3", "Definition 3.2",
    r"""A group $G$ is said to satisfy the \emph{ascending chain condition} (ACC) on normal subgroups if for every chain $G_1 < G_2 < \cdots$ of normal subgroups of $G$ there is an integer $n$ such that $G_i = G_n$ for all $i \geq n$.

$G$ is said to satisfy the \emph{descending chain condition} (DCC) on normal subgroups if for every chain $G_1 > G_2 > \cdots$ of normal subgroups of $G$ there is an integer $n$ such that $G_i = G_n$ for all $i \geq n$.""",
    "The ACC prevents infinite strictly ascending chains of normal subgroups; the DCC prevents infinite strictly descending chains. Together they characterize groups with well-behaved normal subgroup lattices."
)

write_concept(
    "normal-endomorphism",
    "Normal Endomorphism",
    "definition", "group_theory", "intermediate", "II.3", "Definition (p.84)",
    r"""An endomorphism $f$ of a group $G$ is called a \emph{normal endomorphism} if
$$af(b)a^{-1} = f(aba^{-1}) \quad \text{for all } a, b \in G.$$""",
    "A normal endomorphism commutes with all inner automorphisms. Such endomorphisms play a crucial role in the proof of the Krull-Schmidt Theorem.",
)

write_concept(
    "normal-endomorphism-fittings-lemma",
    "Fitting's Lemma for Normal Endomorphisms",
    "lemma", "group_theory", "advanced", "II.3", "Lemma 3.4",
    r"""Let $f$ be a normal endomorphism of a group $G$ that satisfies both the ascending and descending chain conditions on normal subgroups. Then for some $n \geq 1$,
$$G = \operatorname{Ker} f^n \times \operatorname{Im} f^n.$$
In particular, $f$ restricted to $\operatorname{Im} f^n$ is an automorphism, and $f$ restricted to $\operatorname{Ker} f^n$ is nilpotent.""",
    "A normal endomorphism of a group with ACC and DCC on normal subgroups induces a direct product decomposition into its eventual kernel and eventual image, analogous to the Fitting decomposition for modules.",
    proof_deps={"technique": "chain-stabilization"}
)

write_concept(
    "krull-schmidt-theorem",
    "Krull-Schmidt Theorem",
    "theorem", "group_theory", "advanced", "II.3", "Theorem 3.8",
    r"""Let $G$ be a group that satisfies both the ascending and descending chain conditions on normal subgroups. If
$$G = G_1 \times G_2 \times \cdots \times G_s \quad \text{and} \quad G = H_1 \times H_2 \times \cdots \times H_t$$
are two decompositions of $G$ into indecomposable factors, then $s = t$ and (after reindexing) $G_i \cong H_i$ for all $i$. Moreover, for each $r < s$,
$$G = G_1 \times \cdots \times G_r \times H_{r+1} \times \cdots \times H_t.$$""",
    "The Krull-Schmidt Theorem states that a group satisfying both chain conditions on normal subgroups has a unique (up to isomorphism and order) decomposition into indecomposable direct factors, with the replacement property.",
    proof_deps={"technique": "normal-endomorphism-induction"}
)

# ═══════════════════════════════════════════════════════════════
# SECTION 4: Action of a Group on a Set
# ═══════════════════════════════════════════════════════════════

write_concept(
    "group-action-orbits-and-stabilizers",
    "Group Action: Orbits and Stabilizers",
    "theorem", "group_theory", "basic", "II.4", "Theorem 4.2",
    r"""Let $G$ be a group that acts on a set $S$.
\begin{enumerate}
\item[(i)] The relation on $S$ defined by
$$x \sim x' \iff gx = x' \quad \text{for some} \quad g \in G$$
is an equivalence relation.
\item[(ii)] For each $x \in S$, $G_x = \{g \in G \mid gx = x\}$ is a subgroup of $G$.
\end{enumerate}""",
    "The relation of being in the same orbit under a group action is an equivalence relation, and the stabilizer of each element forms a subgroup.",
    proof_deps={"technique": "direct-verification"}
)

write_concept(
    "orbit-stabilizer-theorem",
    "Orbit-Stabilizer Theorem",
    "corollary", "group_theory", "basic", "II.4", "Corollary 4.4",
    r"""Let $G$ be a group acting on a set $S$.
\begin{enumerate}
\item[(i)] For each $x \in S$, $|\bar{x}| = [G : G_x]$.
\item[(ii)] If $G$ is finite and $\bar{x}_1, \ldots, \bar{x}_n$ are the distinct conjugacy classes, then
$$|G| = \sum_{i=1}^{n} [G : C_G(x_i)].$$
\item[(iii)] The number of subgroups of $G$ conjugate to $K$ is $[G : N_G(K)]$, which divides $|G|$.
\end{enumerate}""",
    "The size of an orbit equals the index of the stabilizer. For conjugation actions this yields the class equation, and for subgroup conjugation it gives the number of conjugates of a subgroup.",
    proof_deps={"technique": "coset-counting"}
)

write_concept(
    "group-action-induces-permutation-homomorphism",
    "Group Action Induces Permutation Homomorphism",
    "theorem", "group_theory", "basic", "II.4", "Theorem 4.5",
    r"""If a group $G$ acts on a set $S$, then this action induces a homomorphism $G \to A(S)$, where $A(S)$ is the group of all permutations of $S$. The map is given by $g \mapsto \tau_g$, where $\tau_g(x) = gx$ for all $x \in S$.""",
    "Every group action corresponds to a homomorphism from the group to the symmetric group on the set, establishing the equivalence between group actions and permutation representations.",
    proof_deps={"technique": "map-verification"}
)

write_concept(
    "cayleys-theorem",
    "Cayley's Theorem",
    "corollary", "group_theory", "basic", "II.4", "Corollary 4.6",
    r"""If $G$ is a group, then there is a monomorphism $G \to A(G)$. Hence every group is isomorphic to a group of permutations. In particular, every finite group of order $n$ is isomorphic to a subgroup of $S_n$.""",
    "Every group embeds into the symmetric group on its underlying set, meaning every group is essentially a permutation group.",
    proof_deps={"technique": "left-translation-action"}
)

write_concept(
    "conjugation-action-and-inner-automorphisms",
    "Conjugation Action and Inner Automorphisms",
    "corollary", "group_theory", "basic", "II.4", "Corollary 4.7",
    r"""Let $G$ be a group.
\begin{enumerate}
\item[(i)] For each $g \in G$, the map $\tau_g: G \to G$ given by $x \mapsto gxg^{-1}$ is an automorphism of $G$.
\item[(ii)] The map $\tau: G \to \operatorname{Aut} G$ given by $g \mapsto \tau_g$ is a homomorphism with kernel $C(G)$, the center of $G$. Hence $G/C(G) \cong \operatorname{In} G$, the group of inner automorphisms.
\end{enumerate}""",
    "Conjugation by a fixed element is an automorphism. The map sending each element to its induced inner automorphism is a homomorphism whose kernel is the center of the group.",
    proof_deps={"technique": "homomorphism-verification"}
)

write_concept(
    "kernel-of-action-on-cosets",
    "Kernel of Action on Cosets",
    "proposition", "group_theory", "intermediate", "II.4", "Proposition 4.8",
    r"""Let $H$ be a subgroup of a group $G$ and let $G$ act on the set $S$ of all left cosets of $H$ in $G$ by left translation. Then the kernel of the induced homomorphism $G \to A(S)$ is contained in $H$.""",
    "When a group acts by left translation on the cosets of a subgroup, the kernel of the action is contained in that subgroup, making the action faithful on the quotient.",
    proof_deps={"technique": "kernel-analysis"}
)

write_concept(
    "subgroup-of-index-n-embeds-in-s-n",
    "Subgroup of Index n Embeds in S_n",
    "corollary", "group_theory", "intermediate", "II.4", "Corollary 4.9",
    r"""If $H$ is a subgroup of index $n$ in a group $G$ and no nontrivial normal subgroup of $G$ is contained in $H$, then $G$ is isomorphic to a subgroup of $S_n$.""",
    "A group with a subgroup of index n that contains no nontrivial normal subgroups embeds into the symmetric group S_n, a powerful tool for proving simplicity.",
    proof_deps={"technique": "coset-action"}
)

# ═══════════════════════════════════════════════════════════════
# SECTION 5: The Sylow Theorems
# ═══════════════════════════════════════════════════════════════

write_concept(
    "fixed-point-congruence-for-p-groups",
    "Fixed Point Congruence for p-Groups",
    "lemma", "group_theory", "intermediate", "II.5", "Lemma 5.1",
    r"""If a group $H$ of order $p^n$ ($p$ prime) acts on a finite set $S$ and if
$$S_0 = \{x \in S \mid hx = x \text{ for all } h \in H\},$$
then $|S| \equiv |S_0| \pmod{p}$.""",
    "For a p-group acting on a finite set, the total number of elements is congruent modulo p to the number of fixed points.",
    proof_deps={"technique": "orbit-decomposition"}
)

write_concept(
    "cauchys-theorem",
    "Cauchy's Theorem",
    "theorem", "group_theory", "intermediate", "II.5", "Theorem 5.2",
    r"""If $G$ is a finite group whose order is divisible by a prime $p$, then $G$ contains an element of order $p$.""",
    "Every finite group whose order is divisible by a prime p contains at least one element of order p.",
    proof_deps={"technique": "mckay-combinatorial"}
)

write_concept(
    "center-of-nontrivial-p-group",
    "Center of Nontrivial p-Group is Nontrivial",
    "corollary", "group_theory", "intermediate", "II.5", "Corollary 5.4",
    r"""The center $C(G)$ of a nontrivial finite $p$-group $G$ contains more than one element.""",
    "Every nontrivial finite p-group has a nontrivial center, a crucial fact for the study of p-groups and their nilpotency.",
    proof_deps={"technique": "class-equation"}
)

write_concept(
    "normalizer-index-congruence",
    "Normalizer Index Congruence for p-Subgroups",
    "lemma", "group_theory", "intermediate", "II.5", "Lemma 5.5",
    r"""If $H$ is a $p$-subgroup of a finite group $G$, then
$$[N_G(H) : H] \equiv [G : H] \pmod{p}.$$""",
    "The index of a p-subgroup in its normalizer is congruent modulo p to its index in the whole group, a key step toward the Sylow theorems.",
    proof_deps={"technique": "fixed-point-coset-action"}
)

write_concept(
    "normalizer-properly-contains-p-subgroup",
    "Normalizer Properly Contains p-Subgroup When p Divides Index",
    "corollary", "group_theory", "intermediate", "II.5", "Corollary 5.6",
    r"""If $H$ is a $p$-subgroup of a finite group $G$ such that $p$ divides $[G : H]$, then $N_G(H) \neq H$.""",
    "When p divides the index of a p-subgroup, the normalizer is strictly larger than the subgroup, forcing the existence of larger p-subgroups.",
    proof_deps={"technique": "congruence-argument"}
)

write_concept(
    "first-sylow-theorem",
    "First Sylow Theorem",
    "theorem", "group_theory", "advanced", "II.5", "Theorem 5.7",
    r"""Let $G$ be a finite group of order $p^n m$ with $p$ prime, $n \geq 1$, and $(m,p) = 1$. Then $G$ contains a subgroup of order $p^n$, called a \emph{Sylow $p$-subgroup} of $G$.""",
    "Every finite group has Sylow p-subgroups (subgroups of maximal prime power order) for each prime dividing the group order.",
    proof_deps={"technique": "induction-and-normalizer"}
)

write_concept(
    "sylow-p-subgroup-properties",
    "Properties of Sylow p-Subgroups",
    "corollary", "group_theory", "intermediate", "II.5", "Corollary 5.8",
    r"""Let $G$ be a group of order $p^n m$ with $p$ prime, $n \geq 1$ and $(m,p) = 1$. Let $H$ be a $p$-subgroup of $G$.
\begin{enumerate}
\item[(i)] $H$ is a Sylow $p$-subgroup of $G$ if and only if $|H| = p^n$.
\item[(ii)] Every conjugate of a Sylow $p$-subgroup is a Sylow $p$-subgroup.
\item[(iii)] If there is only one Sylow $p$-subgroup $P$, then $P$ is normal in $G$.
\end{enumerate}""",
    "Sylow p-subgroups are precisely the p-subgroups of maximal order; conjugates of Sylow subgroups are Sylow subgroups; uniqueness implies normality.",
    proof_deps={"technique": "lagrange-and-order"}
)

write_concept(
    "second-sylow-theorem",
    "Second Sylow Theorem",
    "theorem", "group_theory", "advanced", "II.5", "Theorem 5.9",
    r"""If $H$ is a $p$-subgroup of a finite group $G$, and $P$ is any Sylow $p$-subgroup of $G$, then there exists $x \in G$ such that $H < xPx^{-1}$. In particular, any two Sylow $p$-subgroups of $G$ are conjugate.""",
    "Every p-subgroup is contained in some conjugate of any given Sylow p-subgroup, implying that all Sylow p-subgroups are conjugate to one another.",
    proof_deps={"technique": "coset-action-fixed-points"}
)

write_concept(
    "third-sylow-theorem",
    "Third Sylow Theorem",
    "theorem", "group_theory", "advanced", "II.5", "Theorem 5.10",
    r"""Let $G$ be a finite group and $p$ a prime. The number $n_p$ of Sylow $p$-subgroups of $G$ satisfies:
\begin{enumerate}
\item $n_p \equiv 1 \pmod{p}$;
\item $n_p$ divides $|G|$.
\end{enumerate}
Furthermore, $n_p = [G : N_G(P)]$ for any Sylow $p$-subgroup $P$ of $G$.""",
    "The number of Sylow p-subgroups is congruent to 1 modulo p and divides the group order, providing strong constraints on group structure.",
    proof_deps={"technique": "conjugacy-and-counting"}
)

# ═══════════════════════════════════════════════════════════════
# SECTION 6: Classification of Finite Groups
# ═══════════════════════════════════════════════════════════════

write_concept(
    "groups-of-order-p-squared",
    "Groups of Order p^2 are Abelian",
    "proposition", "group_theory", "basic", "II.6", "Proposition 6.1",
    r"""If $p$ is prime, then every group $G$ of order $p^2$ is abelian. Moreover, $G$ is isomorphic to either $\mathbb{Z}_{p^2}$ or $\mathbb{Z}_p \oplus \mathbb{Z}_p$.""",
    "All groups of prime squared order are abelian, and there are exactly two isomorphism types: cyclic and elementary abelian.",
    proof_deps={"technique": "center-and-class-equation"}
)

write_concept(
    "groups-of-order-eight",
    "Classification of Groups of Order 8",
    "proposition", "group_theory", "intermediate", "II.6", "Proposition 6.3",
    r"""Up to isomorphism, there are exactly five distinct groups of order $8$:
\begin{itemize}
\item Three abelian groups: $\mathbb{Z}_8$, $\mathbb{Z}_4 \oplus \mathbb{Z}_2$, $\mathbb{Z}_2 \oplus \mathbb{Z}_2 \oplus \mathbb{Z}_2$.
\item The dihedral group $D_4$ and the quaternion group $Q_8$ (nonabelian).
\end{itemize}
The nonabelian case is characterized by generators $a,b$ with $|a| = 4$, $b \notin \langle a \rangle$, and $bab^{-1} = a^{-1}$. The two possibilities are $b^2 = e$ (giving $D_4$) and $b^2 = a^2$ (giving $Q_8$).""",
    "There are exactly five groups of order 8 up to isomorphism: three abelian and two nonabelian (the dihedral group D_4 and the quaternion group Q_8).",
    proof_deps={"technique": "case-analysis"}
)

write_concept(
    "nonabelian-groups-of-order-12",
    "Nonabelian Groups of Order 12",
    "proposition", "group_theory", "intermediate", "II.6", "Proposition 6.4",
    r"""There are (up to isomorphism) exactly three distinct nonabelian groups of order $12$:
\begin{itemize}
\item The dihedral group $D_6$;
\item The alternating group $A_4$;
\item A group $T$ generated by elements $a, b$ such that $|a| = 6$, $b^2 = a^3$, and $ba = a^{-1}b$.
\end{itemize}""",
    "Up to isomorphism, there are exactly three nonabelian groups of order 12: the dihedral group D_6, the alternating group A_4, and a third group T which is a semidirect product.",
    proof_deps={"technique": "sylow-and-case-analysis"}
)

write_concept(
    "semidirect-product",
    "Semidirect Product of Groups",
    "definition", "group_theory", "intermediate", "II.6", "Definition (Exercise 6.1)",
    r"""Let $G$ and $H$ be groups and $\theta: H \to \operatorname{Aut} G$ a homomorphism. The \emph{semidirect product} $G \times_{\theta} H$ is the set $G \times H$ with the binary operation:
$$(g,h)(g',h') = (g[\theta(h)(g')], hh').$$
The identity is $(e,e)$ and $(g,h)^{-1} = (\theta(h^{-1})(g^{-1}), h^{-1})$.""",
    "The semidirect product generalizes the direct product by allowing the second factor to act on the first via automorphisms. It is the group-theoretic analogue of a split extension.",
)

# ═══════════════════════════════════════════════════════════════
# SECTION 7: Nilpotent and Solvable Groups
# ═══════════════════════════════════════════════════════════════

write_concept(
    "ascending-central-series-and-nilpotent-group",
    "Ascending Central Series and Nilpotent Group",
    "definition", "group_theory", "intermediate", "II.7", "Definition 7.1",
    r"""The \emph{ascending central series} of a group $G$ is the sequence of subgroups $\langle e \rangle = C_0(G) < C_1(G) < C_2(G) < \cdots$ defined by:
$$C_{i+1}(G)/C_i(G) = C(G/C_i(G)).$$
Equivalently, $C_{i+1}(G) = \pi_i^{-1}[C(G/C_i(G))]$ where $\pi_i: G \to G/C_i(G)$ is the canonical epimorphism. $G$ is \emph{nilpotent} if $C_n(G) = G$ for some $n$.""",
    "A group is nilpotent if its ascending central series terminates at the whole group. Equivalently, the group can be built up by repeatedly taking the center of successive quotients.",
)

write_concept(
    "direct-product-of-nilpotent-groups-is-nilpotent",
    "Direct Product of Nilpotent Groups is Nilpotent",
    "theorem", "group_theory", "intermediate", "II.7", "Theorem 7.3",
    r"""The direct product of a finite number of nilpotent groups is nilpotent.""",
    "Nilpotency is preserved under finite direct products, providing a useful closure property.",
    proof_deps={"technique": "central-series-induction"}
)

write_concept(
    "finite-nilpotent-equals-direct-product-of-sylow",
    "Finite Nilpotent iff Direct Product of Sylow Subgroups",
    "proposition", "group_theory", "advanced", "II.7", "Proposition 7.5",
    r"""A finite group $G$ is nilpotent if and only if $G$ is the direct product of its Sylow subgroups.""",
    "For finite groups, nilpotency is equivalent to being the direct product of Sylow subgroups, showing that finite nilpotent groups are precisely those built from p-groups.",
    proof_deps={"technique": "sylow-uniqueness"}
)

write_concept(
    "subgroups-of-all-dividing-orders-in-nilpotent",
    "Subgroups of Every Order Dividing |G| in Finite Nilpotent Groups",
    "corollary", "group_theory", "intermediate", "II.7", "Corollary 7.6",
    r"""If $G$ is a finite nilpotent group and $m$ divides $|G|$, then $G$ has a subgroup of order $m$.""",
    "Finite nilpotent groups enjoy the converse of Lagrange's Theorem: they have subgroups of every possible order dividing the group order.",
    proof_deps={"technique": "direct-product-decomposition"}
)

write_concept(
    "commutator-subgroup",
    "Commutator Subgroup",
    "definition", "group_theory", "basic", "II.7", "Definition 7.7",
    r"""Let $G$ be a group. The subgroup of $G$ generated by the set
$$\{aba^{-1}b^{-1} \mid a,b \in G\}$$
is called the \emph{commutator subgroup} of $G$ and denoted $G'$.""",
    "The commutator subgroup is the subgroup generated by all commutators. It is the smallest normal subgroup whose quotient is abelian, measuring how far a group is from being abelian."
)

write_concept(
    "derived-series-and-solvable-group",
    "Derived Series and Solvable Group",
    "definition", "group_theory", "intermediate", "II.7", "Definition 7.8",
    r"""The \emph{derived series} of a group $G$ is defined by:
$$G^{(0)} = G, \quad G^{(1)} = G', \quad G^{(i+1)} = (G^{(i)})'.$$
$G$ is \emph{solvable} if $G^{(n)} = \langle e \rangle$ for some $n$. The groups $G^{(i)}$ are called the \emph{derived subgroups} of $G$.""",
    "A group is solvable if its derived series (iterated commutator subgroups) terminates at the trivial subgroup. Solvability generalizes abelianness through successive abelian quotients.",
)

write_concept(
    "nilpotent-implies-solvable",
    "Nilpotent Implies Solvable",
    "proposition", "group_theory", "intermediate", "II.7", "Proposition 7.9",
    r"""Every nilpotent group is solvable.""",
    "Nilpotency is a stronger condition than solvability; every nilpotent group is solvable. This follows from the fact that factors of the central series are abelian.",
    proof_deps={"technique": "central-series-derived-series-comparison"}
)

write_concept(
    "solvability-properties",
    "Properties of Solvable Groups",
    "theorem", "group_theory", "intermediate", "II.7", "Theorem 7.11",
    r"""\begin{enumerate}
\item[(i)] Every subgroup and every homomorphic image of a solvable group is solvable.
\item[(ii)] If $N$ is a normal subgroup of a group $G$ such that $N$ and $G/N$ are solvable, then $G$ is solvable.
\end{enumerate}""",
    "Solvability is closed under taking subgroups, quotients, and extensions. An extension of a solvable group by a solvable group is solvable.",
    proof_deps={"technique": "derived-series-tracking"}
)

write_concept(
    "characteristic-subgroups-in-solvable-groups",
    "Characteristic Subgroups in Solvable Groups",
    "lemma", "group_theory", "advanced", "II.7", "Lemma 7.13",
    r"""Let $G$ be a group and $N \triangleleft G$.
\begin{enumerate}
\item[(i)] If $H$ is a characteristic subgroup of $N$, then $H \triangleleft G$.
\item[(ii)] Every normal Sylow $p$-subgroup of $G$ is fully invariant.
\item[(iii)] If $G$ is solvable and $N$ is a minimal normal subgroup, then $N$ is an abelian $p$-group for some prime $p$.
\end{enumerate}""",
    "Characteristic subgroups of normal subgroups are normal. In solvable groups, minimal normal subgroups are elementary abelian p-groups.",
    proof_deps={"technique": "characteristicity-transitivity"}
)

write_concept(
    "p-halls-theorem-for-solvable-groups",
    "P. Hall's Theorem for Solvable Groups",
    "proposition", "group_theory", "advanced", "II.7", "Proposition 7.14",
    r"""Let $G$ be a finite solvable group of order $mn$, with $(m,n) = 1$. Then:
\begin{enumerate}
\item[(i)] $G$ contains a subgroup of order $m$;
\item[(ii)] any two subgroups of $G$ of order $m$ are conjugate;
\item[(iii)] any subgroup of $G$ of order $k$, where $k \mid m$, is contained in a subgroup of order $m$.
\end{enumerate}""",
    "Hall's Theorem generalizes the Sylow theorems: in solvable groups, for any set of primes, there exist Hall subgroups whose order is the product of the corresponding Sylow subgroups.",
    proof_deps={"technique": "induction-on-group-order"}
)

# ═══════════════════════════════════════════════════════════════
# SECTION 8: Normal and Subnormal Series
# ═══════════════════════════════════════════════════════════════

write_concept(
    "subnormal-series",
    "Subnormal Series",
    "definition", "group_theory", "basic", "II.8", "Definition 8.1",
    r"""A \emph{subnormal series} of a group $G$ is a chain of subgroups
$$G = G_0 > G_1 > \cdots > G_n$$
such that $G_{i+1}$ is normal in $G_i$ for each $i$. The \emph{factors} of the series are the quotient groups $G_i/G_{i+1}$, and the \emph{length} of the series is the number of nontrivial factors.""",
    "A subnormal series is a chain of subgroups where each term is normal in the previous one, not necessarily normal in the whole group."
)

write_concept(
    "refinement-of-a-subnormal-series",
    "Refinement of a Subnormal Series",
    "definition", "group_theory", "basic", "II.8", "Definition 8.2",
    r"""A \emph{one-step refinement} of a subnormal series $G = G_0 > G_1 > \cdots > G_n$ is a series $G = G_0 > \cdots > G_i > N > G_{i+1} > \cdots > G_n$ where $N$ is a normal subgroup of $G_i$ and $G_{i+1}$ is normal in $N$.

A \emph{refinement} of a subnormal series $S$ is any subnormal series obtained from $S$ by a finite sequence of one-step refinements. A refinement is \emph{proper} if its length is larger than the length of $S$.""",
    "A refinement of a subnormal series is obtained by inserting intermediate subgroups that are normal in the preceding term."
)

write_concept(
    "composition-series-and-solvable-series",
    "Composition Series and Solvable Series",
    "definition", "group_theory", "basic", "II.8", "Definition 8.3",
    r"""A subnormal series $G = G_0 > G_1 > \cdots > G_n = \langle e \rangle$ is a \emph{composition series} if each factor $G_i/G_{i+1}$ is simple.

A subnormal series $G = G_0 > G_1 > \cdots > G_n = \langle e \rangle$ is a \emph{solvable series} if each factor is abelian.""",
    "A composition series has simple factors, while a solvable series has abelian factors. Composition series are maximal subnormal series; solvable series witness the solvability of the group."
)

write_concept(
    "existence-and-properties-of-composition-series",
    "Existence and Properties of Composition Series",
    "theorem", "group_theory", "intermediate", "II.8", "Theorem 8.4",
    r"""\begin{enumerate}
\item[(i)] Every finite group $G$ has a composition series.
\item[(ii)] Every refinement of a solvable series is a solvable series.
\item[(iii)] A subnormal series is a composition series if and only if it has no proper refinements.
\end{enumerate}""",
    "Every finite group has a composition series. Solvability is preserved under refinement. Composition series are exactly the maximal subnormal series.",
    proof_deps={"technique": "maximal-normal-subgroup-induction"}
)

write_concept(
    "solvable-iff-composition-factors-cyclic-of-prime-order",
    "Solvable iff Composition Factors Cyclic of Prime Order",
    "proposition", "group_theory", "intermediate", "II.8", "Proposition 8.6",
    r"""A finite group $G$ is solvable if and only if $G$ has a composition series whose factors are cyclic of prime order.""",
    "A finite group is solvable precisely when it has a composition series with all factors cyclic of prime order, connecting the Jordan-Hölder framework with solvability.",
    proof_deps={"technique": "refinement-and-abelian-simple"}
)

write_concept(
    "equivalent-subnormal-series",
    "Equivalent Subnormal Series",
    "definition", "group_theory", "intermediate", "II.8", "Definition 8.7",
    r"""Two subnormal series of a group $G$
$$G = G_0 > G_1 > \cdots > G_n = \langle e \rangle,$$
$$G = H_0 > H_1 > \cdots > H_m = \langle e \rangle$$
are \emph{equivalent} if there is a one-to-one correspondence between the nontrivial factors $\{G_i/G_{i+1}\}$ and $\{H_j/H_{j+1}\}$ such that corresponding factors are isomorphic.""",
    "Two subnormal series are equivalent if they have the same multiset of factor groups up to isomorphism, independent of the order in which they appear."
)

write_concept(
    "zassenhaus-lemma",
    "Zassenhaus Lemma (Butterfly Lemma)",
    "lemma", "group_theory", "advanced", "II.8", "Lemma 8.9",
    r"""Let $A^*, A, B^*, B$ be subgroups of a group $G$ such that $A^*$ is normal in $A$ and $B^*$ is normal in $B$. Then:
\begin{enumerate}
\item[(i)] $A^*(A \cap B^*)$ is a normal subgroup of $A^*(A \cap B)$;
\item[(ii)] $B^*(A^* \cap B)$ is a normal subgroup of $B^*(A \cap B)$;
\item[(iii)] $\displaystyle \frac{A^*(A \cap B)}{A^*(A \cap B^*)} \cong \frac{B^*(A \cap B)}{B^*(A^* \cap B)}$.
\end{enumerate}""",
    "The Zassenhaus (Butterfly) Lemma establishes isomorphisms between quotients of certain subgroups constructed from four groups with normality relations. It is the key technical ingredient for the Schreier Refinement Theorem.",
    proof_deps={"technique": "epimorphism-construction"}
)

write_concept(
    "schreier-refinement-theorem",
    "Schreier Refinement Theorem",
    "theorem", "group_theory", "advanced", "II.8", "Theorem 8.10",
    r"""Any two subnormal series of a group $G$ have equivalent refinements.""",
    "Any two subnormal series can be refined to equivalent series, meaning the multiset of composition factors is an invariant of the group (up to refinement).",
    proof_deps={"technique": "zassenhaus-butterfly"}
)

write_concept(
    "jordan-holder-theorem",
    "Jordan-Hölder Theorem",
    "theorem", "group_theory", "advanced", "II.8", "Theorem 8.11",
    r"""Any two composition series of a group $G$ are equivalent. Therefore every group having a composition series determines a unique list of simple groups (up to isomorphism and order), called the \emph{composition factors} of $G$.""",
    "All composition series of a group have the same length and the same composition factors (up to isomorphism and permutation). The composition factors form a unique set of simple group invariants.",
    proof_deps={"technique": "schreier-refinement"}
)

# ─── Mark complete ───
done_path = os.path.join(STAGING, ".done")
with open(done_path, "w") as f:
    f.write(f"Extraction completed on {DATE} by {AGENT}\n")
    f.write(f"{46} concepts extracted from GTM073 Chapter II\n")

print(f"\n=== EXTRACTION COMPLETE ===")
print(f"{46} concepts written to {STAGING}")
print(f".done marker: {done_path}")
