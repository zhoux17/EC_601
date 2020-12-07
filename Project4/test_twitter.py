# # import mathfun as fun
# from pytest import approx

# def test_addints():
# 	assert 1+1 == 2

# # def test_addfloats():
# # 	assert fun.add(1.5, 1.7) == approx(3.1)

import sys
sys.path.append('.')

import twitter

twitter_tweets = twitter.get_all_tweets()

def tweets():
    id = '0000000000000000'
    count = 3
    num = []
    num = twitter.get_all_tweets(twitter_tweets, id, count)
    assert len(num) == 0
    
    
    
# if __name__ == '__main__':
#     pytest.main("twitter.py")
