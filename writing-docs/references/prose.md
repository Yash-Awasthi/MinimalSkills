# prose

Load for editing, shortening, voice and proofreading.

## edit pass, in order

1. Structure: does each section answer one question.
2. Order: is the answer before the context.
3. Paragraphs: one idea each, three sentences maximum.
4. Sentences: subject, verb, object. Under 25 words.
5. Words: delete the ones that change nothing.
6. Mechanics: spelling, punctuation, links.

Editing at the word level before the structure wastes the pass.

## cuts that always work

| pattern | fix |
| --- | --- |
| "In order to" | "to" |
| "It is important to note that" | delete the clause |
| "This allows you to" | "this lets you", or just the verb |
| "We have implemented" | "we added" |
| "utilize" | "use" |
| "very", "really", "quite" | delete |
| "as mentioned above" | delete, or repeat the fact |
| "should be able to" | "can" |
| nominalization: "the implementation of" | "implementing" |

## voice

- Active: the actor performs the verb. "The worker retries the job", not "the job is retried".
- Present tense for behavior: "the endpoint returns 404".
- Second person for instructions: "run the migration".
- One term per concept. A synonym for the same thing is a second concept to the reader.

## claims

| claim | requirement |
| --- | --- |
| performance | a number, a machine and a date |
| compatibility | the version tested |
| security | the threat model, or the word "not" |
| adoption | a source and a period |

An unsourced number is a guess: cite it inline or delete the number.

## mechanical

- Serial comma consistently, or never.
- One space after a period.
- Straight quotes in code, curly in prose only if the style guide says so.
- Numbers: spell out under ten, digits from ten, always digits with a unit.
- Units with a space: 10 ms, 2 GB. Not 10ms.
- Link text describes the destination, never "here".

## review

Read the piece once for structure, once for sentences, once for mechanics. Three passes, one concern each. A single pass sees typos and misses the wrong order.
