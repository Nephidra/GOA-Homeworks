const levels = { error: 0, warn: 1, info: 2 };

export function createLogger({ level = 'info', prefix = '' } = {}) {
  const currentLevel = levels[level] ?? levels.info;

  function log(methodLevel, method, ...args) {
    if (levels[methodLevel] <= currentLevel) {
      console[method](`${prefix}`, ...args);
    }
  }

  return {
    info: (...args) => log('info', 'log', ...args),
    warn: (...args) => log('warn', 'warn', ...args),
    error: (...args) => log('error', 'error', ...args)
  };
}
