import pandas as pd


def formula_aaab(pa, pb):
    numerator = (2 * pa * (2 - pa) * 2 * pa * pb - 2 * pa * pb * 2 * pa * pb)
    denominator = (2 * pa * (2 - pa) * pb * (2 - pb) - 2 * pa * pb * 2 * pa * pb)
    return numerator / denominator

def formula_aabb(pa, pb):
    numerator = (2 * pa * pb * 2 * pa * pb)
    denominator = (pb * (2 - pb))**2
    return numerator / denominator

def formula_aabc(pa, pb, pc):
    numerator = (2 * 2 * pa * pb * 2 * pa * pc)
    denominator = (2 * pb * (2 - pb) * pc * (2 - pc) - 2 * pb * pc * 2 * pb * pc)
    return numerator / denominator

def formula_abaa(pa, pb):
    numerator = (2 * pa * (2 - pa) * 2 * pa * pb - 2 * pa * pb * 2 * pa * pb)
    denominator = (pa * (2 - pa))**2
    return numerator / denominator

def formula_abac(pa, pb, pc):
    numerator = (2 * pa * (2 - pa) * 2 * pb * pc + 2 * 2 * pa * pb * 2 * pa * pc)
    denominator = (2 * pa * (2 - pa) * pc * (2 - pc) - 2 * pa * pc * 2 * pa * pc)
    return numerator / denominator

def formula_abcc(pa, pb, pc):
    numerator = (2 * 2 * pa * pc) * (2 * pb * pc)
    denominator = (pc * (2 - pc))**2
    return numerator / denominator

def formula_abcd(pa, pb, pc, pd):
    numerator = (2 * 2 * pa * pc * 2 * pb * pd + 2 * 2 * pa * pd * 2 * pb * pc)
    denominator = (2 * pc * (2 - pc) * pd * (2 - pd) - 2 * pc * pd * 2 * pc * pd)
    return numerator / denominator

def formula_aa(pa):
    return (pa * (2 - pa))**2

def formula_ab(pa, pb):
    return 2 * pa * (2 - pa) * pb * (2 - pb) - 2 * pa * pb * 2 * pa * pb
'''
Вход:

Выход
'''
def p_calculation_for_siblings(genotype_1, genotype_2, fr, loc):
    list = fr[loc]
    p1 = list[genotype_1[0]]
    p2 = list[genotype_1[1]]
    p3 = list[genotype_2[0]]
    p4 = list[genotype_2[1]]

    if genotype_1[0] == genotype_1[1]:
        # aa

        if genotype_1[0] in genotype_2 and genotype_1[1] in genotype_2:
            # aa or ab

            if genotype_2[0] == genotype_2[1]:
                # aa
                #print("a a a a")
                return 1

            if genotype_2[0] != genotype_2[1]:
                # ab
                # a a a b
                #print("a a a b")
                return formula_aaab(p3, p4)

        if genotype_1[1] in genotype_2 and genotype_1[0] not in genotype_2:
            # ba
            # a a b a
            #print("a a b a")
            return formula_aaab(p4, p3)

        if genotype_1[0] not in genotype_2 and genotype_1[1] not in genotype_2:
            # bb or bc

            if genotype_2[0] == genotype_2[1]:
                # bb
                # a a b b'
                #print("a a b b")
                return formula_aabb(p1, p3)

            else:
                # bc
                # a a b с
                #print("a a b c")
                return formula_aabc(p1, p3, p4)

    else:
        # ab or ba

        if genotype_1[0] in genotype_2 and genotype_1[1] in genotype_2:
            # ab
            # a b a b
            #print("a b a b")
            return 1

        if genotype_1[0] in genotype_2 and genotype_1[1] not in genotype_2:
            # aa or ac or ca

            if genotype_2[0] == genotype_2[1]:
                # aa
                # a b a a
                #print("a b a a")
                return formula_abaa(p1, p2)

            else:
                # ac or ca
                # (a b a c) or (a b c a)
                #print("(a b a c) or (a b c a)")
                if genotype_2[0] in genotype_1:
                    return formula_abac(p1, p2, p4)

                else:
                    return formula_abac(p1, p2, p3)

        if genotype_1[0] not in genotype_2 and genotype_1[1] in genotype_2:
            # aa or ac or ca

            if genotype_2[0] == genotype_2[1]:
                # aa
                # b a a a
                #print("b a a a")
                return formula_abaa(p1, p2)

            else:
                # ac or ca
                # (b a a c) or (b a c a)

                if genotype_2[0] in genotype_1:
                    # a b a c
                    #print('a b a c')
                    return  formula_abac(p1, p2, p4)

                else:
                    # a b c a
                    #print('a b c a')
                    return formula_abac(p2, p1, p3)

        if genotype_1[0] not in genotype_2 and genotype_1[1] not in genotype_2:
            # cc or cd or dc

            if genotype_2[0] == genotype_2[1]:
                # cc
                # a b c c
                #print("a b c c")
                return formula_abcc(p1, p2, p3)

            else:
                # cd or dc
                # (a b c d) or (a b d c)
                #print('(a b c d) or (a b d c)')
                return formula_abcd(p1, p2, p3, p4)

def inv_p_calculation_for_siblings(genotype_1, fr, loc):
    list = fr[loc]
    p1 = list[genotype_1[0]]
    p2 = list[genotype_1[1]]

    if genotype_1[0] == genotype_1[1]:
        # aa
        return formula_aa(p1)

    else:
        # ab or ba
        return formula_ab(p1, p2)

def local_siblings_countingLR(genotype_person, genotype_brother, allele_frequencies):
    calc = 0
    list_p_c = []
    list_not_p_c = []
    for loc in genotype_person:
        calc += 1
        if calc % 2 == 0:
            loc = loc.split('_')[0]
            genotype_in_loc_person = (genotype_person[f"{loc}_1"], genotype_person[f"{loc}_2"])
            genotype_in_loc_brother = (genotype_brother[f"{loc}_1"], genotype_brother[f"{loc}_2"])

            p_c = p_calculation_for_siblings(genotype_in_loc_person, genotype_in_loc_brother, allele_frequencies, loc)
            not_p_c = inv_p_calculation_for_siblings(genotype_in_loc_person, allele_frequencies, loc)

            list_p_c.append(p_c)
            list_not_p_c.append(not_p_c)

    p_c = 0
    for i in list_p_c:
        if p_c == 0:
            p_c = i
        p_c = p_c * i

    not_p_c = 0
    for i in list_not_p_c:
        if not_p_c == 0:
            not_p_c = i
        not_p_c = not_p_c * i

    lr = p_c / not_p_c
    return lr

def testLR():
    allele_frequencies = {'CSF1P0': {10: 0.2, 11: 0.3, 12: 0.4, 13: 0.1}}

    genotypes_data = [
            ('CSF1P0', (10, 10), (10, 10)),
            ('CSF1P0', (10, 10), (10, 11)),
            ('CSF1P0', (10, 10), (11, 11)),
            ('CSF1P0', (10, 10), (11, 12)),
            ('CSF1P0', (10, 11), (10, 10)),
            ('CSF1P0', (10, 11), (10, 11)),
            ('CSF1P0', (10, 11), (10, 12)),
            ('CSF1P0', (10, 11), (12, 12)),
            ('CSF1P0', (10, 11), (12, 13)),
        ]

    for i in genotypes_data:
        print(local_siblings_countingLR(i, allele_frequencies))

def find_and_countingLR_in_brothers(person, el_split, dict_data, allele_frequencies):
    lr_dict = {}
    for brother in list(dict_data):
        if len(brother.split('+')) == len(person.split('+')):
            if brother != person:
                lr = local_siblings_countingLR(dict_data[person], dict_data[brother], allele_frequencies)
                lr_dict[brother] = lr
    return {person: lr_dict}






def siblings_countingLR(df, allele_frequencies, number_children, number_grandchildren):
    dft = df.transpose()
    return_dict = {}
    dict_data = dft.to_dict()
    for person in list(dict_data):
        if '+' in person:
            if len(person.split('+')) > 2:
                # значит это (YAK1+YAK2-3)+(YAK7+YAK8-4)—2
                counting_dict = find_and_countingLR_in_brothers(person, '—', dict_data,
                                                                allele_frequencies)
            else:
                # значит это YAK1+YAK2-3
                counting_dict = find_and_countingLR_in_brothers(person, '-', dict_data,
                                                                allele_frequencies)
            #print('counting_dict', counting_dict)
            return_dict = return_dict | counting_dict
            #print('return_dict', return_dict)
    new_df = pd.DataFrame(return_dict)
    return new_df