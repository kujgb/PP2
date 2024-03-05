names = ['Aizhan', 'Bekasyl', 'Perizat']
with open("a.txt", "w") as fp:
    for i in names:
        fp.write("%s\n" % i)
    print('done')