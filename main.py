from client import DatsCityClient
import regex

def main():
    client = DatsCityClient()

    resp = client.get_words()
    # word = words[0]
    words = resp['words']

    for i, word in enumerate(words):
        print(i, word)

    ps = []
    iters_count = 1
    for base_idx, base_word in enumerate(words):
        if base_idx == iters_count:
            break
        l = None
        for l_ldx, l_word in enumerate(words):
            if l_ldx == base_idx:
                continue
            pos = base_word.find(l_word[-1])
            if pos == -1:
                continue
            for r_ldx, r_word in enumerate(words, l_ldx):
                if r_ldx == base_idx or r_ldx == l_ldx:
                    continue

                r_pos = base_word.rfind(r_word[-1])
                if r_pos == -1 or r_pos == pos:
                    continue

                ps.append({
                    'base_word': base_word,
                    "base_word_id": base_idx,
                    "l_base_intersection": pos,
                    "l_word": l_word,
                    "l_word_id": l_ldx,
                    "r_word": r_word,
                    "r_word_id": r_ldx,
                    "r_base_intersection": r_pos,
                })
    idx = 123
    print(ps[idx])
    x = ps[idx]["r_base_intersection"] - ps[idx]["l_base_intersection"] - 1
    # [***l_ldx(len)r_ldx***]
    for f, s in zip(ps[idx]["l_word"], ps[idx]["r_word"]):
        print(f, s)
        pattern = f".{f}.{x}{s}"
        for i, word in enumerate(words):
            if i in [ps[idx]["base_word_id"], ps[idx]["l_word_id"], ps[idx]["r_word_id"]]:
                continue
            if regex.search(pattern, word) is not None:
                print(word, "###")
# т
# в
# о           р
# р           о
# ч           в
# е           е
# с           с
# т           н
# в           и
# о м е ж н и к

if __name__ == '__main__':
    main()
