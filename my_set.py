"""
Learn about sets
an unordered collection of unique, immutable objects
define it using {}
You can use the set() to create one
"""


def main():
    """
    test function
    :return:
    """
    p = {6,78,21,45}
    print(p, type(p))
    data = [1,3,5,2,88,3,1]
    print(data, type(data))
    #eliminates duplicates
    sdata = set(data)
    print(sdata, type(sdata))
    sdata.add(45)
    sdata.update([2,99,44,33,1,2,88])
    print(sdata)
    #removing elements
    sdata.remove(44)
    print(sdata)
    sdata.discard(77)
    print(sdata)
    bk_data =sdata.copy()
    print(bk_data is sdata)
    print(bk_data == sdata)
    ########### Define some sets
    blue_eyes = {"Olivia", "Harry", "Lily", "Jack"}
    blond_hair = {"Harry", "Jack", "Amelia", "Mia", "Joshua"}
    smell_hcn = {"Harry", "Amelia"}
    taste_ptc = {"Harry","lilly","Amelia","Lola"}
    o_blood = {"Mia", "Joshua", "Lily", "Olivia"}
    b_blood = {"Amelia", "Jack"}
    a_blood = {"Harry"}
    ab_blood = {"Joshua", "Lola"}

    print(blue_eyes.union(blond_hair))
    print(blue_eyes.intersection(taste_ptc))
    print(smell_hcn.symmetric_difference(a_blood))
    print(blond_hair.difference(ab_blood))
    print(taste_ptc.issuperset(smell_hcn))

if __name__ == '__main__':
    main()
    exit(0)