"""Compare 2 versions separated with points e.g 12.10.11b """

def compare_ver(version1, version2):
    return  version1 if version1>=version2 else version2


v1 = "1234.22.523.22c"
v2 = "1234.34.233.22c"
print(compare_ver(v1, v2))