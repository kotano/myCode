// BEGIN
const getIndex = (key) => Math.abs(crc32.str(key)) % 1000;

const make = () => [];

const hasCollision = (map, key) => {
  const index = getIndex(key);
  const [currentKey] = map[index];
  return currentKey !== key;
};

const set = (map, key, value) => {
  const index = getIndex(key);
  if (map[index] && hasCollision(map, key)) {
    return false;
  }
  map[index] = [key, value];

  return true;
};

const get = (map, key, defaultValue = null) => {
  const index = getIndex(key);
  if (!map[index] || hasCollision(map, key)) {
    return defaultValue;
  }
  const [, value] = map[index];

  return value;
};

export { make, set, get };
// END


// @ts-check


describe('MapTest', () => {
  it('testMap', () => {
    const map = make();
    const result1 = get(map, 'key');
    expect(result1).toBeNull();

    const result2 = get(map, 'key', 'value');
    expect(result2).toBe('value');

    set(map, 'key2', 'value2');

    const result3 = get(map, 'key2');
    expect(result3).toBe('value2');

    const result4 = get(map, 'undefined');
    expect(result4).toBeNull();

    set(map, 'key2', 'another value');
    const result5 = get(map, 'key2');
    expect(result5).toBe('another value');
  });

  it('testMapCollisions', () => {
    const map = make();

    expect(set(map, 'aaaaa0.462031558722291', 'vvv')).toBeTruthy();
    expect(set(map, 'aaaaa0.0585754039730588', 'boom!')).toBeFalsy();

    const result1 = get(map, 'aaaaa0.462031558722291');
    expect(result1).toBe('vvv');

    const result2 = get(map, 'aaaaa0.0585754039730588');
    expect(result2).toBeNull();

    set(map, 'aaaaa0.462031558722291', 'wop');
    const result3 = get(map, 'aaaaa0.462031558722291');
    expect(result3).toBe('wop');
  });
});
