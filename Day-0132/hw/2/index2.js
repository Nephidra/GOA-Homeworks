import formatDate, { parseDate } from './utils.js';

const str = "2025-10-04";
const parsed = parseDate(str);
console.log("Parsed:", parsed);

const formatted = formatDate(new Date());
console.log("Formatted:", formatted);