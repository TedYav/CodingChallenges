num_chapters, problems_per_page = map(int,input().strip().split())
problems_per_chapter = list(map(int,input().strip().split()))
start_pages = [1]
for i in range(1, num_chapters + 1):
	start_pages.append(problems_per_chapter[i-1]//problems_per_page + start_pages[i-1])
	if problems_per_chapter[i-1] % problems_per_page != 0:
		start_pages[-1] += 1
special_problems = 0
for i in range(num_chapters):
	if problems_per_chapter[i] > start_pages[i]:
		current_page = start_pages[i]
		current_problem = 1
		while current_page >= current_problem and current_problem <= problems_per_chapter[i]:
			if current_page in range(current_problem, current_problem + problems_per_page):
				special_problems += 1
			current_page += 1
			current_problem += problems_per_page
		if special_problems == start_special:
			# print("SPECIAL PROBLEM %d ON PAGE %d" % (current_page, current_page))
			print(list(range(start_pages[i], start_pages[i+1])))
			print(list(range(1, problems_per_chapter[i] + 1)))
print(special_problems)