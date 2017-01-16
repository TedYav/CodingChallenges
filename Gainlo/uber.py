def permutations(arrs, perms = [[]]):
	if not arrs:
		return perms
	else:
		newperms = []
		for perm in perms:
			for i in arrs[0]:
				newperms.append(perm + [i])
		return permutations(arrs[1:], newperms)

