function normalize_date(s) {
    // Split into words, separated by `,` or a space. This is meant to handle how sometimes
    // there will be multiple dates, or there will be extra words like `Saturday`.
    let words = s.split(/,|\s/);
    let new_words = [];
    for (let i = 0; i < words.length; i++) {
        let word = words[i];
        if (!word.trim()) {
            continue;
        }
        if (word.split('/').length !== 3) {
            new_words.push(word);
            continue;
        }
        let [day, month, year] = word.split('/');
        let likely_thai_year = year.length === 2 && '6' <= year[0] && year[0] < ':';
        if (likely_thai_year) {
            try {
                year = String(parseInt(year) - 43);
            } catch(e) {
                // pass
            }
        }
        new_words.push(`${month}/${day}/${year}`);
    }

    return new_words.join(' ');
}
