export const meta = {
  name: 'content-analysis',
  description: 'Sample books from each series, analyze content: classic/textbook/grad/research difficulty, duplicates',
  phases: [{ title: 'Analyze', detail: 'Each agent reads preface+TOC of one book, classifies difficulty/type/redundancy' }]
}

var SERIES = args.series
var BASE = args.base
var INDICES = args.indices
var GID = args.group || 1

phase('Analyze')

var tasks = INDICES.map(function(idx) {
  return async function() {
    var prompt = [
      '=== BOOK CONTENT ANALYZER ===',
      'Sample pages from a math book and classify its content.',
      '',
      'First, list the book: ls "' + BASE + '/' + SERIES + '" | head -' + (idx+1) + ' | tail -1',
      '',
      'Then sample key pages:',
      'python3 -c "',
      'import fitz, json, os, sys',
      "d = '" + BASE + '/' + SERIES + "'",
      "pdfs = sorted([f for f in os.listdir(d) if f.endswith('.pdf')])",
      "if " + idx + " < len(pdfs):",
      '    doc = fitz.open(os.path.join(d, pdfs[' + idx + ']))',
      '    n = doc.page_count',
      '    # Sample: title page, TOC, preface, first chapter, random middle page',
      '    pages = [0, min(3,n-1), min(5,n-1), min(10,n-1), min(n//4,n-1), min(n//2,n-1)]',
      '    for pg in pages:',
      '        t = doc[pg].get_text("text")[:600]',
      "        print(f'--- PAGE {pg+1} ---')",
      '        print(t)',
      '    doc.close()',
      'else:',
      "    print('NO BOOK at index " + idx + "')",
      '"',
      '',
      'Based on the samples, classify the book in JSON format:',
      '{',
      '  "filename": "...",',
      '  "pages": N,',
      '  "difficulty": "undergrad|grad|research|reference",',
      '  "type": "textbook|monograph|lecture_notes|problem_book|encyclopedia|other",',
      '  "classic": true/false,          // widely used standard text?',
      '  "subject": "algebra|analysis|topology|geometry|number_theory|logic|probability|applied|other",',
      '  "duplicate_of": "if similar to another book, name it; else empty"',
      '}',
      '',
      'Difficulty guide:',
      '- undergrad: assumes calculus/linear algebra, defines concepts from scratch',
      '- grad: assumes undergraduate math major, starts with definitions but moves fast',
      '- research: assumes PhD-level knowledge, Cites current papers, open problems',
      '- reference: encyclopedic, not meant to be read cover-to-cover',
    ].join('\n')

    try {
      await agent(prompt, { label: 'analyze-' + idx, phase: 'Analyze' })
    } catch(e) {}

    // Return placeholder — we collect results from disk
    return { index: idx, status: 'attempted' }
  }
})

var results = await parallel(tasks)
log('Group ' + GID + ' (' + SERIES + '): ' + results.filter(Boolean).length + '/' + INDICES.length)
return { group: GID, series: SERIES, attempted: results.filter(Boolean).length }
