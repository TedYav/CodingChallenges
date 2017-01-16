import balls
# UNIT TESTS (not submitted to HackerRank)

def test():
	test_expected_value()
	test_score_position()
	test_convert_balls()
	test_get_move_result()

def test_get_move_result():
	assert get_move_result((1,1,1),1,0.5,{}) == ((1,1), (1/3)*(1/2))
	assert get_move_result((0,1,0),1,0.5,{}) == ((0,0), (1/3)*(1/2))
	print(get_move_result((1,0,1,0),1,1,{}))
	assert get_move_result((1,0,1,0),1,1,{}) == ((1,0,0), 1/2)

def test_expected_value():
	assert calculate_expected_value([((1,0,1,0,1,1,1),1.0)],0,5) == 0
	assert calculate_expected_value( [((0,1),1)],0, 2) == 1
	# unrealistic as these would be condensed, but testing the same
	assert calculate_expected_value( [((0,1),1/3),((0,1),1/3),((0,1),1/3)],0, 2) == 1
	assert calculate_expected_value( [((0,1),(1/2)*(2/3)),((0,0),(1/2)*(1/3)), ((0,0),(1/2)*(2/3)), ((1,0),(1/2)*(1/3))], 0, 2) == 1.5

def test_score_position():
	position_scores = {}
	assert (1,1,1) not in position_scores
	assert score_position((1,1,1), position_scores) == 1
	assert (1,1,1) in position_scores
	assert score_position((1,1,0), position_scores) == score_position((0,1,1), position_scores) == 1
	assert (1,1,0) in position_scores
	assert score_position((1,0,0,1,0,1,0,1,1,0,0,0), position_scores) == 8.0/12.0

def test_convert_balls():
	assert convert_balls("BWBWB") == (0,1,0,1,0)
	assert convert_balls("WWWWWWWWW") == (1,1,1,1,1,1,1,1,1)

test()