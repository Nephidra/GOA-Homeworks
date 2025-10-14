import { createLogger } from './logger.js';

const logger1 = createLogger({ level: 'info', prefix: '[APP1]' });
const logger2 = createLogger({ level: 'warn', prefix: '[APP2]' });
const logger3 = createLogger({ level: 'error', prefix: '[APP3]' });

logger1.info('Info log visible');
logger1.warn('Warn log visible');
logger1.error('Error log visible');

logger2.info('Info log hidden');
logger2.warn('Warn log visible');
logger2.error('Error log visible');

logger3.info('Info log hidden');
logger3.warn('Warn log hidden');
logger3.error('Error log visible');