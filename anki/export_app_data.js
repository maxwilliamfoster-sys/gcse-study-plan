// Exports the GCSE Plan app's card data (topic cards, AQA German vocab list, History dates/people) to JSON.
// Usage: node export_app_data.js <path to GCSE-Plan/src> <out.json>
const fs = require('fs'), path = require('path'), vm = require('vm');
const [src, out] = process.argv.slice(2);
const ctx = { RG: { subjects: [] } };
vm.createContext(ctx);
for (const f of ['d-maths.js', 'd-science.js', 'd-english.js', 'd-humanities.js', 'd-german.js', 'd-vocab.js', 'd-decks.js']) {
  vm.runInContext(fs.readFileSync(path.join(src, f), 'utf8'), ctx, { filename: f });
}
const RG = ctx.RG;
const data = {
  topics: RG.subjects.flatMap((s) => s.topics.map((t) => ({ subject: s.id, id: t.id, name: t.n, higher: !!t.h, cards: t.cards || [] }))),
  vocab: { F: RG.vocab.F, H: RG.vocab.H },
  histDates: RG.decks.histDates,
  histPeople: RG.decks.histPeople,
};
fs.writeFileSync(out, JSON.stringify(data));
console.log('topics', data.topics.length, 'vocab', data.vocab.F.length + data.vocab.H.length, 'dates', data.histDates.length, 'people', data.histPeople.length);
