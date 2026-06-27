#!/usr/bin/env python3
"""Add missing inline concepts that weren't caught by the bold-header regex."""
import os, yaml, hashlib

STAGING = '/home/a123/文档/mathpkg/pipeline_output/v7_test/staging/_GTM099_Finite_Reflection_Groups'

missing = [
    {
        'slug': 'simple_reflection_maps_neighboring_root_positive',
        'title_en': 'Simple Reflection Sends Neighboring Root to a Positive Root',
        'title_zh': '单反射将相邻根映为正根',
        'type': 'proposition',
        'domain': 'group_theory',
        'subdomain': 'root_systems',
        'chapter': '4',
        'section': '4.1',
        'number': '4.1.5',
        'statement': '''If $r_i, r_j \\in \\Pi$ with $i \\neq j$, then $(r_i, r_j) \\leq 0$ and $S_i r_j$ is a positive root.

More precisely, $S_i r_j = r_j - 2(r_j, r_i) r_i$ is a nonnegative linear combination of simple roots, so $S_i r_j \\in \\Delta^+$.''',
        'description': 'Proposition 4.1.5 from Chapter 4 of Grove and Benson\'s "Finite Reflection Groups" (GTM 99). This result shows that applying a fundamental reflection to another simple root yields a positive root, which is a key property used throughout the theory of root systems.',
    },
    {
        'slug': 'uniqueness_of_simple_root_basis',
        'title_en': 'Uniqueness of the t-Base for a Root System',
        'title_zh': '根系t-基的唯一性',
        'type': 'theorem',
        'domain': 'group_theory',
        'subdomain': 'root_systems',
        'chapter': '4',
        'section': '4.1',
        'number': '4.1.8',
        'statement': '''For a Coxeter group $\\mathcal{G}$ with root system $\\Delta$, the $t$-base $\\Pi_t$ is uniquely determined by the choice of the vector $t \\in V$ (with $(t, r) \\neq 0$ for all $r \\in \\Delta$).

Thus the notion of positivity (a root being $t$-positive or $t$-negative) depends only on $t$ and not on the choice of $\\Pi$.''',
        'description': 'Theorem 4.1.8 from Chapter 4 of Grove and Benson\'s "Finite Reflection Groups" (GTM 99). Establishes the uniqueness of the simple root basis for a given choice of t, a fundamental structural result for Coxeter groups.',
    },
    {
        'slug': 'determinant_formula_for_marked_graphs',
        'title_en': 'Determinant Recursion Formula for Marked Graphs',
        'title_zh': '标号图的行列式递推公式',
        'type': 'proposition',
        'domain': 'linear_algebra',
        'subdomain': 'coxeter_graphs',
        'chapter': '5',
        'section': '5.1',
        'number': '5.1.5',
        'statement': '''Let $G$ be a marked graph having two adjacent nodes $a_1$ and $a_2$, with mark $p = p_{12}$. Denote by $G_1$ the subgraph $G \\setminus a_1$, by $G_2$ the subgraph $G \\setminus \\{a_1, a_2\\}$. Then

$$\\det G = \\det G_1 - (\\cos^2 \\pi/p) \\det G_2.$$''',
        'description': 'Proposition 5.1.5 from Chapter 5 of Grove and Benson\'s "Finite Reflection Groups" (GTM 99). A crucial determinant recursion formula used to classify positive definite Coxeter graphs.',
    },
    {
        'slug': 'subgraph_determinant_positivity_lemma',
        'title_en': 'Positivity of Subgraph Determinants for Positive Definite Graphs',
        'title_zh': '正定图子图行列式的正性引理',
        'type': 'proposition',
        'domain': 'linear_algebra',
        'subdomain': 'coxeter_graphs',
        'chapter': '5',
        'section': '5.1',
        'number': '5.1.6',
        'statement': '''If $G$ is a positive definite marked graph with $m$ nodes and $H$ is a subgraph of $G$ (obtained by deleting some nodes and all incident branches), then $H$ is also positive definite.

Equivalently, all principal minors of the matrix of a positive definite marked graph are positive.''',
        'description': 'Proposition 5.1.6 from Chapter 5 of Grove and Benson\'s "Finite Reflection Groups" (GTM 99). Shows that positive definiteness is inherited by subgraphs, used to exclude certain graphs from the classification.',
    },
    {
        'slug': 'dimension_homogeneous_polynomial_space',
        'title_en': 'Dimension of the Space of Homogeneous Polynomials of Degree d',
        'title_zh': 'd次齐次多项式空间的维数',
        'type': 'corollary',
        'domain': 'invariant_theory',
        'subdomain': 'polynomial_spaces',
        'chapter': '7',
        'section': '7.4',
        'number': 'Corollary 7.4.1.2',
        'statement': '''The dimension of the space $\\mathfrak{P}_d$ of homogeneous polynomial functions of degree $d$ on an $n$-dimensional vector space $V$ is

$$\\dim \\mathfrak{P}_d = \\binom{n + d - 1}{d}$$

for all $d \\geq 0$.''',
        'description': 'Corollary 2 to Proposition 7.4.1 from Chapter 7 of Grove and Benson\'s "Finite Reflection Groups" (GTM 99). Gives the standard combinatorial formula for the dimension of the space of homogeneous polynomials.',
    },
    {
        'slug': 'linear_invariant_implies_trivial_group',
        'title_en': 'Existence of Linear Invariant Implies Trivial Effective Group',
        'title_zh': '线性不变量的存在蕴含有效群平凡',
        'type': 'proposition',
        'domain': 'invariant_theory',
        'subdomain': 'polynomial_invariants',
        'chapter': '7',
        'section': '7.4',
        'number': '7.4.10',
        'statement': '''If $\\mathcal{G} \\leq \\mathcal{O}(V)$ is effective (i.e., $V_0(\\mathcal{G}) = 0$) and $\\mathcal{G}$ has a nonzero linear invariant $L \\in \\mathfrak{I}_1$, then $\\mathcal{G}$ is the trivial group.

In other words, a nontrivial effective Coxeter group cannot have a linear invariant. Consequently, any invariant of degree 1 must be zero.''',
        'description': 'Proposition 7.4.10 from Chapter 7 of Grove and Benson\'s "Finite Reflection Groups" (GTM 99). A structural result used to analyze the basic generators of the invariant ring of a Coxeter group.',
    },
]

for m in missing:
    d = os.path.join(STAGING, m['slug'])
    os.makedirs(d, exist_ok=True)

    # concept.yaml
    ydata = {
        'id': m['slug'],
        'title_en': m['title_en'],
        'title_zh': m['title_zh'],
        'type': m['type'],
        'domain': m['domain'],
        'subdomain': m['subdomain'],
        'difficulty': 'basic',
        'tags': [],
        'depends_on': {'required': [], 'recommended': [], 'suggested': []},
        'proof_deps': {},
        'source_books': [{
            'book_id': 'GTM099',
            'author': 'L.C. Grove, C.T. Benson',
            'title': 'Finite Reflection Groups',
            'chapter': m['chapter'],
            'section': m['section'],
            'pages': '',
            'role_in_book': f'{m["type"].capitalize()} in Chapter {m["chapter"]}'
        }],
        'content_hash': hashlib.sha256(m['statement'].encode()).hexdigest()[:16],
        'extraction_date': '2026-06-24',
        'extraction_agent': 'v7-10books',
    }
    with open(os.path.join(d, 'concept.yaml'), 'w') as f:
        yaml.dump(ydata, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # theorem.tex
    with open(os.path.join(d, 'theorem.tex'), 'w') as f:
        f.write(m['statement'] + '\n')

    # introduce.en.md
    md = f"""---
id: {m['slug']}
title: "{m['title_en']}"
type: {m['type']}
---

{m['description']}
"""
    with open(os.path.join(d, 'introduce.en.md'), 'w') as f:
        f.write(md)

    print(f"  Created {m['slug']}")

print(f"\nAdded {len(missing)} missing inline concepts")
