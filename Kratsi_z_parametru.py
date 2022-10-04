def main(a,b):
    lens = [len(a),len(b)]
    return [a,b][lens.index(max(lens))]



prvni = "nzazr"
druhy = "bazar"
print(main(prvni, druhy))