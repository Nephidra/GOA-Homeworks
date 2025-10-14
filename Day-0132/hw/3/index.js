import { get } from './counter.js';
import { runA } from './a.js';
import { runB } from './b.js';

runA();
runB();

console.log("Final count:", get());